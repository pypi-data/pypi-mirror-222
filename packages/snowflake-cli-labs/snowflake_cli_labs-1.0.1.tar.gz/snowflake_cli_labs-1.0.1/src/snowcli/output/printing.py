from __future__ import annotations

from datetime import datetime
from json import JSONEncoder
from pathlib import Path
from typing import List, Optional, Dict

from rich import box, print, print_json
import click
from snowflake.connector.cursor import SnowflakeCursor

from snowcli.output.formats import OutputFormat


class CustomJSONEncoder(JSONEncoder):
    """Custom JSON encoder handling serialization of non-standard types"""

    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        if isinstance(o, Path):
            return str(o)
        return super().default(o)


def print_db_cursor(
    cursor: SnowflakeCursor,
    columns: Optional[List[str]] = None,
) -> None:
    """
    Prints results fetched by cursor using specified format.

    :param cursor: snowflake cursor for fetching results
    :param columns: list of columns that should be included in output, if
        not provided then all columns are returned
    :return:
    """
    result = cursor.fetchall()
    column_names = [col.name for col in cursor.description]
    columns_to_include = columns or column_names

    data = [
        {k: v for k, v in zip(column_names, row) if k in columns_to_include}
        for row in result
    ]

    _print_formatted(data, columns_to_include)


def _get_format_type():
    context = click.get_current_context()
    format_from_ctx = context.find_root().params.get("output_format")
    if format_from_ctx:
        return OutputFormat(format_from_ctx)
    return OutputFormat.TABLE


def _print_formatted(data: List[Dict], columns: Optional[List[str]] = None):
    output_format = _get_format_type()
    if output_format == OutputFormat.TABLE:
        _print_table(data, columns)
    elif output_format == OutputFormat.JSON:
        import json

        print_json(json.dumps(data, cls=CustomJSONEncoder))
    else:
        raise Exception(f"Unknown {output_format} format option")


def print_data(data: List[Dict], columns: Optional[List[str]] = None) -> None:
    if columns is not None:
        data = [{k: v for k, v in raw.items() if k in columns} for raw in data]
    _print_formatted(data, columns)


def _print_table(data: List[Dict], columns: Optional[List[str]] = None):
    from rich.table import Table

    if not data:
        print("No data")
        return

    columns = columns or list(data[0].keys())

    table = Table(show_header=True, box=box.ASCII)
    for column in columns:
        table.add_column(column)
    for row in data:
        table.add_row(*[str(i) for i in row.values()])
    print(table)

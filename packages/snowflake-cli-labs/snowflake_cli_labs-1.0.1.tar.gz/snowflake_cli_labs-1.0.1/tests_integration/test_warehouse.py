import pytest

from unittest import mock
from tests_integration.snowflake_connector import snowflake_session


@pytest.mark.integration
@mock.patch("snowcli.output.decorators.print_db_cursor")
def test_warehouse_status_query(mock_print, runner, snowflake_session):
    runner.invoke_with_config_and_integration_connection(["warehouse", "status"])

    expected_results = snowflake_session.execute_string("show warehouses")[-1]
    result_names = _get_name_values_from_cursor(mock_print.call_args.args[0])
    expected_names = _get_name_values_from_cursor(expected_results)
    assert result_names == expected_names


def _get_name_values_from_cursor(cursor):
    column_names = [column.name for column in cursor.description]
    column_name_index = column_names.index("name")
    return {row[column_name_index] for row in cursor.fetchall()}

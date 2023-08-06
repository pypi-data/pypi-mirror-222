from __future__ import annotations

import os
from pathlib import Path
from shutil import copytree

import pkg_resources
import typer

from snowcli.cli.common.flags import DEFAULT_CONTEXT_SETTINGS, ConnectionOption
from snowcli.cli.snowpark.procedure_coverage import app as procedure_coverage_app
from snowcli.cli.snowpark_shared import (
    CheckAnacondaForPyPiDependancies,
    PackageNativeLibrariesOption,
    PyPiDownloadOption,
    snowpark_create,
    snowpark_describe,
    snowpark_drop,
    snowpark_execute,
    snowpark_list,
    snowpark_package,
    snowpark_update,
)
from snowcli.utils import check_for_connection

app = typer.Typer(
    name="procedure",
    context_settings=DEFAULT_CONTEXT_SETTINGS,
    help="Manage stored procedures",
)
app.add_typer(procedure_coverage_app)


@app.command("init")
def procedure_init():
    """
    Initialize this directory with a sample set of files to create a procedure.
    """
    copytree(
        pkg_resources.resource_filename(
            "templates",
            "default_procedure",
        ),
        f"{os.getcwd()}",
        dirs_exist_ok=True,
    )


@app.command("create")
def procedure_create(
    environment: str = ConnectionOption,
    pypi_download: str = PyPiDownloadOption,
    check_anaconda_for_pypi_deps: bool = CheckAnacondaForPyPiDependancies,
    package_native_libraries: str = PackageNativeLibrariesOption,
    name: str = typer.Option(
        ...,
        "--name",
        "-n",
        help="Name of the procedure",
    ),
    file: Path = typer.Option(
        "app.zip",
        "--file",
        "-f",
        help="Path to the file or folder to deploy",
        exists=False,
    ),
    handler: str = typer.Option(
        ...,
        "--handler",
        "-h",
        help="Handler",
    ),
    input_parameters: str = typer.Option(
        ...,
        "--input-parameters",
        "-i",
        help="Input parameters - such as (message string, count int)",
    ),
    return_type: str = typer.Option(
        ...,
        "--return-type",
        "-r",
        help="Return type",
    ),
    overwrite: bool = typer.Option(
        False,
        "--overwrite",
        "-o",
        help="Replace if existing procedure",
    ),
    execute_as_caller: bool = typer.Option(
        False,
        "--execute-as-caller",
        help="Execute as caller",
    ),
    install_coverage_wrapper: bool = typer.Option(
        False,
        "--install-coverage-wrapper",
        help="Wraps the procedure with a code coverage measurement tool, so that a coverage report can be later retrieved.",
    ),
):
    snowpark_package(
        pypi_download,  # type: ignore[arg-type]
        check_anaconda_for_pypi_deps,
        package_native_libraries,  # type: ignore[arg-type]
    )
    snowpark_create(
        "procedure",
        environment,
        name,
        file,
        handler,
        input_parameters,
        return_type,
        overwrite,
        execute_as_caller,
        install_coverage_wrapper,
    )


@app.command("update")
def procedure_update(
    environment: str = ConnectionOption,
    pypi_download: str = PyPiDownloadOption,
    check_anaconda_for_pypi_deps: bool = CheckAnacondaForPyPiDependancies,
    package_native_libraries: str = PackageNativeLibrariesOption,
    name: str = typer.Option(
        ...,
        "--name",
        "-n",
        help="Name of the procedure",
    ),
    file: Path = typer.Option(
        "app.zip",
        "--file",
        "-f",
        help="Path to the file to update",
        exists=False,
    ),
    handler: str = typer.Option(
        ...,
        "--handler",
        "-h",
        help="Handler",
    ),
    input_parameters: str = typer.Option(
        ...,
        "--input-parameters",
        "-i",
        help="Input parameters - such as (message string, count int)",
    ),
    return_type: str = typer.Option(
        ...,
        "--return-type",
        "-r",
        help="Return type",
    ),
    replace: bool = typer.Option(
        False,
        "--replace-always",
        help="Replace procedure, even if no detected changes to metadata",
    ),
    execute_as_caller: bool = typer.Option(
        False,
        "--execute-as-caller",
        help="Execute as caller",
    ),
    install_coverage_wrapper: bool = typer.Option(
        False,
        "--install-coverage-wrapper",
        help="Wraps the procedure with a code coverage measurement tool, so that a coverage report can be later retrieved.",
    ),
):
    snowpark_package(
        pypi_download,  # type: ignore[arg-type]
        check_anaconda_for_pypi_deps,
        package_native_libraries,  # type: ignore[arg-type]
    )
    snowpark_update(
        "procedure",
        environment,
        name,
        file,
        handler,
        input_parameters,
        return_type,
        replace,
        execute_as_caller,
        install_coverage_wrapper,
    )


@app.command("package")
def procedure_package(
    pypi_download: str = PyPiDownloadOption,
    check_anaconda_for_pypi_deps: bool = CheckAnacondaForPyPiDependancies,
    package_native_libraries: str = PackageNativeLibrariesOption,
):
    snowpark_package(
        pypi_download,  # type: ignore[arg-type]
        check_anaconda_for_pypi_deps,
        package_native_libraries,  # type: ignore[arg-type]
    )


@app.command("execute")
def procedure_execute(
    environment: str = ConnectionOption,
    select: str = typer.Option(
        ...,
        "--procedure",
        "-p",
        help="Procedure with inputs. E.g. 'hello(int, string)'. Must exactly match those provided when creating the procedure.",
    ),
):
    snowpark_execute("procedure", environment, select)


@app.command("describe")
def procedure_describe(
    environment: str = ConnectionOption,
    name: str = typer.Option("", "--name", "-n", help="Name of the procedure"),
    input_parameters: str = typer.Option(
        "",
        "--input-parameters",
        "-i",
        help="Input parameters - such as (message string, count int)",
    ),
    signature: str = typer.Option(
        "",
        "--procedure",
        "-p",
        help="Procedure signature with inputs. E.g. 'hello(int, string)'",
    ),
):
    snowpark_describe(
        "procedure",
        environment,
        name,
        input_parameters,
        signature,
    )


@app.command("list")
def procedure_list(
    environment: str = ConnectionOption,
    like: str = typer.Option(
        "%%",
        "--like",
        "-l",
        help='Filter procedures by name - e.g. "hello%"',
    ),
):
    snowpark_list("procedure", environment, like=like)


@app.command("drop")
def procedure_drop(
    environment: str = ConnectionOption,
    name: str = typer.Option("", "--name", "-n", help="Name of the procedure"),
    input_parameters: str = typer.Option(
        "",
        "--input-parameters",
        "-i",
        help="Input parameters - such as (message string, count int)",
    ),
    signature: str = typer.Option(
        "",
        "--procedure",
        "-p",
        help="Procedure signature with inputs. E.g. 'hello(int, string)'",
    ),
):
    snowpark_drop("procedure", environment, name, input_parameters, signature)

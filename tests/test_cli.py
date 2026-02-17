#!/usr/bin/env python3

import pathlib

from typer.testing import CliRunner

from aar_doc.cli import app

ROLES_DIR = pathlib.Path("./tests/fixtures/roles")
DEFAULT_ROLE = "minimum"


runner = CliRunner()


def test_cli_help():
    result = runner.invoke(app, [])
    assert result.exit_code == 2

    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0

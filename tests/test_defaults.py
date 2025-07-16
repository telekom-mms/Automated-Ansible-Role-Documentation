#!/usr/bin/env python3

import os
import pathlib

from typer.testing import CliRunner

from aar_doc.cli import app

ROLES_DIR = pathlib.Path("./tests/fixtures/roles")
DEFAULT_ROLE = "minimum"


runner = CliRunner()


def test_generate_defaults(tmp_path):
    """
    This test ensures that the default use case of generating
    defaults for an argument_spec is handled as expected.
    """
    role_path = ROLES_DIR / "generate_defaults"

    output_dir = tmp_path
    output_file = output_dir / "defaults.yml"

    # Default case without extra options
    expected_defaults_file = str(role_path / "defaults" / "main.yml")

    result = runner.invoke(
        app,
        [
            "--output-file",
            output_file,
            str(role_path),
            "defaults",
        ],
    )
    assert result.exit_code == 0
    assert open(expected_defaults_file).read() == open(output_file).read(), f"Generated output differs from fixture"

    # Using --overwrite-duplicates option
    expected_defaults_file = str(role_path / "defaults" / "overwrite.yml")

    result = runner.invoke(
        app,
        [
            "--output-file",
            output_file,
            str(role_path),
            "defaults",
            "--overwrite-duplicates",
        ],
    )

    assert result.exit_code == 0
    assert open(expected_defaults_file).read() == open(output_file).read(), f"Generated output differs from fixture"


def test_generate_defaults_no_defaults():
    """
    This test ensures that generating defaults for an argument_spec
    without any configured defaults is handled as expected.
    """
    role_path = ROLES_DIR / "generate_defaults_no_defaults"
    role_path = str(role_path)

    result = runner.invoke(app, [role_path, "defaults"])

    assert result.exit_code == 0
    assert (
        result.output
        == "No defaults configured in argument_specs. Nothing to do." + os.linesep
    )


def test_generate_defaults_no_options():
    """
    This test ensures that generating defaults for an argument_spec
    without any options is handled as expected.
    """
    role_path = ROLES_DIR / "no_options"
    role_path = str(role_path)

    result = runner.invoke(app, [role_path, "defaults"])

    assert result.exit_code == 0
    assert (
        result.output
        == "No defaults configured in argument_specs. Nothing to do." + os.linesep
    )

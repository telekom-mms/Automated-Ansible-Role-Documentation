#!/usr/bin/env python3

import filecmp
import os
import pathlib
import shutil

from typer.testing import CliRunner
from typing_extensions import assert_never

from ansible_docs.cli import app

ROLES_DIR = pathlib.Path("./tests/fixtures/roles")
DEFAULT_ROLE = "minimum"


runner = CliRunner()


def test_cli_help():
    result = runner.invoke(app, [])
    assert result.exit_code == 0

    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0


def test_cli_config_file(tmp_path):
    role_path = str(ROLES_DIR / DEFAULT_ROLE)

    output_dir = tmp_path
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / "README.md"

    result = runner.invoke(
        app,
        [
            "--config-file",
            ".ansible-docs.yml",
            "--output-file",
            output_file,
            role_path,
            "markdown",
        ],
    )
    assert result.exit_code == 0

    result = runner.invoke(
        app,
        [
            "--config-file",
            "nonexistent.yml",
            "--output-file",
            output_file,
            role_path,
            "markdown",
        ],
    )
    assert result.exit_code == 0

    config = """
    ---
    foo: bar
    baz: kaboom
    """
    config_file = output_dir / "config.yml"
    config_file.write_text(config)
    config_file = str(config_file)

    result = runner.invoke(
        app,
        [
            "--config-file",
            config_file,
            "--output-file",
            output_file,
            role_path,
            "markdown",
        ],
    )
    assert result.exit_code == 2


def test_cli_output_mode(tmp_path):
    role_path = str(ROLES_DIR / DEFAULT_ROLE)

    output_dir = tmp_path
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / "README.md"

    result = runner.invoke(
        app,
        [
            "--output-mode",
            "inject",
            "--output-file",
            output_file,
            role_path,
            "markdown",
        ],
    )
    assert result.exit_code == 0

    result = runner.invoke(
        app,
        [
            "--output-mode",
            "inject",
            "--output-file",
            output_file,
            role_path,
            "markdown",
        ],
    )
    assert result.exit_code == 0

    result = runner.invoke(
        app,
        [
            "--output-mode",
            "replace",
            "--output-file",
            output_file,
            role_path,
            "markdown",
        ],
    )
    assert result.exit_code == 0

    output_file = output_dir / "empty.md"
    output_file.touch()

    result = runner.invoke(
        app,
        [
            "--output-mode",
            "inject",
            "--output-file",
            output_file,
            role_path,
            "markdown",
        ],
    )
    assert result.exit_code == 1

    result = runner.invoke(
        app,
        [
            "--output-mode",
            "replace",
            "--output-file",
            output_file,
            role_path,
            "markdown",
        ],
    )
    assert result.exit_code == 0


def test_role_path(tmp_path):
    current_dir = os.getcwd()

    role = DEFAULT_ROLE

    output_dir = tmp_path
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / "README.md"

    os.chdir(ROLES_DIR)
    result = runner.invoke(app, ["--output-file", output_file, role, "markdown"])
    os.chdir(current_dir)

    assert result.exit_code == 0

    shutil.copytree(ROLES_DIR / role, output_dir / role)

    os.chdir(output_dir)
    result = runner.invoke(app, [role, "markdown"])
    os.chdir(current_dir)

    assert result.exit_code == 0


def test_markdown(tmp_path):
    for role_path in [x for x in ROLES_DIR.iterdir() if x.is_dir()]:
        role = role_path.stem
        readme_md = str(role_path / "README.md")
        role_path = str(role_path)

        output_dir = tmp_path / role
        output_dir.mkdir(exist_ok=True)

        output_file = output_dir / "README.md"

        result = runner.invoke(
            app, ["--output-file", output_file, role_path, "markdown"]
        )

        assert result.output == ""
        assert result.exit_code == 0
        assert filecmp.cmp(readme_md, output_file)

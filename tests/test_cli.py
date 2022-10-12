#!/usr/bin/env python3

import filecmp
import pathlib

from typer.testing import CliRunner

from ansible_docs.cli import app

ROLES_DIR = pathlib.Path("./tests/fixtures/roles")


runner = CliRunner()


def test_cli_help():
    result = runner.invoke(app, [])
    assert result.exit_code == 0

    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0


def test_cli_config_file(tmp_path):
    role_path = str(ROLES_DIR / "role001")

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


def test_output_mode(tmp_path):
    role_path = str(ROLES_DIR / "role001")

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
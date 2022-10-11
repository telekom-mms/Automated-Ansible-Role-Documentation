#!/usr/bin/env python3

import filecmp
import pathlib

from typer.testing import CliRunner

from ansible_docs.cli import app

ROLES_DIR = pathlib.Path("./tests/fixtures/roles")


runner = CliRunner()


def test_markdown(tmp_path):
    for role_path in [x for x in ROLES_DIR.iterdir() if x.is_dir()]:
        role = role_path.stem
        readme_md = str(role_path / "README.md")
        role_path = str(role_path)

        output = tmp_path / role
        output_file = output / "README.md"
        output.mkdir()

        result = runner.invoke(
            app, ["--output-file", output_file, role_path, "markdown"]
        )

        assert result.output == ""
        assert result.exit_code == 0
        assert filecmp.cmp(readme_md, output_file)

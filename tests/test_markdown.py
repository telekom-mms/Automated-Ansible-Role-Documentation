#!/usr/bin/env python3

import filecmp
import os
import pathlib
import shutil

from typer.testing import CliRunner

from aar_doc.cli import app

ROLES_DIR = pathlib.Path("./tests/fixtures/roles")
DEFAULT_ROLE = "minimum"


runner = CliRunner()


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


def test_inject_content(tmp_path):
    role_path = ROLES_DIR / "inject"

    readme_md = str(role_path / "README.md")
    role_path = str(role_path)

    output_dir = tmp_path
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / "README.md"

    shutil.copyfile(readme_md, output_file)

    result = runner.invoke(
        app,
        [
            "--output-file",
            output_file,
            role_path,
            "markdown",
        ],
    )

    assert result.exit_code == 0
    assert filecmp.cmp(readme_md, output_file)


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


def test_output_template(tmp_path):
    role_path = ROLES_DIR / "template"

    output_template = str(role_path / "template.j2")
    config_file = str(role_path / ".ansible-docs.yml")

    output_dir = tmp_path
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / "README.md"

    role = role_path.stem
    readme_md = str(role_path / "README.md")
    role_path = str(role_path)

    output_dir = tmp_path / role
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / "README.md"

    result = runner.invoke(
        app,
        [
            "--output-file",
            output_file,
            "--output-template",
            output_template,
            role_path,
            "markdown",
        ],
    )

    assert result.exit_code == 0
    assert filecmp.cmp(readme_md, output_file)

    result = runner.invoke(
        app,
        [
            "--output-file",
            output_file,
            "--config-file",
            config_file,
            role_path,
            "markdown",
        ],
    )

    assert result.exit_code == 0
    assert filecmp.cmp(readme_md, output_file)


def test_markdown(tmp_path):
    roles = ["minimum", "extended", "multiple_entrypoints", "no_options", "multiline", "markup"]

    for role_path in [ROLES_DIR / x for x in roles]:
        role = role_path.stem
        readme_md = str(role_path / "README.md")
        role_path = str(role_path)

        output_dir = tmp_path / role
        output_dir.mkdir(exist_ok=True)

        output_file = output_dir / "README.md"

        result = runner.invoke(
            app,
            ["--output-file", output_file, role_path, "markdown"],
        )

        assert result.output == ""
        assert result.exit_code == 0
        assert filecmp.cmp(readme_md, output_file)


def test_meta_main_yaml(tmp_path):
    role_path = ROLES_DIR / "meta_main_yaml"
    readme_md = str(role_path / "README.md")
    role_path = str(role_path)

    output_dir = tmp_path
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / "README.md"

    result = runner.invoke(
        app,
        [
            "--output-file",
            output_file,
            role_path,
            "markdown",
        ],
    )

    assert result.exit_code == 0
    assert filecmp.cmp(readme_md, output_file)


def test_missing_arg_spec(tmp_path):
    role_path = ROLES_DIR / "missing_arg_spec"
    role_path = str(role_path)

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
    assert result.output == "Could not find meta/main.y[a]ml\n"
    assert result.exit_code == 1


def test_missing_meta_main_yaml(tmp_path):
    role_path = ROLES_DIR / "missing_meta_main_yaml"
    role_path = str(role_path)

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
    assert result.output == "Could not find meta/main.y[a]ml\n"
    assert result.exit_code == 1


def test_wrong_type(tmp_path):
    role_path = ROLES_DIR / "wrong_type"
    role_path = str(role_path)

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
    assert (
        result.output
        == "The default value of the argument myapp_int is of type int, need str\n"
    )
    assert result.exit_code == 1


def test_missing_doc_string(tmp_path):
    role_path = ROLES_DIR / "missing_doc_strings"

    role_path = str(role_path)

    output_dir = tmp_path
    output_dir.mkdir(exist_ok=True)

    result = runner.invoke(
        app,
        [
            role_path,
            "markdown",
        ],
    )
    assert (
        result.output
        == "Could not find <!-- BEGIN_ANSIBLE_DOCS --> in the output file\n"
    )
    assert result.exit_code == 1


def test_expand_home_path(tmp_path):
    os.environ["HOME"] = str(ROLES_DIR / "home_dir_expand/")

    role_path = pathlib.Path("~/")
    readme_md = pathlib.Path("~/README.md").expanduser()
    config_file = str(role_path / ".ansible-docs.yml")

    output_dir = tmp_path
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "README.md"

    result = runner.invoke(
        app,
        [
            "--config-file",
            config_file,
            "--output-file",
            output_file,
            os.environ["HOME"],
            "markdown",
        ],
    )
    print(result.output)
    assert result.exit_code == 0
    assert filecmp.cmp(readme_md, output_file)

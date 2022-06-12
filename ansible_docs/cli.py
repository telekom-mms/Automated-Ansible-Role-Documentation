#!/usr/bin/env python3

import pathlib

from enum import Enum

import jinja2
import typer
import yaml

app = typer.Typer()
state = {}


class OutputMode(str, Enum):
    inject = "inject"
    replace = "replace"


@app.command()
def markdown() -> None:
    """
    Command for generating role documentation in Markdown format.
    """

    content = render_content("markdown.j2")
    write(content)


@app.callback()
def cli(
    role_path: pathlib.Path = typer.Argument(
        ...,
        help="Path to an Ansible role",
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
        writable=True,
        resolve_path=True,
    ),
    output_file: str = typer.Option(
        "README.md",
        file_okay=True,
        dir_okay=False,
        readable=True,
        writable=True,
    ),
    output_template: str = "<!-- BEGIN_ANSIBLE_DOCS -->\n{{ content }}\n<!-- END_ANSIBLE_DOCS -->\n\n",
    output_mode: OutputMode = typer.Option(OutputMode.inject.name),
):
    """
    A tool for generating docs for Ansible roles.
    """

    state["role"] = role_path.stem
    state["role_path"] = role_path
    state["output_file"] = output_file
    state["output_template"] = output_template
    state["output_mode"] = output_mode

    state["metadata"], state["argument_specs"] = parse_meta()


def write(content: str) -> None:
    """
    Writes a content string to the given file.
    """

    output = pathlib.Path(state["output_file"])

    if not "/" in state["output_file"]:
        output = state["role_path"] / output

    output.resolve()

    if not output.exists():
        state["output_mode"] = OutputMode.replace

    with open(output, "a+") as f:
        if state["output_mode"] == OutputMode.inject:
            f.seek(0)
            lines = f.readlines()

            begin = lines.index("<!-- BEGIN_ANSIBLE_DOCS -->\n")
            end = lines.index("<!-- END_ANSIBLE_DOCS -->\n")

            header = [*lines[:begin]]
            footer = [*lines[1 + end :]]

            content = "".join(header + [content] + footer)

        f.truncate(0)
        f.write(content)


def parse_meta() -> tuple[dict, dict]:
    """
    Parses Ansible role metadata from YAML files in the meta/ directory.
    """

    meta = state["role_path"] / "meta"

    argument_specs_yml = list(meta.glob("argument_specs.y*ml"))[0]
    main_yml = list(meta.glob("main.y*ml"))[0]

    with open(argument_specs_yml, "r") as f:
        argument_specs = yaml.safe_load(f)
        argument_specs = argument_specs["argument_specs"]

    with open(main_yml, "r") as f:
        main = yaml.safe_load(f)

    return main, argument_specs


def render_content(content_template: str) -> str:
    """
    Renders Jinja2 templates twice, the first time to get the parsed
    data into {{ content }} and finally to render the user provided
    (or default) output template to be written to the file.
    """

    templates = pathlib.Path(__file__).parent.parent / "templates"
    loader = jinja2.FileSystemLoader(templates)

    env = jinja2.Environment(loader=loader)
    content = env.get_template(content_template).render(
        role=state["role"],
        metadata=state["metadata"],
        argument_specs=state["argument_specs"],
    )

    env = jinja2.Environment()
    template = env.from_string(source=state["output_template"].replace("\\n", "\n"))

    return template.render(
        content=content,
        role=state["role"],
        metadata=state["metadata"],
        argument_specs=state["argument_specs"],
    )


if __name__ == "__main__":
    app()

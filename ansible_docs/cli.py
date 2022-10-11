#!/usr/bin/env python3

import pathlib
from enum import Enum

import jinja2
import typer
import yaml

app = typer.Typer(no_args_is_help=True)


class OutputMode(str, Enum):
    inject = "inject"
    replace = "replace"


def parse_config(
    ctx: typer.Context, param: typer.CallbackParam, config_file: pathlib.Path
) -> pathlib.Path:
    # FIXME: This will change the defaults when called with --help
    #
    # See: https://github.com/tiangolo/typer/issues/347
    if config_file.exists():
        try:
            with open(config_file, "r") as f:
                content = yaml.safe_load(f)

                ctx.default_map = ctx.default_map or {}
                ctx.default_map.update(content)
        except Exception as ex:
            raise typer.BadParameter(str(ex))

    return config_file


@app.command()
def markdown(ctx: typer.Context) -> None:
    """
    Command for generating role documentation in Markdown format.
    """

    # FIXME: ctx should not be passed to these non-command()'s
    content = render_content(ctx, "markdown.j2")
    write(ctx, content)


@app.callback()
def cli(
    ctx: typer.Context,
    config_file: pathlib.Path = typer.Option(
        ".ansible-docs.yml",
        file_okay=True,
        dir_okay=False,
        readable=True,
        is_eager=True,
        callback=parse_config,
    ),
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
    output_file: pathlib.Path = typer.Option(
        "README.md",
        file_okay=True,
        dir_okay=False,
        readable=True,
        writable=True,
    ),
    output_template: str = "<!-- BEGIN_ANSIBLE_DOCS -->\n{{ content }}\n<!-- END_ANSIBLE_DOCS -->\n",
    output_mode: OutputMode = typer.Option(OutputMode.inject.name),
):
    """
    A tool for generating docs for Ansible roles.
    """

    ctx.ensure_object(dict)

    ctx.obj["data"] = {}
    ctx.obj["config"] = {}

    ctx.obj["config"]["role"] = role_path.stem
    ctx.obj["config"]["role_path"] = role_path
    ctx.obj["config"]["output_file"] = output_file
    ctx.obj["config"]["output_template"] = output_template
    ctx.obj["config"]["output_mode"] = output_mode

    (
        ctx.obj["data"]["metadata"],
        ctx.obj["data"]["argument_specs"],
    ) = parse_meta(ctx)


def write(ctx: typer.Context, content: str) -> None:
    """
    Writes a content string to the given file.
    """

    output = ctx.obj["config"]["output_file"]

    if not "/" in str(output):
        output = ctx.obj["config"]["role_path"] / output

    output.resolve()

    if not output.exists():
        ctx.obj["config"]["output_mode"] = OutputMode.replace

    with open(output, "a+") as f:
        if ctx.obj["config"]["output_mode"] == OutputMode.inject:
            f.seek(0)
            lines = f.readlines()

            begin = lines.index("<!-- BEGIN_ANSIBLE_DOCS -->\n")
            end = lines.index("<!-- END_ANSIBLE_DOCS -->\n")

            header = [*lines[:begin]]
            footer = [*lines[1 + end :]]

            content = "".join(header + [content] + footer)

        f.truncate(0)
        f.write(content)


def parse_meta(ctx: typer.Context) -> tuple[dict, dict]:
    """
    Parses Ansible role metadata from YAML files in the meta/ directory.
    """

    meta = ctx.obj["config"]["role_path"] / "meta"

    argument_specs_yml = list(meta.glob("argument_specs.y*ml"))[0]
    main_yml = list(meta.glob("main.y*ml"))[0]

    with open(argument_specs_yml, "r") as f:
        argument_specs = yaml.safe_load(f)
        argument_specs = argument_specs["argument_specs"]

    with open(main_yml, "r") as f:
        main = yaml.safe_load(f)

    return main, argument_specs


def render_content(ctx: typer.Context, content_template: str) -> str:
    """
    Renders Jinja2 templates twice, the first time to get the parsed
    data into {{ content }} and finally to render the user provided
    (or default) output template to be written to the file.
    """

    templates = pathlib.Path(__file__).parent.parent / "templates"
    loader = jinja2.FileSystemLoader(templates)

    env = jinja2.Environment(loader=loader)
    content = env.get_template(content_template).render(
        role=ctx.obj["config"]["role"],
        metadata=ctx.obj["data"]["metadata"],
        argument_specs=ctx.obj["data"]["argument_specs"],
    )

    env = jinja2.Environment()
    template = env.from_string(
        source=ctx.obj["config"]["output_template"].replace("\\n", "\n")
    )

    return template.render(
        content=content,
        role=ctx.obj["config"]["role"],
        metadata=ctx.obj["data"]["metadata"],
        argument_specs=ctx.obj["data"]["argument_specs"],
    )


if __name__ == "__main__":
    app()

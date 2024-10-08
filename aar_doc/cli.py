#!/usr/bin/env python3
"""
Main class for aar_doc
"""

import pathlib

import typer

from aar_doc.core import (
    OutputMode,
    parse_choices,
    parse_collection,
    parse_config,
    parse_meta,
    parse_options,
    render_content,
)
from aar_doc.defaults import generate_defaults, write_defaults
from aar_doc.markdown import write_markdown

app = typer.Typer(no_args_is_help=True)


@app.command()
def markdown(ctx: typer.Context) -> None:
    """
    Command for generating role documentation in Markdown format.
    """
    content = render_content(ctx, "markdown.j2")
    write_markdown(ctx, content)


@app.command()
def defaults(ctx: typer.Context) -> None:
    """
    Command for generating role defaults.
    """
    role_defaults = generate_defaults(ctx)
    if not role_defaults:
        typer.echo("No defaults configured in argument_specs. Nothing to do.")
        raise typer.Exit(code=0)
    write_defaults(ctx, role_defaults)


@app.callback()
def cli(
    ctx: typer.Context,
    config_file: pathlib.Path = typer.Option(  # pylint: disable=W0613
        ".aar_doc.yml",
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
    output_template: str = typer.Option(
        "<!-- BEGIN_ANSIBLE_DOCS -->\n{{ content }}\n<!-- END_ANSIBLE_DOCS -->\n",
        help="Output template as a string or a path to a file.",
    ),
    output_mode: OutputMode = typer.Option(OutputMode.INJECT.value),
) -> None:
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

    ctx.obj["data"]["galaxy_collection"] = parse_collection(ctx)

    ctx.obj["data"]["entrypoint_options"] = parse_options(ctx)

    ctx.obj["data"]["entrypoint_choices"] = parse_choices(ctx)


if __name__ == "__main__":
    app()  # pragma: no cover

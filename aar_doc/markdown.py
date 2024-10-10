"""
Markdown module for aar_doc.

This module provides the utilities for writing the final markdown file.
"""

import typer

from aar_doc.core import OutputMode


def write_markdown(ctx: typer.Context, content: str) -> None:
    """
    Writes a content string to the given file.
    """

    output = ctx.obj["config"]["output_file"].expanduser()

    if "/" not in str(output):
        output = ctx.obj["config"]["role_path"] / output

    output.resolve()

    if not output.exists():
        ctx.obj["config"]["output_mode"] = OutputMode.REPLACE

    with open(output, "a+", encoding="utf-8") as f:
        if ctx.obj["config"]["output_mode"] == OutputMode.INJECT:
            f.seek(0)
            lines = f.readlines()

            try:
                begin = lines.index("<!-- BEGIN_ANSIBLE_DOCS -->\n")
            except ValueError as exc:
                typer.echo(
                    "Could not find <!-- BEGIN_ANSIBLE_DOCS --> in the output file",
                )
                raise typer.Exit(code=1) from exc

            try:
                end = lines.index("<!-- END_ANSIBLE_DOCS -->\n")
            except ValueError as exc:
                typer.echo(
                    "Could not find <!-- END_ANSIBLE_DOCS --> in the output file",
                )
                raise typer.Exit(code=1) from exc

            header = [*lines[:begin]]
            footer = [*lines[1 + end :]]

            content = "".join(header + [content] + footer)

        f.truncate(0)
        f.write(content)

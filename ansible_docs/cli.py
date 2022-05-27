#!/usr/bin/env python3

import pathlib

import click
import jinja2
import yaml


@click.group()
@click.pass_context
@click.argument(
    "role_path",
    type=click.Path(
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
        writable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
)
@click.option(
    "--output-file",
    help="The output file, by default written into the role's directory",
    default="README.md",
    type=click.Path(
        file_okay=True,
        dir_okay=False,
        readable=True,
        writable=True,
    ),
)
@click.option(
    "--output-template",
    help="The output template string",
    default="<!-- BEGIN_ANSIBLE_DOCS -->\n{{ content }}\n<!-- END_ANSIBLE_DOCS -->\n\n",
    type=click.STRING,
)
@click.option(
    "--output-mode",
    help="The output mode",
    default="inject",
    type=click.Choice(["inject", "replace"], case_sensitive=True),
)
def cli(
    ctx: click.Context,
    role_path: pathlib.Path,
    output_file: str,
    output_template: str,
    output_mode: str,
):
    """
    Acts as the main entrypoint for all commands.
    """

    ctx.ensure_object(dict)

    ctx.obj["role"] = role_path.stem
    ctx.obj["role_path"] = role_path
    ctx.obj["output_file"] = output_file
    ctx.obj["output_template"] = output_template
    ctx.obj["output_mode"] = output_mode

    ctx.obj["metadata"], ctx.obj["argument_specs"] = parse_meta(role_path)


@cli.command()
@click.pass_context
def markdown(ctx: click.Context) -> None:
    """
    Command for generating role documentation in Markdown format.
    """

    role = ctx.obj["role"]
    role_path = ctx.obj["role_path"]
    output_file = ctx.obj["output_file"]
    output_template = ctx.obj["output_template"]
    output_mode = ctx.obj["output_mode"]
    metadata = ctx.obj["metadata"]
    argument_specs = ctx.obj["argument_specs"]

    content = render_content(
        "markdown.j2", output_template, role, metadata, argument_specs
    )

    write(role_path, output_file, output_mode, content)


def write(
    role_path: pathlib.Path, output_file: str, output_mode: str, content: str
) -> None:
    """
    Writes a content string to the given file.
    """

    output = pathlib.Path(output_file)

    if not "/" in output_file:
        output = role_path / output

    output.resolve()

    if not output.exists():
        output_mode = "replace"

    with open(output, "a+") as f:
        if output_mode == "inject":
            f.seek(0)
            lines = f.readlines()

            begin = lines.index("<!-- BEGIN_ANSIBLE_DOCS -->\n")
            end = lines.index("<!-- END_ANSIBLE_DOCS -->\n")

            header = [*lines[:begin]]
            footer = [*lines[1 + end :]]

            content = "".join(header + [content] + footer)

        f.truncate(0)
        f.write(content)


def parse_meta(role_path: pathlib.Path) -> tuple[dict, dict]:
    """
    Parses Ansible role metadata from YAML files in the meta/ directory.
    """

    meta = role_path / "meta"

    argument_specs_yml = list(meta.glob("argument_specs.y*ml"))[0]
    main_yml = list(meta.glob("main.y*ml"))[0]

    with open(argument_specs_yml, "r") as f:
        argument_specs = yaml.safe_load(f)
        argument_specs = argument_specs["argument_specs"]

    with open(main_yml, "r") as f:
        main = yaml.safe_load(f)

    return main, argument_specs


def render_content(
    content_template: str,
    output_template: str,
    role: str,
    metadata: dict,
    argument_specs: dict,
) -> str:
    """
    Renders Jinja2 templates twice, the first time to get the parsed
    data into {{ content }} and finally to render the user provided
    (or default) output template to be written to the file.
    """

    templates = pathlib.Path(__file__).parent / "templates"
    loader = jinja2.FileSystemLoader(templates)

    env = jinja2.Environment(loader=loader)
    content = env.get_template(content_template).render(
        role=role,
        metadata=metadata,
        argument_specs=argument_specs,
    )

    env = jinja2.Environment()
    template = env.from_string(source=output_template.replace("\\n", "\n"))

    return template.render(
        content=content, role=role, metadata=metadata, argument_specs=argument_specs
    )


if __name__ == "__main__":
    cli(obj={})

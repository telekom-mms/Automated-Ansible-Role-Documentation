#!/usr/bin/env python3

import json
import pathlib
from enum import Enum

import jinja2
import typer
import yaml

app = typer.Typer(no_args_is_help=True)


class OutputMode(Enum):
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

    ctx.obj["data"]["galaxy_collection"] = parse_collection(ctx)

    ctx.obj["data"]["entrypoint_options"] = parse_options(ctx)

    ctx.obj["data"]["entrypoint_choices"] = parse_choices(ctx)


def write(ctx: typer.Context, content: str) -> None:
    """
    Writes a content string to the given file.
    """

    output = ctx.obj["config"]["output_file"]

    if "/" not in str(output):
        output = ctx.obj["config"]["role_path"] / output

    output.resolve()

    if not output.exists():
        ctx.obj["config"]["output_mode"] = OutputMode.replace

    with open(output, "a+") as f:
        if ctx.obj["config"]["output_mode"] == OutputMode.inject:
            f.seek(0)
            lines = f.readlines()

            try:
                begin = lines.index("<!-- BEGIN_ANSIBLE_DOCS -->\n")
            except ValueError:
                typer.echo(
                    "Could not find <!-- BEGIN_ANSIBLE_DOCS --> in the output file"
                )
                raise typer.Exit(code=1)

            try:
                end = lines.index("<!-- END_ANSIBLE_DOCS -->\n")
            except ValueError:
                typer.echo(
                    "Could not find <!-- END_ANSIBLE_DOCS --> in the output file"
                )
                raise typer.Exit(code=1)

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

    try:
        argument_specs_yml = list(meta.glob("argument_specs.y*ml"))[0]
    except IndexError:
        typer.echo("Could not find meta/argument_specs.yml")
        raise typer.Exit(code=1)

    with open(argument_specs_yml, "r") as f:
        try:
            argument_specs = yaml.safe_load(f)
        except yaml.YAMLError:
            typer.echo("Not a valid YAML file: meta/argument_specs.yml")
            raise typer.Exit(1)
        try:
            argument_specs = argument_specs["argument_specs"]
        except TypeError:
            typer.echo("Could not read meta/argument_specs.yml")
            raise typer.Exit(1)

    try:
        main_yml = list(meta.glob("main.y*ml"))[0]
    except:
        typer.echo("Could not find meta/main.yml")
        raise typer.Exit(code=1)

    with open(main_yml, "r") as f:
        try:
            main = yaml.safe_load(f)
        except yaml.YAMLError:
            typer.echo("Not a valid YAML file: meta/main.yml")
            raise typer.Exit(1)

    return main, argument_specs


def parse_collection(ctx: typer.Context) -> dict:
    """
    Parses Ansible Galaxy collection metadata from YAML files.
    """

    collection_dir = ctx.obj["config"]["role_path"].parent.parent

    galaxy_files = list(collection_dir.glob("galaxy.y*ml"))

    if len(galaxy_files):
        galaxy_yml = galaxy_files[0]

        with open(galaxy_yml, "r") as f:
            collection = yaml.safe_load(f)

        return collection
    else:
        return {}


def gather_choices(path: list[str], arguments: dict) -> list[tuple[list[str], list]]:
    """
    Walks through an argument_specs 'options' section gathering choices for options
    and adding them to a list with a 'path' describing the entrypoint/options they
    belong to.
    """
    results = []
    options = arguments["options"]
    for name, details in options.items():
        if "choices" in details:
            results.append((path + [name], details["choices"]))
        if "options" in details:
            results.extend(gather_choices(path + [name], details))

    return results


def parse_choices(ctx: typer.Context) -> dict:
    """
    Parses argument_specs into options structure, with sections for subptions
    and translation of formats into display formats.
    """
    entrypoint_choices = {}
    for entrypoint, arguments in ctx.obj["data"]["argument_specs"].items():
        gathered_choices = gather_choices([entrypoint], arguments)
        entrypoint_choices[entrypoint] = gathered_choices

    return entrypoint_choices


def gather_options(path: list[str], arguments: dict) -> list[tuple[list[str], dict]]:
    """
    Walks through an argument_specs 'options' section gathering groups of suboptions
    and adding them to a list with a 'path' describing the entrypoint/options they
    belong to.
    """
    results = []
    options = arguments["options"]
    results.append((path, options))
    for name, details in options.items():
        if "options" in details:
            results.extend(gather_options(path + [name], details))

    return results


def parse_options(ctx: typer.Context) -> dict:
    """
    Parses argument_specs into options structure, with sections for subptions
    and translation of formats into display formats.
    """
    entrypoint_options = {}
    for entrypoint, arguments in ctx.obj["data"]["argument_specs"].items():
        gathered_options = gather_options([entrypoint], arguments)
        for path, options in gathered_options:
            for option, details in options.items():
                details["display_required"] = (
                    "yes" if details.get("required", False) else "no"
                )
                description = details["description"]
                details["display_description"] = (
                    (
                        description
                        if isinstance(description, str)
                        else (" ").join(description)
                    )
                    .replace("\n", " ")
                    .strip()
                )
                details["display_type"] = details.get("type", "str")
                details["display_default"] = ""
                if details["display_type"] == "bool":
                    details["display_default"] = (
                        "true" if details.get("default", False) else "false"
                    )
                elif details["display_type"] == "list":
                    if default := details.get("default", None):
                        details["display_default"] = json.dumps(default)
                    if "elements" in details:
                        if (details["elements"] == "dict") and ("options" in details):
                            details[
                                "display_type"
                            ] = f"list of dicts of '{option}' options"
                        else:
                            details["display_type"] = (
                                "list of '" + details["elements"] + "'"
                            )
                elif details["display_type"] == "dict":
                    if default := details.get("default", None):
                        details["display_default"] = json.dumps(default)
                    if "options" in details:
                        details["display_type"] = f"dict of '{option}' options"
                elif details["display_type"] == "str":
                    try:
                        details["display_default"] = details.get("default", "").strip()
                    except AttributeError:
                        typer.echo(
                            f"The default value of the argument {option} "
                            f"is of type {type(details.get('default')).__name__}, need str"
                        )
                        raise typer.Exit(code=1)
                else:
                    details["display_default"] = str(details.get("default", "")).strip()
        entrypoint_options[entrypoint] = gathered_options

    return entrypoint_options


def render_content(ctx: typer.Context, content_template: str) -> str:
    """
    Renders Jinja2 templates twice, the first time to get the parsed
    data into {{ content }} and finally to render the user provided
    (or default) output template to be written to the file.
    """

    env = jinja2.Environment(
        loader=jinja2.PackageLoader("aar_doc"),
        autoescape=jinja2.select_autoescape(),
        undefined=jinja2.StrictUndefined,
    )

    role = ctx.obj["config"]["role"]
    metadata = ctx.obj["data"]["metadata"]
    argument_specs = ctx.obj["data"]["argument_specs"]
    collection = ctx.obj["data"]["galaxy_collection"]
    entrypoint_options = ctx.obj["data"]["entrypoint_options"]
    entrypoint_choices = ctx.obj["data"]["entrypoint_choices"]

    if "namespace" in collection:
        role = collection["namespace"] + "." + collection["name"] + "." + role

    content = env.get_template(content_template).render(
        role=role,
        metadata=metadata,
        argument_specs=argument_specs,
        galaxy_collection=collection,
        entrypoint_options=entrypoint_options,
        entrypoint_choices=entrypoint_choices,
    )

    role_path = ctx.obj["config"]["role_path"]
    output_template = ctx.obj["config"]["output_template"].replace("\\n", "\n")

    try:
        output_template_file = pathlib.Path(output_template).resolve(strict=True)

        env = jinja2.Environment(
            keep_trailing_newline=True,
            loader=jinja2.FileSystemLoader([role_path, output_template_file.parent]),
        )
        template = env.get_template(output_template_file.name)
    except (FileNotFoundError, OSError):
        env = jinja2.Environment(
            keep_trailing_newline=True, loader=jinja2.FileSystemLoader(role_path)
        )
        template = env.from_string(source=output_template)

    return template.render(
        content=content,
        role=role,
        metadata=metadata,
        argument_specs=argument_specs,
        galaxy_collection=collection,
        entrypoint_options=entrypoint_options,
        entrypoint_choices=entrypoint_choices,
    )


if __name__ == "__main__":
    app()  # pragma: no cover

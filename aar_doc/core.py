"""
Core module for aar_doc.

This module provides utilities for processing Ansible role meta files
and rendering jinja2 templates from processing data.
"""

import json
import pathlib
from enum import Enum

import jinja2
import typer

from ruamel.yaml import YAML, YAMLError

yaml = YAML()
yaml.indent(mapping=2, sequence=2, offset=2)
yaml.version = "1.1"
yaml.encoding = "utf-8"
yaml.allow_unicode = True


class OutputMode(Enum):
    """
    Defines the options for the output mode.
    """

    INJECT = "inject"
    REPLACE = "replace"


def parse_config(
    ctx: typer.Context,
    config_file: pathlib.Path,
) -> None:
    """
    Parses the configuration file
    """
    # This will change the defaults when called with --help
    # See: https://github.com/tiangolo/typer/issues/347

    config_file_full_path: pathlib.Path = config_file.expanduser()

    if config_file_full_path.exists():
        try:
            with open(config_file_full_path, "r", encoding="utf-8") as f:
                content = yaml.load(f)

                ctx.default_map = ctx.default_map or {}
                ctx.default_map.update(content)
        except Exception as ex:
            raise typer.BadParameter(str(ex))


def parse_meta(ctx: typer.Context) -> tuple[dict, dict]:
    """
    Parses Ansible role metadata from YAML files in the meta/ directory.
    """

    meta: pathlib.Path = ctx.obj["config"]["role_path"] / "meta"
    argument_specs: dict = {}

    try:
        argument_specs_yml: pathlib.Path = list(meta.glob("argument_specs.y*ml"))[0]
        with open(argument_specs_yml, "r", encoding="utf-8") as f:
            try:
                argument_specs = yaml.load(f)
            except YAMLError:
                typer.echo("Not a valid YAML file: meta/argument_specs.y[a]ml")
            try:
                argument_specs = argument_specs.get("argument_specs", {})
            except TypeError:
                typer.echo("Could not read meta/argument_specs.y[a]ml")
    except (UnboundLocalError, IndexError):
        pass

    try:
        main_yml = list(meta.glob("main.y*ml"))[0]
    except IndexError as exc:
        typer.echo("Could not find meta/main.y[a]ml")
        raise typer.Exit(code=1) from exc

    with open(main_yml, "r", encoding="utf-8") as f:
        try:
            main = yaml.load(f)
        except YAMLError as exc:
            typer.echo("Not a valid YAML file: meta/main.y[a]ml")
            raise typer.Exit(1) from exc
        if not argument_specs:
            try:
                argument_specs = main["argument_specs"]
            except TypeError as exc:
                typer.echo(
                    "Could not read meta/main.y[a]ml or meta/argument_specs.y[a]ml",
                )
                raise typer.Exit(1) from exc
    return main, argument_specs


def parse_collection(ctx: typer.Context) -> dict:
    """
    Parses Ansible Galaxy collection metadata from YAML files.
    """

    collection_dir = ctx.obj["config"]["role_path"].parent.parent

    galaxy_files = list(collection_dir.glob("galaxy.y*ml"))

    if galaxy_files:
        galaxy_yml = galaxy_files[0]

        with open(galaxy_yml, "r", encoding="utf-8") as f:
            collection = yaml.load(f)

        return collection
    return {}


def gather_choices(path: list[str], arguments: dict) -> list[tuple[list[str], list]]:
    """
    Walks through an argument_specs 'options' section gathering choices for options
    and adding them to a list with a 'path' describing the entrypoint/options they
    belong to.
    """
    results = []
    if "options" in arguments:
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
    if "options" in arguments:
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
        for _, options in gathered_options:
            for option, details in options.items():
                details["display_required"] = (
                    "yes" if details.get("required", False) else "no"
                )
                description = details["description"] if "description" in details else ""
                details["display_description"] = (
                    (
                        description
                        if isinstance(description, str)
                        else (" ").join(description)
                    )
                    .replace("\n", " ")
                    .strip()
                )

                display_type = details.get("type", "str")

                if display_type == "list":
                    elements = details.get("elements", "")
                    if elements == "dict" and "options" in details:
                        display_type = f"list of dicts of '{option}' options"
                    else:
                        display_type = f"list of '{elements}'"
                elif display_type == "dict":
                    if "options" in details:
                        display_type = f"dict of '{option}' options"

                details["display_type"] = display_type

                if "default" in details:
                    default_value = details.get("default", "")
                    details["display_default"] = str(default_value).strip()

                    if display_type in ["list", "dict"]:
                        details["display_default"] = (
                            json.dumps(default_value) if default_value else ""
                        )

                    elif display_type == "str":
                        if not isinstance(default_value, str):
                            typer.echo(
                                f"The default value of the argument {option} "
                                f"is of type {type(default_value).__name__}, need str",
                            )
                            raise typer.Exit(1)

                else:
                    details["display_default"] = ""

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

    role_path: pathlib.Path = ctx.obj["config"]["role_path"]
    output_template: str = ctx.obj["config"]["output_template"].replace("\\n", "\n")

    try:
        output_template_file = pathlib.Path(output_template).resolve(strict=True)

        env = jinja2.Environment(
            keep_trailing_newline=True,
            loader=jinja2.FileSystemLoader([role_path, output_template_file.parent]),
        )
        template = env.get_template(output_template_file.name)
    except (FileNotFoundError, OSError):
        env = jinja2.Environment(
            keep_trailing_newline=True,
            loader=jinja2.FileSystemLoader(role_path),
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

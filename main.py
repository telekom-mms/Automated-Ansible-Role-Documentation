#!/usr/bin/env python3

import textwrap
import yaml
import click
import pathlib

from jinja2 import Environment


@click.group()
def cli():
    pass


@cli.command()
@click.argument(
    "role",
    type=click.Path(
        exists=True,
        file_okay=False,
        readable=True,
        writable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
)
@click.option(
    "--output-file",
    help="The output file",
    default="README.md",
    type=click.File("a+", lazy=True),
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
def markdown(
    role: pathlib.Path,
    output_file: click.File,
    output_template: str,
    output_mode: str,
) -> None:
    env = Environment()
    template = env.from_string(source=output_template.replace("\\n", "\n"))

    metadata, argument_specs = parse_meta(role.stem)

    content = [
        template.render(
            content=generate_content(role.stem, metadata, argument_specs),
            role=role.stem,
            metadata=metadata,
            argument_specs=argument_specs,
        )
    ]

    if output_mode == "inject":
        output_file.seek(0)
        lines = output_file.readlines()

        begin = lines.index("<!-- BEGIN_ANSIBLE_DOCS -->\n")
        end = lines.index("<!-- END_ANSIBLE_DOCS -->\n")

        header = [*lines[:begin]]
        footer = [*lines[1 + end :]]

        content = header + content + footer

    output_file.truncate(0)
    output_file.write("".join(content))


def parse_meta(role: str) -> tuple[dict, dict]:
    meta = pathlib.Path(f"{role}/meta")

    argument_specs_yml = list(meta.glob("argument_specs.y*ml"))[0]
    main_yml = list(meta.glob("main.y*ml"))[0]

    with open(argument_specs_yml, "r") as f:
        argument_specs = yaml.safe_load(f)
        argument_specs = argument_specs["argument_specs"]

    with open(main_yml, "r") as f:
        main = yaml.safe_load(f)

    return main, argument_specs


def generate_content(role: str, metadata: dict, argument_specs: dict) -> str:
    content = """
    Ansible Role: {{ role | capitalize }}
    =========

    {{ metadata.galaxy_info.description }}

    Tags: {{ metadata.galaxy_info.galaxy_tags | join(', ') }}

    Requirements
    ------------

    | Platform | Versions |
    | -------- | -------- |
    {%- for platform in metadata.galaxy_info.platforms %}
    | {{ platform.name }} | {{ platform.versions | join(', ') }} |
    {%- endfor %}

    Role Variables
    --------------
    {% for entrypoint, specs in argument_specs | items %}
    ## {{ entrypoint }}

    {{ specs.short_description }}

    | Variable | Description | Type | Required | Default |
    | -------- | ----------- | ---- | -------- | ------- |
    {%- for name, variable in specs.options | items %}
    | {{ name }} | {{ variable.description }} | {{ variable.type }} | {{ 'yes' if variable.required else 'no' }} | {{ variable.default }} |
    {%- endfor %}
    {% endfor %}

    Dependencies
    ------------
    {% for dependency in metadata.dependencies %}
    - {{ dependency }}
    {%- endfor %}

    Example Playbook
    ----------------

    ```
    - hosts: all
      tasks:
        - name: Importing role: {{ role }}
          ansible.builtin.import_role:
            name: {{ role }}
          vars:
            {% for name, variable in argument_specs.main.options | items -%}
            {%- if variable.required -%}
            {{ name }}:
            {%- endif %}
            {% endfor %}
    ```

    License
    -------

    {{ metadata.galaxy_info.license }}

    Author Information
    ------------------

    {{ metadata.galaxy_info.author }} @ {{ metadata.galaxy_info.company }}

    Issues: {{ metadata.galaxy_info.issue_tracker_url }}
    """

    env = Environment()
    template = env.from_string(source=textwrap.dedent(content.lstrip("\n")))

    return template.render(role=role, metadata=metadata, argument_specs=argument_specs)


if __name__ == "__main__":
    cli()

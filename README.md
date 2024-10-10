# aar-doc - Automated Ansible Role Documentation

`aar-doc` is a tool for generating documentation and defaults automatically from an Ansible role's metadata. Specifically, it reads the `meta/main.yml` and `meta/argument_specs.yml` files.

This is heavily inspired by [terraform-docs](https://github.com/terraform-docs/terraform-docs) which does a similar thing with Terraform modules. `aar-doc` isn't nearly as featureful though, but should do the trick!

For instance, the only output format supported is Markdown. As with `terraform-docs`, you are able to override the default template however. As Ansible users are familiar with [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) `aar-doc` uses it for templating.

Contributions are welcome to add support for more output formats!

## Installation

As `aar-doc` is a Python utility and [exists](https://pypi.org/project/aar-doc/) on PyPI , the usual `pip install` works:

``` sh
pip install aar-doc
```

## Usage

```text
 Usage: aar-doc [OPTIONS] ROLE_PATH COMMAND [ARGS]...

 A tool for generating docs for Ansible roles.

╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    role_path      DIRECTORY  Path to an Ansible role [default: None]       │
│                                [required]                                    │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --config-file               FILE              [default: .aar_doc.yml]        │
│ --output-file               FILE              [default: README.md]           │
│ --output-template           TEXT              Output template as a string or │
│                                               a path to a file.              │
│                                               [default: <!--                 │
│                                               BEGIN_ANSIBLE_DOCS -->         │
│                                               {{ content }}                  │
│                                               <!-- END_ANSIBLE_DOCS -->      │
│                                               ]                              │
│ --output-mode               [inject|replace]  [default: inject]              │
│ --install-completion                          Install completion for the     │
│                                               current shell.                 │
│ --show-completion                             Show completion for the        │
│                                               current shell, to copy it or   │
│                                               customize the installation.    │
│ --help                                        Show this message and exit.    │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ defaults   Command for generating role defaults.                             │
│ markdown   Command for generating role documentation in Markdown format.     │
╰──────────────────────────────────────────────────────────────────────────────╯
```

### Configuration

The configuration options can be provided either via CLI arguments shown in `--help`, or a `--config-file` in YAML format. Note that the options have underscores when provided via the configuration file.

Examples:

```sh
aar-doc --output-file ROLE.md --output-mode replace ...
```

```yaml
---
output_file: ROLE.md
output_mode: replace
```

### Defaults

The defaults are written to the `defaults/main.yml` file in your provided role.

If you want to write them to a different file under `defaults/` you can specify that file via the `--output-file` option.

If your `argument_specs` contains an option with a default value multiple times, it will use the first found value and description by default. If you want the value and description to be overwritten, you can use the `--overwrite-duplicates` option.

### Markdown

#### Modes

The `inject` mode will inject only the changed content in between the `BEGIN_ANSIBLE_DOCS` and `END_ANSIBLE_DOCS` markers. This makes it possible to have header and footer text in the file that is not touched. This is the default mode, and will revert to `replace` if the file does not exist to create it the first time.

The `replace` mode will replace the whole file with the template. Usually, the `inject` mode should be fine for regular usage and changing the mode is not necessary unless you want to overwrite an existing file.

#### Templating

You can override the `--output-template` used for rendering the document. This may be passed in as a string containing Jinja2, or a path to a file. As noted above, this option may be passed in via CLI or the configuration file.

In the configuration file, easiest is to do a multiline string:

```yaml
---
output_template: |
  <!-- BEGIN_ANSIBLE_DOCS -->

  This is my role: {{ role }}

  <!-- END_ANSIBLE_DOCS -->
```

As noted above, the template _must_ start and end with the markers as comments, for the content injection to work.

`{{ content }}` will contain the rendered builtin output specific template content. For Markdown, see [templates/markdown.j2](./templates/markdown.j2).

You will most likely want to skip using it in your own template however, and use the provided variables containing the [role metadata](https://galaxy.ansible.com/docs/contributing/creating_role.html#role-metadata) and [argument specs](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html#specification-format) directly. `aar-doc` does not manipulate the values coming in from the YAML files in any way.

Template variables:

- `role`: The role name
- `content`: Whole content as pre-rendered by the built in templates
- `metadata`: Metadata read from `meta/main.yml`
- `argument_specs`: Metadata read from `meta/argument_specs.yml`

Example:

```jinja2
<!-- BEGIN_ANSIBLE_DOCS -->

This is my role: {{ role }}

<!-- 'metadata' contains all the things in meta/main.yml -->
{{ metadata.galaxy_info.license }}

<!-- All the usual Jinja2 filters are available -->
{{ metadata.galaxy_info.galaxy_tags | sort }}

<!-- Including files is also possible in relation to the role's directory with Jinja2's include directive -->
{% include "defaults/main.yml" %}

<!-- 'argument_specs' contains all the things in meta/argument_specs.yml -->
{% for entrypoint, specs in argument_specs | items %}
Task file name: {{ entrypoint }}.yml has {{ specs | length }} input variables!
{% endfor %}
<!-- END_ANSIBLE_DOCS -->
```

```sh
aar-doc --output-template ./path/to/template.j2 ...
```

More examples can be found in the [tests](./tests/).

## License

MIT

## Aknowledgements

- Kudos to the original author [Miika Kankare](https://github.com/quulah)!
- Kudos to [Kevin P. Fleming](https://github.com/kpfleming) for his additions to the original project!

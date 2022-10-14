# ansible-docs

`ansible-docs` is a tool for generating documentation automatically from an Ansible role's metadata. Specifically, it reads the `meta/main.yml` and `meta/argument_specs.yml` files.

This is heavily inspired by [terraform-docs](https://github.com/terraform-docs/terraform-docs) which does a similar thing with Terraform modules. `ansible-docs` isn't nearly as featureful though, but should do the trick!

For instance, the only output format supported is Markdown. As with `terraform-docs`, you are able to override the default template however. As Ansible users are familiar with [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) `ansible-docs` uses it for templating.

Contributions are welcome to add support for more output formats!

## Installation

As `ansible-docs` is a Python utility, the usual `pip install` works, but the tool isn't (yet) published in Pypi. So you'll need to point `pip` at the repository itself:

``` sh
pip install git+https://gitlab.com/kankare/ansible-docs
```

## Usage

``` sh
Usage: ansible-docs [OPTIONS] ROLE_PATH COMMAND [ARGS]...

  A tool for generating docs for Ansible roles.

Arguments:
  ROLE_PATH  Path to an Ansible role  [required]

Options:
  --config-file FILE              [default: .ansible-docs.yml]
  --output-file FILE              [default: README.md]
  --output-template TEXT          Output template as a string or a path to a
                                  file.  [default: <!-- BEGIN_ANSIBLE_DOCS -->
                                  {{ content }} <!-- END_ANSIBLE_DOCS --> ]
  --output-mode [inject|replace]  [default: inject]
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  markdown  Command for generating role documentation in Markdown format.
```

### Modes

The `inject` mode will inject only the changed content in between the `BEGIN_ANSIBLE_DOCS` and `END_ANSIBLE_DOCS` markers. This makes it possible to have header and footer text in the file that is not touched. This is the default mode, and will revert to `replace` if the file does not exist to create it the first time.

The `replace` mode will replace the whole file with the template. Usually, the `inject` mode should be fine for regular usage and changing the mode is not necessary unless you want to overwrite an existing file.

### Configuration

The configuration options can be provided either via CLI arguments shown in `--help`, or a `--config-file` in YAML format.

You can override the `--output-template` used for rendering the document. This may be passed in as a string containing Jinja2, or a path to a file. The template must start and end with the markers as comments.

Examples:

``` yaml
---
output_file: ROLE.md
output_template: |
  <!-- BEGIN_ANSIBLE_DOCS -->
  {{ content }}
  
  <!-- Metadata is directly accessible as 'metadata' and 'argument_specs' -->
  {{ metadata.galaxy_info.author }} wrote this Markdown!
  
  There's {{ argument_specs.main.options | length }} input variables for main.yml.
  <!-- END_ANSIBLE_DOCS -->
output_mode: replace
```

``` sh
ansible-docs --output-file ROLE.md --output-template ./path/to/template.j2 --output-mode replace ...
```

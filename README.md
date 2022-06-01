# ansible-docs

`ansible-docs` is a tool for generating documentation automatically from an Ansible role's metadata. Specifically, it reads the `meta/main.yml` and `meta/argument_specs.yml` files.

This is heavily inspired by [terraform-docs](https://github.com/terraform-docs/terraform-docs) which does a similar thing with Terraform modules. `ansible-docs` isn't nearly as featureful though, but should do the trick!

For instance, the only output format supported is Markdown. As with `terraform-docs`, you are able to override the default template however. As Ansible users are familiar with [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) `ansible-docs` uses it for templating.

Contributions are welcome to add support for more output formats!

## Installation

As `ansible-docs` is a Python utility, the usual `pip install` works, but the tool isn't (yet) published in Pypi. So you'll need to point `pip` at the repository itself:

``` sh
pip install git+https://gitlab.com/quulah/ansible-docs
```

## Usage

``` sh
Usage: ansible-docs [OPTIONS] ROLE_PATH COMMAND [ARGS]...

  A tool for generating docs for Ansible roles.

Options:
  --output-file FILE              The output file, by default written into the
                                  role's directory
  --output-template TEXT          The output template string
  --output-mode [inject|replace]  The output mode
  --help                          Show this message and exit.

Commands:
  markdown  Command for generating role documentation in Markdown format.
```

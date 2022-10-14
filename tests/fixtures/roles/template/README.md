<!-- BEGIN_ANSIBLE_DOCS -->

template

{'galaxy_info': {'role_name': 'template', 'author': 'your name', 'description': 'Test role with a custom template for the output', 'company': 'ansible-docs', 'license': 'MIT', 'min_ansible_version': '1.2', 'platforms': [{'name': 'Fedora', 'versions': ['all']}]}}

{'main': {'short_description': 'The main entry point for the minimum role.', 'options': {'myapp_int': {'type': 'int', 'required': False, 'default': 42, 'description': 'The integer value, defaulting to 42.'}, 'myapp_str': {'type': 'str', 'required': True, 'description': 'The string value'}}}}

<!-- We can do Jinja2 things -->
Here's our `defaults/main.yml`:

```yaml
---
myapp_int: 42
# myapp_str:

```

<!-- We can also do Markdown things -->

> A quote!

<!-- END_ANSIBLE_DOCS -->

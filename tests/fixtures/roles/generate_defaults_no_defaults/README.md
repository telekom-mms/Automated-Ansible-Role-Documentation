<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: generate_defaults_no_defaults

Test generation of defaults

## Requirements

| Platform | Versions |
| -------- | -------- |
| Fedora | all |

## Role Arguments

### Entrypoint: main

The main entry point for the defaults_no_defaults role.

| Option | Description | Type | Required | Default |
| ------ | ----------- | ---- | -------- | ------- |
| generate_defaults_no_defaults_foo | A string value for foo | str | yes |  |
| generate_defaults_no_defaults_bar | A string value for bar | str | yes |  |

## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Importing role: generate_defaults_no_defaults
      ansible.builtin.import_role:
        name: generate_defaults_no_defaults
      vars:
        generate_defaults_no_defaults_foo: # required, type: str
        generate_defaults_no_defaults_bar: # required, type: str
```

## License

MIT

## Author and Project Information

your name @ ansible-docs

<!-- END_ANSIBLE_DOCS -->

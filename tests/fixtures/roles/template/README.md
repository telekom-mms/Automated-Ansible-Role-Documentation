<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: template

Test role with a custom template for the output

## Requirements

| Platform | Versions |
| -------- | -------- |
| Fedora | all |

## Role Arguments

### Entrypoint: main

The main entry point for the minimum role.

| Option | Description | Type | Required | Default |
| ------ | ----------- | ---- | -------- | ------- |
| myapp_int | The integer value, defaulting to 42. | int | no | `42` |
| myapp_str | The string value | str | yes |  |

## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Importing role: template
      ansible.builtin.import_role:
        name: template
      vars:
        myapp_str: # required, type: str
```

## License

MIT

## Author and Project Information

your name @ ansible-docs

<!-- END_ANSIBLE_DOCS -->

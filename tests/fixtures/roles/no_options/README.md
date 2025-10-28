<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: no_options

Test role with no options

## Requirements

| Platform | Versions |
| -------- | -------- |
| Fedora | all |

## Role Arguments

### Entrypoint: main

The main entry point for the no_options role.

This entrypoint has no options.

## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Importing role: no_options
      ansible.builtin.import_role:
        name: no_options
      vars:
```

## License

MIT

## Author and Project Information

your name @ ansible-docs

<!-- END_ANSIBLE_DOCS -->

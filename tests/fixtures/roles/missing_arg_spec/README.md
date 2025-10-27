<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: missing_arg_spec

Test role without argument_specs

## Requirements

| Platform | Versions |
| -------- | -------- |
| Fedora | all |

## Role Arguments

No arguments are defined for this role.

## Dependencies

None.

## Example Playbook

```
- hosts: all
  tasks:
    - name: Importing role: missing_arg_spec
      ansible.builtin.import_role:
        name: missing_arg_spec
      vars:
```

## License

MIT

## Author and Project Information

your name @ ansible-docs

<!-- END_ANSIBLE_DOCS -->

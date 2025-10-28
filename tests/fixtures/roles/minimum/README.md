<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: minimum

Test role with a minimum amount of metadata

## Requirements

| Platform | Versions |
| -------- | -------- |
| Fedora | all |

## Role Arguments

### Entrypoint: main

The main entry point for the minimum role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| myapp_int | The integer value, defaulting to 42. | int | no | `42` |
| myapp_str | The string value | str | yes |  |

## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Importing role: minimum
      ansible.builtin.import_role:
        name: minimum
      vars:
        myapp_str: # required, type: str
```

## License

MIT

## Author and Project Information

your name @ ansible-docs

<!-- END_ANSIBLE_DOCS -->

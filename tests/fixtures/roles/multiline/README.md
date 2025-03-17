<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: multiline
Test role with multiline descriptions


## Requirements

| Platform | Versions |
| -------- | -------- |
| Fedora | all |

## Role Arguments



### Entrypoint: main

The main entry point for the multiline role.

This is a role description

that consists of multiple line

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| myapp_int | The integer value. Defaults to 42. | int | no | 42 |
| myapp_str | The string value. No default value. | str | yes |  |



## Dependencies
None.

## Example Playbook

```
- hosts: all
  tasks:
    - name: Importing role: multiline
      ansible.builtin.import_role:
        name: multiline
      vars:
        myapp_str: # required, type: str
```

## License

MIT

## Author and Project Information
your name @ ansible-docs

<!-- END_ANSIBLE_DOCS -->

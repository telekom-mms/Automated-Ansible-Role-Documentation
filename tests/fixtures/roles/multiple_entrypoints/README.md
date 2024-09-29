<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: multiple_entrypoints
Test role with a multiple_entrypoints amount of metadata


## Requirements

| Platform | Versions |
| -------- | -------- |
| Fedora | all |

## Role Arguments



### Entrypoint: main

The main entry point for the multiple_entrypoints role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| myapp_int | The integer value, defaulting to 42. | int | no | 42 |
| myapp_str | The string value | str | yes |  |



### Entrypoint: second

The second entry point for the multiple_entrypoints role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| myapp_int_second | The integer value, defaulting to 42. | int | no | 42 |
| myapp_str_second | The string value | str | yes |  |



## Dependencies
None.

## Example Playbook

```
- hosts: all
  tasks:
    - name: Importing role: multiple_entrypoints
      ansible.builtin.import_role:
        name: multiple_entrypoints
      vars:
        myapp_str: # required, type: str
        myapp_str_second: # required, type: str
```

## License

MIT

## Author and Project Information
your name @ ansible-docs

<!-- END_ANSIBLE_DOCS -->

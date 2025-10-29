<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: markup

Test role with markup in descriptions

## Requirements

| Platform | Versions |
| -------- | -------- |
| Fedora | all |

## Role Arguments

### Entrypoint: main

This summary contains **bold**, *italic* and `monospace` text as well as an [URL](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation).

This is an example of **bold** text.

This is an example of *italic* text.

This is an example of `monospace` text.

This is an example of an [URL](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation).

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| myapp_int | The integer value. Defaults to `42`. For string, see `myapp_str`. | int | no | `42` |
| myapp_str | The string value. No default value. For int, see `myapp_int`. | str | yes |  |

## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Importing role: markup
      ansible.builtin.import_role:
        name: markup
      vars:
        myapp_str: # required, type: str
```

## License

MIT

## Author and Project Information

your name @ ansible-docs

<!-- END_ANSIBLE_DOCS -->

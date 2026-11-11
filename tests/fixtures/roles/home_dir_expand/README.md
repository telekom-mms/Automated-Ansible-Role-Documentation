<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: home_dir_expand

Test role with a minimum amount of metadata

## Requirements

| Platform | Versions |
| -------- | -------- |
| Fedora | all |

## Role Arguments

### Entrypoint: main

The main entrypoint for the home_dir_expand role

A longer description of the entrypoint.

Reaching multiple lines.

This contains the various parameters one can give in argument_specs that do not get tested below.

| Option | Description | Type | Required | Default |
| ------ | ----------- | ---- | -------- | ------- |
| name | This one contains option-name, which should override the name given for the option. | str | no |  |

## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Importing role: home_dir_expand
      ansible.builtin.import_role:
        name: home_dir_expand
      vars:
```

## License

MIT

## Author and Project Information

your name @ ansible-docs

<!-- END_ANSIBLE_DOCS -->

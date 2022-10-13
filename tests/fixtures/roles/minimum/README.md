<!-- BEGIN_ANSIBLE_DOCS -->
Ansible Role: Minimum
=========

Test role with a minimum amount of metadata

Requirements
------------

| Platform | Versions |
| -------- | -------- |
| Fedora | all |

Role Variables
--------------

## main

The main entry point for the minimum role.

| Variable | Description | Type | Required | Default |
| -------- | ----------- | ---- | -------- | ------- |
| myapp_int | The integer value, defaulting to 42. | int | no | 42 |
| myapp_str | The string value | str | yes |  |


Dependencies
------------

None.

Example Playbook
----------------

```
- hosts: all
  tasks:
    - name: Importing role: minimum
      ansible.builtin.import_role:
        name: minimum
      vars:
        
        myapp_str:
        
```

License
-------

MIT

Author Information
------------------

your name @ ansible-docs

Issues: 
<!-- END_ANSIBLE_DOCS -->

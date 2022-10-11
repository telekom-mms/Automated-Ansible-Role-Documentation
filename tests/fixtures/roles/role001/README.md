<!-- BEGIN_ANSIBLE_DOCS -->
Ansible Role: Role001
=========

Tests basic rendering of documentation

Tags: 

Requirements
------------

| Platform | Versions |
| -------- | -------- |

Role Variables
--------------

## main

The main entry point for the myapp role.

| Variable | Description | Type | Required | Default |
| -------- | ----------- | ---- | -------- | ------- |
| myapp_int | The integer value, defaulting to 42. | int | no | 42 |
| myapp_str | The string value | str | yes |  |


Dependencies
------------


Example Playbook
----------------

```
- hosts: all
  tasks:
    - name: Importing role: role001
      ansible.builtin.import_role:
        name: role001
      vars:
        
        myapp_str:
        
```

License
-------



Author Information
------------------

 @ ansible-docs

Issues: 
<!-- END_ANSIBLE_DOCS -->
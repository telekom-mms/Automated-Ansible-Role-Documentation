This header content...

...should remain unchanged


<!-- BEGIN_ANSIBLE_DOCS -->
Ansible Role: Inject
=========

Test role with some header and footer text outside of the template

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
    - name: Importing role: inject
      ansible.builtin.import_role:
        name: inject
      vars:
        myapp_str: # required, type: str
```

License
-------

MIT

Author Information
------------------

your name @ ansible-docs
<!-- END_ANSIBLE_DOCS -->

This also stays as-is, as we `inject` only the parts between the markers!

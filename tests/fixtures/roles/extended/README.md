<!-- BEGIN_ANSIBLE_DOCS -->
Ansible Role: Extended
=========

Test role with lots of metadata

Tags: ansible, docs

Requirements
------------

| Platform | Versions |
| -------- | -------- |
| Fedora | all |
| Debian | all, bullseye, bookworm, wheezy |
| Cumulus | 2.5 |

Role Variables
--------------

## main

The main entrypoint for the extended role

| Variable | Description | Type | Required | Default |
| -------- | ----------- | ---- | -------- | ------- |
| name | This one contains option-name, which should override the name given for the option. | str | no |  |
| choices | So many choices to make | str | no |  |
| default | This one has a default | str | no | long |
| required | This one is required | str | yes |  |
| default_type | Type is str by default | str | no |  |

## list

The list entry point for the extended role.

| Variable | Description | Type | Required | Default |
| -------- | ----------- | ---- | -------- | ------- |
| list_int | A list of ints | list(int) | no | [1, 2, 3] |
| list_str | A list of strings | list(str) | no | ['foo', 'bar', 'baz'] |
| list_dict | A list of dicts | list(dict) | no | [{'dict': {'foo': 'bar'}}, {'dict': {'one': 1, 'two': 2}}] |

## dict

The dict entry point for the extended role.

| Variable | Description | Type | Required | Default |
| -------- | ----------- | ---- | -------- | ------- |
| dict | A dictionary of keys and values | dict | no | {'dict': {'foo': 'bar', 'one': 1, 'two': 2}} |

## bool

The bool entry point for the extended role.

| Variable | Description | Type | Required | Default |
| -------- | ----------- | ---- | -------- | ------- |
| bool_true | A true boolean value | bool | no | True |
| bool_false | A false boolean value | bool | no | False |
| bool_yes | A truthy boolean value | bool | no | True |
| bool_no | A falsy boolean value | bool | no | False |

## int

The int entry point for the extended role.

| Variable | Description | Type | Required | Default |
| -------- | ----------- | ---- | -------- | ------- |
| int | An int value | int | no | 1 |

## float

The float entry point for the extended role.

| Variable | Description | Type | Required | Default |
| -------- | ----------- | ---- | -------- | ------- |
| float | A float value | float | no | 1.2 |

## path

The path entry point for the extended role.

| Variable | Description | Type | Required | Default |
| -------- | ----------- | ---- | -------- | ------- |
| path | A path value | path | no | /tmp/foo/bar |

## raw

The raw entry point for the extended role.

| Variable | Description | Type | Required | Default |
| -------- | ----------- | ---- | -------- | ------- |
| raw_str | A raw str value | raw | no | raw |
| raw_int | A raw int value | raw | no | 123 |

## jsonarg

The jsonarg entry point for the extended role.

| Variable | Description | Type | Required | Default |
| -------- | ----------- | ---- | -------- | ------- |
| jsonarg | A JSON value | jsonarg | no | {"foo": "bar"} |

## json

The json entry point for the extended role.

| Variable | Description | Type | Required | Default |
| -------- | ----------- | ---- | -------- | ------- |
| json | A JSON value | json | no | {"foo": "bar"} |

## bytes

The bytes entry point for the extended role.

| Variable | Description | Type | Required | Default |
| -------- | ----------- | ---- | -------- | ------- |
| bytes | A bytes value | bytes | no | 1.15GB |

## bits

The bits entry point for the extended role.

| Variable | Description | Type | Required | Default |
| -------- | ----------- | ---- | -------- | ------- |
| bytes | A bit value | bits | no | 1Mb |


Dependencies
------------

None.

Example Playbook
----------------

```
- hosts: all
  tasks:
    - name: Importing role: extended
      ansible.builtin.import_role:
        name: extended
      vars:
        required: # required, type: str
```

License
-------

MIT

Author Information
------------------

your name @ ansible-docs

Issues: https://gitlab.com/kankare/ansible-docs/-/issues
<!-- END_ANSIBLE_DOCS -->

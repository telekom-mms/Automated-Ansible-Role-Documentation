<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: extended
Test role with lots of metadata

Tags: ansible, docs

## Requirements

| Platform | Versions |
| -------- | -------- |
| Fedora | all |
| Debian | all, bullseye, bookworm, wheezy |
| Cumulus | 2.5 |

## Role Arguments


### Entrypoint: main

The main entrypoint for the extended role

A longer description of the entrypoint.

Reaching multiple lines.
And a line.

This contains the various parameters one can give in argument_specs that do not get tested below.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| name | This one contains option-name, which should override the name given for the option. | str | no |  |
| choices-str | So many choices to make | str | no |  |
| choices-int | So many choices to make | int | no |  |
| default | This one has a default | str | no | long |
| default_null | This one has null as a default | str | no | None |
| required | This one is required | str | yes |  |
| default_type | Type is str by default | str | no |  |

#### Choices for main > choices-str

|Choice|
|---|
| one |
| two |
| three |

#### Choices for main > choices-int

|Choice|
|---|
| 1 |
| 8 |
| 42 |

#### Examples

this is an example how to execute the entrypoint:

    - hosts: all
      roles:
        - extended


### Entrypoint: list

The list entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| list_int | A list of ints | list of 'int' | no | [1, 2, 3] |
| list_int_null | A list of ints, null as a default | list of 'int' | no | None |
| list_str | A list of strings | list of 'str' | no | ['foo', 'bar', 'baz'] |
| list_str_null | A list of strings, null as a default | list of 'str' | no | None |
| list_dict | A list of dicts | list of 'dict' | no | [{'dict': {'foo': 'bar'}}, {'dict': {'one': 1, 'two': 2}}] |
| list_dict_null | A list of dicts, null as a default | list of 'dict' | no | None |



### Entrypoint: dict

The dict entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| dict | A dictionary of keys and values | dict | no | {"dict": {"foo": "bar", "one": 1, "two": 2}} |
| dict_null | A dictionary of keys and values, null as values | dict | no | {"dict": {"foo": null}} |



### Entrypoint: dict-with-options

The dict-with-options entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| opts | A dictionary of keys and values | dict of 'opts' options | no |  |
| opts_null | A dictionary of keys and values, null as a default | dict of 'opts_null' options | no | None |

#### Options for dict-with-options > opts

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| int | An int value | int | no | 1 |
| json | A JSON value | json | no | {"foo": "bar"} |
| subopts | A sub-dictionary of keys and values | dict of 'subopts' options | no |  |

#### Options for dict-with-options > opts > subopts

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| str | A str value | str | no |  |

#### Options for dict-with-options > opts_null

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| int | An int value | int | no | 1 |
| json | A JSON value | json | no | {"foo": "bar"} |
| subopts | A sub-dictionary of keys and values | dict of 'subopts' options | no |  |

#### Options for dict-with-options > opts_null > subopts

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| str | A str value | str | no |  |



### Entrypoint: bool

The bool entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| bool_true | A true boolean value | bool | no | True |
| bool_false | A false boolean value | bool | no | False |
| bool_yes | A truthy boolean value | bool | no | yes |
| bool_no | A falsy boolean value | bool | no | no |



### Entrypoint: int

The int entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| int | An int value | int | no | 1 |
| int_null | An int value, null as a default | int | no | None |



### Entrypoint: float

The float entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| float | A float value | float | no | 1.2 |
| float_null | A float value, null as a default | float | no | None |



### Entrypoint: path

The path entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| path | A path value | path | no | /tmp/foo/bar |
| path_null | A path value, null as a default | path | no | None |



### Entrypoint: raw

The raw entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| raw_str | A raw str value | raw | no | raw |
| raw_str_null | A raw str value, null as a default | raw | no | None |
| raw_int | A raw int value | raw | no | 123 |
| raw_int_null | A raw int value, null as a default | raw | no | None |



### Entrypoint: jsonarg

The jsonarg entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| jsonarg | A JSON value | jsonarg | no | {"foo": "bar"} |
| jsonarg_null | A JSON value, null as a default | jsonarg | no | None |



### Entrypoint: json

The json entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| json | A JSON value | json | no | {"foo": "bar"} |
| json_null | A JSON value, null as a default | json | no | None |



### Entrypoint: bytes

The bytes entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| bytes | A bytes value | bytes | no | 1.15GB |
| bytes_null | A bytes value, null as a default | bytes | no | None |



### Entrypoint: bits

The bits entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| bytes | A bit value | bits | no | 1Mb |
| bytes_null | A bit value, null as a default | bits | no | None |



## Dependencies
None.

## Example Playbook

```
- hosts: all
  tasks:
    - name: Importing role: extended
      ansible.builtin.import_role:
        name: extended
      vars:
        required: # required, type: str
```

## License

MIT

## Author and Project Information
your name @ ansible-docs

Issues: [tracker](https://gitlab.com/kankare/ansible-docs/-/issues)
<!-- END_ANSIBLE_DOCS -->

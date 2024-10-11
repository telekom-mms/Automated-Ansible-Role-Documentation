<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: meta_main_yaml
Test role with a minimum amount of metadata


## Requirements

| Platform | Versions |
| -------- | -------- |
| Fedora | all |

## Role Arguments



### Entrypoint: main

The main entrypoint for the extended role

A longer description of the entrypoint.

Reaching multiple lines.

This contains the various parameters one can give in argument_specs that do not get tested below.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| name | This one contains option-name, which should override the name given for the option. | str | no |  |
| choices-str | So many choices to make | str | no |  |
| choices-int | So many choices to make | int | no |  |
| default | This one has a default | str | no | long |
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



### Entrypoint: list

The list entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| list_int | A list of ints | list of 'int' | no | [1, 2, 3] |
| list_str | A list of strings | list of 'str' | no | ['foo', 'bar', 'baz'] |
| list_dict | A list of dicts | list of 'dict' | no | [{'dict': {'foo': 'bar'}}, {'dict': {'one': 1, 'two': 2}}] |



### Entrypoint: dict

The dict entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| dict | A dictionary of keys and values | dict | no | {"dict": {"foo": "bar", "one": 1, "two": 2}} |



### Entrypoint: dict-with-options

The dict-with-options entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| opts | A dictionary of keys and values | dict of 'opts' options | no |  |

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



### Entrypoint: bool

The bool entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| bool_true | A true boolean value | bool | no | true |
| bool_false | A false boolean value | bool | no | false |
| bool_yes | A truthy boolean value | bool | no | true |
| bool_no | A falsy boolean value | bool | no | false |



### Entrypoint: int

The int entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| int | An int value | int | no | 1 |



### Entrypoint: float

The float entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| float | A float value | float | no | 1.2 |



### Entrypoint: path

The path entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| path | A path value | path | no | /tmp/foo/bar |



### Entrypoint: raw

The raw entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| raw_str | A raw str value | raw | no | raw |
| raw_int | A raw int value | raw | no | 123 |



### Entrypoint: jsonarg

The jsonarg entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| jsonarg | A JSON value | jsonarg | no | {"foo": "bar"} |



### Entrypoint: json

The json entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| json | A JSON value | json | no | {"foo": "bar"} |



### Entrypoint: bytes

The bytes entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| bytes | A bytes value | bytes | no | 1.15GB |



### Entrypoint: bits

The bits entry point for the extended role.

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| bytes | A bit value | bits | no | 1Mb |



## Dependencies
None.

## Example Playbook

```
- hosts: all
  tasks:
    - name: Importing role: meta_main_yaml
      ansible.builtin.import_role:
        name: meta_main_yaml
      vars:
        required: # required, type: str
```

## License

MIT

## Author and Project Information
your name @ ansible-docs

<!-- END_ANSIBLE_DOCS -->

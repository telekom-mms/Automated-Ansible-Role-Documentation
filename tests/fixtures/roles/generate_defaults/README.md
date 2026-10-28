<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: generate_defaults

Test generation of defaults

## Requirements

| Platform | Versions |
| -------- | -------- |
| Fedora | all |

## Role Arguments

### Entrypoint: main

The main entry point for the defaults role.

| Option | Description | Type | Required | Default |
| ------ | ----------- | ---- | -------- | ------- |
| generate_defaults_zero | An integer with value of 0 | int | no | `0` |
| generate_defaults_one | An integer with value of 1 | int | no | `1` |
| generate_defaults_int | An integer value | int | no | `42` |
| generate_defaults_bool | A bool value | bool | no | `False` |
| generate_defaults_str | A string value | str | no | `Some string` |
| generate_defaults_truthy_yes_string | A truthy yes string value | str | no | `yes` |
| generate_defaults_truthy_no_string | A truthy no string value | str | no | `no` |
| generate_defaults_truthy_true_string | A truthy true string value | str | no | `true` |
| generate_defaults_truthy_false_string | A truthy false string value | str | no | `false` |
| generate_defaults_truthy_colon_string | A string value with colons | str | no | `::1` |
| generate_defaults_truthy_colon_nested | A nested dict/list with colons | list of `` | no | `[{'foo': {'bar': '::1'}}]` |
| generate_defaults_umask | A umask string value | str | no | `0755` |
| generate_defaults_list | A list value with a list description with a rather long description, maybe too long. | list of `` | no | `['value1', 'value2', 'value3']` |
| generate_defaults_dict | A dictionary value | dict | no | `{"value1": "first value", "value2": "second value", "value3": "third value"}` |
| generate_defaults_list_of_dict | A list-of-dict value | list of `` | no | `[{'value1': 'first value', 'value2': 'second value'}, {'value3': 'third value', 'value4': 'fourth value'}]` |
| generate_defaults_empty_list_of_dict | A list of dicts with the empty list as the default | list of dicts of `generate_defaults_empty_list_of_dict` [options](#options-for-main--generate_defaults_empty_list_of_dict) | no | `[]` |
| generate_defaults_overwrite | A string value that can be overwritten | str | no | `original value` |
| generate_defaults_non_default | An option without a default | str | yes |  |
| generate_defaults_no_description |  | str | yes | `foo` |
| generate_default_null | This one has null as a default | str | no | `None` |
| generate_nested_log_config | Logging configuration. See: https://example.com/docs/common/logging | dict of `generate_nested_log_config` [options](#options-for-main--generate_nested_log_config) | no |  |
| generate_nested_log_config_tag | Logging configuration. See: https://example.com/docs/common/logging ***defaults_prefix:"__" foo_tag:"brenson asdfdf"*** | dict of `generate_nested_log_config_tag` [options](#options-for-main--generate_nested_log_config_tag) | no |  |
| generate_very_nested_log_config | Logging configuration. See: https://example.com/docs/common/logging | dict of `generate_very_nested_log_config` [options](#options-for-main--generate_very_nested_log_config) | no |  |

#### Options for main > generate_defaults_empty_list_of_dict

| Option | Description | Type | Required | Default |
| ------ | ----------- | ---- | -------- | ------- |
| value1 |  | str | no | `first value` |
| value2 |  | str | no |  |

#### Options for main > generate_nested_log_config

| Option | Description | Type | Required | Default |
| ------ | ----------- | ---- | -------- | ------- |
| level | Log level (e.g., info, debug, warn, error). | str | no | `info` |
| default_null | This one has null as a default | str | no | `None` |

#### Options for main > generate_nested_log_config_tag

| Option | Description | Type | Required | Default |
| ------ | ----------- | ---- | -------- | ------- |
| level | Log level (e.g., info, debug, warn, error). | str | no | `info` |
| default_null | This one has null as a default | str | no | `None` |

#### Options for main > generate_very_nested_log_config

| Option | Description | Type | Required | Default |
| ------ | ----------- | ---- | -------- | ------- |
| level | Log level (e.g., info, debug, warn, error). | str | no | `info` |
| tls | TLS configuration for API server. | dict of `tls` [options](#options-for-main--generate_very_nested_log_config--tls) | no |  |

#### Options for main > generate_very_nested_log_config > tls

| Option | Description | Type | Required | Default |
| ------ | ----------- | ---- | -------- | ------- |
| enable | Enable TLS for logs shipper. | bool | no | `False` |

### Entrypoint: alternate

The alternate entry point for the defaults role.

| Option | Description | Type | Required | Default |
| ------ | ----------- | ---- | -------- | ------- |
| generate_defaults_str_multiline | A multiline string value | str | no | `This is a multi line string.

It contains a lot of lines.

Yar har har.` |
| generate_defaults_jsonarg | A JSON value | jsonarg | no | `{"foo": "bar"}` |
| generate_defaults_json | A JSON value | json | no | `{"foo": "bar"}` |
| generate_defaults_overwrite | A string value that was overwritten | str | no | `overwritten value` |
| generate_defaults_another_non_default | Another option without a default | str | yes |  |

## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Importing role: generate_defaults
      ansible.builtin.import_role:
        name: generate_defaults
      vars:
        generate_defaults_non_default: # required, type: str
        generate_defaults_no_description: # required, type: str
        generate_defaults_another_non_default: # required, type: str
```

## License

MIT

## Author and Project Information

your name @ ansible-docs

<!-- END_ANSIBLE_DOCS -->

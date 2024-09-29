<!-- BEGIN_ANSIBLE_DOCS -->

# Ansible Role: wrong_type

---

Test role with wrong type in argument spec

## Requirements

---

| Platform | Versions |
| -------- | -------- |
| Fedora   | all      |

## Role Arguments

---

### Entrypoint: main

---

The main entry point for the minimum role.

| Option    | Description                          | Type | Required | Default |
| --------- | ------------------------------------ | ---- | -------- | ------- |
| myapp_int | The integer value, defaulting to 42. | int  | no       | foo     |

## Dependencies

---

None.

## Example Playbook

---

```
- hosts: all
  tasks:
    - name: Importing role: wrong_type
      ansible.builtin.import_role:
        name: wrong_type
      vars:

```

## License

---

MIT

## Author and Project Information

---

your name @ ansible-docs

<!-- END_ANSIBLE_DOCS -->

[![tests](https://github.com/boutetnico/ansible-role-sysctl/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-sysctl/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.sysctl-blue.svg)](https://galaxy.ansible.com/boutetnico/sysctl)

ansible-role-sysctl
===================

This role manipulates sysctl entries.

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)
- [Ubuntu - 24.04 (Noble Numbat)](http://releases.ubuntu.com/24.04/)

Role Variables
--------------

| Variable            | Required | Default     | Choices   | Comments                             |
|---------------------|----------|-------------|-----------|--------------------------------------|
| sysctl_dependencies | yes      | `[procps]`  | list      |                                      |
| sysctl_entries      | yes      | `[]`        | list      | See `defaults/main.yml` for example. |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - ansible-role-sysctl
          sysctl_entries:
            - name: vm.overcommit_memory
              value: 1

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)

import pytest

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('key,expected_value', [
  ('vm.overcommit_memory', 1),
])
def test_sysctl_values(host, key, expected_value):
    value = host.sysctl(key)
    assert expected_value == value

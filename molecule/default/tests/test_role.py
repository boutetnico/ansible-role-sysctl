import pytest

import os


@pytest.mark.parametrize(
    "key,expected_value",
    [
        ("vm.overcommit_memory", 1),
    ],
)
def test_sysctl_values(host, key, expected_value):
    value = host.sysctl(key)
    assert expected_value == value

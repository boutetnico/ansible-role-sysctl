import pytest

import os


@pytest.mark.parametrize(
    "package",
    [
        "procps",
    ],
)
def test_dependencies_installed(host, package):
    pkg = host.package(package)
    assert pkg.is_installed


@pytest.mark.parametrize(
    "key,expected_value",
    [
        ("vm.overcommit_memory", 1),
        ("vm.swappiness", 60),
        ("net.ipv4.ip_forward", 0),
    ],
)
def test_sysctl_values(host, key, expected_value):
    value = host.sysctl(key)
    assert expected_value == value

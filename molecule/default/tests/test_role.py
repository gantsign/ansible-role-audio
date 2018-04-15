import pytest
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_alsactl(Command):
    cmd = Command('alsactl --version')
    assert cmd.rc == 0


@pytest.mark.parametrize('group', [
    'sudo',
    'audio',
    'video'
])
def test_java_tools(User, group):
    usr = User('test_usr')
    assert group in usr.groups

import pytest

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_alsactl(Command):
    cmd = Command('alsactl --version')
    assert cmd.rc == 0


@pytest.mark.parametrize('group', [
    ('sudo'),
    ('audio'),
    ('video')
])
def test_java_tools(User, group):
    usr = User('test_usr')
    assert group in usr.groups

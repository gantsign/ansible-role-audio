import pytest


def test_alsactl(host):
    cmd = host.run('alsactl --version')
    assert cmd.rc == 0


@pytest.mark.parametrize('group', [
    'sudo',
    'audio',
    'video'
])
def test_java_tools(host, group):
    usr = host.user('test_usr')
    assert group in usr.groups

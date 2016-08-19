import pytest

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

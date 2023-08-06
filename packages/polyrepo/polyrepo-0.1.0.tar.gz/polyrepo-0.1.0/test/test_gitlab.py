from unittest import TestCase
from unittest.mock import Mock
from unittest.mock import patch
from json import loads

from polyrepo.gitlab import GitLab


def mockget(responses):
    output = Mock()
    output.json = Mock(side_effect=responses)
    output.status_code = 200
    mock = Mock(return_value=output)
    return patch('polyrepo.gitlab.get', mock)


class TestGitLab(TestCase):

    def test_subgroups(self):
        with mockget([[{"path": "a"}, {"path": "b"}], [], []]):
            g = GitLab()
            x = g.group_subgroups('f')
            self.assertEqual(x, ['f', 'f/a', 'f/b'])

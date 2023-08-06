from unittest import TestCase
from unittest.mock import Mock
from unittest.mock import patch
from json import loads

from polyrepo.gitlab import GitLab
from polyrepo.command.groups_command import GroupsCommand

from test.test_gitlab import mockget


class TestGroups(TestCase):

    def test_no_recursion(self):
        with mockget([[{"path": "a"}, {"path": "b"}], [], []]):
            c = GroupsCommand(path='f')
            c.gitlab_host = 'g'
            c.gitlab_token = 'h'
            x = c.execute()
            # self.assertEqual(x, 'f\nf/a\nf/b')
            self.assertEqual(x, 'f')

    def test_with_recursion(self):
        with mockget([[{"path": "a"}, {"path": "b"}], [], []]):
            c = GroupsCommand(path='f', traverse=True)
            c.gitlab_host = 'g'
            c.gitlab_token = 'h'
            x = c.execute()
            self.assertEqual(x, 'f\nf/a\nf/b')

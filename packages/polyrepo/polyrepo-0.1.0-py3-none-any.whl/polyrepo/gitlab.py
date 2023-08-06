from dataclasses import dataclass
from urllib.parse import quote
from json import dumps
from json import loads

from requests import get
from requests import codes


@dataclass
class GitLab:

    host: str = None
    token: str = None

    @property
    def headers(self):
        return {'Private-Token': self.token}

    def group_subgroups(self, path: str, traverse: bool = True):
        paths = [path]
        qpath = quote(path, safe='')
        url = f"https://{self.host}/api/v4/groups/{qpath}/subgroups"
        response = get(url, headers=self.headers)
        if response.status_code == codes.ok:
            spaths = [path + "/" + g['path'] for g in response.json()]
            if traverse and paths:
                for spath in spaths:
                    paths.extend(self.group_subgroups(spath))
            return paths
        else:
            raise Exception(response.json()['message'])

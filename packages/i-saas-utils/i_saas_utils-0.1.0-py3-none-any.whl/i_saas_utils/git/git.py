from typing import Optional

import git
from gitlab import Gitlab

from .project import GitRepo


class Git:
    def __init__(
        self,
        url: Optional[str] = None,
        private_token: Optional[str] = None,
    ):
        self.gitlab = Gitlab(
            url,
            private_token,
        )
        self.gitlab.auth()

    def clone(self, project_url: str, path: str):
        gitlab_project = self.gitlab.projects.get(project_url)
        repo = git.Repo.clone_from(
            f"https://oauth2:{self.gitlab.private_token}@{self.gitlab.url.lstrip('https://')}/{project_url}",
            to_path=path,
        )
        return GitRepo(gitlab_project, repo)

from integrations.github.github_client import (
    GitHubClient,
)

from storage.sqlite.github_repository import (
    GitHubRepository,
)


class IssueSync:

    def __init__(self):

        self.client = GitHubClient()

        self.repo = (
            GitHubRepository()
        )

    def sync(
        self,
        owner: str,
        repository: str,
    ):

        issues = (
            self.client.get_issues(
                owner,
                repository,
            )
        )

        synced = 0

        for issue in issues:

            labels = [
                label["name"]
                for label in issue[
                    "labels"
                ]
            ]

            self.repo.save_issue(
                issue["number"],
                issue["title"],
                issue.get(
                    "body",
                    "",
                ),
                issue["state"],
                labels,
            )

            synced += 1

        return synced
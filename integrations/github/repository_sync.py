from integrations.github.github_client import (
    GitHubClient,
)


class RepositorySync:

    def __init__(self):

        self.client = GitHubClient()

    def sync(
        self,
        owner: str,
        repo: str,
    ):

        repository = (
            self.client.get_repository(
                owner,
                repo,
            )
        )

        contributors = (
            self.client.get_contributors(
                owner,
                repo,
            )
        )

        labels = (
            self.client.get_labels(
                owner,
                repo,
            )
        )

        return {
            "repository": repository,
            "contributors": contributors,
            "labels": labels,
        }
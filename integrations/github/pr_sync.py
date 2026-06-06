from integrations.github.github_client import (
    GitHubClient,
)


class PRSync:

    def __init__(self):

        self.client = GitHubClient()

    def sync(
        self,
        owner,
        repo,
    ):

        prs = (
            self.client.get_pull_requests(
                owner,
                repo,
            )
        )

        return len(prs)
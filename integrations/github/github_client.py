import os
import requests


class GitHubClient:

    BASE_URL = "https://api.github.com"

    def __init__(self):

        token = os.getenv(
            "GITHUB_TOKEN"
        )

        self.headers = {
            "Accept": "application/vnd.github+json"
        }

        if token:

            self.headers[
                "Authorization"
            ] = f"Bearer {token}"

    def get(
        self,
        endpoint: str,
        params=None,
    ):

        response = requests.get(
            f"{self.BASE_URL}{endpoint}",
            headers=self.headers,
            params=params,
        )

        response.raise_for_status()

        return response.json()

    def get_repository(
        self,
        owner,
        repo,
    ):

        return self.get(
            f"/repos/{owner}/{repo}"
        )

    def get_issues(
        self,
        owner,
        repo,
        state="open",
    ):

        return self.get(
            f"/repos/{owner}/{repo}/issues",
            {
                "state": state,
                "per_page": 100,
            },
        )

    def get_pull_requests(
        self,
        owner,
        repo,
        state="open",
    ):

        return self.get(
            f"/repos/{owner}/{repo}/pulls",
            {
                "state": state,
                "per_page": 100,
            },
        )

    def get_labels(
        self,
        owner,
        repo,
    ):

        return self.get(
            f"/repos/{owner}/{repo}/labels"
        )

    def get_contributors(
        self,
        owner,
        repo,
    ):

        return self.get(
            f"/repos/{owner}/{repo}/contributors"
        )

    def get_issue(
        self,
        owner,
        repo,
        issue_number,
    ):

        return self.get(
            f"/repos/{owner}/{repo}/issues/{issue_number}"
        )
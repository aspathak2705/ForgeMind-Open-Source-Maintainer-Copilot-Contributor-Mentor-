from integrations.github.issue_sync import (
    IssueSync,
)


def sync(
    owner: str,
    repo: str,
):

    syncer = IssueSync()

    issues = syncer.sync(
        owner,
        repo,
    )

    print()

    print(
        f"Synced {len(issues)} issues"
    )
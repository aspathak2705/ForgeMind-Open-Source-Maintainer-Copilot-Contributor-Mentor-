from agents.repository_agent.repository_agent import RepositoryAgent


class IssueAnalyzer:

    def __init__(self):
        self.repo_agent = RepositoryAgent()

    def analyze(
        self,
        issue_text: str,
    ):

        words = issue_text.lower().split()

        files = set()
        classes = set()

        for word in words:

            context = self.repo_agent.get_repository_context(word)

            if not context:
                continue

            files.update(context["files"])
            classes.update(context["classes"])

        return {
            "files": list(files),
            "classes": list(classes),
        }

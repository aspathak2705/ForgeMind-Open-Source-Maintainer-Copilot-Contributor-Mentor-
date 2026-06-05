import re

from core.search.repository_search import (
    RepositorySearch,
)


class IssueAnalyzer:

    STOP_WORDS = {
        "a",
        "add",
        "an",
        "api",
        "configure",
        "do",
        "how",
        "i",
        "mode",
        "support",
        "the",
        "to",
        "when",
        "with",
    }

    AUTH_HINTS = {
        "auth",
        "credential",
        "credentials",
        "jwt",
        "login",
        "password",
        "token",
    }

    def __init__(self):

        self.search = RepositorySearch()

    def analyze(self, issue_text: str):

        words = set(
            re.findall(
            r"[a-z0-9_]+",
            issue_text.lower(),
            )
        )

        words = {
            word for word in words
            if len(word) >= 3
            and word not in self.STOP_WORDS
        }

        if words & self.AUTH_HINTS:
            words.update(
                {
                    "auth",
                    "jwt",
                }
            )

        files = set()
        classes = set()

        for word in words:

            results = self.search.search(word)

            for result in results:

                files.add(result.file_path)

                if result.match_type == "class":
                    classes.add(
                        result.matched_value
                    )

        return {
            "files": list(files),
            "classes": list(classes),
        }

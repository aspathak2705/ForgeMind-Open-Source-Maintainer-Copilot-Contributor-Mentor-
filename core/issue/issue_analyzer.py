from agents.repository_agent.repository_agent import (
    RepositoryAgent,
)

from core.nlp.keyword_extractor import (
    KeywordExtractor,
)


class IssueAnalyzer:

    def __init__(self):

        self.repo_agent = (
            RepositoryAgent()
        )

        self.extractor = (
            KeywordExtractor()
        )

    def analyze(
        self,
        issue_text: str,
    ):

        keywords = (
            self.extractor.extract(
                issue_text
            )
        )

        files = {}

        classes = set()

        for keyword in keywords:

            context = (
                self.repo_agent
                .search_repository_context(
                    keyword
                )
            )

            if not context:
                continue

            for file_info in context[
                "files"
            ]:

                file_name = file_info[
                    "file"
                ]

                importance = (
                    file_info[
                        "importance"
                    ]
                )

                files[file_name] = max(
                    files.get(
                        file_name,
                        0,
                    ),
                    importance,
                )

            classes.update(
                context[
                    "classes"
                ]
            )

        ranked_files = sorted(
            files.items(),
            key=lambda x: x[1],
            reverse=True,
        )

        return {
            "files": [
                item[0]
                for item in ranked_files
            ],
            "classes": list(
                classes
            ),
        }
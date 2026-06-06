from collections import defaultdict

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

        file_scores = defaultdict(
            float
        )

        file_hits = defaultdict(
            int
        )

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

                file_name = (
                    file_info["file"]
                )

                importance = (
                    file_info[
                        "importance"
                    ]
                )

                impact_score = (
                    file_info.get(
                        "impact_score",
                        0,
                    )
                )

                file_scores[
                    file_name
                ] += (
                    importance
                    + impact_score
                    * 10
                )

                file_hits[
                    file_name
                ] += 1

            classes.update(
                context.get(
                    "classes",
                    []
                )
            )

        ranked_files = []

        for (
            file_name,
            score,
        ) in file_scores.items():

            hit_count = (
                file_hits[
                    file_name
                ]
            )

            final_score = (
                score
                + hit_count * 25
            )

            ranked_files.append(
                (
                    file_name,
                    final_score,
                )
            )

        ranked_files.sort(
            key=lambda item: item[
                1
            ],
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
            "keywords": keywords,
        }
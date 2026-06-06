from core.services.explain_service import (
    ExplainService,
)

from core.repository.impact_analyzer import (
    ImpactAnalyzer,
)

from core.repository.repository_ranker import (
    RepositoryRanker,
)
from core.search.context_ranker import (
    ContextRanker,
)

class RepositoryAgent:

    def __init__(self):

        self.explainer = ExplainService()

        self.impact_analyzer = (
            ImpactAnalyzer()
        )

        self.ranker = (
            RepositoryRanker()
        )

        self.context_ranker = (
            ContextRanker()
        )

    def explain(
        self,
        query: str,
    ):

        return self.explainer.explain(
            query
        )

    def get_repository_context(
        self,
        query: str,
    ):

        return self.explainer.explain(
            query
        )

    def get_file_impact(
        self,
        file_path: str,
    ):

        return (
            self.impact_analyzer.analyze(
                file_path
            )
        )

    def get_file_importance(
        self,
        file_path: str,
    ):

        ranking = (
            self.ranker.rank_file(
                file_path
            )
        )

        return ranking["importance"]

    def get_file_difficulty(
        self,
        file_path: str,
    ):

        ranking = (
            self.ranker.rank_file(
                file_path
            )
        )

        return ranking["difficulty"]

    def get_enriched_context(
        self,
        query: str,
    ):

        context = (
            self.get_repository_context(
                query
            )
        )

        if not context:
            return None

        enriched_files = []

        for file_path in context["files"]:

            ranking = (
                self.ranker.rank_file(
                    file_path
                )
            )

            impact = (
                self.impact_analyzer.analyze(
                    file_path
                )
            )

            enriched_files.append(
                {
                    "file": file_path,
                    "importance": ranking[
                        "importance"
                    ],
                    "difficulty": ranking[
                        "difficulty"
                    ],
                    "impact_score": impact[
                        "impact_score"
                    ],
                    "dependents": impact[
                        "dependents"
                    ],
                }
            )

        enriched_files = (
            self.context_ranker.rank_files(
                enriched_files
            )
        )

        return {
            "files": enriched_files,
            "classes": list(
                context.get(
                    "classes",
                    []
                )
            ),
            "functions": list(
                context.get(
                    "functions",
                    []
                )
            ),
            "imports": list(
                context.get(
                    "imports",
                    []
                )
            ),
        }

    def search_repository_context(
        self,
        query: str,
    ):

        context = (
            self.explainer.explain(
                query
            )
        )

        if not context:
            return None

        enriched_files = []

        for file_path in context["files"]:

            ranking = (
                self.ranker.rank_file(
                    file_path
                )
            )

            impact = (
                self.impact_analyzer
                .analyze(
                    file_path
                )
            )

            enriched_files.append(
                {
                    "file": file_path,
                    "importance": ranking[
                        "importance"
                    ],
                    "difficulty": ranking[
                        "difficulty"
                    ],
                    "impact_score": impact[
                        "impact_score"
                    ],
                    "dependents": impact[
                        "dependents"
                    ],
                }
            )

        return {
            "files": enriched_files,
            "classes": context[
                "classes"
            ],
            "imports": context[
                "imports"
            ],
        }
import json

from core.services.repository_service import (
    RepositoryService,
)

from core.search.search_result import (
    SearchResult,
)


class RepositorySearch:

    def __init__(self):

        self.repo = RepositoryService()

    def search(
        self,
        query: str,
    ) -> list[SearchResult]:

        query = query.lower()

        rows = self.repo.get_all_files()

        results = []

        for row in rows:

            path = row[1]

            imports = json.loads(row[2])

            classes = json.loads(row[3])

            functions = json.loads(row[4])

            # file match
            if query in path.lower():

                results.append(
                    SearchResult(
                        file_path=path,
                        match_type="file",
                        matched_value=path,
                        score=100,
                    )
                )

            # import match
            for imp in imports:

                if query in imp.lower():

                    results.append(
                        SearchResult(
                            file_path=path,
                            match_type="import",
                            matched_value=imp,
                            score=90,
                        )
                    )

            # class match
            for cls in classes:

                if query in cls.lower():

                    results.append(
                        SearchResult(
                            file_path=path,
                            match_type="class",
                            matched_value=cls,
                            score=95,
                        )
                    )

            # function match
            for func in functions:

                if query in func.lower():

                    results.append(
                        SearchResult(
                            file_path=path,
                            match_type="function",
                            matched_value=func,
                            score=95,
                        )
                    )

        return sorted(
            results,
            key=lambda x: x.score,
            reverse=True,
        )
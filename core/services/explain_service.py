from core.search.repository_search import RepositorySearch

class ExplainService:

    def __init__(self):

        self.search = RepositorySearch()

    def explain(self, query: str):

        results = self.search.search(query)

        if not results:
            return None
        
        explanation ={

            "files": set(),
            "classes": set(),
            "functions": set(),
            "imports": set(),
        }

        for result in results:

            explanation["files"].add(result.file_path)

            if result.match_type == "class":
                explanation["classes"].add(result.matched_value)

            elif result.match_type == "function":
                explanation["functions"].add(result.matched_value)

            elif result.match_type == "import":
                explanation["imports"].add(result.matched_value)

        return explanation
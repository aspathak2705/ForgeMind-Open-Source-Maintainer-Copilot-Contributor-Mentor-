from core.issue.repository_importance import RepositoryImportance
from core.services.explain_service import ExplainService
from pathlib import Path

class RepositoryAgent:

    def __init__(self):

        self.service = ExplainService()
        self.importance = RepositoryImportance()

    def explain(self,
                query: str,):
        
        return self.service.explain(query)

    def get_repository_context(self,query: str):
        explanation = self.service.explain(query)

        if not explanation:
            return None

        files = sorted(
            {
                Path(file_path).name
                for file_path in explanation["files"]
            }
        )
        classes = sorted(explanation["classes"])

        return {
            "files": files,
            "classes": classes,
            "imports": sorted(explanation["imports"]),
            "importance": {
                Path(file_path).name: self.importance.calculate(file_path)
                for file_path in explanation["files"]
            },
        }




    

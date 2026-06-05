from core.services.explain_service import ExplainService

class RepositoryAgent:

    def __init__(self):

        self.service = ExplainService()

    def explain(self,
                query: str,):
        
        return self.service.explain(query)
    

    
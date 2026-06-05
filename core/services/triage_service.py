from agents.issue_agent.issue_agent import IssueAgent
from core.issue.issue_model import IssueAnalysis


class TriageService:

    def __init__(self):
        self.issue_agent = IssueAgent()

    def triage(self, issue_text: str) -> IssueAnalysis:
        return self.issue_agent.analyze(issue_text)

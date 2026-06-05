from pydantic import BaseModel

class IssueAnalysis(BaseModel):

    issue_type: str

    severity: str

    verification: str

    confidence: int

    related_files: list[str]

    related_classes: list[str]

    reproduction_steps: list[str]

    recommendation: str

    
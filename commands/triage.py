import typer

from core.services.triage_service import TriageService


def triage(issue: str | None = None):

    if issue is None:
        issue = typer.prompt("Describe issue")

    analysis = TriageService().triage(issue)

    print()
    print("Issue Analysis")
    print("==============")
    print()
    print(f"Type: {analysis.issue_type}")
    print()
    print(f"Severity: {analysis.severity}")
    print()
    print(f"Verification: {analysis.verification}")
    print()
    print(f"Confidence: {analysis.confidence}")
    print()
    print("Related Files:")

    for file_name in analysis.related_files or ["None"]:
        print(f"- {file_name}")

    print()
    print("Related Classes:")

    for class_name in analysis.related_classes or ["None"]:
        print(f"- {class_name}")

    print()
    print("Reproduction Steps:")

    for index, step in enumerate(analysis.reproduction_steps, start=1):
        print(f"{index}. {step}")

    print()
    print("Recommendation:")
    print(analysis.recommendation)

class PromptBuilder:

    @staticmethod
    def issue_analysis_prompt(
        issue_text: str,
        repository_context: dict,
    ):

        return f"""
You are ForgeMind Issue Intelligence.

Issue:
{issue_text}

Repository Context:
{repository_context}

Provide:

1. Root Cause Analysis
2. Relevant Files
3. Relevant Classes
4. Confidence Score
5. Recommended Fix
"""

    @staticmethod
    def mentor_prompt(
        issue_context: dict,
        repository_context: dict,
    ):

        return f"""
You are ForgeMind Mentor.

Issue Context:
{issue_context}

Repository Context:
{repository_context}

Provide:

1. Difficulty
2. Learning Path
3. Required Concepts
4. Recommended Files
"""

    @staticmethod
    def maintainer_prompt(
        repository_context: dict,
    ):

        return f"""
You are ForgeMind Maintainer Advisor.

Repository Context:
{repository_context}

Provide:

1. Repository Health
2. Risk Areas
3. Hotspots
4. Recommendations
"""
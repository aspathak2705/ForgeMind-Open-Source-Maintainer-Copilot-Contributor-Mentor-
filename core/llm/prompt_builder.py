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

            Generate a structured engineering report.

            IMPORTANT:
            - Do NOT use markdown tables.
            - Do NOT use HTML.
            - Use plain text headings.
            - Use bullet points for findings.
            - Use numbered lists for actions.
            - Keep the report repository-specific.

            Format:

            ISSUE SUMMARY
            =============

            ROOT CAUSE ANALYSIS
            ===================

            RELATED FILES
            =============

            RELATED CLASSES
            ===============

            VERIFICATION STATUS
            ===================

            RECOMMENDED FIX
            ===============

            CONFIDENCE
            ==========
            """

    @staticmethod
    def mentor_prompt(
        issue_context: dict,
        repository_context: dict,
    ):

        return f"""
            You are ForgeMind Contributor Mentor.

            Issue Context:
            {issue_context}

            Repository Context:
            {repository_context}

            Generate a structured contributor guide.

            IMPORTANT:
            - Do NOT use markdown tables.
            - Do NOT use HTML.
            - Use plain text headings.
            - Use bullet points.
            - Focus on contributor onboarding.

            Format:

            ISSUE OVERVIEW
            ==============

            REQUIRED CONCEPTS
            =================

            LEARNING PATH
            =============

            RECOMMENDED FILES
            =================

            ESTIMATED DIFFICULTY
            ====================

            NEXT STEPS
            ==========
            """

    @staticmethod
    def maintainer_prompt(
        repository_context: dict,
    ):

        return f"""
            You are ForgeMind Maintainer Advisor.

            Repository Context:
            {repository_context}

            Generate a detailed repository maintenance report.

            IMPORTANT:
            - Do NOT use markdown tables.
            - Do NOT use HTML.
            - Do NOT use pipe-separated formatting.
            - Use plain text headings.
            - Use bullet points for findings.
            - Use numbered lists for recommendations.
            - Keep the report repository-specific.

            Format:

            EXECUTIVE SUMMARY
            =================

            REPOSITORY HEALTH
            =================

            ARCHITECTURAL HOTSPOTS
            ======================

            DEPENDENCY OBSERVATIONS
            =======================

            RISK ANALYSIS
            =============

            RECOMMENDED ACTIONS
            ===================

            NEXT SPRINT PRIORITIES
            ======================
            """
    @staticmethod
    def pr_review_prompt(
        review_context: dict,
    ):

        return f"""
            You are ForgeMind PR Review Agent.

            Repository Context:
            {review_context}

            Generate a detailed code review report.

            IMPORTANT:
            - Do NOT use markdown tables.
            - Use plain text headings.
            - Focus on architectural impact.
            - Focus on testing risks.
            - Focus on maintainability.
            - Focus on regression risks.

            Format:

            PR SUMMARY
            ==========

            RISK LEVEL
            ==========

            AFFECTED MODULES
            ================

            ARCHITECTURAL IMPACT
            ====================

            REVIEW COMMENTS
            ===============

            TESTING RECOMMENDATIONS
            =======================

            FINAL RECOMMENDATION
            ====================
            """
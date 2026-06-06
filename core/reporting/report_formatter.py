class ReportFormatter:

    @staticmethod
    def maintainer_report(
        summary: str,
    ):

        return f"""
FORGEMIND MAINTAINER REPORT
===========================

EXECUTIVE SUMMARY
-----------------
{summary}
"""

    @staticmethod
    def issue_report(
        recommendation: str,
    ):

        return f"""
FORGEMIND ISSUE ANALYSIS
========================

RECOMMENDATION
--------------
{recommendation}
"""

    @staticmethod
    def mentor_report(
        guidance: str,
    ):

        return f"""
FORGEMIND CONTRIBUTOR GUIDE
===========================

GUIDANCE
--------
{guidance}
"""

class ReportFormatter:

    @staticmethod
    def maintainer_report(
        summary: str,
    ):

        return f"""
            FORGEMIND MAINTAINER REPORT
            ==================================================

            {summary}

            ==================================================
            END OF REPORT
            ==================================================
            """

    @staticmethod
    def issue_report(
        recommendation: str,
    ):

        return f"""
            FORGEMIND ISSUE ANALYSIS
            ==================================================

            {recommendation}

            ==================================================
            END OF ANALYSIS
            ==================================================
            """

    @staticmethod
    def mentor_report(
        guidance: str,
    ):

        return f"""
            FORGEMIND CONTRIBUTOR GUIDE
            ==================================================

            {guidance}

            ==================================================
            END OF GUIDE
            ==================================================
            """
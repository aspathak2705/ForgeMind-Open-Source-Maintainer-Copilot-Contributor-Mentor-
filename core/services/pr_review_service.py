from agents.pr_review_agent.pr_review_agent import (
    PRReviewAgent,
)


class PRReviewService:

    def __init__(self):

        self.agent = (
            PRReviewAgent()
        )

    def review(
        self,
        files: list[str],
    ):

        return (
            self.agent.review(
                files
            )
        )
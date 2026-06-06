from agents.maintainer_agent.maintainer_agent import (
    MaintainerAgent,
)


class MaintainerService:

    def __init__(self):

        self.agent = (
            MaintainerAgent()
        )

    def analyze(self):

        return (
            self.agent.analyze()
        )
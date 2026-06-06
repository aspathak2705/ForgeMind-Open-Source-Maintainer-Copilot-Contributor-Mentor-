from agents.maintainer_agent.hotspot_analyzer import (
    HotspotAnalyzer,
)

from agents.maintainer_agent.repository_health import (
    RepositoryHealth,
)

from agents.maintainer_agent.release_notes_generator import (
    ReleaseNotesGenerator,
)


class MaintainerAgent:

    def __init__(self):

        self.hotspots = (
            HotspotAnalyzer()
        )

        self.health = (
            RepositoryHealth()
        )

        self.release_notes = (
            ReleaseNotesGenerator()
        )

    def analyze(self):

        health = (
            self.health.analyze()
        )

        hotspots = (
            self.hotspots.analyze()
        )

        context = {
            "health": health,
            "hotspots": hotspots,
        }

        summary = (
            self.release_notes.generate(
                context
            )
        )

        return {
            "health": health,
            "hotspots": hotspots,
            "summary": summary,
        }
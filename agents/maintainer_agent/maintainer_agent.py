from agents.maintainer_agent.hotspot_analyzer import (
    HotspotAnalyzer,
)

from agents.maintainer_agent.repository_health import (
    RepositoryHealth,
)

from agents.maintainer_agent.release_notes_generator import (
    ReleaseNotesGenerator,
)
from storage.memory.agent_memory import (
    AgentMemory,
)

from core.reflection.reflection_service import (
    ReflectionService,
)

from core.reporting.report_formatter import (
    ReportFormatter,
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

        self.memory = AgentMemory()

        self.reflection = (
            ReflectionService()
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

        raw_summary = (
            self.release_notes.generate(
                context
            )
        )

        summary = (
            ReportFormatter
            .maintainer_report(
                raw_summary
            )
        )

        self.memory.remember(
            "maintainer_agent",
            "repository_analysis",
            {
                "health": health,
                "top_hotspot": (
                    hotspots[0]["file"]
                    if hotspots
                    else None
                ),
                "impact_score": (
                    hotspots[0]["impact_score"]
                    if hotspots
                    else 0
                ),
                "hotspot_count": len(
                    hotspots
                ),
            },
        )

        self.reflection.record(
            "maintainer_agent",
            "Repository analysis completed",
            {
                "hotspots": len(
                    hotspots
                )
            },
        )

        return {
            "health": health,
            "hotspots": hotspots,
            "summary": summary,
        }
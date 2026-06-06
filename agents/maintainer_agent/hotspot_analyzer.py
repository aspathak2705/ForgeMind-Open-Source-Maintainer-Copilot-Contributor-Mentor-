from core.repository.impact_analyzer import (
    ImpactAnalyzer,
)


class HotspotAnalyzer:

    def __init__(self):

        self.impact = (
            ImpactAnalyzer()
        )

    def analyze(self):

        data = (
            self.impact.analyze_all()
        )

        hotspots = sorted(
            data.values(),
            key=lambda x: x["impact_score"],
            reverse=True,
        )

        return hotspots[:10]
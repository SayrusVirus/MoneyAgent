class AnalystAgent:
    def analyze(self, project):
        score = 0

        budget = (project.budget or "").lower()
        title = (project.title or "").lower()
        description = (project.description or "").lower()

        if "$" in budget:
            score += 30

        if "python" in title:
            score += 30

        if "api" in description:
            score += 20

        if "telegram" in title:
            score += 20

        if score >= 70:
            priority = "high"
        elif score >= 40:
            priority = "medium"
        else:
            priority = "low"

        return {
            "project_id": project.id,
            "title": project.title,
            "score": score,
            "priority": priority
        }
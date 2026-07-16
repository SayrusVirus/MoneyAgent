class AnalystAgent:

    def analyze(self, project):

        score = 80

        return {
            "project_id": project.id,
            "title": project.title,
            "score": score,
            "profitability": "high",
            "difficulty": "medium",
            "recommendation": "take",
            "reason": "Demo AI analysis"
        }
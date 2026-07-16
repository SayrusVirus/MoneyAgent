from app.memory.agent_memory import AgentMemory


class AnalystAgent:

    def __init__(self, db=None):
        self.db = db


    def analyze(self, project):

        score = 50

        profitability = "medium"
        difficulty = "medium"


        # Оценка бюджета
        if project.budget:

            if "500" in project.budget or "1000" in project.budget:
                score += 20
                profitability = "high"

            elif "250" in project.budget:
                score += 10


        # Оценка сложности по описанию
        description = (
            project.description or ""
        ).lower()


        if "api" in description or "fastapi" in description:
            score += 15
            difficulty = "medium"


        if "telegram" in description or "bot" in description:
            score += 10
            difficulty = "low"


        # Ограничение
        if score > 100:
            score = 100


        if score >= 70:
            recommendation = "take"
            reason = "Good profitability and acceptable complexity"

        elif score >= 40:
            recommendation = "review"
            reason = "Needs additional analysis"

        else:
            recommendation = "skip"
            reason = "Low potential"


        result = {
            "project_id": project.id,
            "title": project.title,
            "score": score,
            "profitability": profitability,
            "difficulty": difficulty,
            "recommendation": recommendation,
            "reason": reason
        }


        if self.db:

            memory = AgentMemory(self.db)

            memory.save(
                agent_name="AnalystAgent",
                project_id=project.id,
                action="ANALYSIS",
                result=str(result)
            )


        return result
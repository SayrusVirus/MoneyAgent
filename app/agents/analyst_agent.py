from app.memory.agent_memory import AgentMemory


class AnalystAgent:

    def __init__(self, db=None):
        self.db = db


    def analyze(self, project):

        score = 80

        result = {
            "project_id": project.id,
            "title": project.title,
            "score": score,
            "profitability": "high",
            "difficulty": "medium",
            "recommendation": "take",
            "reason": "Demo AI analysis"
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
from app.memory.agent_memory import AgentMemory


class DecisionAgent:

    def __init__(self, db=None):
        self.db = db


    def decide(self, analysis):

        score = analysis["score"]

        if score >= 70:
            decision = "TAKE"
            reason = "High potential project"

        elif score >= 40:
            decision = "REVIEW"
            reason = "Need additional analysis"

        else:
            decision = "SKIP"
            reason = "Low profitability"


        result = {
            "project_id": analysis["project_id"],
            "title": analysis["title"],
            "score": score,
            "decision": decision,
            "reason": reason
        }


        if self.db:
            memory = AgentMemory(self.db)

            memory.save(
                agent_name="DecisionAgent",
                project_id=analysis["project_id"],
                action="DECISION",
                result=str(result)
            )

        return result

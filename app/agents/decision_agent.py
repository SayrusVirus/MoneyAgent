class DecisionAgent:

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

        return {
            "project_id": analysis["project_id"],
            "title": analysis["title"],
            "score": score,
            "decision": decision,
            "reason": reason
        }
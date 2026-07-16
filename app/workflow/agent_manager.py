from app.agents.scout_agent import ScoutAgent
from app.agents.analyst_agent import AnalystAgent
from app.agents.decision_agent import DecisionAgent


class AgentManager:

    def __init__(self, db):
        self.db = db


    def run(self):

        # 1. Scout
        scout = ScoutAgent(self.db)
        scout_result = scout.run()


        # 2. Analyst + Decision
        projects = self.db.query(
            __import__(
                "app.database.models",
                fromlist=["Project"]
            ).Project
        ).all()


        analyst = AnalystAgent(self.db)
        decision_agent = DecisionAgent(self.db)


        decisions = []


        for project in projects:

            analysis = analyst.analyze(project)

            decision = decision_agent.decide(
                analysis
            )

            decisions.append(decision)


        return {
            "scout": scout_result,
            "decisions": decisions
        }
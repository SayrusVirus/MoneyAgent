from app.agents.scout_agent import ScoutAgent
from app.agents.analyst_agent import AnalystAgent
from app.agents.decision_agent import DecisionAgent

from app.services.task_service import TaskService
from app.database.models import Project


class AgentManager:

    def __init__(self, db):
        self.db = db
        self.tasks = TaskService(db)


    def run(self):

        task = self.tasks.create(
            "Full Agent Workflow"
        )

        try:

            task.status = "RUNNING"
            self.db.commit()


            scout = ScoutAgent(self.db)

            scout_result = scout.run()


            projects = self.db.query(
                Project
            ).all()


            analyst = AnalystAgent(self.db)
            decision_agent = DecisionAgent(self.db)


            decisions = []


            for project in projects:

                analysis = analyst.analyze(
                    project
                )

                decision = decision_agent.decide(
                    analysis
                )

                decisions.append(
                    decision
                )


            result = {
                "scout": scout_result,
                "decisions": decisions
            }


            self.tasks.complete(
                task,
                result
            )


            return result


        except Exception as e:

            self.tasks.fail(
                task,
                e
            )

            raise e
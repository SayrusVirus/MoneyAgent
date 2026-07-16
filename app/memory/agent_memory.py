from app.database.models import AgentLog


class AgentMemory:

    def __init__(self, db):
        self.db = db


    def save(
        self,
        agent_name,
        project_id,
        action,
        result
    ):

        log = AgentLog(
            agent_name=agent_name,
            project_id=project_id,
            action=action,
            result=result
        )

        self.db.add(log)
        self.db.commit()

        return log
from datetime import datetime

from app.database.models import AgentTask


class TaskService:


    def __init__(self, db):
        self.db = db


    def create(self, name):

        task = AgentTask(
            name=name,
            status="NEW"
        )

        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)

        return task


    def complete(self, task, result):

        task.status = "COMPLETED"
        task.result = str(result)
        task.completed_at = datetime.utcnow()

        self.db.commit()

        return task


    def fail(self, task, error):

        task.status = "FAILED"
        task.result = str(error)

        self.db.commit()

        return task
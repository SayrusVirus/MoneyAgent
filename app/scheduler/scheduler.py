from threading import Thread
from time import sleep

from app.workflow.agent_manager import AgentManager


class AgentScheduler:

    def __init__(self, db_factory):
        self.db_factory = db_factory
        self.running = False
        self.thread = None


    def run_cycle(self):

        db = self.db_factory()

        try:
            manager = AgentManager(db)
            manager.run()

        finally:
            db.close()


    def worker(self):

        while self.running:

            self.run_cycle()

            sleep(1800)  # 30 минут


    def start(self):

        if self.running:
            return {
                "status": "already running"
            }

        self.running = True

        self.thread = Thread(
            target=self.worker,
            daemon=True
        )

        self.thread.start()

        return {
            "status": "started"
        }


    def stop(self):

        self.running = False

        return {
            "status": "stopped"
        }


    def status(self):

        return {
            "running": self.running
        }
from apscheduler.schedulers.background import BackgroundScheduler

from app.database.database import SessionLocal
from app.workflow.agent_manager import AgentManager


scheduler = BackgroundScheduler()


def run_agents():

    db = SessionLocal()

    try:
        manager = AgentManager(db)
        result = manager.run()

        print(
            "Scheduled Agent Run:",
            result
        )

    except Exception as e:
        print(
            "Scheduler error:",
            e
        )

    finally:
        db.close()



def start_scheduler():

    scheduler.add_job(
        run_agents,
        "interval",
        hours=6,
        id="moneyagent_cycle",
        replace_existing=True
    )

    scheduler.start()
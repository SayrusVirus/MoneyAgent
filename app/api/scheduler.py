from fastapi import APIRouter

from app.database.database import SessionLocal
from app.scheduler.scheduler import AgentScheduler
from app.workflow.agent_manager import AgentManager


router = APIRouter(
    prefix="/scheduler",
    tags=["Scheduler"]
)


scheduler = AgentScheduler(
    SessionLocal
)


@router.post("/start")
def start():

    return scheduler.start()



@router.post("/stop")
def stop():

    return scheduler.stop()



@router.get("/status")
def status():

    return scheduler.status()



@router.post("/run-now")
def run_now():

    db = SessionLocal()

    try:

        manager = AgentManager(db)

        result = manager.run()

        return result

    finally:

        db.close()
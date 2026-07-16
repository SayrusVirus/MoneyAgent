from fastapi import APIRouter

from app.database.database import SessionLocal
from app.scheduler.scheduler import AgentScheduler


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
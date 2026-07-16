from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI

from app.api.tasks import router as tasks_router
from app.api.projects import router as projects_router
from app.api.scout import router as scout_router
from app.api.analyst import router as analyst_router
from app.api.decision import router as decision_router
from app.api.memory import router as memory_router
from app.api.agents import router as agents_router
from app.api.scheduler import router as scheduler_router
from app.scheduler.agent_scheduler import start_scheduler

from app.database.database import Base, engine
from app.database.models import Project


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="MoneyAgent",
    version="0.9.0",
)
start_scheduler()

app.include_router(projects_router)
app.include_router(scout_router)
app.include_router(analyst_router)
app.include_router(decision_router)
app.include_router(memory_router)
app.include_router(agents_router)
app.include_router(tasks_router)
app.include_router(scheduler_router)


@app.get("/")
def root():
    return {
        "status": "online",
        "database": "connected",
        "version": "0.9.0"
    }
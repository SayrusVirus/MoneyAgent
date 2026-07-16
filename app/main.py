from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI

from app.api.projects import router as projects_router
from app.api.scout import router as scout_router
from app.api.analyst import router as analyst_router
from app.api.decision import router as decision_router

from app.database.database import Base, engine
from app.database.models import Project


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="MoneyAgent",
    version="0.5.0",
)


app.include_router(projects_router)
app.include_router(scout_router)
app.include_router(analyst_router)
app.include_router(decision_router)


@app.get("/")
def root():
    return {
        "status": "online",
        "database": "connected",
        "version": "0.5.0"
    }
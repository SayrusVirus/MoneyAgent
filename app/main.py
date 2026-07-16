from fastapi import FastAPI

from app.api.projects import router as projects_router
from app.database.database import Base, engine
from app.database.models import Project

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MoneyAgent",
    version="0.2.0",
)

app.include_router(projects_router)


@app.get("/")
def root():
    return {
        "status": "online",
        "database": "connected",
        "version": "0.2.0"
    }
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.models import Project
from app.agents.analyst_agent import AnalystAgent


router = APIRouter(
    prefix="/analyst",
    tags=["Analyst Agent"]
)


@router.get("/projects")
def analyze_projects(db: Session = Depends(get_db)):

    projects = db.query(Project).all()

    agent = AnalystAgent()

    results = []

    for project in projects:
        results.append(
            agent.analyze(project)
        )

    return results
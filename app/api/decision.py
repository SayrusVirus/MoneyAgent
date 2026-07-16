from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.models import Project

from app.agents.analyst_agent import AnalystAgent
from app.agents.decision_agent import DecisionAgent


router = APIRouter(
    prefix="/decision",
    tags=["Decision Agent"]
)


@router.get("/projects")
def decide_projects(db: Session = Depends(get_db)):

    projects = db.query(Project).all()

    analyst = AnalystAgent(db)
    decision_agent = DecisionAgent(db)

    results = []

    for project in projects:
        analysis = analyst.analyze(project)
        decision = decision_agent.decide(analysis)
        results.append(decision)

    return results
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.workflow.agent_manager import AgentManager


router = APIRouter(
    prefix="/agents",
    tags=["Agent Workflow"]
)


@router.post("/run")
def run_agents(
    db: Session = Depends(get_db)
):

    manager = AgentManager(db)

    return manager.run()
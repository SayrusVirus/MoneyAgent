from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.agents.scout_agent import ScoutAgent

router = APIRouter(
    prefix="/scout",
    tags=["Scout Agent"]
)


@router.post("/run")
def run_scout(db: Session = Depends(get_db)):
    agent = ScoutAgent(db)
    return agent.run()
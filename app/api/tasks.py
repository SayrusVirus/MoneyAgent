from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.models import AgentTask


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/")
def tasks(
    db: Session = Depends(get_db)
):

    return db.query(AgentTask).all()
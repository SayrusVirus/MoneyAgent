from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.models import AgentLog


router = APIRouter(
    prefix="/memory",
    tags=["Agent Memory"]
)


@router.get("/logs")
def get_logs(db: Session = Depends(get_db)):

    return db.query(AgentLog).all()
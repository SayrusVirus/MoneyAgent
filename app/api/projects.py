from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.models import Project

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.post("/demo")
def create_demo_project(db: Session = Depends(get_db)):
    project = Project(
        title="Telegram Bot Developer",
        description="Need a bot built with Python and FastAPI",
        budget="$300-500",
        url="demo://project-1",
        source="demo"
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    return {
        "id": project.id,
        "title": project.title
    }


@router.get("/")
def get_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()
    
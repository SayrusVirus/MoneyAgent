from sqlalchemy.orm import Session

from app.database.models import Project


class ProjectService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Project).all()

    def get_by_url(self, url: str):
        return self.db.query(Project).filter(Project.url == url).first()

    def create(
        self,
        title: str,
        description: str,
        budget: str,
        url: str,
        source: str,
    ):
        existing = self.get_by_url(url)

        if existing:
            return existing

        project = Project(
            title=title,
            description=description,
            budget=budget,
            url=url,
            source=source,
        )

        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)

        return project
        
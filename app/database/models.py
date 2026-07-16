from sqlalchemy import Column, Integer, String, Text

from app.database.database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(300), nullable=False)

    description = Column(Text)

    budget = Column(String(100))

    url = Column(String(500), unique=True)

    source = Column(String(50))

    status = Column(String(50), default="new")
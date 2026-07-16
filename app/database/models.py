from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.database.database import Base


class Project(Base):

    __tablename__ = "projects"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(300),
        nullable=False
    )

    description = Column(
        Text
    )

    budget = Column(
        String(100)
    )

    url = Column(
        String(500),
        unique=True
    )

    source = Column(
        String(50)
    )

    status = Column(
        String(50),
        default="new"
    )


class AgentLog(Base):

    __tablename__ = "agent_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    agent_name = Column(
        String(100),
        nullable=False
    )

    project_id = Column(
        Integer
    )

    action = Column(
        String(100)
    )

    result = Column(
        Text
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class AgentTask(Base):

    __tablename__ = "agent_tasks"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    status = Column(
        String(50),
        default="NEW"
    )

    result = Column(
        Text
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    completed_at = Column(
        DateTime
    )
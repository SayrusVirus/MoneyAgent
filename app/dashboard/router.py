from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.database.models import Project, AgentTask
from app.database.models import Project, AgentTask, AgentLog
from app.database.models import Project, AgentTask



router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/", response_class=HTMLResponse)
def dashboard(request: Request):

    db: Session = SessionLocal()

    try:
        projects = db.query(Project).all()

        tasks = (
            db.query(AgentTask)
            .order_by(AgentTask.id.desc())
            .limit(5)
            .all()
        )

        html = """
        <html>
        <head>
            <title>MoneyAgent Dashboard</title>
            <style>
                body {
                    font-family: Arial;
                    margin: 40px;
                    background: #f5f5f5;
                }

                .card {
                    background:white;
                    padding:20px;
                    margin:15px;
                    border-radius:10px;
                }

                button {
                    padding:12px;
                    background:#2563eb;
                    color:white;
                    border:none;
                    border-radius:8px;
                }
            </style>
        </head>

        <body>

        <h1>🤖 MoneyAgent Dashboard</h1>

        <div class="card">
        <h2>Projects</h2>
        """

        for p in projects:
            html += f"""
            <p>
            <b>{p.title}</b><br>
            Budget: {p.budget}<br>
            Source: {p.source}
            </p>
            <hr>
            """

        html += """
        </div>

        <div class="card">

        <h2>Tasks</h2>
        """

        for t in tasks:
            html += f"""
            <p>
            #{t.id}
            {t.name}
            -
            {t.status}
            </p>
            """

        html += """

        </div>

        <div class="card">

        <form action="/scheduler/run-now" method="post">

        <button>
        🚀 RUN AGENTS
        </button>

        </form>

        </div>

        </body>
        </html>

        """

        return html

    finally:
        db.close()
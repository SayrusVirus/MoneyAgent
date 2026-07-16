from app.services.project_service import ProjectService


class ScoutAgent:

    def __init__(self, db):
        self.projects = ProjectService(db)


    def run(self):

        demo_projects = [
            {
                "title": "Python FastAPI Developer",
                "description": "Build REST API",
                "budget": "$500",
                "url": "demo://1",
                "source": "demo",
            },
            {
                "title": "Telegram Bot",
                "description": "Python Telegram Bot",
                "budget": "$250",
                "url": "demo://2",
                "source": "demo",
            },
        ]


        added = 0
        skipped = 0


        for item in demo_projects:

            if self.projects.exists_by_url(item["url"]):
                skipped += 1
                continue


            self.projects.create(**item)
            added += 1


        return {
            "status": "completed",
            "added": added,
            "skipped": skipped,
        }
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.db.database import get_db
from app.db.models import Team

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/teams/{team_id}", response_class=HTMLResponse)
async def get_team(request: Request, team_id: int):
    async with get_db() as session:
        team = await session.get(Team, team_id)
        if team:
            return templates.TemplateResponse("team.html", {"request": request, "team": team})
        return templates.TemplateResponse("404.html", {"request": request}, status_code=404)

@router.get("/teams", response_class=HTMLResponse)
async def list_teams(request: Request):
    async with get_db() as session:
        teams = await session.execute("SELECT * FROM teams")
        return templates.TemplateResponse("teams.html", {"request": request, "teams": teams})

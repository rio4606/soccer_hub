from fastapi import APIRouter
from app.routes import teams, matches

router = APIRouter()
router.include_router(teams.router)
router.include_router(matches.router)

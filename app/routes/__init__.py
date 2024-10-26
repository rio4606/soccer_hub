from fastapi import APIRouter
from app.routes import teams, matches

router = APIRouter()
router.include_router(teams.router)
router.include_router(matches.router)

from .teams import router as teams_router
from .matches import router as matches_router
from .analytics import router as analytics_router
from .players import router as players_router

# Экспортируем маршруты
__all__ = ["teams_router", "matches_router", "analytics_router", "players_router"]

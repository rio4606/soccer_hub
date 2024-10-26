from fastapi import APIRouter
from typing import List

router = APIRouter()

@router.get("/", summary="Получить аналитику команд", response_model=List[dict])
async def get_analytics():
    # Логика получения аналитики (например, топ команд и т.д.)
    analytics_data = [
        {"team_id": 1, "points": 45, "wins": 15, "losses": 5},
        {"team_id": 2, "points": 40, "wins": 13, "losses": 7},
    ]
    return analytics_data

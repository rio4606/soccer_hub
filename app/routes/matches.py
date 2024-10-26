from fastapi import APIRouter
from typing import List

router = APIRouter()

@router.get("/", summary="Получить список матчей", response_model=List[dict])
async def get_matches():
    # Логика получения списка матчей
    matches_data = [
        {"id": 1, "home_team": "Команда A", "away_team": "Команда B", "date": "2024-10-26", "home_score": 2, "away_score": 1},
        {"id": 2, "home_team": "Команда C", "away_team": "Команда D", "date": "2024-10-27", "home_score": 1, "away_score": 3},
    ]
    return matches_data

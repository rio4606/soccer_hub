from fastapi import APIRouter
from typing import List

router = APIRouter()

@router.get("/", summary="Получить список игроков", response_model=List[dict])
async def get_players():
    # Логика получения списка игроков
    players_data = [
        {"id": 1, "name": "Игрок 1", "position": "Нападающий", "team_id": 1},
        {"id": 2, "name": "Игрок 2", "position": "Защитник", "team_id": 1},
    ]
    return players_data

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

# --- Схемы для команд ---
class TeamBase(BaseModel):
    name: str
    city: Optional[str] = None
    founded: Optional[int] = None
    stadium: Optional[str] = None

class TeamCreate(TeamBase):
    pass

class TeamUpdate(TeamBase):
    name: Optional[str] = None

class Team(TeamBase):
    id: int
    players: List["Player"] = []  # Список игроков, если нужно включить их в ответе

    class Config:
        from_attributes = True  # Включаем поддержку ORM для моделей SQLAlchemy


# --- Схемы для игроков ---
class PlayerBase(BaseModel):
    name: str
    position: str

class PlayerCreate(PlayerBase):
    team_id: int

class PlayerUpdate(PlayerBase):
    name: Optional[str] = None
    position: Optional[str] = None

class Player(PlayerBase):
    id: int
    team: Optional[Team] = None  # Включение информации о команде в ответе, если нужно

    class Config:
        from_attributes = True


# --- Схемы для матчей ---
class MatchBase(BaseModel):
    home_team_id: int
    away_team_id: int
    date: datetime

class MatchCreate(MatchBase):
    home_score: Optional[int] = None
    away_score: Optional[int] = None

class MatchUpdate(BaseModel):
    home_score: Optional[int] = None
    away_score: Optional[int] = None

class Match(MatchBase):
    id: int
    home_score: Optional[int] = None
    away_score: Optional[int] = None
    home_team: Optional[Team] = None  # Включение информации о домашней команде
    away_team: Optional[Team] = None  # Включение информации о гостевой команде

    class Config:
        from_attributes = True

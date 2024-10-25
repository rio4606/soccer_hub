# db/schemas.py
from pydantic import BaseModel
from datetime import datetime

class TeamCreate(BaseModel):
    name: str
    city: str
    founded: int
    stadium: str

class TeamOut(BaseModel):
    id: int
    name: str
    city: str
    founded: int
    stadium: str

    class Config:
        orm_mode = True

class MatchCreate(BaseModel):
    home_team_id: int
    away_team_id: int
    date: datetime
    score: str

class MatchOut(BaseModel):
    id: int
    home_team: TeamOut
    away_team: TeamOut
    date: datetime
    score: str

    class Config:
        orm_mode = True

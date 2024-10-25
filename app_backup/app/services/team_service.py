# services/team_service.py
from sqlalchemy.orm import Session
from db.models import Team
from db.schemas import TeamCreate

def get_team(db: Session, team_id: int):
    return db.query(Team).filter(Team.id == team_id).first()

def create_team(db: Session, team: TeamCreate):
    db_team = Team(**team.dict())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

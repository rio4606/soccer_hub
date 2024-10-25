from sqlalchemy.orm import Session
from app.db import models, schemas

# Получение всех матчей
def get_all_matches(db: Session):
    return db.query(models.Match).all()

# Создание нового матча
def create_match(db: Session, match: schemas.MatchCreate):
    db_match = models.Match(
        home_team_id=match.home_team_id,
        away_team_id=match.away_team_id,
        date=match.date,
        home_score=match.home_score,
        away_score=match.away_score
    )
    db.add(db_match)
    db.commit()
    db.refresh(db_match)
    return db_match

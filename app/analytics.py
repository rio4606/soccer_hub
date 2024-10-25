from datetime import datetime
from sqlalchemy.orm import Session
from app.db import models

# Запись действия пользователя
def log_user_action(db: Session, user_id: int, action: str):
    action_log = models.ActionLog(
        user_id=user_id,
        action=action,
        timestamp=datetime.utcnow()
    )
    db.add(action_log)
    db.commit()
    db.refresh(action_log)
    return action_log

# Получение статистики по действиям пользователей
def get_user_actions(db: Session, user_id: int):
    actions = db.query(models.ActionLog).filter(models.ActionLog.user_id == user_id).all()
    return actions

# Получение общего количества посещений
def get_visit_count(db: Session):
    return db.query(models.ActionLog).count()

# Получение статистики по действиям за определенный период
def get_actions_by_period(db: Session, start_date: datetime, end_date: datetime):
    actions = db.query(models.ActionLog).filter(models.ActionLog.timestamp.between(start_date, end_date)).all()
    return actions

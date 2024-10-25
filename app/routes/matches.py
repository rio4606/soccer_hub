from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.db import models, schemas
from app.services.match_service import get_all_matches, create_match

router = APIRouter()

# Маршрут для получения списка матчей
@router.get("/matches/", response_model=List[schemas.Match])
def get_matches(db: Session = Depends(get_db)):
    matches = get_all_matches(db)
    if not matches:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Матчи не найдены")
    return matches

# Маршрут для создания нового матча
@router.post("/matches/", response_model=schemas.Match, status_code=status.HTTP_201_CREATED)
def create_new_match(match: schemas.MatchCreate, db: Session = Depends(get_db)):
    return create_match(db=db, match=match)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# app/db/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL, settings

Base = declarative_base()

# Создаем движок для подключения к базе данных
engine = create_engine(DATABASE_URL)

# Создание локальной сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для всех моделей
Base = declarative_base()

# Функция для создания сессии для каждого запроса
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

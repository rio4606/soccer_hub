import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from app.db.database import engine, Base
from app.routes import teams, matches
from app.core.config import settings

# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Создание экземпляра FastAPI
app = FastAPI(title="Soccer Hub API")

# Настройка CORS
origins = [
    "http://localhost:3000",
    "https://your-frontend-url.com",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение маршрутов
app.include_router(teams.router, prefix="/teams", tags=["Команды"])
app.include_router(matches.router, prefix="/matches", tags=["Матчи"])

# Обработка ошибок
@app.exception_handler((RequestValidationError, SQLAlchemyError))
async def global_exception_handler(request, exc):
    if isinstance(exc, RequestValidationError):
        logger.warning(f"Ошибка валидации: {exc.errors()} на запросе: {await request.json()}")
        return JSONResponse(
            status_code=422,
            content={"detail": exc.errors(), "body": exc.body},
        )
    elif isinstance(exc, SQLAlchemyError):
        logger.error(f"Ошибка базы данных: {exc} на запросе: {await request.json()}")
        return JSONResponse(
            status_code=500,
            content={"detail": "Ошибка базы данных. Пожалуйста, попробуйте позже."},
        )

# Создание таблиц базы данных
@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)
    logger.info("База данных инициализирована.")

@app.on_event("shutdown")
async def shutdown():
    logger.info("Приложение завершает работу.")

# Основной маршрут
@app.get("/", summary="Главная страница")
async def root() -> dict:
    return {"message": "Добро пожаловать в Soccer Hub API."}

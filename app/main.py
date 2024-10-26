import logging
from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.db.database import engine, Base, get_db
from app.db.models import Match, Player
from app.routes import teams_router, matches_router, analytics_router, players_router
from app.core.config import Settings

# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Создание экземпляра FastAPI
app = FastAPI(title="Soccer Hub API")
templates = Jinja2Templates(directory="app/templates")

# Получение настроек из класса Settings
settings = Settings()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["*"],  # Можно ограничить, если нужно
)

# Подключение маршрутов
# app.include_router(teams_router, prefix="/teams", tags=["Команды"])
# app.include_router(matches_router, prefix="/matches", tags=["Матчи"])
# app.include_router(analytics_router, prefix="/analytics", tags=["Аналитика"])
# app.include_router(players_router, prefix="/players", tags=["Игроки"])

# Обработка ошибки валидации
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.warning(f"Ошибка валидации: {exc.errors()} на запросе: {await request.json()}")
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )

# Обработка ошибки SQLAlchemy
@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
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
@app.get("/", response_class=HTMLResponse, summary="Главная страница")
async def root(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("index.html", {"request": request})

# Дополнительные маршруты для страниц
@app.get("/teams", response_class=HTMLResponse, summary="Команды")
async def teams_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("teams.html", {"request": request})

@app.get("/matches", response_class=HTMLResponse, summary="Матчи")
async def matches_page(request: Request, db: Session = Depends(get_db)):
    matches = db.query(Match).all()
    return templates.TemplateResponse("matches.html", {"request": request, "matches": matches})

@app.get("/players", response_class=HTMLResponse, summary="Игроки")
async def get_players(request: Request, db: Session = Depends(get_db)):
    players = db.query(Player).all()  # Получаем всех игроков
    return templates.TemplateResponse("players.html", {"request": request, "players": players})

@app.get("/analytics", response_class=HTMLResponse, summary="Аналитика")
async def analytics_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("analytics.html", {"request": request})

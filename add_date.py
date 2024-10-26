from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from app.db.models import Team, Player, Match, Base  # Импорт моделей и базового класса
from app.core.config import DATABASE_URL

# Создаем движок для подключения к базе данных
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

# Создаем сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# Функции для добавления записей
def add_team(name, city, founded, stadium):
    team = Team(name=name, city=city, founded=founded, stadium=stadium)
    session.add(team)
    session.commit()
    print(f"Added team: {team.name}")

def add_player(name, position, team_id):
    player = Player(name=name, position=position, team_id=team_id)
    session.add(player)
    session.commit()
    print(f"Added player: {player.name} to team ID {team_id}")

def add_match(home_team_id, away_team_id, date, home_score=None, away_score=None):
    match = Match(
        home_team_id=home_team_id,
        away_team_id=away_team_id,
        date=date,
        home_score=home_score,
        away_score=away_score
    )
    session.add(match)
    session.commit()
    print(f"Added match on {match.date} between teams {home_team_id} and {away_team_id}")

# Добавление российских футбольных клубов
try:
    add_team("Зенит", "Санкт-Петербург", 1925, "Газпром Арена")
    add_team("Спартак", "Москва", 1922, "Открытие Арена")
    add_team("ЦСКА", "Москва", 1911, "ВЭБ Арена")
    add_team("Локомотив", "Москва", 1922, "РЖД Арена")
    add_team("Краснодар", "Краснодар", 2008, "Стадион Краснодар")
    add_team("Динамо", "Москва", 1923, "ВТБ Арена")
    add_team("Рубин", "Казань", 1958, "Казань Арена")
    add_team("Ростов", "Ростов-на-Дону", 1930, "Ростов Арена")
    add_team("Ахмат", "Грозный", 1946, "Ахмат Арена")
    add_team("Сочи", "Сочи", 2018, "Фишт")

    # Добавление игроков для каждой команды
    add_player("Артем Дзюба", "Forward", team_id=1)  # Зенит
    add_player("Вилмар Барриос", "Midfielder", team_id=1)
    add_player("Малком", "Forward", team_id=1)

    add_player("Александр Соболев", "Forward", team_id=2)  # Спартак
    add_player("Зелимхан Бакаев", "Midfielder", team_id=2)
    add_player("Джордан Ларссон", "Forward", team_id=2)

    add_player("Федор Чалов", "Forward", team_id=3)  # ЦСКА
    add_player("Игорь Акинфеев", "Goalkeeper", team_id=3)
    add_player("Никола Влашич", "Midfielder", team_id=3)

    add_player("Антон Миранчук", "Midfielder", team_id=4)  # Локомотив
    add_player("Гжегож Крыховяк", "Midfielder", team_id=4)
    add_player("Эдер", "Forward", team_id=4)

    add_player("Маркус Берг", "Forward", team_id=5)  # Краснодар
    add_player("Реми Кабелла", "Midfielder", team_id=5)
    add_player("Юрий Газинский", "Midfielder", team_id=5)

    add_player("Клинтон Н'Жи", "Forward", team_id=6)  # Динамо
    add_player("Александр Ташаев", "Midfielder", team_id=6)

    add_player("Георгий Махатадзе", "Midfielder", team_id=7)  # Рубин
    add_player("Дмитрий Полоз", "Forward", team_id=8)  # Ростов
    add_player("Бернард Бериша", "Forward", team_id=9)  # Ахмат
    add_player("Алексей Помазун", "Goalkeeper", team_id=10)  # Сочи

    # Добавление матчей между командами
    add_match(home_team_id=1, away_team_id=2, date=datetime(2024, 10, 25), home_score=2, away_score=1)  # Зенит vs Спартак
    add_match(home_team_id=2, away_team_id=3, date=datetime(2024, 10, 30), home_score=1, away_score=1)  # Спартак vs ЦСКА
    add_match(home_team_id=3, away_team_id=4, date=datetime(2024, 11, 5), home_score=0, away_score=3)   # ЦСКА vs Локомотив
    add_match(home_team_id=4, away_team_id=5, date=datetime(2024, 11, 10), home_score=2, away_score=2)  # Локомотив vs Краснодар
    add_match(home_team_id=5, away_team_id=1, date=datetime(2024, 11, 15), home_score=1, away_score=4)  # Краснодар vs Зенит
    add_match(home_team_id=6, away_team_id=7, date=datetime(2024, 11, 20), home_score=0, away_score=1)  # Динамо vs Рубин
    add_match(home_team_id=7, away_team_id=8, date=datetime(2024, 11, 25), home_score=3, away_score=3)  # Рубин vs Ростов
    add_match(home_team_id=8, away_team_id=9, date=datetime(2024, 11, 30), home_score=2, away_score=2)  # Ростов vs Ахмат
    add_match(home_team_id=9, away_team_id=10, date=datetime(2024, 12, 5), home_score=1, away_score=1)  # Ахмат vs Сочи
    add_match(home_team_id=10, away_team_id=6, date=datetime(2024, 12, 10), home_score=1, away_score=0)  # Сочи vs Динамо

finally:
    # Закрываем сессию после завершения добавления
    session.close()
    print("Session closed.")

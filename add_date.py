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

# Функции для добавления записей
def add_team(session, name, city, founded, stadium):
    team = Team(name=name, city=city, founded=founded, stadium=stadium)
    session.add(team)
    session.commit()
    print(f"Added team: {team.name}")

def add_player(session, name, position, team_id, goals=0):  # Предполагая, что у вас есть поле goals
    player = Player(name=name, position=position, team_id=team_id, goals=goals)  # goals = 0 по умолчанию
    session.add(player)
    session.commit()
    print(f"Added player: {player.name} to team ID {team_id}")

def add_match(session, home_team_id, away_team_id, date, home_score=None, away_score=None):
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
session = SessionLocal()
try:
    # Добавление команд
    teams_data = [
        ("Зенит", "Санкт-Петербург", 1925, "Газпром Арена"),
        ("Спартак", "Москва", 1922, "Открытие Арена"),
        ("ЦСКА", "Москва", 1911, "ВЭБ Арена"),
        ("Локомотив", "Москва", 1922, "РЖД Арена"),
        ("Краснодар", "Краснодар", 2008, "Стадион Краснодар"),
        ("Динамо", "Москва", 1923, "ВТБ Арена"),
        ("Рубин", "Казань", 1958, "Казань Арена"),
        ("Ростов", "Ростов-на-Дону", 1930, "Ростов Арена"),
        ("Ахмат", "Грозный", 1946, "Ахмат Арена"),
        ("Сочи", "Сочи", 2018, "Фишт"),
    ]
    
    for team in teams_data:
        add_team(session, *team)

    # Добавление игроков для каждой команды
    players_data = [
        ("Артем Дзюба", "Forward", 1),
        ("Вилмар Барриос", "Midfielder", 1),
        ("Малком", "Forward", 1),
        ("Александр Соболев", "Forward", 2),
        ("Зелимхан Бакаев", "Midfielder", 2),
        ("Джордан Ларссон", "Forward", 2),
        ("Федор Чалов", "Forward", 3),
        ("Игорь Акинфеев", "Goalkeeper", 3),
        ("Никола Влашич", "Midfielder", 3),
        ("Антон Миранчук", "Midfielder", 4),
        ("Гжегож Крыховяк", "Midfielder", 4),
        ("Эдер", "Forward", 4),
        ("Маркус Берг", "Forward", 5),
        ("Реми Кабелла", "Midfielder", 5),
        ("Юрий Газинский", "Midfielder", 5),
        ("Клинтон Н'Жи", "Forward", 6),
        ("Александр Ташаев", "Midfielder", 6),
        ("Георгий Махатадзе", "Midfielder", 7),
        ("Дмитрий Полоз", "Forward", 8),
        ("Бернард Бериша", "Forward", 9),
        ("Алексей Помазун", "Goalkeeper", 10),
    ]
    
    for player in players_data:
        add_player(session, *player)

    # Добавление матчей между командами
    matches_data = [
        (1, 2, datetime(2024, 10, 25), 2, 1),
        (2, 3, datetime(2024, 10, 30), 1, 1),
        (3, 4, datetime(2024, 11, 5), 0, 3),
        (4, 5, datetime(2024, 11, 10), 2, 2),
        (5, 1, datetime(2024, 11, 15), 1, 4),
        (6, 7, datetime(2024, 11, 20), 0, 1),
        (7, 8, datetime(2024, 11, 25), 3, 3),
        (8, 9, datetime(2024, 11, 30), 2, 2),
        (9, 10, datetime(2024, 12, 5), 1, 1),
        (10, 6, datetime(2024, 12, 10), 1, 0),
    ]
    
    for match in matches_data:
        add_match(session, *match)

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    # Закрываем сессию после завершения добавления
    session.close()
    print("Session closed.")

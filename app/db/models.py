from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.database import Base

class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    city = Column(String, index=True)
    founded = Column(Integer)  # Год основания команды
    stadium = Column(String)   # Стадион команды

    players = relationship("Player", back_populates="team", cascade="all, delete-orphan")  # Связь с игроками, каскадное удаление


class Match(Base):
    __tablename__ = 'matches'
    
    id = Column(Integer, primary_key=True, index=True)
    home_team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    away_team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    date = Column(DateTime, nullable=False)  # Дата матча
    home_score = Column(Integer, nullable=True)  # Счёт команды дома
    away_score = Column(Integer, nullable=True)  # Счёт команды гостей

    home_team = relationship('Team', foreign_keys=[home_team_id], backref='home_matches')
    away_team = relationship('Team', foreign_keys=[away_team_id], backref='away_matches')

    # Ограничение на уникальность сочетания команд и даты
    __table_args__ = (UniqueConstraint('home_team_id', 'away_team_id', 'date', name='unique_match_constraint'),)


class Player(Base):
    __tablename__ = "players"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)  # Имя игрока
    position = Column(String, nullable=False)          # Позиция игрока
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)  # Идентификатор команды
    team = relationship("Team", back_populates="players")  # Связь с командой

    # Ограничение уникальности на имя игрока и команду (два игрока с одинаковым именем в одной команде недопустимы)
    __table_args__ = (UniqueConstraint('name', 'team_id', name='unique_player_in_team'),)


class ActionLog(Base):
    __tablename__ = 'action_logs'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))  # Предполагаем, что у вас есть модель пользователей
    action = Column(String)                              # Действие пользователя
    timestamp = Column(DateTime)                         # Время действия

    user = relationship("User")                         # Связь с пользователем

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    action_logs = relationship("ActionLog", back_populates="user")  # Обратная связь с action_logs

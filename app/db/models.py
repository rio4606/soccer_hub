from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.types import Enum as SQLAEnum
from enum import Enum
from app.db.database import Base

class PositionEnum(str, Enum):
    """Перечисление для позиций игроков."""
    FORWARD = "Forward"
    MIDFIELDER = "Midfielder"
    DEFENDER = "Defender"
    GOALKEEPER = "Goalkeeper"

class Team(Base):
    """
    Модель команды, включающая информацию о названии, городе, дате основания и стадионе.
    """
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    city = Column(String, index=True)
    founded = Column(Integer)  # Год основания команды
    stadium = Column(String)   # Стадион команды
    points = Column(Integer, default=0)
    
    players = relationship("Player", back_populates="team", cascade="all, delete-orphan")  # Связь с игроками

    def __repr__(self):
        return f"<Team(id={self.id}, name='{self.name}', city='{self.city}')>"


class Match(Base):
    """
    Модель матча, связывающая команды, дату и результаты.
    """
    __tablename__ = 'matches'
    
    id = Column(Integer, primary_key=True, index=True)
    home_team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    away_team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    date = Column(DateTime, nullable=False)  # Дата матча
    home_score = Column(Integer, nullable=True, default=0)  # Счёт команды дома
    away_score = Column(Integer, nullable=True, default=0)  # Счёт команды гостей

    home_team = relationship('Team', foreign_keys=[home_team_id], backref='home_matches')
    away_team = relationship('Team', foreign_keys=[away_team_id], backref='away_matches')

    # Ограничение на уникальность сочетания команд и даты
    __table_args__ = (UniqueConstraint('home_team_id', 'away_team_id', 'date', name='unique_match_constraint'),)

    def __repr__(self):
        return f"<Match(id={self.id}, home_team_id={self.home_team_id}, away_team_id={self.away_team_id}, date={self.date})>"


class Player(Base):
    """
    Модель игрока, включая информацию о имени, позиции и команде.
    """
    __tablename__ = "players"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)                  # Имя игрока
    position = Column(SQLAEnum(PositionEnum), nullable=False)          # Позиция игрока
    goals = Column(Integer, default=0)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)  # Идентификатор команды
    team = relationship("Team", back_populates="players")              # Связь с командой

    # Ограничение уникальности на имя игрока и команду
    __table_args__ = (UniqueConstraint('name', 'team_id', name='unique_player_in_team'),)

    def __repr__(self):
        return f"<Player(id={self.id}, name='{self.name}', position='{self.position}', team_id={self.team_id})>"


class ActionLog(Base):
    """
    Лог действий пользователя.
    """
    __tablename__ = 'action_logs'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))      # Предполагаем, что у вас есть модель пользователей
    action = Column(String)                                # Действие пользователя
    timestamp = Column(DateTime)                           # Время действия

    user = relationship("User", back_populates="action_logs")  # Связь с пользователем

    def __repr__(self):
        return f"<ActionLog(id={self.id}, user_id={self.user_id}, action='{self.action}', timestamp={self.timestamp})>"


class User(Base):
    """
    Модель пользователя, содержащая информацию о логине и пароле.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    action_logs = relationship("ActionLog", back_populates="user")  # Обратная связь с action_logs

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"

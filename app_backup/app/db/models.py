from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.database import Base

class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    city = Column(String)
    founded = Column(Integer)  # Год основания команды
    stadium = Column(String)   # Стадион команды

    players = relationship("Player", back_populates="team")  # Связь с игроками


class Match(Base):
    __tablename__ = 'matches'
    
    id = Column(Integer, primary_key=True, index=True)
    home_team_id = Column(Integer, ForeignKey('teams.id'))
    away_team_id = Column(Integer, ForeignKey('teams.id'))
    date = Column(DateTime)      # Дата матча
    score = Column(String)       # Результат матча, например, "2:1"

    home_team = relationship('Team', foreign_keys=[home_team_id], backref='home_matches')
    away_team = relationship('Team', foreign_keys=[away_team_id], backref='away_matches')


class Player(Base):
    __tablename__ = "players"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)                      # Имя игрока
    position = Column(String)                              # Позиция игрока
    team_id = Column(Integer, ForeignKey("teams.id"))      # Идентификатор команды
    team = relationship("Team", back_populates="players")  # Связь с командой

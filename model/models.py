from sqlalchemy import Column, INT, VARCHAR, DATE, ForeignKey

from .base import Base


class Team(Base):
    name = Column(VARCHAR(128), nullable=False, unique=True)

    def __repr__(self):
        return self.name


class City(Base):
    name = Column(VARCHAR(128), nullable=False, unique=True)

    def __repr__(self):
        return self.name


class Position(Base):
    name = Column(VARCHAR(128), nullable=False, unique=True)

    def __repr__(self):
        return self.name


class Footballer(Base):
    full_name = Column(VARCHAR(128), nullable=False)
    date_of_birth = Column(DATE, nullable=False)
    team_id = Column(INT, ForeignKey('team.id', ondelete='CASCADE'), nullable=False)
    city_id = Column(INT, ForeignKey('city.id', ondelete='CASCADE'), nullable=False)
    position_id = Column(INT, ForeignKey('position.id', ondelete='CASCADE'), nullable=False)

    @property
    def birthdate(self):
        return self.date_of_birth.strftime('%d.%m.%Y')

    @property
    def info(self):
        return f'{self.full_name} {self.birthdate} {Team.get(self.team_id).name} {City.get(self.city_id).name} {Position.get(self.position_id).name}'

    def __repr__(self):
        return self.full_name

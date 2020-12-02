# Pulled in tables and columns with sqlacodegen --outfile
# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class NocRegion(Base):
    __tablename__ = 'noc_regions'

    region = Column(String(100), primary_key=True)
    NOC = Column(String(10), nullable=False)


t_athlete_medals = Table(
    'athlete_medals', metadata,
    Column('Sex', String(2), nullable=False),
    Column('Team', ForeignKey('noc_regions.region'), nullable=False),
    Column('NOC', String(10), nullable=False),
    Column('Games', String(100), nullable=False),
    Column('Year', Integer, nullable=False),
    Column('Season', String(50), nullable=False),
    Column('City', String(100), nullable=False),
    Column('Sport', String(50), nullable=False),
    Column('Medal', String(50), nullable=False)
)


t_city_average_temperature = Table(
    'city_average_temperature', metadata,
    Column('Country', ForeignKey('noc_regions.region'), nullable=False),
    Column('City', String(100), nullable=False),
    Column('Year', Integer, nullable=False),
    Column('Latitude', Integer, nullable=False),
    Column('Longitude', Integer, nullable=False),
    Column('AverageTemperature', Integer, nullable=False)
)


t_country_average_temperatue = Table(
    'country_average_temperatue', metadata,
    Column('Country', ForeignKey('noc_regions.region'), nullable=False),
    Column('Year', Integer, nullable=False),
    Column('AverageTemperature', Integer, nullable=False)
)


t_country_medals = Table(
    'country_medals', metadata,
    Column('NOC', String(10), nullable=False),
    Column('region', ForeignKey('noc_regions.region'), nullable=False),
    Column('Bronze', Integer, nullable=False),
    Column('Silver', Integer, nullable=False),
    Column('Gold', Integer, nullable=False)
)

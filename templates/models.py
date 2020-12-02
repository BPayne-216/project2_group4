# coding: utf-8
#pulled SQL tables using sqlacodegen
from sqlalchemy import BigInteger, Column, Float, ForeignKey, Integer, String, Table, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


t_country_average_temperature = Table(
    'country_average_temperature', metadata,
    Column('Country', Text, index=True),
    Column('Year', BigInteger),
    Column('NOC', Text),
    Column('AverageTemperature', Float(53))
)


class NocRegion(Base):
    __tablename__ = 'noc_regions'

    region = Column(String(100), nullable=False)
    NOC = Column(String(10), primary_key=True)


t_athlete_medals = Table(
    'athlete_medals', metadata,
    Column('Sex', String(2), nullable=False),
    Column('Team', String(100), nullable=False),
    Column('NOC', ForeignKey('noc_regions.NOC'), nullable=False),
    Column('Games', String(100), nullable=False),
    Column('Year', Integer, nullable=False),
    Column('Season', String(50), nullable=False),
    Column('City', String(100), nullable=False),
    Column('Sport', String(50), nullable=False),
    Column('Medal', String(50), nullable=False)
)


t_city_average_temperature = Table(
    'city_average_temperature', metadata,
    Column('region', String(100), nullable=False),
    Column('NOC', ForeignKey('noc_regions.NOC'), nullable=False),
    Column('City', String(100), nullable=False),
    Column('Year', Integer, nullable=False),
    Column('Latitude', Integer, nullable=False),
    Column('Longitude', Integer, nullable=False),
    Column('AverageTemperature', Integer, nullable=False)
)


t_country_average_temperatue = Table(
    'country_average_temperatue', metadata,
    Column('Country', String(100), nullable=False),
    Column('Year', Integer, nullable=False),
    Column('NOC', ForeignKey('noc_regions.NOC'), nullable=False),
    Column('AverageTemperature', Integer, nullable=False)
)


t_country_medals = Table(
    'country_medals', metadata,
    Column('NOC', ForeignKey('noc_regions.NOC'), nullable=False),
    Column('region', String(100), nullable=False),
    Column('Bronze', Integer, nullable=False),
    Column('Silver', Integer, nullable=False),
    Column('Gold', Integer, nullable=False)
)

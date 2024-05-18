import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

# !!!
# No estoy seguro de que informacion es necesaria en cada tabla ni hace falta una tabla de imagenes aparte. 
# He dado por hecho que seria una url de una imagen de internet
# !!!

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    subscription_date = Column(DateTime, default=datetime.utcnow)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    birth_year = Column(String(10))
    eye_color = Column(String(10))
    gender = Column(String(10))
    hair_color = Column(String(20))
    height = Column(String(10))
    mass = Column(String(10))
    skin_color = Column(String(20))
    homeworld = Column(String(100))
    created = Column(DateTime)
    edited = Column(DateTime)
    image_url = Column(String(250))
    url = Column(String(250))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    climate = Column(String(50))
    diameter = Column(String(20))
    gravity = Column(String(20))
    orbital_period = Column(String(20))
    population = Column(Integer)
    rotation_period = Column(String(20))
    surface_water = Column(String(20))
    terrain = Column(String(50))
    created = Column(DateTime)
    edited = Column(DateTime)
    image_url = Column(String(250))
    url = Column(String(250))

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    model = Column(String(50))
    manufacturer = Column(String(50))
    cost_in_credits = Column(Integer)
    length = Column(String(20))
    max_atmosphering_speed = Column(String(20))
    crew = Column(String(20))
    passengers = Column(String(20))
    cargo_capacity = Column(String(20))
    consumables = Column(String(50))
    vehicle_class = Column(String(50))
    created = Column(DateTime)
    edited = Column(DateTime)
    image_url = Column(String(250))
    url = Column(String(250))

class Favorites(Base):
    __tablename__ = 'favorites'   
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=True)

    user = relationship('User', backref='favorites')
    character = relationship('Character', backref='favorites')
    planet = relationship('Planet', backref='favorites')
    vehicle = relationship('Vehicle', backref='favorites')

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e

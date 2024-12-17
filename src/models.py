import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    fecha_subscripcion = Column(Integer, nullable=False)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)

class Personaje(Base):
    __tablename__ = 'personaje'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    raza = Column(String(250), nullable=False)
    genero = Column(String(50), nullable=True)
    especie_id = Column(Integer, ForeignKey('especie.id'), nullable=False)

    especie = relationship('Especie')

class Especie(Base):
    __tablename__ = 'especie'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    descripcion = Column(String(500), nullable=True)

class Planeta(Base):
    __tablename__ = 'planeta'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    clima = Column(String(250), nullable=True)
    terreno = Column(String(250), nullable=True)

class Pelicula(Base):
    __tablename__ = 'pelicula'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(250), nullable=False)
    fecha_lanzamiento = Column(Integer, nullable=False)
    episodio = Column(Integer, nullable=False)

class Favoritos(Base):
    __tablename__ = 'favoritos'

    usuario_id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=True)
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=True)
    pelicula_id = Column(Integer, ForeignKey('pelicula.id'), nullable=True)

    usuario = relationship('Usuario')
    personaje = relationship('Personaje')
    planeta = relationship('Planeta')
    pelicula = relationship('Pelicula')

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

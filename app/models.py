from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Utilisateur(Base):
    __tablename__ = "utilisateurs"

    id_user = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), index=True)  # Réduit la longueur du champ username
    email = Column(String(100), unique=True, index=True)  # Réduit la longueur du champ email
    password = Column(String(255))

class Enceinte(Base):
    __tablename__ = 'enceintes'
    id_enceinte = Column(Integer, primary_key=True, index=True)
    nom = Column(String(100), index=True)
    macAdress = Column(String(50), unique=True)  # Réduit la longueur du champ macAdress
    status = Column(Boolean, default=True)
    volumeLevel = Column(Integer, default=50)
    id_user = Column(Integer, index=True)

class Connexion(Base):
    __tablename__ = 'connexions'
    id_connexion = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, index=True)
    speakerId = Column(Integer, index=True)
    connectedAt = Column(DateTime, nullable=False)

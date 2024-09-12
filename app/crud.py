from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UtilisateurCreate):
    db_user = models.Utilisateur(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Utilisateur).offset(skip).limit(limit).all()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Utilisateur).offset(skip).limit(limit).all()

def create_enceinte(db: Session, enceinte: schemas.EnceinteCreate):
    db_enceinte = models.Enceinte(nom=enceinte.nom, macAdress=enceinte.macAdress, status=enceinte.status, volumeLevel=enceinte.volumeLevel, id_user=enceinte.id_user)
    db.add(db_enceinte)
    db.commit()
    db.refresh(db_enceinte)
    return db_enceinte

def get_enceinte(db: Session, enceinte_id: int):
    return db.query(models.Enceinte).filter(models.Enceinte.id_enceinte == enceinte_id).first()

def get_enceintes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Enceinte).offset(skip).limit(limit).all()

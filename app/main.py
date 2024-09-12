from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import crud, models, schemas
from .database import engine, SessionLocal, get_db

# Créer les tables dans la base de données
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Route pour créer un utilisateur
@app.post("/utilisateurs/", response_model=schemas.Utilisateur)
def create_user(user: schemas.UtilisateurCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

# Route pour obtenir tous les utilisateurs
@app.get("/utilisateurs/", response_model=List[schemas.Utilisateur])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)

# Route pour créer une enceinte
@app.post("/enceintes/", response_model=schemas.Enceinte)
def create_enceinte(enceinte: schemas.EnceinteCreate, db: Session = Depends(get_db)):
    return crud.create_enceinte(db=db, enceinte=enceinte)

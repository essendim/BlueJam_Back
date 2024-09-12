from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UtilisateurBase(BaseModel):
    username: str
    email: EmailStr

class UtilisateurCreate(UtilisateurBase):
    password: str

class Utilisateur(UtilisateurBase):
    id_user: int

    class Config:
        from_attributes = True  # Remplacement de orm_mode par from_attributes

class EnceinteBase(BaseModel):
    nom: str
    macAdress: str
    status: Optional[bool] = True
    volumeLevel: Optional[int] = 50
    id_user: int

class EnceinteCreate(EnceinteBase):
    pass

class Enceinte(EnceinteBase):
    id_enceinte: int

    class Config:
        from_attributes = True  # Remplacement de orm_mode par from_attributes

class ConnexionBase(BaseModel):
    userId: int
    speakerId: int
    connectedAt: datetime

class ConnexionCreate(ConnexionBase):
    pass

class Connexion(ConnexionBase):
    id_connexion: int

    class Config:
        from_attributes = True  # Remplacement de orm_mode par from_attributes

from database import Base
from models import Utilisateur, Enceinte, Connexion
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Remplacez cette chaîne de connexion par celle de votre base de données
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/bluejambdd"

# Créez l'objet engine et la session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# Insérer des données en dur
def insert_data():
    # Créer des utilisateurs
    user1 = Utilisateur(username="john_doe", email="john@example.com", password="password123")
    user2 = Utilisateur(username="jane_smith", email="jane@example.com", password="password456")

    # Ajouter les utilisateurs à la session
    session.add(user1)
    session.add(user2)
    session.commit()  # Commit pour sauvegarder les utilisateurs dans la base de données

    # Créer des enceintes
    enceinte1 = Enceinte(nom="Enceinte A", macAdress="00:11:22:33:44:55", status=True, volumeLevel=70, id_user=user1.id_user)
    enceinte2 = Enceinte(nom="Enceinte B", macAdress="66:77:88:99:AA:BB", status=False, volumeLevel=50, id_user=user2.id_user)

    # Ajouter les enceintes à la session
    session.add(enceinte1)
    session.add(enceinte2)
    session.commit()  # Commit pour sauvegarder les enceintes dans la base de données

    # Créer des connexions
    connexion1 = Connexion(userId=user1.id_user, speakerId=enceinte1.id_enceinte, connectedAt=datetime.now())
    connexion2 = Connexion(userId=user2.id_user, speakerId=enceinte2.id_enceinte, connectedAt=datetime.now())

    # Ajouter les connexions à la session
    session.add(connexion1)
    session.add(connexion2)
    session.commit()  # Commit pour sauvegarder les connexions dans la base de données

if __name__ == "__main__":
    insert_data()
    print("Données insérées avec succès.")

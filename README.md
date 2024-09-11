# BlueJam

BlueJam est une application mobile innovante qui permet de synchroniser et de gérer plusieurs haut-parleurs Bluetooth simultanément. Avec BlueJam, vous pouvez connecter votre téléphone à plusieurs enceintes Bluetooth et contrôler la lecture de musique, le volume, et d'autres paramètres depuis une seule interface.

## Fonctionnalités
- Connexion de plusieurs haut-parleurs Bluetooth simultanément.
- Contrôle de la lecture de musique et du volume depuis une seule interface.
- Communication en temps réel entre l'application et les haut-parleurs via WebSocket.

## Prérequis
- Python 3.8 ou supérieur
- Node.js 14.x ou supérieur
- `pip` pour installer les dépendances Python
- `npm` ou `yarn` pour gérer les dépendances du front-end

## Installation

### Backend (Python)
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/BlueJam.git

Allez dans le dossier du backend :
bash
Copier le code
cd BlueJam/server
Créez un environnement virtuel et activez-le :
bash
Copier le code
python -m venv env
source env/bin/activate  # Sur Windows : .\env\Scripts\activate
Installez les dépendances :
bash
Copier le code
pip install -r requirements.txt
Lancez le serveur FastAPI :
bash
Copier le code
uvicorn app.main:app --reload
Frontend (React)
Allez dans le dossier du front-end :
bash
Copier le code
cd BlueJam/client
Installez les dépendances :
bash
Copier le code
npm install
Démarrez le serveur de développement React :
bash
Copier le code
npm start
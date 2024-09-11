from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuration des CORS pour permettre les requêtes depuis le front React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Origine du front-end React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

connected_clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Broadcast du message à tous les clients connectés
            for client in connected_clients:
                await client.send_text(f"Message du serveur : {data}")
    except Exception as e:
        print(f"Erreur: {e}")
    finally:
        connected_clients.remove(websocket)

from fastapi import WebSocket, WebSocketDisconnect
from typing import List

# Class to manage WebSocket connections
class ConnectionManager:
    """
    Manages active WebSocket connections, allowing clients to connect, disconnect, and
    receive broadcast messages.
    """
    def __init__(self):
        # List to keep track of active WebSocket connections
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        """
        Accepts a new WebSocket connection and adds it to the active connections list.

        Args:
            websocket (WebSocket): The WebSocket connection to add.
        """
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        """
        Removes a WebSocket connection from the active connections list.

        Args:
            websocket (WebSocket): The WebSocket connection to remove.
        """
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        """
        Sends a broadcast message to all active WebSocket connections.

        Args:
            message (str): The message to send to all clients.
        """
        for connection in self.active_connections:
            await connection.send_text(message)

# Create an instance of the ConnectionManager to handle WebSocket connections
manager = ConnectionManager()

# WebSocket endpoint to join a quiz session
async def quiz_session(websocket: WebSocket, quiz_id: str, user_id: int):
    """
    Handles WebSocket communication for a quiz session. Allows a user to join a quiz
    and participate in real-time interactions.
    Warning: Simplified for ease of demo.

    Args:
        websocket (WebSocket): The WebSocket connection for the user.
        quiz_id (str): The unique identifier for the quiz session.
        user_id (int): The unique identifier for the user.
    """
    await manager.connect(websocket)
    try:
        # Send a welcome message to the connected user
        await websocket.send_text(f"Welcome to quiz {quiz_id}, user {user_id}")

        # Continuously listen for messages from the user
        while True:
            data = await websocket.receive_text() # Receive data from the WebSocket
            # Handle incoming data (e.g., answer submission)
            await manager.send_message(websocket, f"Your submission: {data}")
    except WebSocketDisconnect:
        # Handle the case where the WebSocket connection is closed
        manager.disconnect(websocket) # Remove the user from the connection manager

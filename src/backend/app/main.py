from fastapi import FastAPI, WebSocket
from app.database import init_db
from app.quiz_logic import join_quiz
from app.websocket import quiz_session

# Initialize the FastAPI app
app = FastAPI()

# Event triggered on application startup
@app.on_event("startup")
def startup():
    init_db()  # Call the database initialization function

# REST API endpoint to join a quiz
@app.post("/join_quiz/{quiz_id}/{user_id}")
def join_quiz_route(quiz_id: str, user_id: str):
    """
    REST API route to allow a user to join a quiz.

    Args:
    - quiz_id (str): The unique identifier for the quiz.
    - user_id (str): The ID of the user attempting to join the quiz.

    Returns:
    - Response from the `join_quiz` function in `app.quiz_logic`.
    """
    return join_quiz(quiz_id, user_id)

# WebSocket endpoint for real-time quiz interaction
@app.websocket("/ws/quiz/{quiz_id}/{user_id}")
async def websocket_endpoint(websocket: WebSocket, quiz_id: str, user_id: str):
    """
    WebSocket endpoint to manage real-time communication during a quiz session.

    Args:
    - websocket (WebSocket): Represents the WebSocket connection with the client.
    - quiz_id (str): The unique identifier for the quiz.
    - user_id (str): The ID of the user connected to the WebSocket.

    Behavior:
    - Establishes a WebSocket connection.
    - Calls the `quiz_session` function to handle the quiz logic and communication.
    """
    await quiz_session(websocket, quiz_id, user_id)

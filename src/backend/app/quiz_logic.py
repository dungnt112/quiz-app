from datetime import datetime
from app.database import SessionLocal
from app.models import Quiz, Leaderboard, User

# Create a new session instance to interact with the database
db = SessionLocal()

# Function to handle the logic of joining a quiz
def join_quiz(quiz_id: str, user_id: str):
    """
    Allows a user to join a quiz session.
    
    Args:
        quiz_id (str): The unique identifier of the quiz.
        user_id (str): The unique identifier of the user.
    
    Returns:
        dict: A response dictionary indicating success, error, or informational status.
    """
    # Query the database to check if the quiz with the given ID exists
    quiz = db.query(Quiz).filter(Quiz.quiz_id == quiz_id).first()
    if not quiz:
        return {"error": "Quiz not found"}
    
    # Query the database to check if the user with the given ID exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return {"error": "User not found"}
    
    # Check if the user is already on the leaderboard for the quiz
    leaderboard_entry = db.query(Leaderboard).filter(
        Leaderboard.quiz_id == quiz_id, Leaderboard.user_id == user_id
    ).first()

    if not leaderboard_entry:
        # If the user is not already on the leaderboard, create a new entry
        new_entry = Leaderboard(quiz_id=quiz_id, user_id=user_id, score=0)
        db.add(new_entry) # Add the new leaderboard entry to the session
        db.commit()       # Commit the transaction to save the changes
        return {"success": f"User {user_id} joined quiz {quiz_id}"}
    
    # If the user is already in the leaderboard, return an informational response
    return {"info": "User already joined the quiz"}

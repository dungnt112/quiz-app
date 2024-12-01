from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB

# Create a base class for defining ORM models
Base = declarative_base()

class Quiz(Base):
    """
    Represents the quizzes table in the database.
    Warning: Simplified for ease of demo.

    Attributes:
    - quiz_id (str): The unique identifier for the quiz (primary key).
    - name (str): The name or title of the quiz.
    - start_time (datetime): The start time of the quiz.
    - end_time (datetime): The end time of the quiz.
    - questions (JSONB): A JSONB field containing a list of question IDs for the quiz.
    """
    __tablename__ = "quizzes" # Table name in the database

    quiz_id = Column(String, primary_key=True) # Unique quiz identifier
    name = Column(String, nullable=False) # Name of the quiz
    start_time = Column(DateTime, nullable=False) # Quiz start time
    end_time = Column(DateTime, nullable=False) # Quiz end time
    questions = Column(JSONB, nullable=False)  # List of question IDs

# Model for storing user profile
class User(Base):
    """
    Represents the users table in the database.
    Warning: Simplified for ease of demo.

    Attributes:
    - id (str): The unique identifier for the user (primary key).
    - username (str): The unique username of the user.
    - password (str): The hashed password for the user.
    """
    __tablename__ = "users" # Table name in the database

    id = Column(String, primary_key=True)  # Unique user identifier
    username = Column(String, unique=True, nullable=False)  # User's unique username
    password = Column(String, nullable=False)  # User's password (should be hashed)

class Leaderboard(Base):
    """
    Represents the leaderboard table in the database.
    Warning: Simplified for ease of demo.

    Attributes:
    - id (int): The unique identifier for the leaderboard entry (primary key, auto-incremented).
    - quiz_id (str): The identifier of the quiz (foreign key to the quizzes table).
    - user_id (int): The identifier of the user (foreign key to the users table).
    - score (int): The user's score in the quiz (default: 0).
    """
    __tablename__ = "leaderboard"

    id = Column(Integer, primary_key=True, autoincrement=True)
    quiz_id = Column(String, ForeignKey("quizzes.quiz_id"), nullable=False)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    score = Column(Integer, default=0, nullable=False)

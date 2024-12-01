from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

# Connection string to the PostgreSQL database
# Format: dialect+driver://username:password@host/database_name
DATABASE_URL = "postgresql+psycopg2://quizuser:quizpassword@localhost/quiz_app"

# Create a SQLAlchemy engine
# The engine manages the connection pool and communication with the database
engine = create_engine(DATABASE_URL)

# Create a session factory
# Sessions are used to interact with the database
SessionLocal = sessionmaker(
    autocommit=False,  # Disable auto-commit to ensure transactions are explicitly committed
    autoflush=False,   # Disable auto-flush to control when data is pushed to the database
    bind=engine        # Bind the session to the database engine
)

# Initialize the database
def init_db():
    """
    Initializes the database by creating all tables defined in the ORM models.
    This uses SQLAlchemy's `Base.metadata.create_all` method to generate
    the necessary SQL commands and execute them against the database.

    Note:
    - This will only create tables if they do not already exist.
    - It will not drop or alter existing tables.
    """
    Base.metadata.create_all(bind=engine)

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Purpose: Create database engine and session factory.
# Inputs: Database URL from configuration.
# Outputs: SQLAlchemy engine and session objects.
# Flow: Configure engine and expose the base class for model definitions.

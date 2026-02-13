"""Database connection and session management - SQLite for Streamlit Cloud"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from ..core.config import settings
import logging

logger = logging.getLogger(__name__)

# Base for models
Base = declarative_base()

# Lazy-loaded database connections
_engine = None
_SessionLocal = None


def get_engine():
    """Get or create SQLite engine"""
    global _engine, _SessionLocal
    if _engine is None:
        try:
            # SQLite configuration optimized for Streamlit Cloud
            _engine = create_engine(
                settings.database_url,
                connect_args={
                    "check_same_thread": False,  # Required for SQLite with FastAPI
                    "timeout": 30  # Timeout for database locks
                },
                pool_pre_ping=True,
                echo=False  # Disable SQL logging for performance
            )
            _SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)
            logger.info("SQLite database engine created successfully")
            
            # Create tables if they don't exist
            Base.metadata.create_all(bind=_engine)
            logger.info("Database tables verified/created")
        except Exception as e:
            logger.error(f"Could not create SQLite engine: {e}")
            raise
    return _engine


def get_db():
    """Get SQLite database session"""
    engine = get_engine()
    if engine is None or _SessionLocal is None:
        logger.error("SQLite database not available")
        raise RuntimeError("Database not initialized")
    
    db = _SessionLocal()
    try:
        yield db
    finally:
        db.close()

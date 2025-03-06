from sqlalchemy.orm import Session
from src.services.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
from sqlalchemy.orm import Session
from src.models import user as models_user
from src.schemas import user as schemas_user
from src.core.security import get_password_hash

def get_user_by_email(db: Session, email: str):
    return db.query(models_user.User).filter(models_user.User.email == email).first()

def create_user(db: Session, user: schemas_user.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models_user.User(name=user.name, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
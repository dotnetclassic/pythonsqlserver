from sqlalchemy.orm import Session
from . import models

def get_users(db: Session, skip: int = 0, limit: int = 100):
    #return db.query(models.User).offset(skip).limit(limit).all()
    return db.query(models.User).all()
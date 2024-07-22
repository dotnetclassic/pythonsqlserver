from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import engine, Base, get_db
#fastapi dev main.py   to run file on web
app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/get", response_model = List[schemas.User])
async def get_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip = skip, limit = limit)
    return users

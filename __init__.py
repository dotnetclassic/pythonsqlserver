from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, crud
from .database import engine, Base, get_db
import imp
from email.policy import default

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = "sqlite:///./db.sqlite"

engine = create_engine(DB_URL, connect_args = { "check_same_thread": False })

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() 

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    complete = Column(Boolean, default=False) 

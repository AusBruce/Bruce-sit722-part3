from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://brucedemo_u7fg_user:wiBWxGRJjtEUj2GQn58g0UAy6w2EGJwj@dpg-crfqm1t6l47c73e3vfo0-a.singapore-postgres.render.com/brucedemo_u7fg" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

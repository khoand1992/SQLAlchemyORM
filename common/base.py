import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(os.getenv("POSTGRES_URL"))
_SessionFactory = sessionmaker(bind=engine)
Base = declarative_base()


def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()

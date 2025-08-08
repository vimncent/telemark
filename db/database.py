from sqlalchemy import create_engine, Column, Integer, String, Text, TIMESTAMP, ARRAY, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(String, index=True)
    timestamp = Column(TIMESTAMP)
    text = Column(Text)
    tags = Column(ARRAY(String))
    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now()
    )

def init_db():
    Base.metadata.create_all(bind=engine)

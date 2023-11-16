from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Text
from main import engine


Base = declarative_base()


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String, nullable=False)
    ingredients = Column(Text, nullable=False)
    instructions = Column(Text, nullable=False)


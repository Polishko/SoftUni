from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from main import engine


Base = declarative_base()

# class Recipe(Base):
#     __tablename__ = "recipes"
#
#     id = Column(Integer, primary_key=True, unique=True)
#     name = Column(String, nullable=False)
#     ingredients = Column(Text, nullable=False)
#     instructions = Column(Text, nullable=False)


class Chef(Base):
    __tablename__ = "chefs"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    recipes = relationship("Recipe", back_populates="chefs")


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    ingredients = Column(Text, nullable=False)
    instructions = Column(Text, nullable=False)
    chef_id = Column(Integer, ForeignKey("chefs.id"))
    chefs = relationship("Chef", back_populates="recipes")





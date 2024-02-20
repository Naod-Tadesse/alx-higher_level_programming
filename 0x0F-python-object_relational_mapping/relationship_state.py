#!/usr/bin/python3
"""
class state for orm relationship
"""

from sqlalchemy import Column, Integer, String, orm
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    class blueprint state class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = orm.relationship('City', cascade="all, delete-orphan",
                              backref="state")

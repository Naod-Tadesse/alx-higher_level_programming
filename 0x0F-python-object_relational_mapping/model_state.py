#!/usr/bin/python3
"""
class states for orm
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """
    blue print state class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)

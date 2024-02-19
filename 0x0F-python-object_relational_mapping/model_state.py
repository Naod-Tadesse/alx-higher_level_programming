#!/usr/bin/python3
"""
class states for orm
"""
from sqlalchemy import Column, Integer, String, ext

Base = ext.declarative.declarative_base()


class States(Base):
    """
    blue print state class
    """
    __tablename__ = 'states'
    id = Column(integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)

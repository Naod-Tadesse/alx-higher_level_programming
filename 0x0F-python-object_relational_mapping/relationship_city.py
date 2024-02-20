#!/usr/bin/python3
"""
class city for orm relationship
"""

import sqlalchemy
from relationship_state import Base


class City(Base):
    """
    class blueprint city
    """

    __tablename__ = 'cities'

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, nullable=False,
        unique=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)
    state_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('states.id'),
        nullable=False)

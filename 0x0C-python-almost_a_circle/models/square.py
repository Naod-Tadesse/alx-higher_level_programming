#!/usr/bin/python3
"""this is square class rep"""
from models.rectangle import Rectangle
from models.validate import validate
from models.l import ls


class Square(Rectangle):
    """implementation of the class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return self.width

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @size.setter
    def size(self, value):
        """setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """set attr"""
        if args:
            for count, argument in enumerate(args):
                setattr(self, ls[count], argument)
        else:
            for v, k in kwargs.items():
                setattr(self, v, k)

    def to_dictionary(self):
        """dict rep"""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }

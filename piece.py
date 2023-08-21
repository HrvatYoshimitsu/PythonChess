from abc import ABC


class Piece(ABC):
    def __init__(self, color, value='', abr=''):
        self.color = color
        self.value = value
        self.abr = abr
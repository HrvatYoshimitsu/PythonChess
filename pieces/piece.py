from abc import ABC


class Piece(ABC):
    def __init__(self, color, value='0', abr=''):
        self.color = color
        self.value = value
        self.abr = abr

from piece import Piece


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color, value=5, abr='R')
        self.has_moved = False

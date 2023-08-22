from piece import Piece


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color, value=1)
        self.has_moved = False

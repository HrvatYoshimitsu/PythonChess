from piece import Piece


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color, value=3, abr='N')

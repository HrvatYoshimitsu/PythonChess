from piece import Piece


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color, value=9, abr='Q')

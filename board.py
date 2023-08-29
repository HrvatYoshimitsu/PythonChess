import game_options


class Board:

    def __init__(self, config=None):
        board = [[None] * 8 for _ in range(8)]
        if config is None:
            self.config = game_options.default_config
        else:
            self.config = config
        print(board)

    # TODO: Initialize the board with pieces
    # TODO: Add helper functions for printing, getting pieces, converting notation


if __name__ == "__main__":
    game_board = Board()
    print(game_board.config)

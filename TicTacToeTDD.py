def is_complete(item):
    result = set(item)
    if len(result) == 1 and (result == {'X'} or result == {'O'}):
        return True

    return False


def is_any_complete(board):
    lines = make_3x3_board_filed_with_false()
    diagonals = make_3x3_board_filed_with_false()

    for row_index, row in enumerate(board):
        if is_complete(row):
            return True

        diagonals[0][row_index] = row[row_index]
        diagonals[1][row_index] = row[2 - row_index]

        for line_index, content in enumerate(row):
            if row_index == 2 and line_index == 0 and is_complete(diagonals[0]):
                return True
            if row_index == 2 and line_index == 2 and is_complete(diagonals[1]):
                return True
            lines[line_index][row_index] = content
            if row_index == 2 and is_complete(lines[line_index]):
                return True

    return False


def make_3x3_board_filed_with_false():
    return [[False for _ in range(3)] for _ in range(3)]


def is_board_filled(board):
    for row in board:
        for item in row:
            if item is False:
                return False

    return True


class TicTacToe:
    def __init__(self):
        self.board = make_3x3_board_filed_with_false()
        self._x_turn = True

    def play(self, row, line):
        if is_any_complete(self.board):
            print("Game is over")

        if is_board_filled(self.board):
            print("Cannot play: board is full")

        if self.board[row][line]:
            print(f"Cannot play: {row}, {line} position is already played")

        if self._x_turn:
            mark = "X"
            self._x_turn = False
        else:
            mark = "O"
            self._x_turn = True

        self.add(row, line, mark)

        if is_any_complete(self.board):
            print("Game is over")
            if not self._x_turn:
                print("Player one wins")
            else:
                print("Player two wins")

        if is_board_filled(self.board):
            print("Board is full, game is a draw")

    def add(self, row, line, mark):
        if is_any_complete(self.board) or is_board_filled(self.board) or self.board[row][line]:
            return False

        self.board[row][line] = mark

        return True

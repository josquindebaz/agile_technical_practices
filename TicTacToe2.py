class TicTacToe2:
    def __init__(self):
        self.players = Players()
        self.board = Board()
        self._game_on = True

    def get_player_turn(self):
        return self.players.whose_turn()

    def play(self, x, y):
        if not self._game_on:
            print("Game is over")
            return

        position = Position(x, y)
        result = self.board.play(position, self.players.whose_turn())
        if result:
            print(self.eval_turn())

    def eval_turn(self):
        if self.board.evaluate_board():
            self._game_on = False
            return f"{self.get_player_turn()} wins"

        if self.board.is_full():
            self._game_on = False
            return f"Game is a draw"

        self.players.next()

        return f"{self.get_player_turn()} turn"


class Player:
    def __init__(self, mark):
        self.mark = mark
        self.opponent = None


class Players:
    def __init__(self):
        _playerX = Player("X")
        _playerO = Player("O")

        _playerX.opponent = _playerO
        _playerO.opponent = _playerX

        self._player = _playerX

    def whose_turn(self):
        return self._player.mark

    def next(self):
        self._player = self._player.opponent


class Board:
    def __init__(self):
        self._board = [[None]]

    def play(self, position, player):
        if self._board[position.y][position.x]:
            return False

        self._board[position.y][position.x] = player

        return True

    def evaluate_board(self):
        return any(self.eval_series(series) for series in self.compute_board())

    def eval_series(self, series):
        return any(self.is_series_complete(item) for item in series)

    def compute_board(self):
        lines = [[], [], []]
        diagonals = [[], [], []]
        for y, row in enumerate(self._board):
            for x, item in enumerate(row):
                lines[x].append(item)

            diagonals[0].append(row[y])
            diagonals[1].append(row[2 - y])

        return self._board, lines, diagonals

    @staticmethod
    def is_series_complete(series):
        series_set = set(series)
        possible_marks = [{'X'}, {'O'}]

        return len(series_set) == 1 and (series_set in possible_marks)

    def is_full(self):
        return not any(None in row for row in self._board)


class Position:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

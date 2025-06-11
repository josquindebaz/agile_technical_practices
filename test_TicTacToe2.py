from unittest import TestCase

from TicTacToe2 import Players, Board, Position


class TestTicTacToe2(TestCase):
    def test_x_is_first(self):
        players = Players()
        assert players.whose_turn() == "X"

    def test_cannot_play_on_played_position(self):
        board = Board()
        position = Position(0, 0)
        result = board.play(position, "X")
        assert result == True
        assert board._board == [['X']]

        result = board.play(position, "O")
        assert result == False
        assert board._board == [['X']]

    def test_complete_row_win(self):
        board = Board()

        board._board = [['X', 'X', None], [None, None, None]]
        assert board.evaluate_board() == False

        board._board = [['X', 'X', 'X']]
        assert board.evaluate_board() == True

    def test_complete_line_win(self):
        board = Board()

        board._board = [['X', None, None], ['X', None, None], [None, None, None]]
        assert board.evaluate_board() == False

        board._board = [['X', None, None], ['X', None, None], ['X', None, None]]
        assert board.evaluate_board() == True

    def test_complete_diagonal_win(self):
        board = Board()

        board._board = [['X', None, None], [None, 'X', None], [None, None, None]]
        assert board.evaluate_board() == False

        board._board = [['X', None, None], [None, 'X', None], [None, None, 'X']]
        assert board.evaluate_board() == True

    def test_full_board(self):
        board = Board()

        board._board = [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', None]]
        assert board.is_full() == False

        board._board = [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]
        assert board.is_full() == True



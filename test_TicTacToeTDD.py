from unittest import TestCase

from TicTacToeTDD import TicTacToe, is_any_complete, is_board_filled


class TestTicTacToe(TestCase):
    def test_x_is_first(self):
        instance = TicTacToe()

        assert instance._x_turn == True

    def test_cannot_play_on_played(self):
        instance = TicTacToe()

        arrange = instance.add(0, 0, "X")
        assert arrange is True
        expected = [['X', False, False], [False, False, False], [False, False, False]]

        assert instance.board == expected

        result = instance.add(0, 0, "X")
        assert result is False
        assert instance.board == expected

        is_board_filled(instance.board)

    def test_can_assert_board_is_filled(self):
        instance = TicTacToe()

        empty_board_result = is_board_filled(instance.board)
        assert empty_board_result is False

        instance.add(0, 0, "X")
        unfilled_board_result = is_board_filled(instance.board)
        assert unfilled_board_result is False

        instance.board = [['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]
        filled_board_result = is_board_filled(instance.board)
        assert filled_board_result is True

        add_one_more = instance.add(0, 1, "X")
        assert add_one_more is False

    def test_can_assert_a_row_is_completed(self):
        instance = TicTacToe()

        instance.board[0] = ['X', 'O', 'X']
        assert is_any_complete(instance.board) is False

        instance.board[1] = ['O', 'O', 'O']
        assert is_any_complete(instance.board) is True

    def test_can_assert_a_line_is_completed(self):
        instance = TicTacToe()

        instance.board[0] = ['X', 'O', 'X']
        assert is_any_complete(instance.board) is False

        instance.board[1] = [False, 'O', False]
        instance.board[2] = [False, 'O', False]

        assert is_any_complete(instance.board) is True

    def test_can_assert_a_diagonal_is_completed(self):
        instance = TicTacToe()

        instance.board[0] = ['X', 'O', 'X']
        instance.board[1] = ['X', 'O', 'O']
        instance.board[2] = ['O', 'X', 'X']
        assert is_any_complete(instance.board) is False

        instance.board[0] = ['X', 'O', 'O']
        instance.board[1] = ['X', 'O', 'O']
        instance.board[2] = ['O', 'X', 'X']
        assert is_any_complete(instance.board) is True

        instance.board[0] = ['X', 'O', 'X']
        instance.board[1] = ['X', 'X', 'O']
        instance.board[2] = ['O', 'O', 'X']
        assert is_any_complete(instance.board) is True

    def test_make_player_two_win(self):
        instance = TicTacToe()

        instance.board[0] = ['O', 'O', 'X']
        instance.board[1] = ['O', 'X', 'O']

        instance.play(2, 1)
        instance.play(2, 0)

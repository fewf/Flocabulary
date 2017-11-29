import unittest
from Board import Board
from GameEngine import GameEngine
import random

class TestTicTacToe(unittest.TestCase):
    """
    This class contains a few test cases to check the correctness of code.

    """
    def setUp(self):
        self.board = Board()

    def test_Board_Empty(self):
        self.assertEqual(self.board.isEmpty(4), True)

    def test_Board_Full(self):
        possibleMoves = list(xrange(1, 10))
        letter = 'X'
        for i in xrange(1, 10):
            move = random.choice(possibleMoves)
            possibleMoves.remove(move)
            self.board.makeMove(move, letter)
            letter = 'X' if letter == 'O' else 'O'
        self.assertEqual(self.board.isBoardFilled(), True)

    def test_Board_Player_Wins(self):
        self.board.board[1] = self.board.board[2] = self.board.board[3] = 'X'
        letter = 'O'
        for i in xrange(4, 10):
            self.board.makeMove(i, letter)
            letter = 'X' if letter == 'O' else 'O'

        self.assertEqual(self.board.isWinner('X'), True)

    def test_Board_Player_Loses(self):
        self.board.board[1] = self.board.board[2] = self.board.board[3] = 'X'
        letter = 'O'
        for i in xrange(4, 10):
            self.board.makeMove(i, letter)
            letter = 'X' if letter == 'O' else 'O'

        self.assertEqual(self.board.isWinner('O'), False)



if __name__ == '__main__':
    unittest.main()












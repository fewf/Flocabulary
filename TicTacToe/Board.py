class Board(object):
    """
    class Board maintains a representation of the board at all times.

    A dictionary represents board state with its keys corresponding to positions of the board.
    They can be either 'X', 'O' or ' '. ' ' indicates an empty space.

    """

    def __init__(self):
        """Sets up the initial board."""
        self.board = dict.fromkeys(list(range(1,10)), ' ')

    def isEmpty(self, pos):
        """ This function checks if a position in the board state is free."""
        return self.board[pos] == ' '

    def printBoard(self):
        """This function prints the current board state of the game."""
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('-----------')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('-----------')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])

    def makeMove(self, pos, player):
        """This function marks a move by a player."""
        self.board[pos] = player

    def isWinner(self, player):
        """This function checks if a game has been won by the player."""
        return ((self.board[1] == player and self.board[2] == player and self.board[3] == player) or  # top row
                (self.board[4] == player and self.board[5] == player and self.board[6] == player) or  # middle row
                (self.board[7] == player and self.board[8] == player and self.board[9] == player) or  # bottom row
                (self.board[7] == player and self.board[4] == player and self.board[1] == player) or  # leftmost column
                (self.board[8] == player and self.board[5] == player and self.board[2] == player) or  # middle column
                (self.board[9] == player and self.board[6] == player and self.board[3] == player) or  # rightmost column
                (self.board[7] == player and self.board[5] == player and self.board[3] == player) or  # diagonal
                (self.board[9] == player and self.board[5] == player and self.board[1] == player))  # diagonal

    def getBoard(self):
        """This function returns the board dictionary."""
        return self.board

    def isBoardFilled(self):
        """This function checks if every space in the board has been filled."""
        for i in range(1, 10):
            if self.isEmpty(i):
                return False
        return True

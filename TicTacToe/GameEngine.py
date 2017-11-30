import random
import copy as cp

class GameEngine(object):
    """

    The Game Engine enables both the human player and the computer to make moves.
    The engine also calculates the best possible move for the computer using Newell and Simon's AI algorithm.

    """

    def __init__(self, player):
        """Sets up the initial board engine that has two players."""
        self.player = player
        self.computer = 'X' if player =='O' else 'O'

    def whoseTurn(self):
        """This function decides which player plays first."""
        return 'player' if self.player == 'X' else 'computer'

    def getHumanMove(self, boardObj):
        """This function takes a move from the human player and adds it to the board state."""
        while True:
            print 'Make your move by giving a number as input. [Grid is labeled 1-9 from the right]'
            try:
                move = int(raw_input())
                if 1 <= move <= 9 and boardObj.isEmpty(move):
                    boardObj.makeMove(move,self.player)
                    break
            except:
                print 'Illegal input. Enter only a numeral value between 1-9'

    def ComputerMove(self, boardObj):
        """This function gets the next best move for the computer."""
        move = self.getBestMove(boardObj)
        boardObj.makeMove(move, self.computer)

    def getBestMove(self, boardObj):
        """This function returns which move would be the best move."""
        #checking for a possible win
        for i in range(1, 10):
            copy = cp.deepcopy(boardObj)
            if copy.isEmpty(i):
                copy.makeMove(i, self.computer)
                if copy.isWinner(self.computer):
                    return i

        # Check if the player can win. If player can win with a move, computer takes that move to block it
        for i in range(1, 10):
            copy = cp.deepcopy(boardObj)
            if copy.isEmpty(i):
                copy.makeMove(i, self.player)
                if copy.isWinner(self.player):
                    return i

        # Make a fork - check if corners are free
        move = self.makeRandomMove(boardObj, [1, 3, 7, 9])
        if move != None:
            return move

        # Check if center is free
        if boardObj.isEmpty(5):
            return 5

        # check if there are any empty sides
        return self.makeRandomMove(boardObj, [2, 4, 6, 8])

    def makeRandomMove(self, board, moves):
        """This function returns a valid move from the random possible moves."""
        availableMoves = []
        for i in moves:
            if board.isEmpty(i):
                availableMoves.append(i)

        if len(availableMoves) != 0:
            return random.choice(availableMoves)
        else:
            return None

    def checkForWinsAndTies(self, boardObj):
        """This function decides if the game is won or resulted in a tie."""
        if boardObj.isWinner(self.player):
            print 'You win!!\n\n'
        elif boardObj.isWinner(self.computer):
            print 'The computer wins\n\n'
        elif boardObj.isBoardFilled():
                print('The game is a tie!\n\n')
        else:
            return True

        return False











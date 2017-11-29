# Fizzbuzz and TicTacToe

#### This project contains two folders. The code is in Python 2.7.14

1. Fizzbuzz
  - This contains fizzbuzz.py.
  - Prints between 1-100
  - Can be run as:  python fizzbuzz.py
2. TicTacToe
  - This folder contains the game.
  - To run the game : python TicTacToeGame.py
  - To run tests : python TestTicTacToeGame.py

## Game Design:

For this game, the tic-tac-toe grid is a 3x3 grid. A human player plays against the computer by inputting numerals from 1-9.
The grid is numbered 1-9 from the right.
The computer picks the best possible move using Newell and Simon's algorithm. (no minimax search strategy)
Time Complexity: O(N), Space Complexity: O(N)

The code is structured as follows:

1. Board.py - contains the class Board. Board maintains a representation of the state of the board.
It does this through a dictionary where keys (ranging from 1-9) correspond to the state of the grid.
Board contains methods such as
    * isEmpty - to check if a cell in a grid is empty
    * printBoard - to display the board
    * isWinner- to check if board has a winning combination
    * isBoardFilled - to check if the board has no cells to fill
    * getBoard - return the board dictionary

2. GameEngine.py - contains the class GameEngine. This class contains the logic of the game. It acts as a controller,
 getting input from the human player, getting the best move from the computer and checking for wins and ties.
 Game Engine contains methods such as
    * getHumanMove - getting a legal move from the human player
    * getComputerMove - making a move from the computer calling the getBestMove function
    * getBestMove - calculates the best move through the Newell and simon algorithm
    * checkForWinsAndTies - checks if a player wins or draws the game

3. TicTacToeGame.py - contains the main method. It asks users their choice of being player X or player O

4. TestTicTacToeGame.py - contains unit tests

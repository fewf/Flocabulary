#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Board import Board
from GameEngine import GameEngine


def main():
    """

    This function contains the main method where user input is taken in.
    Game continues on infinitely till the user specifies otherwise.

    """
    print 'xxxxxx  TIC TAC TOE  xxxxxx \n\n\n'

    while True:
        # sets the board
        board = Board()
        player = ''
        while not (player == 'X' or player == 'O'):
            print('Do you want to be X or O? X goes first.\n')
            player = raw_input().upper()

        engine = GameEngine(player)
        turn = engine.whoseTurn()
        print('The ' + turn + ' will go first.')
        game = True
        if turn =='player':
            board.printBoard()
        while game:
            if turn == 'player':
                # Player’s turn.
                engine.getHumanMove(board)
                game = engine.checkForWinsAndTies(board)
                turn = 'computer'
            else:
                # Computer’s turn.
                engine.getComputerMove(board)
                board.printBoard()
                game = engine.checkForWinsAndTies(board)
                turn = 'player'
        print('Do you want to play again? (y or n)')
        again = raw_input().lower().startswith('y')
        if not again:
            break

if __name__ == '__main__':
    main()
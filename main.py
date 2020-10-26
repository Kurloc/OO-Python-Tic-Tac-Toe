import time
from GameBoard import GameBoard

gameGoing = True

while gameGoing:
    try:
        inputValue = input("Do you want to play a game?\n1.Play\n2.Quit\n): ")
        if inputValue == '1' or inputValue == '2':
            if inputValue == '1':
                inGame = True
                playerOne = input("Player One: X's or O's: ")
                gameBoard = GameBoard(inGame, playerOne)
                gameBoard.printGameBoard()
                while inGame:
                    gameBoard.makeMove()
                    inGame = gameBoard.checkWinConditions()
            if inputValue == '2':
                gameGoing = False
                print('Goodbye!')
                break

        else:
            raise ValueError("Sorry, please input a valid option")

    except ValueError:
        pass

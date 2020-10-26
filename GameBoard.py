class GameBoard:
    lastTurn = ''
    currentTurn = ''
    firstPlayer = ""
    secondPlayer = ""
    gameGoing: bool
    validPlayerIcons = ['x', 'o']
    tl = " "
    tm = " "
    tr = " "
    ml = " "
    mm = " "
    mr = " "
    bl = " "
    bm = " "
    br = " "

    def __init__(self, goingGoing, firstPlayer: str):
        self.validatePlayersAndPlayOrder(firstPlayer)
        self.gameGoing = goingGoing

    def validatePlayersAndPlayOrder(self, firstPlayer: str):
        secondPlayer = ''

        validatingPlayerInput = True
        if firstPlayer in self.validPlayerIcons:
            pass
        else:
            while validatingPlayerInput:
                if firstPlayer in self.validPlayerIcons:
                    validatingPlayerInput = False
                else:
                    print("Invalid Input try again")
                    firstPlayer = input("Is playerOne going to be X or O's?")

        if firstPlayer.lower() == 'x':
            secondPlayer = 'o'
        if firstPlayer.lower() == 'o':
            firstPlayer = 'x'

        self.currentTurn = firstPlayer
        self.firstPlayer = firstPlayer
        self.secondPlayer = secondPlayer

    def printGameBoard(self):
        topLine = self.tl + "|" + self.tm + "|" + self.tr
        middleLine = self.ml + "|" + self.mm + "|" + self.mr
        bottomLine = self.bl + "|" + self.bm + "|" + self.br
        print("\n" * 1 + topLine + "\n" + middleLine + "\n" + bottomLine)

    def makeMove(self):
        attributeName = input(self.currentTurn + ": Where do you want to move?")
        attributeName, value = self.validateMove(attributeName, self.currentTurn)
        self.updateGameBoard(attributeName, value)
        self.printGameBoard()
        if self.currentTurn.lower() == 'x':
            self.currentTurn = 'o'
            self.lastTurn = 'x'
        elif self.currentTurn.lower() == 'o':
            self.currentTurn = 'x'
            self.lastTurn = 'o'

    def updateGameBoard(self, attributeName, value):
        setattr(self, attributeName, value.lower())

    def validateMove(self, attributeName, value):
        validatingBoolean = True
        validatingValue = True

        while validatingBoolean:
            if attributeName in dir(self) and getattr(self, attributeName) == " ":
                validatingBoolean = False
            else:
                self.printGameBoard()
                attributeName = input("Please input a valid board space: ")

        while validatingValue:
            if value.lower() in self.validPlayerIcons:
                validatingValue = False
            else:
                self.printGameBoard()
                value = input("Please input a valid move")
        return attributeName, value

    def endGame(self, playerIcon) -> bool:
        print(playerIcon + " Wins!\n")
        self.gameGoing = False
        return self.gameGoing

    def endGameDraw(self) -> bool:
        print("Game Over! Draw\n")
        self.gameGoing = False
        return self.gameGoing

    def checkWinConditions(self) -> bool:
        playerIcon = self.lastTurn.lower()

        # straight across
        # up and down
        #  X|X|X
        #  |  |
        #  |  |
        if self.tl.lower() == playerIcon and self.tm.lower() == playerIcon and self.tr.lower() == playerIcon:
            return self.endGame(playerIcon)

        # straight across
        # up and down
        #  |  |
        #  X|X|X
        #  |  |
        if self.ml.lower() == playerIcon and self.mm.lower() == playerIcon and self.mr.lower() == playerIcon:
            return self.endGame(playerIcon)

        # straight across
        # up and down
        #  |  |
        #  |  |
        #  X|X|X
        if self.bl.lower() == playerIcon and self.bm.lower() == playerIcon and self.br.lower() == playerIcon:
            return self.endGame(playerIcon)

        # diagonal across
        # X| |
        #  |X|
        #  | |X
        if self.tl.lower() == playerIcon and self.mm.lower() == playerIcon and self.br.lower() == playerIcon:
            return self.endGame(playerIcon)

        #   | |X
        #   |X|
        #  X| |
        if self.br.lower() == playerIcon and self.mm.lower() == playerIcon and self.tl.lower() == playerIcon:
            return self.endGame(playerIcon)

        # up and down
        #  X| |
        #  X| |
        #  X| |
        if self.tl.lower() == playerIcon and self.ml.lower() == playerIcon and self.bl.lower() == playerIcon:
            return self.endGame(playerIcon)

        # up and down
        #   |X|
        #   |X|
        #   |X|
        if self.tm.lower() == playerIcon and self.mm.lower() == playerIcon and self.bm.lower() == playerIcon:
            return self.endGame(playerIcon)

        # up and down
        #  | |X
        #  | |X
        #  | |X
        if self.tr.lower() == playerIcon and self.br.lower() == playerIcon and self.mr.lower() == playerIcon:
            return self.endGame(playerIcon)

        if self.tr != " " and self.tm != " " and self.tl != " " and self.ml != " " and self.mm != " " and self.mr != " " \
                and self.br != " " and self.bm != " " and self.bl != " ":
            return self.endGameDraw()

        return True

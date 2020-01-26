boardGame = [['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', 'W', 'B', '.', '.', '.'],
             ['.', '.', '.', 'B', 'W', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.']]
DicDirection = {0: "Top", 1: "Bottom",
                2: "Left", 3: "Right",
                4: "Top Right", 5: "Bottom Right",
                6: "Top Left", 7: "Bottom Left"}


def drawBoard():
    print("  a b c d e f g h")
    for row in range(8):
        for column in range(8):
            if column == 0:
                letter = str(row + 1) + " " + boardGame[row][column]
            else:
                letter = " " + boardGame[row][column]
            print(letter, end='')
        print("")


def changeColor(row, column, PlayerColor):
    if PlayerColor == 'W':
        OtherPlayer = 'B'
    else:
        OtherPlayer = 'W'
    rowbegin = row
    columnbegin = column
    for i in range(8):
        direction = DicDirection[i]
        if direction == "Top":
            MoveChange = [-1, 0]
        elif direction == "Bottom":
            MoveChange = [1, 0]
        elif direction == "Left":
            MoveChange = [0, -1]
        elif direction == "Right":
            MoveChange = [0, 1]
        elif direction == "Top Right":
            MoveChange = [-1, 1]
        elif direction == "Bottom Right":
            MoveChange = [1, 1]
        elif direction == "Top Left":
            MoveChange = [-1, -1]
        elif direction == "Bottom Left":
            MoveChange = [1, -1]
        run = 0
        changeList = []
        while True:
            run += 1
            rowCurrent = run * MoveChange[0] + rowbegin
            columnCurrent = run * MoveChange[1] + columnbegin
            if rowCurrent > 7 or columnCurrent > 7:
                break
            elif rowCurrent < 0 or columnCurrent < 0:
                break
            if run == 1:
                if boardGame[rowCurrent][columnCurrent] == '.':
                    break
                elif boardGame[rowCurrent][columnCurrent] == OtherPlayer:
                    changeList.append([rowCurrent, columnCurrent])
                elif boardGame[rowCurrent][columnCurrent] == PlayerColor:
                    break
            else:
                if boardGame[rowCurrent][columnCurrent] == OtherPlayer:
                    changeList.append([rowCurrent, columnCurrent])
                elif boardGame[rowCurrent][columnCurrent] == '.':
                    break
                elif boardGame[rowCurrent][columnCurrent] == PlayerColor:
                    for item in changeList:
                        boardGame[item[0]][item[1]] = PlayerColor
                    break
    boardGame[rowbegin][columnbegin] = PlayerColor


def checkMove(CurrentPlayer):
    '''
    this function will return every valid move at CurrentPlayer
    '''
    if CurrentPlayer == "W":
        OtherPlayer = "B"
    else:
        OtherPlayer = "W"
    ''' when we check valid move need store it in list '''
    MoveChange = []
    #
    ListValidMove = []
    # when run mode change color still need list store where we change color
    # if it between 2 same color
    for row in range(8):
        for col in range(8):
            if boardGame[row][col] == CurrentPlayer:
                rowStart = row
                columnsStart = col
                '''
                only change color we just run once at valid move
                check everything between is different color >> same color
                check each direction from that location
                 '''
                for i in range(8):
                    direction = DicDirection[i]
                    if direction == "Top":
                        MoveChange = [-1, 0]
                    elif direction == "Bottom":
                        MoveChange = [1, 0]
                    if direction == "Left":
                        MoveChange = [0, -1]
                    elif direction == "Right":
                        MoveChange = [0, 1]
                    if direction == "Top Right":
                        MoveChange = [-1, 1]
                    elif direction == "Bottom Right":
                        MoveChange = [1, 1]
                    if direction == "Top Left":
                        MoveChange = [-1, -1]
                    elif direction == "Bottom Left":
                        MoveChange = [1, -1]
                    move = 0
                    ChangeRow = MoveChange[0]
                    ChangeColumn = MoveChange[1]
                    while True:
                        move += 1
                        whereRow = rowStart + move * ChangeRow
                        whereColumn = columnsStart + move * ChangeColumn
                        if whereRow < 0 or whereColumn < 0:
                            break
                        elif whereRow > 7 or whereColumn > 7:
                            break
                        if move == 1:
                            if (boardGame[whereRow][whereColumn]
                               == OtherPlayer):
                                ''' meet different COLOR
                                 still continous jump '''
                                pass
                            elif (boardGame[whereRow][whereColumn]
                                  == CurrentPlayer):
                                # first time jump meet Same COLOR
                                # that will invalid move
                                break
                            elif boardGame[whereRow][whereColumn] == ".":
                                ''' when first run meet (".")
                                 that also invalid move '''
                                break
                        else:
                            if (boardGame[whereRow][whereColumn]
                               == CurrentPlayer):
                                ''' After second jump if meet Same Color
                                That will invalid move
                                '''
                                break
                            elif (boardGame[whereRow][whereColumn]
                                  == OtherPlayer):
                                ''' After second jump if meet Same Color
                                That will invalid move
                                '''
                                pass
                            elif boardGame[whereRow][whereColumn] == ".":
                                ''' when meet after first time jump
                                 everytime meet "." this is valid move
                                 we will store that location '''
                                ListValidMove.append([whereRow, whereColumn])
                                break
    return ListValidMove


def EndGame():
    countWhite = 0
    countBlack = 0
    for row in range(8):
        for col in range(8):
            if boardGame[row][col] == "W":
                countWhite += 1
            else:
                countBlack += 1
    print("End of the game. W: {}, B: {}".format(countWhite, countBlack))
    if countWhite > countBlack:
        print("W wins.")
    elif countWhite < countBlack:
        print("B wins.")
    else:
        print("Two player draw.")


def Input(Player, ValidMove):
    KeyColummn = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
                  'e': 4, 'f': 5, 'g': 6, 'h': 7}
    KeyRow = {'1': 0, '2': 1, '3': 2, '4': 3,
              '5': 4, '6': 5, '7': 6, '8': 7}
    Location = input("Player {}: ".format(Player))
    # index 0 is column, index 1 is row
    # decode value input to location in board
    # check is value input is in board or not
    # only valid move
    while True:
        if Location == "":
            print("{}: Invalid value".format(Location))
            print("Valid choices: {}".format(" ".join(ValidMovePlayer)))
        elif Location[0] not in KeyColummn:
            print("{}: Invalid value".format(Location))
            print("Valid choices: {}".format(" ".join(ValidMovePlayer)))
        # check is value input is in board or not
        elif Location[1] not in KeyRow:
            print("{}: Invalid value".format(Location))
            print("Valid choices: {}".format(" ".join(ValidMovePlayer)))
        elif len(Location) > 2:
            print("{}: Invalid value".format(Location))
            print("Valid choices: {}".format(" ".join(ValidMovePlayer)))
        elif Location not in ValidMove:
            print("{}: Invalid value".format(Location))
            print("Valid choices: {}".format(" ".join(ValidMovePlayer)))
        elif Location in ValidMove:
            break
    changeColor(PlayerColor=Player, row=KeyRow[Location[1]],
                column=KeyColummn[Location[0]])


def Decode(listLocation):
    ''' Change listLocation Valid move to
    the way Player can understand it '''

    KeyColummn = {0: 'a', 1: 'b', 2: 'c', 3: 'd',
                  4: 'e', 5: 'f', 6: 'g', 7: 'h'}
    KeyRow = {0: '1', 1: '2', 2: '3', 3: '4',
              4: '5', 5: '6', 6: '7', 7: '8'}
    ListPositionPlayer = []
    for position in listLocation:
        # index 0 is row index 1 is column
        # player can understand let column first and row after
        # coz only understand if when decode location
        key = KeyColummn[position[1]]+KeyRow[position[0]]
        # only add new postion not old position
        if key not in ListPositionPlayer:
            ListPositionPlayer.append(key)
    return sorted(ListPositionPlayer)


color = 'B'
count = 0
while True:
    drawBoard()
    ValidMovePlayer = Decode(checkMove(color))
    if len(ValidMovePlayer) < 1:
        print("Player {} cannot play".format(color))
        count += 1
        if count == 2:
            EndGame()
            break
    else:
        count = 0
        print("Valid choices: {}".format(" ".join(ValidMovePlayer)))
        Input(color, ValidMovePlayer)
    if color == 'W':
        color = 'B'
    else:
        color = 'W'

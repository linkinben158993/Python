boardGame = [['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', 'W', 'B', '.', '.', '.'],
             ['.', '.', '.', 'B', 'W', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.']]


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


def checkMove(Player, position=[0, 0], Mode="No"):
    COLOR = {'B': 'W', 'W': 'B'}
    OtherPlayer = COLOR[Player]
    MoveChange = []
    DicDirection = {0: "Top", 1: "Bottom", 2: "Left", 3: "Right",
                    4: "Top Right", 5: "Bottom Right",
                    6: "Top Left", 7: "Bottom Left"}
    # when we check valid move need store it in list
    ListValidMove = []
    # when run mode change color still need list store where we change color
    # if it between 2 same color
    ListChangeColor = []
    # when check valid move
    # at each location same color
    # need check 8 direction to find location valid move
    # each direction have some rule
    # different with each direction
    for row in range(8):
        for col in range(8):
            if boardGame[row][col] == Player or Mode == "Change":
                rowStart = row
                columnsStart = col
                # only change color we just run once at valid move
                # check everything between is different color >> same color
                # check each direction from that location
                if Mode == "Change":
                    rowStart = position[0]
                    columnsStart = position[1]
                for i in range(8):
                    ListChangeColor = []
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
                            if boardGame[whereRow][whereColumn] == OtherPlayer:
                                # when run mode change color
                                # that first time jump to
                                # next from that direction
                                # is differen color we store that location
                                if Mode == "Change":
                                    ListChangeColor.append([whereRow,
                                                            whereColumn])
                            elif boardGame[whereRow][whereColumn] == Player:
                                # when run check move or change color
                                # if same color is mean that invalid direction
                                # so we move to next direction
                                break
                            else:
                                # when first run meet (".")
                                # that also invalid move
                                break
                        else:
                            if boardGame[whereRow][whereColumn] == Player:
                                # when run mode change color
                                # we meet same color that mean valid direction
                                # change color between where start to here
                                if Mode == "Change":
                                    for location in ListChangeColor:
                                        rowNow = location[0]
                                        colNow = location[1]
                                        boardGame[rowNow][colNow] = Player
                                break
                            elif (boardGame[whereRow][whereColumn]
                                  == OtherPlayer):
                                # if different color can be continous jump more
                                if Mode == "Change":
                                    ListChangeColor.append([whereRow,
                                                            whereColumn])
                                    # coz when in mode change color
                                    # need store that location
                                    # so when it is valid direction
                                    # we change color between that direction
                            elif boardGame[whereRow][whereColumn] == ".":
                                # when at check valid move
                                # we will store location
                                ListValidMove.append([whereRow, whereColumn])
                                break
                if Mode == "Change":
                    # coz when finish check 8 direction
                    # change color at place player choose it
                    boardGame[position[0]][position[1]] = Player
                    return
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


def Input(Player, ValidMove, Flag):
    KeyColummn = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
                  'e': 4, 'f': 5, 'g': 6, 'h': 7}
    KeyRow = {'1': 0, '2': 1, '3': 2, '4': 3,
              '5': 4, '6': 5, '7': 6, '8': 7}
    while True:
        Location = input("Player {}: ".format(Player))
        # index 0 is column, index 1 is row
        # decode value input to location in board
        # check is value input is in board or not
        # only valid move
        if Location == "":
            Flag = True
        elif Location[0] not in KeyColummn:
            Flag = True
        # check is value input is in board or not
        elif Location[1] not in KeyRow:
            Flag = True
        elif len(Location) > 2:
            Flag = True
        elif Location not in ValidMove:
            Flag = True
        break
    if Flag:
        print("{}: Invalid value".format(Location))
        print("Valid choices: {}".format(" ".join(ValidMovePlayer)))
        return True
    else:
        checkMove(Player, position=[KeyRow[Location[1]],
                  KeyColummn[Location[0]]], Mode="Change")
        return False


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
    ValidMovePlayer = Decode(checkMove(Player=color))
    if len(ValidMovePlayer) < 1:
        print("Player {} cannot play".format(color))
        count += 1
        if count == 2:
            EndGame()
            break
    else:
        count = 0
        print("Valid choices: {}".format(" ".join(ValidMovePlayer)))
        if Input(color, ValidMovePlayer, Flag=False):
            break
    if color == 'W':
        color = 'B'
    else:
        color = 'W'

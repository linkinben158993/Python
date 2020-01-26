def checkMove(board, position, color, direction):
    rowStart = position[0]
    columnsStart = position[1]
    defaultRow = 8
    defaultColumn = 8
    COLOR = { 'B':'W','W':'B'}
    MoveChange=[]
    if direction == "Top":
        MoveChange = [-1,0]
    elif direction == "Bottom":
        MoveChange = [1,0]
    if direction == "Left":
        MoveChange = [0,-1]
    elif direction == "Right":
        MoveChange = [0,1]
    if direction == "Top Right":
        MoveChange = [-1,1]
    elif direction == "Bottom Right":
        MoveChange = [1,-1]
    if direction == "Top Left":
        MoveChange = [-1,-1]
    elif direction == "Bottom Left":
        MoveChange = [1,-1]
    move = 0
    ChangeRow = MoveChange[0]
    ChangeColumn = MoveChange[1]
    ListCheck = []
    while True:
        move += 1
        whereRow = rowStart + move * ChangeRow
        whereColumn = columnsStart + move * ChangeColumn
        if whereRow < 0 or whereColumn < 0:
            return ""
        elif whereRow > defaultRow - 1 or whereColumn > defaultColumn - 1:
            return ""
        if move == 1:
            if board[whereRow][whereColumn] == COLOR[color]:
                pass
            elif board[whereRow][whereColumn] == color:
                return ""
            else:
                return ""
        else:
            if board[whereRow][whereColumn] == color:
                return ""
            elif board[whereRow][whereColumn] == ".":
                return [whereRow,whereColumn]

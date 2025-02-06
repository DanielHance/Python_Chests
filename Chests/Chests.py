board = [[[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [3, 1], [2, 1], [1, 1]],
         [[0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1]],
         [[0, 0], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2]],
         [[0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2]],
         [[0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2]],
         [[0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2]],
         [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
         [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [3, 0], [2, 0], [1, 0]]
        ]

#Prints row of board to console
def printRow(_board, _row):
    pieces = [[" ♙ ", " ♖ ", " ♘ ", " ♗ ", " ♕ ", " ♔ "],
           [" ▲ ", " ♜ ", " ♞ ", " ♝ ", " ♛ ", " ♚ "],
           ["   ", "   ", "   ", "   ", "   ", "   "]]
    out = str(_row + 1) + " ║"
    for i in range(8):
        out += pieces[_board[_row][i][1]][_board[_row][i][0]] + "║"
    print(out)

#Prints whole board to console
def printBoard(_board):
    print("    A   B   C   D   E   F   G   H")
    print("  ╔ ═ ╦ ═ ╦ ═ ╦ ═ ╦ ═ ╦ ═ ╦ ═ ╦ ═ ╗")
    for i in range(7):
        printRow(_board, i)
        print("  ╠ ═ ╬ ═ ╬ ═ ╬ ═ ╬ ═ ╬ ═ ╬ ═ ╬ ═ ╣")
    printRow(_board, 7)
    print("  ╚ ═ ╩ ═ ╩ ═ ╩ ═ ╩ ═ ╩ ═ ╩ ═ ╩ ═ ╝")

#Returns opponenet of colour entered
def getOpponent(_col):
    if _col == 0:
        return 1
    elif _col == 1:
        return 0
    else:
        print("Error, blank square entered!")
        return -1

#Returns type of piece at position on board (can be a 'ghost' piece so check that colour is not 2)
def getColour(_pos, _board):
    return _board[_pos[0]][_pos[1]][1]

#Returns colour of piece at position on board (2 if empty)
def getPiece(_pos, _board):
    return _board[_pos[0]][_pos[1]][0]

#Prints message saying which pieces was taken
def deathMessage(_attacker, _death, _board):
    _letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    _colours = ["White", "Black"]
    _pieces = ["pawn", "rook", "knight", "bishop", "queen", "king"]
    print(_colours[getColour(_attacker, _board)] + "'s " + _pieces[getPiece(_attacker, _board)] + " takes " + _colours[getColour(_death, _board)] + "'s " + _pieces[getPiece(_death, _board)] + " at " + _letters[_death[1]] + str(_death[0] + 1))

#Moves a piece on the board (DOES NOT VALIDATE MOVE!)
def updateBoard(_start, _end, _board):
    _board[_end[0]][_end[1]][0] = getPiece(_start, _board)
    _board[_end[0]][_end[1]][1] = getColour(_start, _board)
    _board[_start[0]][_start[1]][1] = 2

#Will get user input and put in format of board position (VALIDATES INPUTS!)
def getInput(_message):
    while True:
        _inp = input(_message)
        if len(_inp) == 2:
            letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
            numbers = ["1", "2", "3", "4", "5", "6", "7", "8"] #This is such a bad way of doing this!

            if _inp[0].upper() in letters and _inp[1] in numbers:
                rtn = [numbers.index(_inp[1]), letters.index(_inp[0].upper())]
                return rtn
            elif _inp[0] in numbers and _inp[1].upper() in letters:
                rtn = [numbers.index(_inp[0]), letters.index(_inp[1].upper())]
                return rtn
        
        print("Invalid space!")

#Will check that pawn movement is valid (make move and return true if valid, return false if invalid)
def movePawn(_start, _end, _board):
    _col = getColour(_start, _board)
    if _col == 0:
        _dir = -1
    else:
        _dir == 1

    #print(_dir)
    #print(_start[1] == _end[1])
    #print(getColour(_end, _board) == 2)
    #print(" ")
    #print(_col == 0 and _start[0] == 6 and getColour([5, _start[0]], _board) == 2 and _end[0] == 4)
    #print(_col == 1 and _start[0] == 1 and getColour([2, _start[0]], _board) == 2 and _end[0] == 3)
    #print(_end[0] - _start[0] == _dir)
    #print(" ")
    if _end[0] - _start[0] == _dir and (_start[1] - _end[1] == 1 or _start[1] - _end[1] == -1) and getColour(_end, _board) == getOpponent(_col):
        deathMessage(_start, _end, _board)
    elif not (_start[1] == _end[1] and getColour(_end, _board) == 2 and ((_col == 0 and _start[0] == 6 and getColour([5, _start[0]], _board) == 2 and _end[0] == 4) or (_col == 1 and _start[0] == 1 and getColour([2, _start[0]], _board) == 2 and _end[0] == 3) or _end[0] - _start[0] == _dir)):
        print("Invalid move")
        return False

    updateBoard(_start, _end, _board)
    return True 

def move(_start, _end, _col, _board):
    if getColour(_start, _board) != _col:
        return False

    _piece = getPiece(_start, _board)

    if _piece == 0:
        return movePawn(_start, _end, _board)
    
    print("Error in move() something went VERY wrong!")
    return False

printBoard(board)
start = getInput("Enter the space of the piece you would like to move: ")
end = getInput("Enter the space of the location you would like to move the piece too: ")
move(start, end, 0, board)
printBoard(board)


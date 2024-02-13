import tkinter as tk

# Define names
#pawn = "Pawn"
#rook = "Rook"
#knight = "Knight"
#bishop = "Bishop"
#queen = "Queen"
#king = "King"

debug_mode = True

white = "White"
black = "Black"

# Define tkinter window
window = tk.Tk()

# tkinter window setup
window.grid()
window.title("Chess Python")
window['padx'] = 10
window['pady'] = 10

empty = tk.PhotoImage(width = 1, height = 1)
tempGoldPawn = tk.PhotoImage(file = './assets/tempGoldPawn.png')
tempBlackPawn = tk.PhotoImage(file = './assets/tempBlackPawn.png')

pieces = [[0]*8 for _ in range(8)]

class chessPiece:
    def __init__(self, pieceType, team, i, j):
        self.pieceType = pieceType
        self.team = team
        self.i = i 
        self.j = j 
    
    def __str__(self):
        return f"{team} {self.pieceType}"
    

class pawn(chessPiece): # Jace helped here
    def __init__(self, team, i, j):
        chessPiece.__init__(self, "Pawn", team, i, j)
        if (team == white):
            self.image = tempGoldPawn
        else:
            self.image = tempBlackPawn
    

class rook(chessPiece):
    def __init__(self, team, i, j):
        chessPiece.__init__(self, "Rook", team, i, j)
    

class knight(chessPiece):
    def __init__(self, team, i, j):
        chessPiece.__init__(self, "Knight", team, i, j)
    

class bishop(chessPiece):
    def __init__(self, team, i, j):
        chessPiece.__init__(self, "Bishop", team, i, j)
    

class queen(chessPiece):
    def __init__(self, team, i, j):
        chessPiece.__init__(self, "Queen", team, i, j)
    

class king(chessPiece):
    def __init__(self, team, i, j):
        chessPiece.__init__(self, "King", team, i, j)
    
def placeNewPiece(piece):
    global grid
    pieces[piece.i][piece.j] = piece
    grid[piece.i][piece.j].config(image = piece.image)
    return

#def movePiece(i, j, newi, newj):
    
    

def left(i, j):
    print("left,", i, j)
    return

def right(i, j):
    print("right,", i, j)
    return

def generateGame():
    global grid
    grid = [[0]*8 for _ in range(8)]
    iLabels = [0 for _ in range(8)]
    jLabels = [0 for _ in range(8)]
    k = 0
    for i in range(0, 8):
        for j in range(0, 8):
            grid[i][j] = tk.Button(window, image = empty, width = 32, height = 32, command = None)
            grid[i][j].grid(column = j+1, row = i+1)
            grid[i][j].bind('<ButtonRelease-1>', lambda k=k, i=i, j=j: left(i, j))
            grid[i][j].bind('<Button-3>', lambda k=k, i=i, j=j: right(i, j))
    if (debug_mode == True):
        for i in range(0, 8):
            iLabels[i] = tk.Label(window, text = str(i))
            iLabels[i].grid(row = i + 1, column = 0)
            jLabels[i] = tk.Label(window, text = str(i))
            jLabels[i].grid(row = 0, column = i + 1)
        Labels = tk.Label(window, text = "i \ j")
        Labels.grid(row = 0, column = 0)
        
    return

generateGame()

placeNewPiece(pawn(white, 1, 1))

window.mainloop()
    
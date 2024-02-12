import tkinter as tk

# Define names
#pawn = "Pawn"
#rook = "Rook"
#knight = "Knight"
#bishop = "Bishop"
#queen = "Queen"
#king = "King"


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

class chessPiece:
    def __init___(self, pieceType, team, i, j):
        self.pieceType = pieceType
        self.team = team
        self.i = i 
        self.j = j 
    
    def __str__(self):
        return f"{team} {self.pieceType}"
    

class pawn(chessPiece):
    def __init__(self, team, i, j):
        chessPiece.__init__(self, "Pawn", team, i, j)
    

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
    

def left(i, j):
    print("left,", i, j)
    return

def right(i, j):
    print("right,", i, j)
    return

def generateGame():
    grid = [[0]*8 for _ in range(8)]
    k = 0
    for i in range(0, 8):
        for j in range(0, 8):
            grid[i][j] = tk.Button(window, image = empty, width = 32, height = 32, command = None)
            grid[i][j].grid(column = j, row = i)
            grid[i][j].bind('<ButtonRelease-1>', lambda k=k, i=i, j=j: left(i, j))
            grid[i][j].bind('<Button-3>', lambda k=k, i=i, j=j: right(i, j))
    return

generateGame()
window.mainloop()
    
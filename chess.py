import tkinter as tk
from base64 import b64decode
from functools import partial

# Flags
debug_mode = True
isSelected = False
enPassant = False

# References
white = "White"
black = "Black"
selected_i = 8 # 8 means none selected
selected_j = 8
whosTurn = white
enPassant_j = 8

# Define tkinter window
window = tk.Tk()

# tkinter window setup
window.grid()
window.title("Chess Python")
window['padx'] = 10
window['pady'] = 10

# Image references
empty = tk.PhotoImage(width = 1, height = 1)
empty_green = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAC9JREFUWEft0EERAAAMwjDwL3qTwSdV0EtzuQyrAQIECBAgQIAAAQIECBAgQGAt8IXeP+HAVxIZAAAAAElFTkSuQmCC"))
tempGoldPawn = tk.PhotoImage(file = './assets/tempGoldPawn.png')
tempBlackPawn = tk.PhotoImage(file = './assets/tempBlackPawn.png')

whitePawn = tk.PhotoImage(file = './assets/WhitePawn.png')
blackPawn = tk.PhotoImage(file = './assets/BlackPawn.png')
whitePawn_green = tk.PhotoImage(file = './assets/WhitePawn_green.png')
blackPawn_green = tk.PhotoImage(file = './assets/BlackPawn_green.png')


# 2D Array for storing piece locations
pieces = [[0]*8 for _ in range(8)]

class CustomButton(tk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_green = False

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
            self.image = whitePawn
            self.image_green = whitePawn_green
        else:
            self.image = blackPawn
            self.image_green = blackPawn_green
    
    def generateValidMoves(self):
        # if it hasn't moved and has two spaces in front of it clear
        try:
            if (self.team == white and self.i == 6 and pieces[5][self.j] == 0 and pieces[4][self.j] == 0):
                grid[4][self.j].config(image = empty_green)
                grid[4][self.j].is_green = True
            if (self.team == black and self.i == 1 and pieces[2][self.j] == 0 and pieces[3][self.j] == 0):
                grid[3][self.j].config(image = empty_green)
                grid[3][self.j].is_green = True
        except:
            None
        
        # if the space in front of it is clear
        try:
            if (self.team == white and pieces[self.i - 1][self.j] == 0):
                grid[self.i - 1][self.j].config(image = empty_green)
                grid[self.i - 1][self.j].is_green = True
            if (self.team == black and pieces[self.i + 1][self.j] == 0):
                grid[self.i + 1][self.j].config(image = empty_green)
                grid[self.i + 1][self.j].is_green = True
        except:
            None
        
        # diagonal killing left
        try:
            if (self.team == white and pieces[self.i - 1][self.j - 1].team == black):
                grid[self.i - 1][self.j - 1].config(image = pieces[self.i - 1][self.j - 1].image_green)
                grid[self.i - 1][self.j - 1].is_green = True
            if (self.team == black and pieces[self.i + 1][self.j - 1].team == white):
                grid[self.i + 1][self.j - 1].config(image = pieces[self.i + 1][self.j - 1].image_green)
                grid[self.i + 1][self.j - 1].is_green = True
        except:
            None
        
        # diagonal killing right
        try:
            if (self.team == white and pieces[self.i - 1][self.j + 1].team == black):
                grid[self.i - 1][self.j + 1].config(image = pieces[self.i - 1][self.j + 1].image_green)
                grid[self.i - 1][self.j + 1].is_green = True
            if (self.team == black and pieces[self.i + 1][self.j + 1].team == white):
                grid[self.i + 1][self.j + 1].config(image = pieces[self.i + 1][self.j + 1].image_green)
                grid[self.i + 1][self.j + 1].is_green = True
        except:
            None
        
        # en passant
        #if (enPassant == True):
        #    if (self.team == white and self.i == 3):
        #        if (enP)
        #    if (self.team == black and self.i == 4):
                
        
        return
    
    
    

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
    
# Function for reverting greened spaces to regular
def revert():
    # Define global variables
    global isSelected, selected_i, selected_j
    
    isSelected = False
    #selected_i = 8
    #selected_j = 8
    
    for i in range(0, 8):
        for j in range(0, 8):
            if (grid[i][j].is_green == True):
                if (pieces[i][j] == 0):
                    grid[i][j].config(image = empty)
                else:
                    grid[i][j].config(image = pieces[i][j].image)
                grid[i][j].is_green = False
    
    return

def placeNewPiece(piece):
    global grid
    pieces[piece.i][piece.j] = piece
    grid[piece.i][piece.j].config(image = piece.image)
    return

def movePiece(oldi, oldj, i, j):
    # Define global variables
    global whosTurn, enPassant
    
    pieces[i][j] = pieces[oldi][oldj]
    pieces[i][j].i = i
    pieces[i][j].j = j
    pieces[oldi][oldj] = 0
    grid[oldi][oldj].config(image = empty)
    revert()
    if (whosTurn == white):
        whosTurn = black
    else:
        whosTurn = white
    if (pieces[i][j].pieceType == "Pawn" and abs(oldi - i) == 2):
        enPassant = True
        enPassant_j = j
    elif (enPassant == True):
        enPassant == False
        enPassant_j = 8
    else:
        None
    return

def left(i, j):
    # Define global variables
    global isSelected, selected_i, selected_j
    
    if (grid[i][j].is_green == True):
        movePiece(selected_i, selected_j, i, j)
        return
    
    # if selected space is empty
    if (pieces[i][j] == 0):
        print("empty")
        return
    
    # if selected space has the wrong team
    if (pieces[i][j].team != whosTurn):
        print("wrong team")
        return
    
    if (isSelected == True and i == selected_i and j == selected_j):
        revert()
        return
    
    # if a piece is already selected, hide previous valid moves
    if (isSelected == True):
        revert()
    
    # select current square
    isSelected = True
    selected_i = i
    selected_j = j
    print("selected", i, j)
    
    # generate valid moves
    pieces[i][j].generateValidMoves()
    
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
            grid[i][j] = CustomButton(window, image = empty, width = 32, height = 32, command = None)
            grid[i][j].grid(column = j+1, row = i+1)
            grid[i][j].bind('<Button-1>', lambda k=k, i=i, j=j: left(i, j))
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

for i in range(0,8):
    placeNewPiece(pawn(white, 6, i))

placeNewPiece(pawn(black, 4, 1))
placeNewPiece(pawn(black, 5, 5))

for i in range(0,8):
    placeNewPiece(pawn(black, 1, i))

placeNewPiece(pawn(white, 2, 2))
placeNewPiece(pawn(white, 3, 5))


window.mainloop()
    
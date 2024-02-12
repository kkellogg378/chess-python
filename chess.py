import tkinter as tk

# Define names
pawn = "Pawn"
rook = "Rook"
knight = "Knight"
bishop = "Bishop"
queen = "Queen"
king = "King"

white = "White"
black = "Black"

# Define tkinter window
window = tk.Tk()

# tkinter window setup
window.grid()
window.title("Chess Python")
window['padx'] = 10
window['pady'] = 10

class chessPiece:
    def __init___(self, pieceType, team):
        self.pieceType = pieceType
        self.team = team
    
    def __str__(self):
        return f"{team} {self.pieceType}"
        
    
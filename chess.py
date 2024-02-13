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

whitePawn       = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAr5JREFUWEeNV23a4yAI1Gts7JHavWv7nmibvNdwH0AU+dD0T9NEcRhmIM3p5ienlGpbK6/hlv49Qtpd3t4grEDmnpBTTrWDQhQApg6gdEMgd260bT5mS46HhEPUBRMezRTLAGDQ8M2Um+0x53HSTkAIw8QtKryqsaI4ArYAjAAGiSrX7NSUl2h9qQxzTqkihWu63BKExthQvzZU26xiDADb4HYBZench4K66hc2EXhmG+KDlX/p2fkplYxIJB/PE+DsLa2r7DUGDkrhbIbn54EQ8cCaES/4/3h9lyUdxhsnwNbRUJiWLiBb1evzaGnS4fD58/yXrp8HRjqeDYQl0dWjRayVLwLR4Xx+WwgMVQLx+/NATZTXmXtL7Pt9kc0inKxkN1zvIlpXL0IrReMyp1SeX9Bn3MgEsRjl7mJgAPOvgIN2IaLMbZhqV14X0sLZrZp0IJpZLlIJrAFAgml2H9AVZO/3g7AEaqr13eO+3kouqFjvznWjfnIOb/QEKQzrAB47piv8QUdgOdBNNeWa0wHCC6ru5S6xEYBQCOJBuxx9gFRAjcCKbwoZxGctLdv4vJd+XW+yZGsFqWAnXOXKSdpovRr8hrNzBaD+vkvN+PpDndATny/lWXNkQzNUeJGkf26P6IbOfm2zwNYySqZrYJdtVBsoAcmRXH78PXEyeeXiGFGBtqXzFlyfgu0IXZHzXALuBApQAECb1S7TpgQXjMlLXRFwlM009NhkrAHTFozuhNAM0EoYCbRwjUE0uVtMOeXsuQkI+jSqITw5C6Tw6Ozde4HUxO2pdTbf48zL1Ib7EOpzgYw8vRdMWbTULQN+BfDQvrgpCvmaddMHE7/oYDWoLJM2HBVuNDDel+ReLVsvyWVrFQ+3AKIxoZ2hvT6BVJnrZNRgDP6Q3exY22XjH0ufgZYtqxUBUgEM194rwn/EdG8y+A94EQAAAA5lWElmTU0AKgAAAAgAAAAAAAAA0lOTAAAAAElFTkSuQmCC"))
whitePawn_green = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAA8lJREFUWEd9V1F22zAMo46xOe2Fmp026YUWZ7tFvScSIEE5XT5aP9uSQBIA6TG+xnGY2TCzY+SVxc/v4pr/hg074i5fX96Y9+fK+Yeb+07+fuzJv7mXL5oLTsfWgROfHxxobYxvgKzAEhCOa0CwhwexLPQDxzxPFyK6ykPFLxsHQM0fo+55zQww2XoYAs0DPK2SwCoT0ZtllrSCGoQnsBJ/AhDreLuKmOkmHCmZrzkGOBSZDPDKobpeACjm/ihDn+xB+JoFgemH8sB8ByUlt0nnhOLbKgfA/KmLWfuTEv7D+gmwmB4kZT2cC9zQ0XBnD7gy0MjGGp5hBMwl4txWwkwSg8xNObnvF0SZ8gMMiQCJEZUMe94vTf3b9ZHaLu4vPhKSKm/xEnxF6UIk9YvagIRS/xngfrtAYsMzwaUTRJJfSboQNqQUMn3BgYaDrAiLOA57fL6lP/Lwn9ff9uf27kAIIlGl6xUvisjIQMJmdjJz4XbBcLPn/S3S55IDkQKZ/bg+7O/93Z9fPvZ6zoQ3AovrTDdtBBrNBZrnB4D+i0JJqY5h2y+WYkmwgCgIqgIQr/qBb0022H5/E7fWkOKagVzIBSolX10bm5dgHOmf7lxVhzKa2HxWY/+c7MeO0pzIB1cD74OR2v9a/r4zonMLhr2iuTxvKEUTzmHb9SkBgCONA5V4BuEyXBR4lgFNAxlMQmatDtt+7WktYUDnxp7JpVZROCd0J+IrKdY7TkbvD1oys8t1l326grhj5oCtvlQQTB7Y1FuE2iqoQfl1RRy2fcwM0OlYMm00Ui8SihlI9zprTK0xr0nG2WDYcZ35OYCAduwBsq825Qh4+kBaJftAzW4rphCm2QN2TNVs1z3mAJmCqu3GGp0p2DnFKYQJyp+1zcZW9rxdaraCBb+SW3VN1pDajPqiGUX9awYQNXWeeYgT9cOJWNOv94AX88K63OctnDWfNRmKQ2NOwcvAGuk90BO0OGHI4YABEPFW43ox4EcAzQfOeDPPiC7ngOztPVvakglCocbsWE8EQGdukkQ+LvxwHpwje8XKCgSI1fV4R11nZsszUBrt/g8v8FY8e0Dz3uwJ6kmUeDhjtJmUZ1MJKete0VtwFHDY43PLQ9GO6stpMUI/h6l13PAIm0NKgGmlKPjytYU3oNoamBdZnrxBBlSdhE6qWFXiQchAUnVfv+F4JAtPDWtcReDYB9+OTA2+LepzD+2EYeonCY9bjYWL1wxUzyiNw27kY5d5DSnXGeDAGss6ETO1nJYDXJG0WA9GcdBL3nK6Ugma/QNkFE4BUJn9YAAAAA5lWElmTU0AKgAAAAgAAAAAAAAA0lOTAAAAAElFTkSuQmCC"))
blackPawn       = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAApZJREFUWEedV21i7CAI1KN0k7T3P06bbHsU35MPBQSy7f7YJEoAZxg0tdZSWqullFZK4WvRPzPsWgWvSkcYa3VtouWPlZIEP25iNNgv3aSJpSl7fCAzlSehQQ7kU50OOX6/mkVhYmIiWjlgfo+cbzFGvenB6Ir5NLcIeGmmbOSpR7M2cab0hvhsJfSqjRjmpyd0DcBcz6n1i0NuqJM/Y8W16kdL1HhTGTfK0pWwGC/OCRnQFFX38djbFFEr1/flKOpe4aiCUbUWCH+d+3Y07igYFUh7LQnj0qEgr6Z92xGGIf5azudned8+YPD8efZsHEqdVfa+EoNkeapl37bWW+lU8CTh6zrLsb9DYE3HjVzl9GqqR4B3ThnU0sONjMZaegJrmS39ksjj11QsJ+tayv5G8Jt3MJUJ+6kKkmRNbRc3o0AFEVhyHGqgL9pQyn6vZ6wGhTbtwlQGHjwxd8fjgD3OvpVKkeSGepkQOkWYFI1Y9f7oSEzb6+ei6pcQ+13V1l3eX4U13/bgkLnZIhQC7jpWibMfKWt3D7ByxU44N6LB/SuFJJwNCpYVkaPhzzgGCoSQru8z2Vn1yysFSlY2MkLNRys2ZRpeqf5sRyAEplZnQWAi/K+rt5SJALqX/CdlvOTiqGDN16MhS2A0CaXTmVZMgYkdrYQ3JJin03y/P5cmlGGBvL52JBOJ9SY0tkPlH8GEYgy+LyTRWL+ziSe9YEaxsMOMPMzSvW5KQQmKWncLw7ZZFRwCzc3H+xC4nh0J/5fKsDas927Ug9oPtpBVnhiSnZZDIc7RH7O0XqPukwk6+q7k8SDz+y+jaMm/ETt3bN6C6zhSQo+b57c/OLWgLC5Sn1IFypM4xZjjpeyPLiMpfSab//j/A5G8RzqoJETPAAAADmVYSWZNTQAqAAAACAAAAAAAAADSU5MAAAAASUVORK5CYII="))
blackPawn_green = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAA5hJREFUWEeVV1uy3TAIw2tJ0v2vp0m2UncAAcLO7UzPV+JjYx6SIEOmTJEhQx+m6KPoiox40PchY+ii/+X/64PvySPxpoZo0R51aeC8H8ZudSANYr1dwhd+/0+uivo5wzmLKJyNx9rtTvn1Fof7RZFSQuKvHgWlDI+RkzFhGM5Yhld79v4HOdSX9J7dRhTqXtQI5Uh/I6NI0JhDJvZE+jPrUW6kxhwDAnyJDlchHQfm4fJjp7kUdnZOhxJVcbXgrgZoNvOJFYAuNhTCIrWRX78vVz8sMmRzZ8cxYLAzwkAD41SZ8K5fS3UJ6hT4M6CGgaj8nuhWDJQq0O6nvmMG7wao+sE2OteNcJKVGRywmrvOA8VVEyLPe2e6myU6mBghR9yB/9SB6zxlOtmTtoq253EnOhg32LZzmQFHM6jWatXNnedZkeoZGXK/v+U6f4ly/37fcipoGSwAzTtzSAc2yIJ6LlFT9HJWWd5/v7dcxy/b9zQnmk5+OJfl5ejrOZMxRa7rdMU0lWvqYSAMrXreh2L3MrX6UyspEFq0HwxO6ollwNVwsR+ig/ie58lmZc4mond0GA2bvkO9/JpQ9ohB5DqOrukQSItxTHmewsBKzl2WKeBNwRpVokW5S+dx9ZaFwDz1zn1bIv5XkEECd5iEaAELUu2GdmqpE3WTyPu+pBal3Fn9pRVm17ROwI1mGxzCRDl4HmfjejhptQdmuK33Ltv7S2WAL27CtGdG06lOpBZJiRBrUxuVwBqSLpdw9MI+yaTwure9VUETjhKkUMHmKrf1zHAf/XS/Z8BuwfGcB9nXnT6KgZJRcfSTSjnoiAeYK7t+YCRbR6VGlx+aSZNkEbmVAZuhxfFAcw1h/5wcvrsbVguIHqX3AIy/UbcoHjtmfE8O/OTALiHedJ15x6WK2DuHmkwn9E8GcurCIveaiQBhzHxBGS9DnwPVrRNKmLhR5TStcCl77pvmf4IwKJNjOObPpOEGM44QHSnFpwe/TESjDSdJy5Rs4D0H1Rp2mt5mF7BUTuN9ctI6YsxJymW3Vo0VurDKeb4jIgMjfT/kpxkivExsqv22ttpIzwbj8602VHvuuuLs/0PTVUttzPUBv14TbbPWy/JboU9TCWM7BsWDfab5DwM8DSRI2zYpE0C/ZuLIiTdcp2eN9OhuEYIny9HMVK7PqQ11Dgc4kc7x6MzD6T+wABpWDJ0N61u9e1TLl++WrWXI/YjjL0RPOgmoSEbRAAAADmVYSWZNTQAqAAAACAAAAAAAAADSU5MAAAAASUVORK5CYII="))


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
        # define direction depending on team
        if (self.team == white):
            direction = -1
            eligibleRow = 6
        else:
            direction = 1
            eligibleRow = 1
        
        try:
            # check if pawn is eligible for moving two spaces
            if (self.i == eligibleRow and pieces[self.i + direction][self.j] == 0 and pieces[self.i + 2 * direction][self.j] == 0):
                grid[self.i + 2 * direction][self.j].config(image = empty_green)
                grid[self.i + 2 * direction][self.j].is_green = True
        except:
            None
        
        try:
            # check if the space in front of it is clear
            if (pieces[self.i + direction][self.j] == 0):
                grid[self.i + direction][self.j].config(image = empty_green)
                grid[self.i + direction][self.j].is_green = True
        except:
            None
        
        # check for both right and left directions
        for k in [-1, 1]:
            try:
                # check whether the diagonal has an enemy piece
                if (pieces[self.i + direction][self.j + k].team != self.team):
                    grid[self.i + direction][self.j + k].config(image = pieces[self.i + direction][self.j + k].image_green)
                    grid[self.i + direction][self.j + k].is_green = True
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
    
# imported kociemba library to use for front and backend start
# later hard code a solver 

import kociemba # Kociemba's algorithm for solving Rubik's cubes

# input is COLORS (R,G,W,O,B,Y) that gets converted to face letters (U,R,F,D,L,B)
COLOR_TO_FACE = {
    "R": "U",
    "G": "R",
    "W": "F",
    "O": "D",
    "B": "L",
    "Y": "B",
}

# Solved state in face letters (URFDLB order)
SOLVED = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"

def solve_kociemba(stickers: str):
    
    # Join list input into a string (from R,R,R to RRR)
    if isinstance(stickers, list):
        stickers = "".join(stickers)

    # Convert colors to face letters (R->U, G->R, W->F, O->D, B->L, Y->B) 
    face_string = "".join(COLOR_TO_FACE[c] for c in stickers) 

    # solved check
    if face_string == SOLVED:
        return [] 

    return kociemba.solve(face_string).split() # Return the solution moves as a list of strings



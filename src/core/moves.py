"""
Error 1: fixed with 53 and 47 swap in L
L: top row of L is invert 
L': bottom row of L is invert
Error 2: fixed with swapping 2nd and 4th in F and B
F & B: 4 sides flip the opposite
Error 3: fixed with swapping 36 and 42 in B
B:  down 3 row is reversed 
B': up 3 row is reversed
"""

# 54 stickers indexed in URFDLB order:
# U: 0-8,  R: 9-17,  F: 18-26,  D: 27-35,  L: 36-44,  B: 45-53

# Declare the cube face index ranges
U = [0, 1, 2, 3, 4, 5, 6, 7, 8]             # Red
R = [9, 10, 11, 12, 13, 14, 15, 16, 17]     # Green
F = [18, 19, 20, 21, 22, 23, 24, 25, 26]    # White
D = [27, 28, 29, 30, 31, 32, 33, 34, 35]    # Orange
L = [36, 37, 38, 39, 40, 41, 42, 43, 44]    # Blue
B = [45, 46, 47, 48, 49, 50, 51, 52, 53]    # Yellow

# Helper function to cycle four positions in the cube state
# works like a 4-cycle: d -> a -> b -> c -> d (last goes to first).
def cycle(s, a, b, c, d):
    s[a], s[b], s[c], s[d] = s[d], s[a], s[b], s[c]

# To rotate a face clockwise
# face9 is the 9 indices of that face in row-major order (0-8 for that face).
def rotate_face_cw(s, face9):
    # rotate corners
    cycle(s, face9[0], face9[2], face9[8], face9[6])
    # rotate edges
    cycle(s, face9[1], face9[5], face9[7], face9[3])

# Define move functions for each face, which rotate the face and the adjacent pieces 
def move_U(s):
    rotate_face_cw(s, U) # Rotate the U face clockwise
    # U clockwise: L top -> B top -> R top -> F top -> L top
    cycle(s, 18, 36, 45, 9)  # F0 R0 B0 L0
    cycle(s, 19, 37, 46, 10) # F1 R1 B1 L1
    cycle(s, 20, 38, 47, 11) # F2 R2 B2 L2


def move_D(s):
    rotate_face_cw(s, D)
    # D clockwise: L bottom -> F bottom -> R bottom -> B bottom -> L bottom
    cycle(s, 24, 15, 51, 42)  # F6 L6 B6 R6
    cycle(s, 25, 16, 52, 43)  # F7 L7 B7 R7
    cycle(s, 26, 17, 53, 44)  # F8 L8 B8 R8


def move_R(s):
    rotate_face_cw(s, R)
    # R clockwise: U right -> B right -> D right -> F right -> U right
    cycle(s, 2, 51, 29, 20)   # U2 F2 D2 B6
    cycle(s, 5, 48, 32, 23)   # U5 F5 D5 B3
    cycle(s, 8, 45, 35, 26)   # U8 F8 D8 B0


def move_L(s):
    rotate_face_cw(s, L)
    # L clockwise: U left -> F left  -> D left -> B left -> U left
    cycle(s, 0, 18, 27, 53)   # U0 B2 D0 F0
    cycle(s, 3, 21, 30, 50)   # U3 B5 D3 F3
    cycle(s, 6, 24, 33, 47)   # U6 B8 D6 F6


def move_F(s):
    rotate_face_cw(s, F)
    # F clockwise: U front -> R front -> D front -> L front -> U front
    cycle(s, 6, 9, 29, 44)    # U6 R0 D2 L8
    cycle(s, 7, 12, 28, 41)   # U7 R3 D1 L5
    cycle(s, 8, 15, 27, 38)   # U8 R6 D0 L2


def move_B(s):
    rotate_face_cw(s, B)
    # B clockwise: U back -> L back -> D back -> R back -> U back
    cycle(s, 0, 42, 35, 11)   # U0 L0 D8 R2
    cycle(s, 1, 39, 34, 14)   # U1 L3 D7 R5
    cycle(s, 2, 36, 33, 17)   # U2 L6 D6 R8

# Move functions tied to their face characters
MOVE_FUNCS = {"U": move_U, "D": move_D, "R": move_R, "L": move_L, "F": move_F, "B": move_B}

# Apply a move to the cube 
def apply_move(stickers, move: str):
    move = move.strip() 
    if not move:
        raise ValueError("Empty move")

    face = move[0].upper()                         # Get the face character (U, D, L, R, F, B) and convert to uppercase
    if face not in MOVE_FUNCS:
        raise ValueError(f"Invalid move: {move}")

    suffix = move[1:] # Get the suffix (if any) which can be "", "'", or "2" to indicate the type of move (normal, inverse, or double)

    # base move funcs are acting like CCW, so "" is 3 turns, "'" is 1 turn.
    if suffix == "":
        reps = 1
    elif suffix == "2":
        reps = 2
    elif suffix == "'":
        reps = 3
    else:
        raise ValueError(f"Invalid move suffix: {move}")

    # Compute moves based on the face and the number of repetitions 
    f = MOVE_FUNCS[face] 
    for _ in range(reps):
        f(stickers) # rotates face and adjacent pieces in place
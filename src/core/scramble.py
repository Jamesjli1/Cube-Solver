# Generate a random scramble of moves for a cube and apply it to the cube

import random

# Turn definitions
FACES = ["U", "D", "R", "L", "F", "B"]
SUFFIXES = ["", "'", "2"]

# Axis definitions for checking move legality (no same axis twice in a row)
AXIS = {
    "U": "UD", "D": "UD",
    "R": "RL", "L": "RL",
    "F": "FB", "B": "FB",
}

# Generate a random scramble of moves for a cube
def gen_scramble(n: int = 20) -> str: # 20 moves by default
    moves = []
    prev_face = None
    prev_axis = None

    # Generate moves until we have n moves in the scramble
    while len(moves) < n:
        face = random.choice(FACES) # Choose a random face to turn

        # Rule 1: no same face twice in a row
        if face == prev_face:
            continue

        # Rule 2: no same axis twice in a row (prevents things like U D U2 etc.)
        if AXIS[face] == prev_axis:
            continue

        suf = random.choice(SUFFIXES) # Choose a random suffix for the move (normal, prime, or double)
        moves.append(face + suf)      # Add the move to the list of moves

        # Update previous face and axis for the next iteration
        prev_face = face 
        prev_axis = AXIS[face]

    return " ".join(moves) # Join the list of moves into a single string separated by spaces

# Tester
# print(gen_scramble())        

# Run a command interface to test the cube 
import sys 
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src")) # Add src to path for imports

from core.cube import Cube              # for Cube class
from core.scramble import gen_scramble  # for generating scrambles
from core.customcube import custom_cube # for loading custom cube states

# Face index ranges (URFDLB)
U = list(range(0, 9))
R = list(range(9, 18))
F = list(range(18, 27))
D = list(range(27, 36))
L = list(range(36, 45))
B = list(range(45, 54))

# Helper to get rows of a face for printing
def rows(face9, s):
    return [
        "".join(s[i] for i in face9[0:3]),
        "".join(s[i] for i in face9[3:6]),
        "".join(s[i] for i in face9[6:9]),
    ]

# Print the cube in a net layout:
def print_net(cube: Cube):
    s = cube.s
    u = rows(U, s)
    l = rows(L, s)
    f = rows(F, s)
    r = rows(R, s)
    b = rows(B, s)
    d = rows(D, s)

    # Top (U)
    for row in u:
        print("    " + row)

    # Middle (L F R B)
    for i in range(3):
        print(f"{l[i]} {f[i]} {r[i]} {b[i]}")

    # Bottom (D)
    for row in d:
        print("    " + row)


def main():
    cube = Cube()           # Make a new cube (solved by default)
    print("Solved cube:")
    print_net(cube)         # Call the print_net function to display the cube state

    print("\nMoves: U D L R F B, with ' or 2 (example: R, U', F2)")
    print("Type multiple moves: R U R' U'")
    print("Commands: scramble, create, reset, quit\n")

    while True:
        cmd = input("").strip()
       
        # Command to quit the program
        if cmd.lower() in {"quit", "q"}: 
            break
        # Command to reset the cube to the solved state
        if cmd.lower() in {"reset"}:
            cube.reset() # Reset the cube to the solved state
            print("\nReset:")
            print_net(cube)
            continue
        # Scramble cube
        if cmd.lower() in {"scramble", "s"}:
            # Generate a random scramble and apply it to the cube
            scramble = gen_scramble()
            print(f"\nScramble: {scramble}")
            for m in scramble.split(): # Apply each move in the scramble to the cube
                cube.move(m)
            print_net(cube)
            continue
        # Create a custom state
        if cmd.lower() in {"create", "c"}:
            stickers = custom_cube() # Get a custom cube state from user input
            cube.set_state(stickers) # Set the cube to the custom state
            print("\nCustom cube:")
            print_net(cube)          # Print the custom cube state
            continue
        if not cmd:
            continue # Skip empty input

        # Apply the moves entered by the user with loop
        moves = [t for t in cmd.split() if t]
        for m in moves:
            if m not in {"U", "D", "L", "R", "F", "B", "U'", "D'", "L'", "R'", "F'", "B'", "U2", "D2", "L2", "R2", "F2", "B2"}:
                print(f"\nInvalid move: {m}")
                continue
            cube.move(m)
            print(f"\nAfter {m}:")
            print_net(cube)


if __name__ == "__main__":
    main()
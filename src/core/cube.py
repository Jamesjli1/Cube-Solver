from .moves import apply_move

# Initialize solved cube
# State order is URFDLB with colors R G W O B Y (Red, Green, White, Orange, Blue, Yellow)
SOLVED = (
    "R" * 9 +  # U
    "G" * 9 +  # R
    "W" * 9 +  # F
    "O" * 9 +  # D
    "B" * 9 +  # L
    "Y" * 9    # B
)

# Cube class to represent the cube state and apply moves
class Cube:
    def __init__(self, stickers: str = SOLVED):
        self.set_state(stickers) # Initialize the cube state with the provided stickers or default to solved

    # Set the cube state from a string of 54 characters (URFDLB order)
    def set_state(self, stickers: str):
        if len(stickers) != 54:
            raise ValueError("Cube state must be 54 characters (URFDLB order).")
        self.s = list(stickers)

    # Reset the cube to the solved state
    def reset(self):
        self.s = list(SOLVED)

    # Get the current cube state as a string
    def state(self) -> str:
        return "".join(self.s)

    # Check if the cube is in the solved state
    def is_solved(self) -> bool:
        return self.state() == SOLVED

    # Apply a single move to the cube state
    def move(self, m: str):
        apply_move(self.s, m)

    # Apply a sequence of moves to the cube state
    def alg(self, seq):
        # seq can be "R U R' U'" or ["R", "U", "R'", "U'"]
        if isinstance(seq, str):
            seq = [t for t in seq.split() if t]
        for m in seq:
            self.move(m)
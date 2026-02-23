# Custom cube input function for the cube solver
def custom_cube():
    print("\nEnter 9 lines of the cube net:")

    lines = [input() for _ in range(9)] # Read 9 lines of input for the cube net

    # U face (top 3 lines, strip leading spaces)
    U_face = "".join(lines[i].strip() for i in range(3)) 

    # Middle 3 lines: L F R B
    L_face = ""
    F_face = ""
    R_face = ""
    B_face = ""

    # Loop through the middle 3 lines to extract L, F, R, B faces
    for i in range(3, 6):
        parts = lines[i].split()
        L_face += parts[0]
        F_face += parts[1]
        R_face += parts[2]
        B_face += parts[3]

    # D face (bottom 3 lines)
    D_face = "".join(lines[i].strip() for i in range(6, 9))

    # Build URFDLB order
    stickers = U_face + R_face + F_face + D_face + L_face + B_face

    return stickers
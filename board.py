# Initialize the board (15x15 grid)
board = [[" " for _ in range(15)] for _ in range(15)]

def display_board():
    for row in board:
        print(" ".join(row))
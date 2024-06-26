from rack import computer_rack, draw_tiles
from board import board
from tile import letter_points
import random

def compplays(computer_rack):
    word = "".join(random.sample(computer_rack, random.randint(1, 7)))
    print(f"Computer plays: {word}")
    
    direction = random.choice(['H', 'V'])
    row = random.randint(0, 14)
    col = random.randint(0, 14)

    if direction == 'H':
        col = min(col, 15 - len(word))
        for i, letter in enumerate(word):
            board[row][col + i] = letter
            computer_rack.remove(letter)
    elif direction == 'V':
        row = min(row, 15 - len(word))
        for i, letter in enumerate(word):
            board[row + i][col] = letter
            computer_rack.remove(letter)
    
    score = sum(letter_points[letter] for letter in word)
    print(f"Word played: {word}, Score: {score}")
    return score

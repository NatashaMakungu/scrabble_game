from rack import player_rack
from board import board, display_board
from tile import letter_points

def play_word(player_rack):
    display_board()
    print(f"Your rack: {player_rack}")
    
    word = input("Enter the word you want to play: ").strip().upper()
    row = int(input("Enter the row number (0-14): ").strip())
    col = int(input("Enter the column number (0-14): ").strip())
    direction = input("Enter direction (H for horizontal, V for vertical): ").strip().upper()

    if all(letter in player_rack for letter in word):
        if direction == 'H':
            for i, letter in enumerate(word):
                board[row][col + i] = letter
                player_rack.remove(letter)
        elif direction == 'V':
            for i, letter in enumerate(word):
                board[row + i][col] = letter
                player_rack.remove(letter)
        
        score = sum(letter_points[letter] for letter in word)
        print(f"Word played: {word}, Score: {score}")
        return score
    else:
        print("You don't have the letters to play this word.")
        return 0
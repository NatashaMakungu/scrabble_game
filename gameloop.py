from human import play_word
from comp import compplays
from rack import player_rack, computer_rack, draw_tiles
from tilebag import letter_bag
from board import display_board

def gameloop():
    player_score = 0
    computer_score = 0

    while True:
        player_score += play_word(player_rack)
        if len(player_rack) < 7:
            player_rack.extend(draw_tiles(7 - len(player_rack)))

        print(f"Computer's rack: {computer_rack}")
        computer_score += compplays(computer_rack)
        if len(computer_rack) < 7:
            computer_rack.extend(draw_tiles(7 - len(computer_rack)))

        print(f"Player score: {player_score}")
        print(f"Computer score: {computer_score}")

        display_board()

        if not letter_bag:
            break
    
    if player_score > computer_score:
        print("Player wins!")
    else:
        print("Computer wins!")

gameloop()
from tilebag import draw_tiles

def display_racks():
    player_rack = draw_tiles(7)
    computer_rack = draw_tiles(7)
    return player_rack, computer_rack

player_rack, computer_rack = display_racks()
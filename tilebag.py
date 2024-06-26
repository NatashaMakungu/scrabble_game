import random

# Define letter distribution
letter_distribution = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1,
    'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6,
    'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1, ' ': 2  # blank tiles
}

# Create the letter bag
letter_bag = []
for letter, count in letter_distribution.items():
    letter_bag.extend([letter] * count)
random.shuffle(letter_bag)

def draw_tiles(num):
    return [letter_bag.pop() for _ in range(num)]
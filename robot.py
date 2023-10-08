from gasp import *
from random import randint

class Player:
    pass
class Robot:
    pass

def place_player():
    print("hi!")
    player_x = random.randint(0, 63)
    player_y = random.randint(0, 47)
    player_shape = Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)
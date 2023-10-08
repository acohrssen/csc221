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

    def move_player():
    global player_x, player_y, player_form
    key = update_when('key_pressed')
    if key == 'w' and player_y < 47:
        player_y = player_y + 1
    elif key == 'a' and player_x > 0:
        player_x = player_x - 1
    elif key == 's' and player_y > 0:
        player_y = player_y - 1
    elif key == 'd' and player_x < 63:
        player_x = player_x + 1
    elif key == 'q' and player_y < 47 and player_x > 0:
        player_y = player_y + 1
        player_x = player_x - 1
    elif key == 'e' and player_y < 47 and player_x < 63:
        player_y = player_y + 1
        player_x = player_x + 1
    elif key == 'z' and player_y > 0 and player_x > 0:
        player_y = player_y - 1
        player_x = player_x - 1
    elif key == 'c' and player_y > 0 and player_x < 63:
        player_y = player_y - 1
        player_x = player_x + 1
    elif key == 'space':
        player_y = random.randint(0, 47)
        player_x = random.randint(0, 63)
    move_to(player_form, (player_x * 10 + 5, player_y * 10 + 5))
    move_robot()


def place_robots(amount):
    global rob_x
    global rob_y
    global robot
    rob_x = random.randint(25, 50)
    rob_y = random.randint(25, 50)
    robot = Box((10 *  rob_x, 10 * rob_y), 10, 10, filled=True, color=color.PURPLE, thickness=1)

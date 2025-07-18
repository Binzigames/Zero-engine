import pyray as pr
import math

player_position = pr.Vector3(0, 1, 0)
player_speed = 0.2
position_initialized = False

def set_player_position(pos: pr.Vector3):
    global player_position
    player_position = pos

def move_player(direction: pr.Vector3):
    global player_position

    if direction.x == 0 and direction.y == 0 and direction.z == 0:
        return

    length = math.sqrt(direction.x ** 2 + direction.y ** 2 + direction.z ** 2)
    if length == 0:
        return

    norm_dir = pr.Vector3(direction.x / length, direction.y / length, direction.z / length)

    player_position.x += norm_dir.x * player_speed
    player_position.y += norm_dir.y * player_speed
    player_position.z += norm_dir.z * player_speed

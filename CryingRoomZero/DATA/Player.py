#-------------> importing
import pyray as pr
import math
import DATA.Config as con
#-------------> bools
player_position = pr.Vector3(con.Px, 1, con.Pz)
player_speed = con.Pspeed

PpositionSet= False
#-------------> functions
def set_player_position(pos: pr.Vector3):
    global player_position, PpositionSet
    if not PpositionSet and pos:
        player_position.x = pos.x
        player_position.y = pos.y
        player_position.z = pos.z
        PpositionSet = True

#> colisions
def can_move_to(pos: pr.Vector3, level_map):
    radius = con.Pradius
    offsets = [
        (-radius, -radius),
        (-radius,  radius),
        ( radius, -radius),
        ( radius,  radius)
    ]

    for offset_x, offset_z in offsets:
        check_x = int(pos.x + offset_x)
        check_z = int(pos.z + offset_z)

        if check_z < 0 or check_z >= len(level_map):
            return False
        if check_x < 0 or check_x >= len(level_map[0]):
            return False

        cell = level_map[check_z][check_x]
        if cell in (1, 3):
            return False

    return True




#> movement
def move_player(direction: pr.Vector3):
    global player_position

    if direction.x == 0 and direction.y == 0 and direction.z == 0:
        return

    length = math.sqrt(direction.x ** 2 + direction.y ** 2 + direction.z ** 2)
    if length == 0:
        return

    norm_dir = pr.Vector3(direction.x / length, direction.y / length, direction.z / length)

    new_pos = pr.Vector3(
        player_position.x + norm_dir.x * player_speed,
        player_position.y + norm_dir.y * player_speed,
        player_position.z + norm_dir.z * player_speed
    )

    if can_move_to(new_pos, con.Mmap):
        player_position.x = new_pos.x
        player_position.y = new_pos.y
        player_position.z = new_pos.z
    else:
        test_pos_x = pr.Vector3(new_pos.x, player_position.y, player_position.z)
        if can_move_to(test_pos_x, con.Mmap):
            player_position.x = test_pos_x.x

        test_pos_z = pr.Vector3(player_position.x, player_position.y, new_pos.z)
        if can_move_to(test_pos_z, con.Mmap):
            player_position.z = test_pos_z.z

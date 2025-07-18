#-------------> importing
import pyray as pr
import DATA.SceneManager as SM
import DATA.Camera as cam
import DATA.Player as player
#-------------> controls
def handle_controls():
    forward, right = cam.get_forward_right()
    direction = pr.Vector3(0, 0, 0)

    # Player
    if pr.is_key_down(pr.KEY_W):
        direction.x += forward.x
        direction.z += forward.z
    if pr.is_key_down(pr.KEY_S):
        direction.x -= forward.x
        direction.z -= forward.z
    if pr.is_key_down(pr.KEY_D):
        direction.x += right.x
        direction.z += right.z
    if pr.is_key_down(pr.KEY_A):
        direction.x -= right.x
        direction.z -= right.z

    if direction.x != 0 or direction.z != 0:
        length = (direction.x ** 2 + direction.z ** 2) ** 0.5
        direction.x /= length
        direction.z /= length


        delta = pr.get_frame_time()
        direction.x *= player.player_speed * delta
        direction.z *= player.player_speed * delta


        player.move_player(direction)

    # debug
    if pr.is_key_down(pr.KEY_R):
        SM.change_lvl(1)
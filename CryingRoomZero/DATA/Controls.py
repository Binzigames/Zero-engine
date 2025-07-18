#-------------> importing
import pyray as pr
import DATA.SceneManager as SM
import DATA.Camera as cam
import DATA.Player as player
#-------------> Controls

def handle_controls():
    forward, right = cam.get_forward_right()

    direction = pr.Vector3(0, 0, 0)

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

    player.move_player(direction)



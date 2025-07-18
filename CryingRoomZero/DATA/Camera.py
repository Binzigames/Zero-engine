import pyray as pr
import math
from DATA.Player import player_position

yaw = 0.0
pitch = 0.0
mouse_sensitivity = 0.1

camera = pr.Camera3D()
camera.position = player_position
camera.target = pr.Vector3(player_position.x, player_position.y, player_position.z + 1)
camera.up = pr.Vector3(0, 1, 0)
camera.fovy = 60.0
camera.projection = pr.CAMERA_PERSPECTIVE

def update_camera():
    global yaw, pitch, camera

    camera.position = player_position

    mouse_delta = pr.get_mouse_delta()
    mouse_dx = mouse_delta.x
    mouse_dy = mouse_delta.y

    yaw += mouse_dx * mouse_sensitivity
    pitch -= mouse_dy * mouse_sensitivity

    pitch = max(-89.0, min(89.0, pitch))

    rad_yaw = math.radians(yaw)
    rad_pitch = math.radians(pitch)

    forward = pr.Vector3(
        math.cos(rad_pitch) * math.cos(rad_yaw),
        math.sin(rad_pitch),
        math.cos(rad_pitch) * math.sin(rad_yaw)
    )

    camera.target = pr.Vector3(
        camera.position.x + forward.x,
        camera.position.y + forward.y,
        camera.position.z + forward.z
    )

    pr.update_camera(camera, pr.CAMERA_CUSTOM)

def get_forward_right():
    rad_yaw = math.radians(yaw)
    forward = pr.Vector3(
        math.cos(rad_yaw),
        0,
        math.sin(rad_yaw)
    )
    right = pr.Vector3(
        -math.sin(rad_yaw),
        0,
        math.cos(rad_yaw)
    )
    return forward, right

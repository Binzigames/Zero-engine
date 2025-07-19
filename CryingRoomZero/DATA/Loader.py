import os
from pyray import *

#> textures name
wall = None
window_wall = None
door_wall = None
exit_wall = None
floor = None

def load_texture_flipped(path):
    img = load_image(path)
    image_flip_vertical(img)
    tex = load_texture_from_image(img)
    unload_image(img)
    return tex

def load_textures_1():
    global wall, window_wall, door_wall, floor, exit_wall
    base_path = os.path.join(os.path.dirname(__file__), "Textures", "Hause")

    def load_texture_safe(name):
        path = os.path.join(base_path, name)
        try:
            texture = load_texture_flipped(path)
            print(f"Loaded texture: {name}")
            return texture
        except Exception as e:
            print(f"Failed to load {name}: {e}")
            return None

    wall = load_texture_safe("Wall.png")
    window_wall = load_texture_safe("Wall_window.png")
    door_wall = load_texture_safe("Wall_door.png")
    floor = load_texture_safe("flour.png")
    exit_wall = load_texture_safe("Wall_door_exit.png")
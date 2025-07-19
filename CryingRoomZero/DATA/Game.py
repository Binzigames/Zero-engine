#-------------> importing
import pyray as pr
from DATA.Camera import camera
import DATA.SceneManager as SM
from DATA.Config import *
from DATA.Controls import handle_controls
from DATA.UI import handle
from DATA.Loader import load_textures_1
#-------------> Game Function
#layer functions
IsTexturesLoaded = False
def update_logic():
    global IsTexturesLoaded
    handle_controls()
    if not IsTexturesLoaded:
        load_textures_1()
        IsTexturesLoaded = True

def draw_3d():
    pr.begin_mode_3d(camera)
    SM.Handle()
    pr.end_mode_3d()

def draw_UI():
    handle()

#>layered game
def game_layered():
    update_logic()

    pr.begin_drawing()
    pr.clear_background(pr.BLACK)

    draw_3d()
    draw_UI()

    pr.end_drawing()

# > run
def run():
    screen_width = Sx
    screen_height = Sy

    pr.init_window(screen_width, screen_height, Sname)
    pr.set_target_fps(Sfps)

    while not pr.window_should_close():
        game_layered()

    pr.close_window()
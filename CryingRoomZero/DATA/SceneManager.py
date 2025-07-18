#-------------> Importing
import DATA.Scenes.test_lvl as Tlvl
import DATA.Player as P
import pyray as pr
#-------------> bools
Curent_scene = 0
InGame = True
#-------------> functions
def Handle():
    scene_map = {
        1: Tlvl.draw,
    }
    scene_map.get(Curent_scene, lambda: None)()


#> lvl work
def change_lvl(index: int):
    global Curent_scene
    init_lvl()
    Curent_scene = index

def init_lvl():
    from DATA.Scenes.test_lvl import get_spawn_position
    spawn = get_spawn_position()

    if spawn:
        P.PpositionSet = False
        P.set_player_position(spawn)
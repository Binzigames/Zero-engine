#-------------> Importing
import DATA.Scenes.test_lvl as Tlvl
#-------------> bools
Curent_scene = 0
#-------------> functions
def Handle():
    global Curent_scene
    if Curent_scene == 0:
        Tlvl.draw()
    else:
        Curent_scene = 0


#> lvl work
def change_lvl(index: int):
    global Curent_scene
    Curent_scene = index
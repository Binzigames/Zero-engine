#-------------> importing
import pyray as pr
import DATA.Camera as cam
import DATA.Config as con
#------------->scene context
lvl_name = "test zone"
lvl_index = 0
Intro_text =  "debug"

#------------->level data
# 1 - wall
# 2 - Player spawn
level_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]
]


#-------------> draw level function
Intro_start_time = None

def draw():
    global Intro_text, Intro_start_time

    if con.UIInIntro:
        if pr.get_time() - Intro_start_time > 5.0:
            con.UIInIntro = False
        else:
            return

    elif Intro_start_time is None:
        con.UIIntroText = Intro_text
        con.UIInIntro = True
        Intro_start_time = pr.get_time()
        return

    render_level()



def render_level():
    if not level_map == con.Mmap:
        # > saving map to global...
        con.Mmap = level_map
    if not con.UIInGame:
        con.UIInGame = True
    cam.update_camera()
    map_width = len(level_map[0])
    map_height = len(level_map)
    pr.draw_plane(pr.Vector3(map_width / 2.0 - 0.5, 0, map_height / 2.0 - 0.5), (map_width, map_height),
                  pr.DARKPURPLE)

    pr.draw_cube(pr.Vector3(map_width / 2.0 - 0.5, 1.5, map_height / 2.0 - 0.5), map_width, 0.1, map_height, pr.VIOLET)

    for z, row in enumerate(level_map):
        for x, cell in enumerate(row):
            if cell == 1:
                pr.draw_cube(pr.Vector3(float(x), 0.5, float(z)), 1.0, 2, 1.0, pr.GRAY)
            else:
                pass


def get_spawn_position():
    for z, row in enumerate(level_map):
        for x, cell in enumerate(row):
            if cell == 2:
                return pr.Vector3(float(x), -1, float(z))
    return None


P_spawn = get_spawn_position()
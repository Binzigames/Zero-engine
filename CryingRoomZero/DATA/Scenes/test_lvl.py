import pyray as pr
import DATA.Camera as cam
import DATA.Config as con
import DATA.Loader as lod
import struct
from pyray import ffi

#------------->scene context
lvl_name = "test zone"
lvl_index = 0
Intro_text =  "debug"

#------------->level data
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
#-------------> draw function
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

    render_level_with_textures()

#-------------> tiling shit < real shit...
def ensure_texture_repeat(texture):
    if hasattr(texture, "id"):
        pr.set_texture_wrap(texture, pr.TEXTURE_WRAP_REPEAT)


def get_tiled_floor_model(map_width, map_height, tile_x=1.0, tile_y=1.0, texture=None):
    if not hasattr(lod, "tiled_floor_model"):
        mesh = pr.gen_mesh_plane(map_width, map_height, int(map_width), int(map_height))
        vertex_count = (map_width + 1) * (map_height + 1)
        texcoords_ptr = ffi.cast("float *", mesh.texcoords)
        for y in range(map_height + 1):
            for x in range(map_width + 1):
                idx = (y * (map_width + 1) + x) * 2
                texcoords_ptr[idx] = x * tile_x
                texcoords_ptr[idx + 1] = y * tile_y
        lod.tiled_floor_model = pr.load_model_from_mesh(mesh)
        if texture:
            ensure_texture_repeat(texture)
            MATERIAL_MAP_DIFFUSE = getattr(pr, "MATERIAL_MAP_DIFFUSE", 1)
            pr.set_material_texture(lod.tiled_floor_model.materials[0], MATERIAL_MAP_DIFFUSE, texture)
    return lod.tiled_floor_model

#-------------> wall models
def get_wall_model(texture=None, tile_x=1.0, tile_y=2.0):
    key = f"wall_model_{tile_x}_{tile_y}_flipped"
    if not hasattr(lod, key):
        mesh = pr.gen_mesh_cube(1.0, 2.0, 1.0)
        texcoords_ptr = ffi.cast("float *", mesh.texcoords)
        for face in range(6):
            for vert in range(4):
                idx = face * 4 * 2 + vert * 2
                if vert == 0:
                    u, v = 0, tile_y
                elif vert == 1:
                    u, v = tile_x, tile_y
                elif vert == 2:
                    u, v = tile_x, 0
                else:
                    u, v = 0, 0
                texcoords_ptr[idx] = u
                texcoords_ptr[idx + 1] = v
        model = pr.load_model_from_mesh(mesh)
        if texture:
            ensure_texture_repeat(texture)
            MATERIAL_MAP_DIFFUSE = getattr(pr, "MATERIAL_MAP_DIFFUSE", 1)
            pr.set_material_texture(model.materials[0], MATERIAL_MAP_DIFFUSE, texture)
        setattr(lod, key, model)
    return getattr(lod, key)

def get_window_wall_model(texture=None, tile_x=1.0, tile_y=2.0):
    key = f"window_wall_model_{tile_x}_{tile_y}_flipped"
    if not hasattr(lod, key):
        mesh = pr.gen_mesh_cube(1.0, 2.0, 1.0)
        texcoords_ptr = ffi.cast("float *", mesh.texcoords)
        for face in range(6):
            for vert in range(4):
                idx = face * 4 * 2 + vert * 2
                if vert == 0:
                    u, v = 0, tile_y
                elif vert == 1:
                    u, v = tile_x, tile_y
                elif vert == 2:
                    u, v = tile_x, 0
                else:
                    u, v = 0, 0
                texcoords_ptr[idx] = u
                texcoords_ptr[idx + 1] = v
        model = pr.load_model_from_mesh(mesh)
        if texture:
            ensure_texture_repeat(texture)
            MATERIAL_MAP_DIFFUSE = getattr(pr, "MATERIAL_MAP_DIFFUSE", 1)
            pr.set_material_texture(model.materials[0], MATERIAL_MAP_DIFFUSE, texture)
        setattr(lod, key, model)
    return getattr(lod, key)

def get_door_wall_model(texture=None, tile_x=1.0, tile_y=2.0):
    key = f"door_wall_model_{tile_x}_{tile_y}_flipped"
    if not hasattr(lod, key):
        mesh = pr.gen_mesh_cube(1.0, 2.0, 1.0)
        texcoords_ptr = ffi.cast("float *", mesh.texcoords)
        for face in range(6):
            for vert in range(4):
                idx = face * 4 * 2 + vert * 2
                if vert == 0:
                    u, v = 0, tile_y
                elif vert == 1:
                    u, v = tile_x, tile_y
                elif vert == 2:
                    u, v = tile_x, 0
                else:
                    u, v = 0, 0
                texcoords_ptr[idx] = u
                texcoords_ptr[idx + 1] = v
        model = pr.load_model_from_mesh(mesh)
        if texture:
            ensure_texture_repeat(texture)
            MATERIAL_MAP_DIFFUSE = getattr(pr, "MATERIAL_MAP_DIFFUSE", 1)
            pr.set_material_texture(model.materials[0], MATERIAL_MAP_DIFFUSE, texture)
        setattr(lod, key, model)
    return getattr(lod, key)
#-------------> level render
def render_level_with_textures():
    if not level_map == con.Mmap:
        con.Mmap = level_map
    if not con.UIInGame:
        con.UIInGame = True
    cam.update_camera()
    map_width = len(level_map[0])
    map_height = len(level_map)
    # ------------->flour
    if lod.floor:
        tile_x = tile_y = 20.0
        tiled_model = get_tiled_floor_model(map_width, map_height, tile_x, tile_y, lod.floor)
        pr.draw_model(
            tiled_model,
            pr.Vector3(map_width / 2.0 - 0.5, 0, map_height / 2.0 - 0.5),
            1.0,
            pr.WHITE
        )
    else:
        pr.draw_plane(
            pr.Vector3(map_width / 2.0 - 0.5, 0, map_height / 2.0 - 0.5),
            (map_width, map_height),
            pr.DARKPURPLE
        )

    pr.draw_plane(
        pr.Vector3(map_width / 2.0 - 0.5, 2.0, map_height / 2.0 - 0.5),
        (map_width, map_height),
        pr.GRAY
    )


    wall_tile_x = 1.0
    wall_tile_y = 2.0
    for z, row in enumerate(level_map):
        for x, cell in enumerate(row):
            pos = pr.Vector3(float(x), 1.0, float(z))
            if cell == 1:
                if lod.wall:
                    model = get_wall_model(lod.wall, wall_tile_x, wall_tile_y)
                    pr.draw_model(model, pos, 1.0, pr.WHITE)
                else:
                    pr.draw_cube(pos, 1.0, 2.0, 1.0, pr.GRAY)
            elif cell == 3:
                if lod.window_wall:
                    model = get_window_wall_model(lod.window_wall, wall_tile_x, wall_tile_y)
                    pr.draw_model(model, pos, 1.0, pr.WHITE)
                else:
                    pr.draw_cube(pos, 1.0, 2.0, 1.0, pr.LIGHTGRAY)
            elif cell == 4:
                if lod.door_wall:
                    model = get_door_wall_model(lod.door_wall, wall_tile_x, wall_tile_y)
                    pr.draw_model(model, pos, 1.0, pr.WHITE)
                else:
                    pr.draw_cube(pos, 1.0, 2.0, 1.0, pr.BROWN)

#-------------> player spawn
def get_spawn_position():
    for z, row in enumerate(level_map):
        for x, cell in enumerate(row):
            if cell == 2:
                return pr.Vector3(float(x), -1, float(z))
    return None

P_spawn = get_spawn_position()
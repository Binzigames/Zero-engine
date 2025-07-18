#-------------> importing
import pyray as pr
import DATA.Config as con

#-------------> in game ui
def draw_game_ui():
    pr.draw_text(f"{pr.get_fps()} : FPS" , 20 , 20 , 20 , pr.GREEN)
#>Intro
def draw_game_intro(text):
    pr.draw_text("welcome" , 20 , 20 , 40 , pr.WHITE)
    pr.draw_text(f"about : {text}", 20, 60, 20, pr.WHITE)
    pr.draw_text("wait a few seconds..." , 20 , con.Sy - 20 , 40 , pr.WHITE)


#-------------> Logic Handler
def handle():
    if con.UIInGame:
        draw_game_ui()
    if con.UIInIntro:
        draw_game_intro(con.UIIntroText)
    else:
        pass
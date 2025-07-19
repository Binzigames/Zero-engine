#-------------> importing
import pyray as pr
import DATA.Config as con
import os

#-------------> Fonts
font_title_path = "DATA/Fonts/text.ttf"
font_text_path = "DATA/Fonts/Title.ttf"

font_title = pr.load_font(font_title_path) if os.path.exists(font_title_path) else None
font_text = pr.load_font(font_text_path) if os.path.exists(font_text_path) else None

if font_title is None:
    print("Font title not loaded.")
if font_text is None:
    print("Font text not loaded.")

#-------------> in game ui
def draw_game_ui():
    fps_text = f"{pr.get_fps()} : FPS"
    pr.draw_text_ex(font_text, fps_text, pr.Vector2(20, 20), 20, 2, pr.GREEN)

#>Intro
def draw_game_intro(text):
    pr.draw_text_ex(font_title, "welcome", pr.Vector2(20, 20), 40, 2, pr.WHITE)
    pr.draw_text_ex(font_text, f"about : {text}", pr.Vector2(20, 70), 20, 2, pr.WHITE)
    pr.draw_text_ex(font_text, "wait a few seconds...", pr.Vector2(20, con.Sy - 50), 20, 2, pr.WHITE)

#-------------> Logic Handler
def handle():
    if con.UIInGame:
        draw_game_ui()
    if con.UIInIntro:
        draw_game_intro(con.UIIntroText)

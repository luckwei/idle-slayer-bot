#IMPORTS: 3rd party
import win32api, win32con
from pyautogui import pixel

#IMPORTS: Built-in
from itertools import repeat
from time import sleep

#IMPORTS: Local
from helper.mouse import click, click_iter, slide, scroll
from helper.screen import detect_screen
from helper.keyboard import type
from helper.coords import coords, coords_iter_from_names

def craft_rage(screen):
    """
    Quickly craft and use the rage pill
    """
    initial_pos = win32api.GetCursorPos()

    click_iter(coords_iter_from_names(screen, [
        ("craft_button", 0.2), ("temporary_craft", 0.1),
        ("down_scroll", 0.05), ("down_scroll", 0.05),
        ("craft_rage_pill", 0.01), ("rage_button", 0.01)
    ]))

    win32api.SetCursorPos(initial_pos)


## TO DO: NULL CONDITIONS NEED IMPROVEMENTS
def claim_divinities(screen):
    """
    Claims points and sends minions on trips when ready
    """
    #NULL CONDITION: Souls outline is absent
    if pixel(*coords[screen]["souls_outline"]) not in [(34, 29, 93), (4, 4, 11), (29, 67, 93), (4, 8, 11)]:
        return

    ascension_before = pixel(*coords[screen]["ascension_tab"]) #sample ascension
    
    #NULL CONDITION: menu is out (white close button is present)
    if pixel(*coords[screen]["close_ascension"]) == (255, 255, 255):
        return

    sleep(0.05)
    ascension_after = pixel(*coords[screen]["ascension_tab"]) #sample ascension again

    #NULL CONDITION: ascension tab is not blinking
    if ascension_before == ascension_after:
        return

    initial_pos = win32api.GetCursorPos()

    click_iter(coords_iter_from_names(screen, [
        ("ascension_tab", 0.2), ("skilltree_tab", 0.1)
    ]))

    minions_before = pixel(*coords[screen]["minions_tab"]) #sample minion
    sleep(0.1)
    minions_after = pixel(*coords[screen]["minions_tab"]) #sample minion again

    #NULL CONDITION: minions tab is not blinking
    if minions_before == minions_after:
        click(coords[screen]["close_ascension"])
        return
    
    click(coords[screen]["minions_tab"], 0.1)

    #CHECK if daily activated
    if pixel(*coords[screen]["daily"]) == (255, 255, 255):
        send_minions = "send_minions2"
    else:
        send_minions = "send_minions"
    
    click_iter(coords_iter_from_names(screen, [
        (send_minions, 0.1), (send_minions, 0.1),
        ("close_ascension", 0.2)
    ]))

    win32api.SetCursorPos(initial_pos)


def special_stage_start(screen, sleeptime=None):

    #NULL CONDITION: Souls outline is present
    if pixel(*coords[screen]["souls_outline"]) in [(34, 29, 93), (4, 4, 11), (29, 67, 93), (4, 8, 11)]:
        return

    b_before = pixel(*coords[screen]["B"]) #sample title

    #NULL CONDITION: Pixel where title usually is, is not bright
    if b_before[1] < 250:
        return
    
    sleep(0.05)
    b_after = pixel(*coords[screen]["B"]) #sample title again

    #NULL CONDITION: Pixel was bright but not a static start run screen
    if b_before != b_after:
        return

    print("BLOCKED : SPECIAL STAGE DETECTED")
    
    match screen:
        case "side":
            x_left = -818
            x_right = -455
            y_up = 900
            y_down = 920

        case "large":
            x_left = 687
            x_right = 1232
            y_up = 825
            y_down = 875

        case _:
            return

    initial_pos = win32api.GetCursorPos()
    
    for y_i in (y_up, y_down):
        slide((x_left, y_i), (x_right, y_i), sleeptime)
        slide((x_right, y_i), (x_left, y_i), sleeptime)

    win32api.SetCursorPos(initial_pos)


def special_stage_close(screen, sleeptime=None):
    #NULL CONDITION: Souls outline is present
    if pixel(*coords[screen]["souls_outline"]) in [(34, 29, 93), (4, 4, 11), (29, 67, 93), (4, 8, 11)]:
        return

    close_run_before = pixel(*coords[screen]["close_run"]) #sample close run

    #NULL CONDITION: Pixel where close run button usually is, is not bright
    if close_run_before[1] < 250:
        return
    
    sleep(0.05)
    close_run_after = pixel(*coords[screen]["close_run"]) #sample close run again

    #NULL CONDITION: Pixel was bright but not a static close run screen
    if close_run_before != close_run_after:
        return
    
    print("BLOCKED : SPECIAL STAGE TO BE CLOSED")

    initial_pos = win32api.GetCursorPos()

    click(coords[screen]["close_run"], sleeptime)

    win32api.SetCursorPos(initial_pos)


def organise_levels(screen):
    """
    Buys maximum levels in 50s for all equipment except most expensive
    """

    initial_pos = win32api.GetCursorPos()

    if pixel(*coords[screen]["shop_button"])[2] > 50:
        click(coords[screen]["shop_button"], 0.3)

    click_iter(coords_iter_from_names(screen, [
        ("weapon_button", 0.2), ("fifty_button", 0.2), 
        ("bottom_scroll_button", 0.1), ("bottom_scroll_button", 0.1)
    ]))

    match screen:
        case "side":
            x_pos = -51
            Y = (912, 821, 724, 633, 533)

        case "large":
            x_pos = 1840
            Y = (830, 685, 540, 395, 255)

    def buy_page(x_pos, Y):
        while True:
            green_buys = [(x_pos, y_pos) for y_pos in Y if pixel(x_pos, y_pos)[1] > 100]

            if len(green_buys) == 0:
                return
            
            for green_buy in green_buys:
                click(green_buy, 0.01)
    
    buy_page(x_pos, Y[1:])

    scroll(coords[screen]["bottom_scroll_button"], "up", 10)
    buy_page(x_pos, Y)

    scroll(coords[screen]["bottom_scroll_button"], "up", 10)
    buy_page(x_pos, Y)

    click_iter(coords_iter_from_names(screen, [
        ("bottom_scroll_button", 0.1), ("bottom_scroll_button", 0.1),
        ("max_button", 0.3), ("upgrade_button", 0.01), ("upgrade_button", 0.01)
    ]))

    win32api.SetCursorPos(initial_pos)

def beat_stage_2():
    #side
    #(-802, 1036) should be (16, 30, 41)
    pass

def chest_hunt(screen):
    #NULL CONDITION: Souls outline is present
    if pixel(*coords[screen]["souls_outline"]) in [(34, 29, 93), (4, 4, 11), (29, 67, 93), (4, 8, 11)]:
        return

    match screen:
        case "side":
            X = [-1102, -1005, -912, -816, -721, -627, -529, -435, -341, -245]
            Y = [647, 742, 836]
        case "large":
            X = [271, 413, 554, 697, 839, 982, 1125, 1267, 1410, 1553]
            Y = [431, 579, 716]

    completed = (88, 58, 12)
    unopened_chests = [(x, y) for x in X for y in Y if pixel(x, y) != completed]

    if len(unopened_chests) == 0:
        return

    for chest in unopened_chests:
        if pixel(*coords[screen]["close_chest_hunt"]) == (255, 255, 255):
            click(coords[screen]["close_chest_hunt"])
            break
        click(chest, 1)

    
    
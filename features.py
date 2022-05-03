#IMPORTS: 3rd party
import win32api, win32con
from pyautogui import pixel

#IMPORTS: Built-in
from time import sleep

#IMPORTS: Local
from devices.mouse import click, click_iter, slide
from devices.screen import detect_screen
from devices.keyboard import type
from gameplay.coords import coords, coords_iter_from_names

def craft_rage(screen):
    """
    Quickly craft and use the rage pill
    """
    click_iter(coords_iter_from_names(screen, [
        ("craft_button", 0.2), ("temporary_craft", 0.1),
        ("down_scroll", 0.05), ("down_scroll", 0.1),
        ("craft_rage_pill", 0.1), ("rage_button", 0.1)
    ]))

def claim_divinities(screen):
    """
    Claims points and sends minions on trips when ready
    """
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
        click(coords[screen]["close_tab"])
        return
    
    click(coords[screen]["minions_tab"], 0.1)

    #CHECK if daily activated
    if pixel(*coords[screen]["daily"]) == (255, 255, 255):
        send_minions = "send_minions2"
    else:
        send_minions = "send_minions"
    
    click_iter(coords_iter_from_names(screen, [
        (send_minions, 0.1, 2), ("close_tab", 0.2)
    ]))

    win32api.SetCursorPos(initial_pos)


def special_stage_start(screen, sleeptime=None):
    b_before = pixel(*coords[screen]["B"]) #sample title

    #NULL CONDITION: Pixel where title usually is, is not bright
    if b_before[1] < 250:
        return
    
    sleep(0.05)
    b_after = pixel(*coords[screen]["B"]) #sample title again

    #NULL CONDITION: Pixel was bright but not a static start run screen
    if b_before != b_after:
        return

    # #NULL CONDITION:
    # if pixel(*coords[screen]["divinities"]) == (255, 255, 255):
    #     return       

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
        slide((x_left, y_i), (x_right, y_i), sleeptime)

    win32api.SetCursorPos(initial_pos)


def special_stage_close(screen, sleeptime=None):
    close_run_before = pixel(*coords[screen]["close_run"]) #sample close run

    #NULL CONDITION: Pixel where close run button usually is, is not bright
    if close_run_before[1] < 250:
        return
    
    sleep(0.05)
    close_run_after = pixel(*coords[screen]["close_run"]) #sample close run again

    #NULL CONDITION: Pixel was bright but not a static close run screen
    if close_run_before != close_run_after:
        return

    # #NULL CONDITION: ?
    # if pixel(*coords[screen]["man"]) == (255, 255, 255):
    #     return
    
    print("closable")

    initial_pos = win32api.GetCursorPos()

    click(coords[screen]["close_run"], sleeptime)

    win32api.SetCursorPos(initial_pos)
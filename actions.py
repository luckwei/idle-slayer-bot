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

def dash(screen, sleeptime=None):
    """
    Dash if button is ready, based on color comparison
    """
    #NULL CONDITION: Last part of dash button is different to complete dash button
    if pixel(*coords[screen]["dash_end"]) != pixel(*coords[screen]["dash_button"]):
        return

    type("d")

    if sleeptime:
        sleep(sleeptime)

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

def shortjump(sleeptime=None):
    """
    Jumps/shoots arrow
    """
    type("w")

    if sleeptime:
        sleep(sleeptime)
    






    
#IMPORTS: 3rd party
import win32api, win32con
from pyautogui import pixel

#IMPORTS: Built-in
from time import sleep

#IMPORTS: Local
from devices.mouse import click, click_iter, slide
from devices.screen import detect_screen
from devices.keyboard import key_code
from gameplay.coords import coords, coords_iter_from_names

def craft_rage(screen):
    """
    Quickly craft and use the rage pill
    """
    names_iter = (
        ("craft_button", 0.2),
        ("temporary_craft", 0.1),
        ("down_scroll", 0.05),
        ("down_scroll", 0.1),
        ("craft_rage_pill", 0.1),
        ("rage_button", 0.1)
    )

    click_iter(coords_iter_from_names(screen, names_iter))

def dash(screen, sleeptime=None):
    """
    Dash if button is ready, based on color comparison
    """

    #NULL CONDITION
    if pixel(*coords[screen]["dash_end"]) in ((4, 22, 48), (4, 23, 50)):
        return

    win32api.keybd_event(key_code["d"], 0, 0, 0)
    win32api.keybd_event(key_code["d"], 0, win32con.KEYEVENTF_KEYUP, 0)

    if sleeptime:
        sleep(sleeptime)

def claim_divinities(screen):
    """
    Claims points and sends minions on trips when ready
    """
    ascension_before = pixel(*coords[screen]["ascension_tab"])
    sleep(0.1)
    ascension_after = pixel(*coords[screen]["ascension_tab"])

    #NULL CONDITION
    if ascension_before == ascension_after or pixel(*coords[screen]["close_ascension"]) == (255, 255, 255):
        return
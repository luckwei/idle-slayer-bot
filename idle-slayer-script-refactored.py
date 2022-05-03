import keyboard as kb
import mouse as ms
from pynput import keyboard
from pynput import mouse
from pynput.keyboard import Key
from pynput.mouse import Button
from time import sleep
import win32gui, win32ui, win32con, win32api
from win32gui import GetWindowText, GetForegroundWindow
import time
from pyautogui import pixel
import pyautogui
from itertools import chain
import screeninfo

## DIAGNOSTICS

def initiate_cursor_typer():
    cursor = mouse.Controller()
    typer = keyboard.Controller()
    return cursor, typer

def detect_screen():
    screen_width = win32api.GetSystemMetrics(78)
    if screen_width == 3200:
        return "side"
    elif screen_width in (1920, 1536):
        return "large"
    else:
        #unknown monitor
        print(f"MONITOR NOT RECOGNISED, INFO: {screen_width}")
        return "unknown"

def click(xy, sleeptime=None, button="left"):
    if win32api.GetCursorPos() != xy:
        win32api.SetCursorPos(xy)
        sleep(0.01)
    
    match button:
        case "left":
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        case "middle":
            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN,0,0)
            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP,0,0)

    if sleeptime:
        sleep(sleeptime)

def click_iter(xy_iter):
    for xy, sleeptime in xy_iter:
        click(xy, sleeptime)

def slide(start, end, sleeptime=None):
    if win32api.GetCursorPos() != start:
        win32api.SetCursorPos(start)
        sleep(0.01)
        
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.03)

    win32api.SetCursorPos(end)
    sleep(0.03)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    if sleeptime:
        sleep(sleeptime)

## GAMEPLAY
coords = {
    "side": {
        #craft_rage
        "craft_button": (-1109, 425),
        "temporary_craft": (-1020, 1020),
        "down_scroll": (-804, 928),
        "craft_rage_pill": (-881, 668),
        "rage_button": (-185, 450),
        "exit_menu": (-831, 1013),

        #dash
        "dash_end": (-1171, 935),

        #claim divinities
        "ascension_tab": (-1188, 445),
        "close_ascension": (-688, 1009),
        "minions_tab": (-928, 1006),
        "skilltree_tab": (-1043, 1006),
        "send_minions": (-973, 505),
        "daily": (-1197, 635),
        "send_minions2": (-1185, 752)
    },
    "large": {
        #craft_rage
        "craft_button": (256, 104),
        "temporary_craft": (390, 997),
        "down_scroll": (715, 860),
        "craft_rage_pill": (600, 453),
        "rage_button": (1644, 177),
        "exit_menu": (660, 995),

        #dash
        "dash_end": (167, 862),

        #claim divinities
        "ascension_tab": (134, 132),
        "close_ascension": (884, 985),
        "minions_tab": (524, 973),
        "skilltree_tab": (355, 975),
        "send_minions": (486, 228),
        "daily": (488, 211),
        "send_minions2": (485, 359)
    }
}

key_code = {
    "d": 0x44
}


def coords_iter_from_names(screen, names_iter):
    return [(coords[screen][name], sleeptime) for name, sleeptime in names_iter]

def craft_rage(screen):
    names_iter = (
        ("craft_button", 0.2),
        ("temporary_craft", 0.1),
        ("down_scroll", 0.05),
        ("down_scroll", 0.1),
        ("craft_rage_pill", 0.1),
        ("rage_button", 0.1),
    )
    click_iter(coords_iter_from_names(screen, names_iter))

def dash(screen, sleeptime=None):
    if pixel(*coords[screen]["dash_end"]) in ((4, 22, 48), (4, 23, 50)):
        return
    win32api.keybd_event(key_code["d"], 0, 0, 0)
    win32api.keybd_event(key_code["d"], 0, win32con.KEYEVENTF_KEYUP, 0)

    if sleeptime:
        sleep(sleeptime)

def claim_divinities(screen):
    ascension_before = pixel(*coords[screen]["ascension_tab"])
    sleep(0.1)
    ascension_after = pixel(*coords[screen]["ascension_tab"])

    if ascension_before == ascension_after or pixel(*coords[screen]["close_ascension"]) == (255, 255, 255):
        return

    
    
    
    
    
if __name__ == "__main__":
    cursor, typer = initiate_cursor_typer()
    

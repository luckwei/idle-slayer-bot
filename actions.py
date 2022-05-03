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

def shortjump(sleeptime=None):
    """
    Jumps/shoots arrow
    """
    type("w")

    if sleeptime:
        sleep(sleeptime)
    






    
#IMPORTS: 3rd party
import win32api, win32con
from pyautogui import pixel

#IMPORTS: Built-in
from time import sleep

#IMPORTS: Local
from devices.mouse import click, click_iter, slide
from devices.screen import detect_screen
from devices.keyboard import type
from devices.coords import coords, coords_iter_from_names

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

def rage(screen, sleeptime=None):
    """
    Activate rage uf ready
    """

    #NULL CONDITION: rage button is not red enough
    if pixel(*coords[screen]["rage_button"])[0] < 55:
        return

    initial_pos = win32api.GetCursorPos()

    #Check if side, if so mouse should be on the left
    if screen == "side" and initial_pos[0] >= 0:

        somewhere_on_side = (-10, 1078)

        click(somewhere_on_side, button="middle")

        win32api.SetCursorPos(initial_pos)

    else:
        click(initial_pos, button="middle")

    if sleeptime:
        sleep(sleeptime)

def activate_silver_boxes(screen, sleeptime=None):
    """
    Activate silver boxes when available
    """

    #NULL CONDITION: activate button is not white
    if pixel(*coords[screen]["activate_boxes"]) != (255, 255, 255):
        return

    initial_pos = win32api.GetCursorPos()

    click(coords[screen]["activate_boxes"], sleeptime)

    win32api.SetCursorPos(initial_pos)
# IMPORTS: 3rd party
import win32api, win32con

# IMPORTS: Built-in
from itertools import repeat
from time import sleep


def click(xy, sleeptime=0.01, button="left"):
    """
    click on an xy coord tuple
    """
    if win32api.GetCursorPos() != xy:
        win32api.SetCursorPos(xy)
        sleep(0.01)

    match button:
        case "left":
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            sleep(0.01)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        case "middle":
            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN, 0, 0)
            sleep(0.01)
            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP, 0, 0)

    sleep(sleeptime)


def click_iter(xy_iter):
    """
    clicks on xy coords in an iterable
    """
    for xy in xy_iter:
        click(*xy)


def slide(start, end, sleeptime=0.01):
    """
    Slides down from one coordinate to another
    """
    if win32api.GetCursorPos() != start:
        win32api.SetCursorPos(start)
        sleep(0.01)

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.03)
    win32api.SetCursorPos(end)
    sleep(0.01)

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    sleep(sleeptime)


def scroll(xy, direction="up", n=1):
    """
    Scrolls at xy coord n number of times in given direction
    """
    direction = 1 if direction == "up" else -1
    x, y = xy

    for _ in repeat(None, n):
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, x, y, direction, 0)
        sleep(0.01)

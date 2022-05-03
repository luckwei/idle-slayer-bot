#IMPORTS: 3rd party
import win32api, win32con

#IMPORTS: Built-in
from itertools import repeat
from time import sleep

#IMPORTS: Local
#from coords import coords

def click(xy, sleeptime=None, n=1, button="left"):
    """
    click on an xy coord tuple
    """
    if win32api.GetCursorPos() != xy:
        win32api.SetCursorPos(xy)
        sleep(0.01)
    
    #Click n times
    for _ in repeat(None, n):
        match button:
            case "left":
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                sleep(0.01)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            case "middle":
                win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN,0,0)
                sleep(0.01)
                win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP,0,0)

    if sleeptime:
        sleep(sleeptime)

def click_iter(xy_iter):
    """
    clicks on xy coords in an iterable
    """
    for xy in xy_iter:
        click(*xy)

# def coords_iter_from_names(screen, names_iter):
#     return [(coords[screen][name], sleeptime) for name, sleeptime in names_iter]

# def click_names(screen, names_iter):
#     """
#     clicks on xy coords given names
#     """
#     for name_tuple in names_iter:
#         if len(name) == 3:
#             name, sleeptime, n = name_tuple
#             xy = coords[screen][name]
#             click(xy, sleeptime, n)
#         elif len(name) == 2:
#             name, sleeptime = name_tuple
#             xy = coords[screen][name]
#             click(xy, sleeptime)
#         else:
#             xy = coords[screen][name]
#             click(xy)
        

def slide(start, end, sleeptime=None):
    """
    Slides down from one coordinate to another
    """
    if win32api.GetCursorPos() != start:
        win32api.SetCursorPos(start)
        sleep(0.01)
        
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.03)
    win32api.SetCursorPos(end)
    sleep(0.01)

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    if sleeptime:
        sleep(sleeptime)
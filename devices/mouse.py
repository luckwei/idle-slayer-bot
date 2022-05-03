from time import sleep
import win32api, win32con

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
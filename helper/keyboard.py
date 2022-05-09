# IMPORTS: 3rd party
import win32api, win32con

# IMPORTS: Built-in
from time import sleep

key_code = {"d": 0x44, "w": 0x57}


def type(key, sleeptime=0.01):
    """
    press on given key
    """

    win32api.keybd_event(key_code[key], 0, 0, 0)
    sleep(0.01)
    win32api.keybd_event(key_code[key], 0, win32con.KEYEVENTF_KEYUP, 0)

    sleep(sleeptime)

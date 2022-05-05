#IMPORTS: 3rd party
import win32api, win32ui, win32gui
import subprocess

def detect_screen():
    """
    Categorise screen based on combined virtual width of monitor(s)
    """

    screen_width = win32api.GetSystemMetrics(78) #Width of virtual screen

    #My dual monitor setup: 1280x720* | 1920x1080
    if screen_width == 3200:
        return "side"
    
    #My single monitor setups: 1920x1080* or 1536x864*
    elif screen_width == 1920 or screen_width == 1536:
        return "large"

    #Unknown monitor
    print(f"MONITOR NOT RECOGNISED, INFO: {screen_width}")
    return "unknown"

def run_idle_slayer():
    window_name = "Idle Slayer"

    try:
        hwnd = win32gui.FindWindow(None, window_name)
        win32ui.CreateWindowFromHandle(hwnd)
        return True
    
    except win32ui.error:
        subprocess.run("start steam://rungameid/1353300", shell=True)
        return False

def close_idle_slayer():
    window_name = "Idle Slayer"

    try:
        hwnd = win32gui.FindWindow(None, window_name)
        win32ui.CreateWindowFromHandle(hwnd)

        subprocess.run('taskkill/im "Idle Slayer.exe"', shell=True)
        print("IDLE SLAYER CLOSED")
    
    except win32ui.error:
        return False
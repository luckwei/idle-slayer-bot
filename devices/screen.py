#IMPORTS: 3rd party
import win32api

def detect_screen():
    """
    Categorise screen based on combined virtual width of monitor(s)
    """

    screen_width = win32api.GetSystemMetrics(78) #width of virtual screen

    #my dual monitor setup: 1280x720* | 1920x1080
    if screen_width == 3200:
        return "side"
    
    #my single monitor setups: 1920x1080* or 1536x864*
    elif screen_width == 1920 or screen_width == 1536:
        return "large"

    #unknown monitor
    print(f"MONITOR NOT RECOGNISED, INFO: {screen_width}")
    return "unknown"
#IMPORTS: 3rd party
import win32api

def detect_screen():
    screen_width = win32api.GetSystemMetrics(78)
    if screen_width == 3200:
        return "side" #1280x720* | 1920x1080
    elif screen_width in (1920, 1536):
        return "large" #1920x1080*
    else:
        #unknown monitor
        print(f"MONITOR NOT RECOGNISED, INFO: {screen_width}")
        return "unknown"
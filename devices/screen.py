import win32api

#side: 1280x720* | 1920x1080
#large: 1920x1080*

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
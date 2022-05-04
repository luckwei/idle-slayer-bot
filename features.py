#IMPORTS: 3rd party
import win32api, win32con
from pyautogui import pixel

#IMPORTS: Built-in
from itertools import repeat
from time import sleep
import keyboard as kb

#IMPORTS: Local
from helper.mouse import click, click_iter, slide, scroll
from helper.coords import coords_iter_from_names
from helper import COORDS

def craft_rage(screen):
    """
    Quickly craft and use the rage pill
    """
    initial_pos = win32api.GetCursorPos()

    click_iter(coords_iter_from_names(screen, [
        ("craft_button", 0.2), ("temporary_craft", 0.1),
        ("down_scroll", 0.05), ("down_scroll", 0.05),
        ("craft_rage_pill", 0.05), ("rage_button", 0.05)
    ]))

    win32api.SetCursorPos(initial_pos)


## TO DO: NULL CONDITIONS NEED IMPROVEMENTS
def claim_divinities(screen):
    """
    Claims points and sends minions on trips when ready
    """
    #NULL CONDITION: Souls outline is absent
    if pixel(*COORDS[screen]["souls_outline"]) not in [(34, 29, 93), (4, 4, 11), (29, 67, 93), (4, 8, 11)]:
        return

    ascension_before = pixel(*COORDS[screen]["ascension_tab"]) #sample ascension
    
    #NULL CONDITION: menu is out (white close button is present)
    if pixel(*COORDS[screen]["close_ascension"]) == (255, 255, 255):
        return

    sleep(0.05)
    ascension_after = pixel(*COORDS[screen]["ascension_tab"]) #sample ascension again

    #NULL CONDITION: ascension tab is not blinking
    if ascension_before == ascension_after:
        return

    initial_pos = win32api.GetCursorPos()

    click_iter(coords_iter_from_names(screen, [
        ("ascension_tab", 0.2), ("skilltree_tab", 0.1)
    ]))

    minions_before = pixel(*COORDS[screen]["minions_tab"]) #sample minion
    sleep(0.1)
    minions_after = pixel(*COORDS[screen]["minions_tab"]) #sample minion again

    #NULL CONDITION: minions tab is not blinking
    if minions_before == minions_after:
        click(COORDS[screen]["close_ascension"])
        return
    
    click(COORDS[screen]["minions_tab"], 0.1)

    #CHECK if daily activated
    if pixel(*COORDS[screen]["daily"]) == (255, 255, 255):
        send_minions = "send_minions2"
    else:
        send_minions = "send_minions"
    
    click_iter(coords_iter_from_names(screen, [
        (send_minions, 0.1), (send_minions, 0.1),
        ("close_ascension", 0.2)
    ]))

    win32api.SetCursorPos(initial_pos)


def special_stage_start(screen, sleeptime=None):

    #NULL CONDITION: Souls outline is present
    if pixel(*COORDS[screen]["souls_outline"]) in [(34, 29, 93), (4, 4, 11), (29, 67, 93), (4, 8, 11)]:
        return

    b_before = pixel(*COORDS[screen]["B"]) #sample title

    #NULL CONDITION: Pixel where title usually is, is not bright
    if b_before[1] < 250:
        return
    
    sleep(0.05)
    b_after = pixel(*COORDS[screen]["B"]) #sample title again

    #NULL CONDITION: Pixel was bright but not a static start run screen
    if b_before != b_after:
        return

    print("BLOCKED : SPECIAL STAGE DETECTED")
    
    match screen:
        case "side":
            x_left = -818
            x_right = -455
            y_up = 900
            y_down = 920

        case "large":
            x_left = 687
            x_right = 1232
            y_up = 825
            y_down = 875

        case _:
            return

    initial_pos = win32api.GetCursorPos()
    
    for y_i in (y_up, y_down):
        slide((x_left, y_i), (x_right, y_i), sleeptime)
        slide((x_right, y_i), (x_left, y_i), sleeptime)

    win32api.SetCursorPos(initial_pos)


def special_stage_close(screen, sleeptime=None):
    #NULL CONDITION: Souls outline is present
    if pixel(*COORDS[screen]["souls_outline"]) in [(34, 29, 93), (4, 4, 11), (29, 67, 93), (4, 8, 11)]:
        return

    close_run_before = pixel(*COORDS[screen]["close_run"]) #sample close run

    #NULL CONDITION: Pixel where close run button usually is, is not bright
    if close_run_before[1] < 250:
        return
    
    sleep(0.05)
    close_run_after = pixel(*COORDS[screen]["close_run"]) #sample close run again

    #NULL CONDITION: Pixel was bright but not a static close run screen
    if close_run_before != close_run_after:
        return
    
    print("BLOCKED : SPECIAL STAGE TO BE CLOSED")

    initial_pos = win32api.GetCursorPos()

    click(COORDS[screen]["close_run"], sleeptime)

    win32api.SetCursorPos(initial_pos)


def organise_levels(screen):
    """
    Buys maximum levels in 50s for all equipment except most expensive
    """

    initial_pos = win32api.GetCursorPos()

    if pixel(*COORDS[screen]["shop_button"])[2] > 50:
        click(COORDS[screen]["shop_button"], 0.3)

    click_iter(coords_iter_from_names(screen, [
        ("weapon_button", 0.2), ("fifty_button", 0.2), 
        ("bottom_scroll_button", 0.1), ("bottom_scroll_button", 0.1)
    ]))

    match screen:
        case "side":
            x_pos = -51
            Y = (912, 821, 724, 633, 533)

        case "large":
            x_pos = 1840
            Y = (830, 685, 540, 395, 255)

    def buy_page(x_pos, Y):
        while True:
            green_buys = [(x_pos, y_pos) for y_pos in Y if pixel(x_pos, y_pos)[1] > 100]

            if len(green_buys) == 0:
                return
            
            for green_buy in green_buys:
                click(green_buy, 0.01)
    
    buy_page(x_pos, Y[1:])

    scroll(COORDS[screen]["bottom_scroll_button"], "up", 11)
    buy_page(x_pos, Y)

    scroll(COORDS[screen]["bottom_scroll_button"], "up", 11)
    buy_page(x_pos, Y)

    click_iter(coords_iter_from_names(screen, [
        ("bottom_scroll_button", 0.1), ("bottom_scroll_button", 0.1),
        ("max_button", 0.3), ("upgrade_button", 0.01), ("upgrade_button", 0.01)
    ]))

    win32api.SetCursorPos(initial_pos)

def beat_stage_2():
    #side
    #(-802, 1036) should be (16, 30, 41)
    pass

def chest_hunt(screen):
    """
    Clicks the chest during a chest hunt, 3rd chest being the saver
    """
    #NULL CONDITION: Souls outline is present
    if pixel(*COORDS[screen]["souls_outline"]) in [(34, 29, 93), (4, 4, 11), (29, 67, 93), (4, 8, 11)]:
        return

    #NULL CONDITION: TOP BANNER DOES NOT INDICATE SPECIAL CHEST EVENT
    if pixel(*COORDS[screen]["top_banner"]) not in ((221, 215, 204), (220, 214, 204)):
        return


    match screen:
        case "side":
            X = [-1102, -1005, -912, -815, -721, -627, -529, -435, -341, -245]
            Y = [647, 742, 836]
        case "large":
            X = [271, 413, 554, 697, 839, 982, 1125, 1267, 1410, 1553]
            Y = [431, 579, 716]

    chest_status_dict = {
        (255, 235, 4): "saver",
        (34, 28, 17): "missing",
        (33, 27, 17): "missing",
        (64, 44, 7): "missing",
        (59, 40, 7): "missing",
        (88, 58, 12): "open",
        (92, 60, 13): "open",
        (255, 187, 49): "closed",
        (245, 280, 47): "closed"

    }

    def get_status(identifier):
        if len(identifier) == 3:
            color = identifier
        else:
            color = pixel(*identifier)
        
        if color in chest_status_dict:
            return chest_status_dict[color]
        return "unknown"

    def sample_chests():
        chest_positions = [(x, y) for y in Y for x in X]
        chest_status = [get_status(chest) for chest in chest_positions]

        saver_index = chest_status.index("saver")

        saver_pos = chest_positions.pop(saver_index)

        chest_status.pop(saver_index)

        return saver_pos, zip(chest_positions, chest_status)

    sleep(2) #add timeout

    try:
        saver_pos, chest_info = sample_chests()
    except ValueError:
        print("too fast: Chest not out yet")
        return

    initial_pos = win32api.GetCursorPos()

    chest_opened = 0

    for pos, status in chest_info:
        
        if status != "closed":
            continue
        click(pos, 1)
        while get_status(pos) in ("closed", "unknown") and kb.is_pressed("q") is False:
            if pixel(*COORDS[screen]["close_chest_hunt"]) == (255, 255, 255):
                click(COORDS[screen]["close_chest_hunt"])
                print("END OF CHEST HUNT")
                win32api.SetCursorPos(initial_pos)
                return
            click(pos, 0.5)
        chest_opened += 1
        if chest_opened == 2:
            click(saver_pos, 1)
    if pixel(*COORDS[screen]["close_chest_hunt"]) == (255, 255, 255):
        click(COORDS[screen]["close_chest_hunt"])
        print("END OF CHEST HUNT")
        win32api.SetCursorPos(initial_pos)
    
    
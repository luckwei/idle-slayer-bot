import keyboard as kb
import mouse as ms
from pynput import keyboard
from pynput import mouse
from pynput.keyboard import Key
from pynput.mouse import Button
from time import sleep
import win32gui, win32ui, win32con, win32api
from win32gui import GetWindowText, GetForegroundWindow
import time
import pyautogui
from itertools import chain
import subprocess
import itertools
import playsound

cursor = mouse.Controller()
typer = keyboard.Controller()

print('Hi! Program starting..')

def run_idle_slayer():
    window_name = "Idle Slayer"

    try:
        hwnd = win32gui.FindWindow(None, "Idle Slayer")
        win = win32ui.CreateWindowFromHandle(hwnd)
        return True
    
    except win32ui.error:
        subprocess.run("start steam://rungameid/1353300", shell=True)
        return False

def detect_screen():
    import screeninfo

    if len(screeninfo.get_monitors()) == 2:
        return "side"
    elif screeninfo.get_monitors()[0].width == 1920:
        return "large"        
    elif screeninfo.get_monitors()[0].width == 1536:
        return "large"

    print(screeninfo.get_monitors())
    return "unknown"

def craft_rage(screen):
    match screen:
        case "side":
            craft_button = (-1109, 425)
            temporary_craft = (-1020, 1020)
            down_scroll = (-807, 954)
            craft_rage_pill = (-881, 668)
            rage_button = (-185, 450)
            exit_menu = (-831, 1013)
        case "large":
            craft_button = (256, 104)
            temporary_craft = (390, 997)
            down_scroll = (718, 907)
            craft_rage_pill = (600, 453)
            rage_button = (1642, 129)
            exit_menu = (660, 995)
        case _:
            return

    initial_pos = cursor.position
    click(craft_button, 0.2)
    click(temporary_craft, 0.1)
    click(down_scroll, 0.05)
    click(down_scroll, 0.1)
    click(craft_rage_pill, 0.1)
    click(rage_button, 0.1)
    #click(exit_menu, 0.01)
    cursor.position = initial_pos
    
    

def dash(screen, sleeptime=None):
    match screen:
        case "side":
            dash_end = (-1171, 935)
            dash_button = (-1160, 935)
        case "large":
            dash_end = (167, 862)
            dash_button = (177, 871)
            
        case "small":
            dash_end = (134, 689)
            dash_button = (147, 696)
            
    if pyautogui.pixel(*dash_end) != pyautogui.pixel(*dash_button):
        return
            
    typer.press("d")
    typer.release("d")

    if sleeptime:
        sleep(sleeptime)


def claim_divinities(screen):
    match screen:
        case "side":
            ascension_tab = (-1188, 445)
            minions_tab = (-928, 1006)
            skilltree_tab = (-1043, 1006)
            close_tab = (-688, 1009)
            send_minions = (-973, 505)

            daily = (-1197, 635)
            send_minions2 = (-1185, 752)

            
        case "large":
            ascension_tab = (134, 132)
            minions_tab = (524, 973)
            skilltree_tab = (355, 975)
            close_tab = (884, 985)
            send_minions = (486, 228)

            daily = (488, 211)
            send_minions2 = (485, 359)

    
    first = pyautogui.pixel(*ascension_tab)
    sleep(0.05)
    second = pyautogui.pixel(*ascension_tab)

    if first == second:
        return
    
    if pyautogui.pixel(*ascension_tab)[0] < 100:
        return

    print("claiming")
    click(ascension_tab, 0.2)
    click(skilltree_tab, 0.1)

    sample1 = pyautogui.pixel(*minions_tab)
    sleep(0.3)
    sample2 = pyautogui.pixel(*minions_tab)

    if sample1 == sample2:
        click(close_tab, 0.3)
        return

    

    click(minions_tab, 0.1)

    if pyautogui.pixel(*daily) == (255, 255, 255):
        click(send_minions2, 0.1)
        click(send_minions2, 0.1)
        #click(daily, 0.1)
        click(close_tab, 0.3)
        return

    click(send_minions, 0.1)
    click(send_minions, 0.1)

    click(close_tab, 0.3)
    
    

def shortjump(sleeptime=None):
    typer.press("w")
    typer.release("w")

    if sleeptime:
        sleep(sleeptime)


def rage(screen, sleeptime=None):
    match screen:
        case "side":
            rage_button = (-186, 444)
            
        case "large":
            rage_button = (1641, 127)
    
            
    if pyautogui.pixel(*rage_button)[0] < 55:
        return
    print("RAGE ON")
            

    if screen == "side" and cursor.position[0] >= 0:
        
        initial_pos = cursor.position
        
        win32api.SetCursorPos((-10, 1078))

        sleep(0.02)

        cursor.press(Button.middle)
        sleep(0.01)
        cursor.release(Button.middle)

        sleep(0.02)

        win32api.SetCursorPos((14, 1079))
        
        sleep(0.02)

        win32api.SetCursorPos(initial_pos)

    else:
        cursor.press(Button.middle)
        cursor.release(Button.middle)

    if sleeptime:
        sleep(sleeptime)



def click(x, sleeptime=None):
    
    if x != cursor.position:
        win32api.SetCursorPos(x)
        sleep(0.01)
        
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
    if sleeptime:
        sleep(sleeptime)


def slide(x, y, sleeptime=None):
    
    if x != cursor.position:
        win32api.SetCursorPos(x)
        sleep(0.01)
        
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.03)
    win32api.SetCursorPos(y)
    sleep(0.03)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    if sleeptime:
        sleep(sleeptime)

def slide_screen(screen, sleeptime=None):
    match screen:
        case "side":
            x_s = (-200, -1000)
            y_s = (500, 600, 700)

            B = (-772, 496)
            div = (-1187, 440)
    
        case "large":
            x_s = (450, 1500)
            y_s = (250, 350, 450)

            B = (763, 199)
            div = (140, 102)
    
    if pyautogui.pixel(*B)[0] != 255 or pyautogui.pixel(*div) == (255, 255, 255):
        return       


    print("BLOCKED : SPECIAL STAGE DETECTED")
    
    match screen:
        case "side":
            x = (-818, -455)
            y = (900, 920)

        case "large":
            x = (687, 1232)
            y = (825, 875)

        #redo
        case "small":
            x = (670, 1240)
            y = (809, 865)
            return

    for y_i in y:
        slide((x[0], y_i), (x[1], y_i), sleeptime)
        slide((x[1], y_i), (x[0], y_i), sleeptime)


def close_run(screen, sleeptime=None):
    match screen:
        case "side":
            close_run_button = (-532, 913)
            man = (-644, 598)

        case "large":
            close_run_button = (1123, 833)
            man = (959, 371)

    if pyautogui.pixel(*close_run_button)[0] != 255 or pyautogui.pixel(*man) == (255, 255, 255):
        return
    print("closable")

    start = cursor.position

    click(close_run_button, sleeptime)

    win32api.SetCursorPos(start)

    return 
    
        
def activate(screen, sleeptime=None):
    match screen:
        case "side":
            activate_button = (-701, 378)
            
        case "large":
            activate_button = (870, 27)

    if pyautogui.pixel(*activate_button) != (255, 255, 255):
        return

    print("activatable")

    start = cursor.position

    click(activate_button, sleeptime)

    win32api.SetCursorPos(start)


def cancel_menu(screen, sleeptime=None):
    match screen:
        case "side":
            if pyautogui.pixel(-44, 1012)[0] < 160:
                return
            cancel_button = (-40, 1031)
        case "large":
            if pyautogui.pixel(1856, 993)[0] < 160:
                return
            cancel_button = (1856, 993)


    click(cancel_button, sleeptime)
    print("Menu Cancelled")


## WIP
def organise_levels_50(screen):

    def buy_page(x_pos, Y):
        while True:
            green_buys = [(x_pos, y_pos) for y_pos in Y if pyautogui.pixel(x_pos, y_pos)[1] > 100]

            if len(green_buys) == 0:
                print("page cleared")
                return
            
            for green_buy in green_buys:
                click(green_buy, 0.01)

    def buy_page_except_last(x_pos, Y):
        while True:
            green_buys = [(x_pos, y_pos) for y_pos in Y[1:] if pyautogui.pixel(x_pos, y_pos)[1] > 100]

            if len(green_buys) == 0:
                print("page cleared")
                return
            
            for green_buy in green_buys:
                click(green_buy, 0.01)
                click(green_buy, 0.01)

    ini_pos = cursor.position

    match screen:
        
            
        case "side":
            shop_button = (-81, 1011)
            weapon_button = (-421, 1018)
            fifty_button = (-170, 955)
            bottom_scroll_button = (-35, 918)
            max_button = (-83, 955)
            upgrade_button = (-352, 1014)
            
            x_pos = -51
            Y = (912, 821, 724, 633, 533)

        case "large":
            shop_button = (1798, 976)
            weapon_button = (1284, 984)
            fifty_button = (1669, 889)
            bottom_scroll_button = (1864, 848)
            max_button = (1801, 901)
            upgrade_button = (1396, 987)
            
            x_pos = 1840
            Y = (830, 685, 540, 395, 255)
            
        case "small":
            return

    if pyautogui.pixel(*shop_button)[2] > 50:
        print("bringing up shop")
        click(shop_button, 0.4)

    click(weapon_button, 0.2)
    click(fifty_button, 0.2)
    click(bottom_scroll_button, 0.1)
    click(bottom_scroll_button, 0.1)

        
    buy_page_except_last(x_pos, Y)
    
    for _ in range(2):
        

        for _ in range(10):
            cursor.scroll(0, 1)
            sleep(0.01)

        buy_page(x_pos, Y)

    click(bottom_scroll_button, 0.1)
    click(bottom_scroll_button, 0.1)
    click(max_button, 0.3)
    click(upgrade_button, 0.1)
    click(upgrade_button)

    win32api.SetCursorPos(ini_pos)

#KEYBOARD
#def on_press(key):



                    
            
def on_release(key):
    if key == Key.f6:
        
        screen = detect_screen()
        if screen == "unknown":
            return
        
        organise_levels_50(screen)

    if key == Key.f8:
        craft_rage(detect_screen())
        
        
    if key == Key.delete:
        print(f"position is {cursor.position}")
        print(f"pixel is {pyautogui.pixel(*cursor.position)}")

    if key == Key.insert:
             
        
        playsound.playsound("gaming_lock2.wav", block=False)
        if run_idle_slayer() is False:
            playsound.playsound("page_turn2.wav", block=False)
            return

        screen = detect_screen()
        dig_museum = itertools.repeat(0)

        if screen == "unknown":
            return
        elif screen == "side":
            initial_pos = cursor.position
            click((-550, 1077), 0.01)
            win32api.SetCursorPos(initial_pos)
                
        print("STARTING")

        print(f"screen is {screen}")

        interval = 0.10

        while True:

            activate(screen, 0.01)
            claim_divinities(screen)
            slide_screen(screen, 0.03)
            
            close_run(screen, 0.01)
            
            rage(screen)
 
            dash(screen, 0.01)

            if dig_museum.__next__():
                subprocess.call("adb shell input tap 200 250", shell=True)
                print('dig')

            for _ in range(10):

                if kb.is_pressed("f6"):
                    organise_levels_50(screen)

                if kb.is_pressed("f7"):
                    print('DIGGING ON')
                    dig_museum = itertools.cycle([1]+[0]*50)

                if kb.is_pressed("f8"):
                    craft_rage(screen)
                    return
                
                if kb.is_pressed("end") or kb.is_pressed("page_up"):
                    print("--STOPPING--")
                    playsound.playsound("page_turn2.wav", block=False)
                    return

                if ms.is_pressed(button="right"):
                    print("--STOPPING-- : Right mouse button clicked")
                    playsound.playsound("page_turn2.wav", block=False)
                    return

                if GetWindowText(GetForegroundWindow()) != "Idle Slayer":
                    print("--STOPPING-- : Idle Slayer no longer main program")
                    playsound.playsound("page_turn2.wav", block=False)
                    return

                
                shortjump(interval)

    

def main():
    
    run_idle_slayer()
    #keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    keyboard_listener = keyboard.Listener(on_release=on_release)
    keyboard_listener.start()
    #keyboard_listener.join()

main()

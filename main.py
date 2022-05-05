#IMPORTS: 3rd party
import win32api
from win32gui import GetWindowText, GetForegroundWindow
from pyautogui import pixel
from pynput.keyboard import Key
from pynput import keyboard
from playsound import playsound
import keyboard as kb
import mouse as ms

#IMPORTS: Built-in
from itertools import repeat

#IMPORTS: Local
from actions import dash, shortjump, rage, activate_silver_boxes
from features import craft_rage, claim_divinities, special_stage_start, special_stage_close, organise_levels, chest_hunt
from helper.screen import detect_screen, run_idle_slayer, close_idle_slayer
from helper.mouse import click

def on_release(key):
    audio_start = "resources/gaming_lock.wav"
    audio_end = "resources/page_turn.wav"

    if key == Key.f6:
        organise_levels(detect_screen())

    if key == Key.f7:
        chest_hunt(detect_screen())

    if key == Key.f8:
        craft_rage(detect_screen())

    if key == Key.esc and kb.is_pressed("shift"):
        close_idle_slayer()
        playsound(audio_end, block=False)
        return False
        
    if key == Key.delete:
        print(f"position is {win32api.GetCursorPos()}")
        print(f"pixel is {pixel(*win32api.GetCursorPos())}\n")

    if key == Key.insert:
        playsound(audio_start, block=False)
        if run_idle_slayer() is False:
            playsound(audio_end, block=False)
            return

        screen = detect_screen()
        if screen == "side" and GetWindowText(GetForegroundWindow()) != "Idle Slayer":
            initial_pos = win32api.GetCursorPos()
            somewhere_on_side = (-10, 1078)
            click(somewhere_on_side, 0.01)
            win32api.SetCursorPos(initial_pos)
            win32api.SetCursorPos(initial_pos) #second time because of a bug
                
        print("STARTING")

        print(f"screen is {screen}")

        interval = 0.10

        while True:

            activate_silver_boxes(screen, 0.01)
            claim_divinities(screen)
            special_stage_start(screen, 0.03)
            special_stage_close(screen, 0.01)
            chest_hunt(screen)
            
            rage(screen)
            dash(screen)

            for _ in repeat(None, 10):

                if kb.is_pressed("f6"):
                    organise_levels(screen)

                if kb.is_pressed("f8"):
                    craft_rage(screen)
                    return
                
                if kb.is_pressed("end"):
                    print("--STOPPING--")
                    playsound(audio_end, block=False)
                    return

                if ms.is_pressed(button="right"):
                    print("--STOPPING-- : Right mouse button clicked")
                    playsound(audio_end, block=False)
                    return

                if GetWindowText(GetForegroundWindow()) != "Idle Slayer":
                    print("--STOPPING-- : Idle Slayer no longer main program")
                    playsound(audio_end, block=False)
                    return
                
                shortjump(interval)

def main():
    print("PROGRAM STARTING")
    run_idle_slayer()

    keyboard_listener = keyboard.Listener(on_release=on_release)
    keyboard_listener.start()
    keyboard_listener.join()
    
main()
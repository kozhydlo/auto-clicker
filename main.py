import keyboard
import mouse
import time

isClicking = False

def set_Clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print("Клікер OFF")
    else:
        isClicking = True
        print("Клікер ON")

keyboard.add_hotkey('Alt + X', set_Clicker)

while True:
    if isClicking:
        mouse.double_click(button='left')
        time.sleep(0.01)
import time
import pyautogui as pag
import keyboard as kb

def get_target_color():
    print("Press SPACE to capture the tergat color!")
    target_color = ""
    while True:
        if target_color == "":
            if kb.is_pressed('space'):
                x, y = pag.position()
                target_color = pag.pixel(x, y)
                time.sleep(0.5)  # Prevent rapid capturing
                return target_color
            time.sleep(0.05)    
if __name__ == "__main__":
    get_target_color()

import target_finder as find
import pyautogui as pag
import time
import keyboard as kb

def colors_are_close(c1, c2, tolerance=15):
     return sum(abs(a - b) for a, b in zip(c1, c2)) <= tolerance

def shoot(): 
    print("Press ESC to exit.")
    target_color = find.get_target_color()  # Get the target color from the target_finder module

    while True:
        x, y = pag.position()
        if pag.pixel(x,y) == target_color:
            pag.click( )
            print("Target color found! Shooting...")
            time.sleep(0.01)   # Faster clicking

        if kb.is_pressed('esc'): 
            print("Exiting...")
            break
if __name__ == "__main__":
        shoot()
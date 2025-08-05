import target_finder as find
import pyautogui as pag
import time
import keyboard as kb

def shoot():
    print("Press ESC to exit.")
    get_target_color, terget_pos = find.get_target_color()  # Get the target color from the target_finder module
    while True:
        corrupted_color = pag.pixel(*terget_pos)
        if corrupted_color == get_target_color:
            pag.click()
            print("Target color found! Shooting...")
            time.sleep(0.1)     
        if kb.is_pressed('esc'): 
            print("Exiting...")
            break
if __name__ == "__main__":
        shoot()  
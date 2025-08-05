import pyautogui as pag
import keyboard as kb
import time 

def get_color():
    target_color = None

    print("Press SPACE to capture the current pixel color or ESC to exit.")
    while True:
            if kb.is_pressed('space'):
                x, y = pag.position()
                target_color = pag.pixel(x, y)
                print(f"Captured color: {target_color} at position ({x}, {y})")
                time.sleep(0.5)    
            if kb.is_pressed('esc'):
                print("Exiting...")
                time.sleep(0.5) 
                break
    print(f"Final captured color: {target_color}")
 
if __name__ == "__main__": 
    get_color()                     
    
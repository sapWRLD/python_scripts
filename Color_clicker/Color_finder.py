import pyautogui as pag
import keyboard as kb

def get_color():
    while True:
        target_color = ""
        if target_color == "":
            if kb.is_pressed ('esc'):
                print("Exiting...")
                return None
            if kb.is_pressed('space'):
                x, y = pag.position()  # Get the current mouse position 
                target_color = pag.pixel(x, y)
                break  # Get the color at the current position
    return target_color
     

def main(): 
    color = get_color()
    print(f"the current color is {color}")
if __name__ == "__main__":
    main()
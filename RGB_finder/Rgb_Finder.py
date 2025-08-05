import pyautogui as pag
import keyboard as kb
import time

def rgb_to_hex(rgb):
    """Convert RGB tuple to HEX string."""
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def get_color():
    print("Press SPACE to capture the current pixel color or ESC to exit.")
    last_rgb = None
    while True:     
        if kb.is_pressed('space'):
            x, y = pag.position()
            rgb = pag.pixel(x, y)
            print(f"Captured color: {rgb} with HAX {rgb_to_hex(rgb)} at position ({x}, {y})") 
            last_rgb = rgb
            time.sleep(0.5)
            
        if kb.is_pressed('esc'):
            print("Exiting...")
            time.sleep(0.5)
            return last_rgb

if __name__ == "__main__":
    rgb = get_color()
    hex = rgb_to_hex(rgb)
    if rgb:
        print(f"Final captured color: {rgb} with HEX value {hex}")       
    else:
        print("No color captured.")
   
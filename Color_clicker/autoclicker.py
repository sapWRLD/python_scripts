import pyautogui as pag
import Color_finder as find
import time


def click():
    print("Press SPACE to capture the current pixel color or ESC to exit.")
    target_color = find.get_color()  # Replace with your desired RGB color

    while True:
        x, y = pag.position()  # Get the current mouse position
        #print(f"Current position: ({x}, {y})")  # Print the current position for debugging
        if pag.pixel(x, y) == target_color:  # Compare with the target color
            pag.click()  # Click if the pixel color matches
            print(f"Clicked at position: ({x}, {y})")
            time.sleep(0.1)  # Sleep for a short duration to avoid high CPU usagei

if __name__ == "__main__":
    click()
import pyautogui as pag
import keyboard as kb
import time
text = input("Enter the text to spam: ")
print("Press SPACE to start spamming. Press ESC to stop.")

while True:
    if kb.is_pressed('space'):
        print("Spamming started!")
        while not kb.is_pressed('esc'):
            for i in range(100):
                pag.write(text)
                pag.press('enter')
                time.sleep(0.8)
        print("Spamming stopped!")
        break


    time.sleep(0.05)

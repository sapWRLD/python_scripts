import speech_recognition as sr
import pyaudio
import keyboard as kb
import time
import winsound
from datetime import datetime

# Start de spraakherkenner en microfoon
recognizer = sr.Recognizer()
mic = sr.Microphone()

print("Druk op SPATIE om spraakherkenning te starten. Druk op ESC om te stoppen.")

stop_listening = None

# Callback-functie die automatisch wordt aangeroepen wanneer er spraak wordt gedetecteerd
def callback(recognizer, audio):
    try:
        # Herken spraak met behulp van Google en print het
        text = recognizer.recognize_google(audio, language='nl-NL')
        print(f"Je zei: {text}.")

        # Slaat herkende tekst op in een logbestand met tijdstempel
        with open("speech_log.txt", "a", encoding="utf-8") as log_file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
            log_file.write(f"{timestamp} - {text}.\n")
    except sr.UnknownValueError:
        print("Sorry, ik kon de audio niet begrijpen.")
    except sr.RequestError as e:
        print(f"Kan geen resultaat aanvragen; {e}")

# Hoofdlus van het programma
while True: 
    # Start spraakherkenning als op SPATIE wordt gedrukt en er nog niet wordt geluisterd
    if kb.is_pressed('space') and stop_listening is None:
        winsound.Beep(1000, 200)  # Start pieptoon
        print("Spraakherkenning gestart. Druk op ESC om te stoppen.")
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)  # Omgevingsgeluid kalibreren
        # Start de achtergrondherkenning
        

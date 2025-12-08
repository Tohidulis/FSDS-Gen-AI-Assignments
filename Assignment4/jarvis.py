import pyttsx3
import speech_recognition as sr
import logging
import os
import subprocess
import datetime


LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"
os.makedirs(LOG_DIR, exist_ok=True)
log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)
logging.basicConfig(
    filename=log_path,
    format="[ %(asctime)s ] - %(name)s %(levelname)s - %(message)s",
    level=logging.INFO,
)


engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 150)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(txt):
    engine.say(txt)
    engine.runAndWait()

# text = "Hello, How are you? I like to talk with you. Like to take some assistance from you."
# speak(text)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognize.....")
        query = r.recognize_google(audio, language = "en-IN")
        print(f"user said: {query}\n")
    except Exception as e:
        logging.info(e)
        print("Say it again")
        return "none"
    return query



# print(query)

while True:
    query = listen()
    if "your name" in query:
        print(query)
        speak("My name is Tohid")
    elif "exit" in query:
        speak("Thanks for you correct response")
        exit()
    else:
        print("Sorry")


"""
Author: Mariam Diab
Created on 7/27/2022 4:48 PM
"""
import speech_recognition as sp
import pywhatkit
import datetime
import pyttsx3
from AppOpener import run

user = sp.Recognizer()
monica = pyttsx3.init()
voices = monica.getProperty("voices")
monica.setProperty("voice", voices[1].id)


def say(text):
    monica.say(text)
    monica.runAndWait()

def ask_monica():
    try:
        with sp.Microphone() as source:
            voice = user.listen(source)
            command = user.recognize_google(voice)
            command.lower()
    except:
        pass
    return command

def run_monica():
    while (True):
        print("listening...")
        command = ask_monica()
        if "date" in command:
            today = datetime.date.today()
            date = today.strftime("%B %d, %Y")
            say("It is " + date)
        elif "time" in command:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            say("The time is " + time)
        elif "help" in command:
            pywhatkit.sendwhatmsg_instantly("+201*********", "I need help urgently!!!")
            say("SOS has been sent")
        elif "search" in command:
            command = command.replace("search for", "")
            say("searching for " + command)
            pywhatkit.search(command)
        elif "play" in command:
            command = command.replace("play", "")
            say("playing " + command)
            pywhatkit.playonyt(command)
        elif "open" in command:
            command = command.replace("open", "")
            say("opening " + command)
            run(command)
        elif "no" in command:
            say("Goodbye")
            break
        else:
            say("I can not hear you")

        say("Do you want anything else?")

say("Hey! Monica is here for you")
run_monica()



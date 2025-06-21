import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import os
from datetime import datetime
import pyjokes


recognizer = sr.Recognizer()
engine = pyttsx3.init() 

def speak(text):
    engine.say(text)
    engine.runAndWait()

def tell_time():
    now=datetime.now()
    current_time= now.strftime("%I:%M %p")  
    speak(f"the current time is {current_time}")
    print(f"the current time is {current_time}")





def tell_joke():
    joke=pyjokes.get_joke()
    speak(f"here is a joke for you {joke}")
    print(f"here is a joke for you {joke}")






def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
   
   
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)


    elif c.lower().startswith("hello"):
        speak("Hello, how can I assist you today?")

    elif c.lower().startswith("what is the time"):
        tell_time()

    elif c.lower().startswith("tell me a joke"):
        tell_joke()
   



if __name__ == "__main__":
    speak("Initializing Echo....")
    while True:
        # Listen for the wake word 
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
            word = r.recognize_google(audio)
            if(word.lower() == "Echo"):
                speak("Ki re")
                # Listen for command
                with sr.Microphone() as source:
                    print("Echo Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))
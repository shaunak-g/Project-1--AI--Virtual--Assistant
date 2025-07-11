import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import os
from datetime import datetime
import pyjokes
import random


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


def speak(text):
    engine.say(text)
    engine.runAndWait()
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
    elif c.lower().startswith("let's play a game"):
        speak("Let's play a game of snake water gun")
        computer=random.randint[(1,2,3)]
        choice=[1,2,3]
        user=int(input("enter a choice: "))

        if choice == "1":
            if computer == "Snake":
                speak("It's a tie!")
            elif computer == "Water":
                speak("You lose, computer chose water!")
            elif computer == "Gun":
                speak("You win, computer chose gun!")
            elif choice == "2":
                if computer == "Water":
                    speak("It's a tie!")
                elif computer == "Snake":
                    speak("You win, computer chose snake!")
                elif computer == "Gun":
                    speak("You lose, computer chose gun!")
                elif choice == "3":
                    if computer == "Gun":
                        speak("It's a tie!")
                    elif computer == "Snake":
                        speak("You win, computer chose snake!")
                    elif computer == "Water":
                        speak("You lose, computer chose water!")
                    else:
                        speak("Invalid choice!") 
                        




if __name__ == "__main__":
    speak("Initializing Echo....")
    while True:
        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print("Listening for wake word...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                print("Recognizing...")
                word = r.recognize_google(audio)
                print("You said:", word)
        except sr.WaitTimeoutError:
            print("No speech detected.")
            continue
        except sr.UnknownValueError:
            print("Could not understand wake word.")
            continue
        except sr.RequestError as e:
            print(f"API error: {e}")
            continue

        if word.lower() == "echo":
            speak("Ki re !")

            try:
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=1)
                    print("Echo Active, listening for command...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    print("Recognizing command...")
                    command = r.recognize_google(audio)
                    print("Command:", command)
                    processCommand(command)
            except sr.UnknownValueError:
                print("Sorry, I didn't get that.")
                speak("Sorry, I didn't get that.")
            except sr.RequestError as e:
                print(f"API Error: {e}")
                speak("API error occurred.")

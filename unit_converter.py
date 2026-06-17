import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime

engine = pyttsx3.init()

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except:
        return ""

speak("Hello! I am Jarvis. How can I help you?")

while True:
    command = take_command()

    if "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak("Current time is " + current_time)

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        break

    elif command != "":
        speak("Sorry, I did not understand that command.")

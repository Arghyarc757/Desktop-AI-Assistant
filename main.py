import speech_recognition as sr
import os
import subprocess
import pyttsx3
import webbrowser
import openai
import datetime
from call_ai import ask_ai

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing.......")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry could you say it again"

if __name__ == '__main__':
    print("Hi")
    say("Hello, I am Jolly, How may I help you ?")
    while True:
        print("listening........")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["google", "https://www.google.com"], ["wikipedia", "https://www.wikipedia.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}.....")
                webbrowser.open(site[1])
        
        # todo: add specific music
        if "open music" in query.lower():
            music_path = r"dir"
            if os.path.exists(music_path):
                os.startfile(music_path)
        
        if "the time" in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"The time is {hour} Hour and {min} Minutes")
            print(f"The time is {hour} Hr and {min} Min")

        if "open games" in query.lower():
            games_dir = r"C:\Users\arghy\OneDrive\Desktop\Games"
            if os.path.exists(games_dir):
                say("Opening games folder")
                games_process = subprocess.Popen(f'explorer "{games_dir}"')

        apps = [["camera", "start microsoft.windows.camera:"], 
                ["whatsapp", "start whatsapp:"], 
                ["calculator", "start calculator:"],
                ["chrome", r"C:\Program Files\Google\Chrome\Application\chrome.exe"]
        ]
        for app in apps:
            if f"Open {app[0]}".lower() in query.lower():
                say(f"Opening {app[0]}.....")
                if app[1].startswith("start "):
                    os.system(app[1])
                else:
                    os.startfile(app[1])

        if "ask ai" in query.lower() or "question" in query.lower():
            say("What would you like to ask?")
            user_question = takeCommand()

            if "some error occurred" not in user_question.lower():
                say("Let me check with AI...")
                response = ask_ai(user_question)
                print("AI Response:", response)
                say(response)
            else:
                say("Sorry, I could not understand your question")

        
        if "please exit".lower() in query.lower():
            say("Closing this Application")
            exit()
            

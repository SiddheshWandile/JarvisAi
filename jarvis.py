import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get  
import wikipedia
import webbrowser
import pywhatkit

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):  # text to speak
    engine.say(audio)
    engine.runAndWait()


def takecommand1():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Audio captured. Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f"User Said: {query}")
            return query
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Can you please repeat?")
        except sr.RequestError as e:
            speak("I'm having trouble accessing the Google API. Please check your internet connection.")
        except sr.WaitTimeoutError:
            speak("Listening timed out. Please try again.")
        except KeyboardInterrupt:
            print("User interrupted the program.")
        return "none"


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Im Jarvis sir, Please tell me how can i help you")


if __name__ == "__main__":
    # wish()
    if True:
        query = takecommand1().lower()

        # Actual Program start
        if "open vs code" in query:
            npath = "C:\\Users\\siddh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(npath)

        elif "open chrome" in query:
            apath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
            os.startfile(apath)

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(5)
                if(k == 2):
                    break;
            cap.realease()
            cv2.destroyAllWindows()

        elif "play music" in query:
            speak("There is no music available")
            # musicdir = ""
            # song = os.listdir(musicdir)
            # rd = random.choice(song)
            # os.startfile(os.path.join(musicdir, rd))         
        
        elif "ip address" in query:
            ip = get('http://api.ipify.org').text
            print(f"Your ip address is {ip}")
            speak(f"Your ip address is {ip}")

        elif "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result + " thats all sir")

        elif "open youtube" in query:
            webbrowser.open("http://www.youtube.com/")

        elif "open my website" in query:
            webbrowser.open("https://siddheshwandile.netlify.app/")        
            
        elif "send massage" in query:
            kit.sendwhatmsg("+919307587557", "this is a new msg", 2,25)



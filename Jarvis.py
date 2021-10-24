import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    # pass
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

    speak("I am Jarvis Sir, Please tell me how may I help you")




def takeCommand():
    # It takes Microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...........")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing........")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query )

    except Exception as e:
        # print(e)

        print("Say that again, Please.............")
        return "None"

    return query




def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'yourpassword')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    # speak("Welcome Sir, How can i help you")
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()
    # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia......")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 5 )
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'play music' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime} ")

        elif 'open atom' in query:
            codePath = "C:\\Users\\AppData\\Local\\atom\\atom"
            os.startfile(codePath)

        elif 'thank you' in query:
            speak("Welcome ! it is my pleasure to serve you Sir....")

        elif 'email to omkar' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "other@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir , i am not able to send this email.....")

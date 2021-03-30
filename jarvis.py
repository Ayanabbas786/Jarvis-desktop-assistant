# Importing modules
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


# Selecting a voice for our AI
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Speak - This will make the assistant speak a sentence which is given to it
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Wish the user as soon as it starts
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning!")

    elif hour > 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good evening")
    speak("I am Jarvis, sir. Please tell me how may I help you.")


# Listens to a command and gives a string output containing the command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


# Send an email to a given account
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@example.com', 'your-password')
    server.sendmail('youremail@example.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    # All the commands that Jarvis can handle. We can add more if we want.
    while True:
        input("Press enter to talk to Jarvis\n")
        query = takeCommand().lower()

        if 'wikipedia' in query:
            print("Searching...")
            speak("Searching on wikipedia..")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("Here's a summary of what I found on wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")

        elif 'the date' in query:
            date = datetime.datetime.now()
            speak(
                f"Sir, today is {date.day}, {date.date} {date.month} {date.year}")

        elif 'open code' in query:
            codePath = "C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open chrome' in query:
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)


        elif 'send an email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = input("Please enter the email ID to which you want to send the message: ")
                sendEmail(to, content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry, could not send the email. Please try again later.")

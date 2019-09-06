import pyttsx3 #for audio
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import tkinter as tk
from tkinter import ttk


win=tk.Tk()
win.title("jarvis")
win.mainloop()



file=open("email.txt",'r')

engine= pyttsx3.init('sapi5')    #sapi5 is an api used for using the voice of windows
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good afternoon")
    else:
        speak("Good Evening")
   # speak("time is {}".format(hour))
    speak("I am jarvis please tell me how can i help you")

def takecommand():
    #it takes microphone input from the user and returns string output
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print("user said: {}\n".format(query))


    except Exception as e:

        #print(e)
    
        print("say that again please")
        return "None"
    return query

def sendEmail(to,content): #function to import smtp and we also have to make allow our app to less secure ""
    server=smtplib.SMTP('smtp.gmail.com',587) 
    server.ehlo()
    server.starttls()
    server.login("yourid@gmail.com",file.read())
    server.sendmail("yourid@gmail.com",to,content)
    server.close()



if __name__=="__main__":
    wishMe()
    while True:
        query = takecommand().lower()
        #logic for executing task based on query
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia"," ")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'hello jarvis' in query:
            speak("hello sir.. how are you??")

        
        elif 'i am good' or 'i am fine ' in query:
            speak("happy to hear that sir... any istructions for me sir")





        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        

        elif "open python files" in query:
            folder="C:\\Users\\jsaur"
            files=os.listdir(folder)
            for i in files:
                print(i)        
    
        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak("sir..the time is {}".format(strTime))
        
        elif "open code" in query:
            code_path="C:\\Users\\jsaur\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        
        elif "open turbo" in query:
            code_path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Turbo C++\\Turbo C++ 3.2"
            os.startfile(code_path)


        elif "open gmail" in query:
            try:
                speak("what should i say?")
                content=takecommand()
                to="reciversid@gmail.com"
                sendEmail(to,content)
                speak("Email has sent")
            except Exception as e:
                print(e)
                speak("sorry sir i m not able to send this email at the moment")

        
file.close()


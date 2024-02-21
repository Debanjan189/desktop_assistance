import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>12 and hour<=18:    
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis....sir...How can i help you?")        


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio=r.listen(source)
    
    try:
        print("regognising.....")
        query =r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)


        print("say that again please......")
        return "None"
    return query    



 

if __name__==  "__main__":
   wishMe()
   while True:
    query=takeCommand().lower()

    if 'wikipedia' in query:
        speak("searching wikipedia.....")
        query= query.replace("wikipedia","")
        results=wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
       webbrowser.open("youtube.com") 
    elif 'open google' in query:
       webbrowser.open("google.com") 
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir,...the time is {strTime}")



   


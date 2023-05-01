import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
r=sr.Recognizer()

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audiovoice):
    #engine.say('Hello Dear')
    print(audiovoice)
    engine.say(audiovoice)
    engine.runAndWait()

def greet():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=11:
        speak('Good Morning Sir')
    elif hour>=11 and hour<15:
        speak('Good Afternoon Sir')    
    elif hour<=15 and hour<24:
        speak('Good Evening Sir')  
    speak("I am Your Personal Assistant")  

def askname():
    speak("What is your name Sir?")    
    name=takevoicecommand()
    speak("Welcome "+name)
    speak("How can I help You Sir?")

def locate():
    speak('Say location you want to search')
    with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2,duration=0.1)
        audio2=r.listen(source2)
        MyText=r.recognize_google(audio2)
        MyText=MyText.lower()
        # print("did you say "+MyText)
            # ch=input("Enter [y/n]")
        speak(MyText)
        # if(ch=='y'):
        location=MyText
        #webbrowser.open("https://www.google.com/maps/place/"+location)
        # else:
            #     print("say location again")
            # continue

def takevoicecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        try:
            audio=r.listen(source, timeout=30, phrase_time_limit=10)
            print("Compiling Your Voice please wait...")
            text=r.recognize_google(audio, language='en-in')
            print(text)
        except Exception as e:
            speak('Unable to recognize your voice')
            # takevoicecommand()
        return text
    
    
# speak('My audio voice')

if __name__=='__main__':
    greet()
    askname()
    # locate()
    while True:
        work=takevoicecommand().lower() 
        if 'how are you' in work:
            speak('I am fine. Thank You')
            speak('How Are You Sir?')

        elif 'fine' in work or 'good' in work:
            speak('It is good to know that you are fine')
        
        elif 'i love you' in work or 'Love you' in work:
            speak('Oh my God!!!    Thank You')

        elif 'open map' in work:
            # url="https://www.google.com/maps"
            # chrome_path="C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            
            # webbrowser.get(chrome_path).open(url)
            locate()
        elif 'close map' in work:
            os.system("TASKKILL /F /IM chrome.exe")

        elif 'open notepad' in work:
            path="c:\\windows\\system32\\notepad.exe"
            os.startfile(path)

        elif 'close notepad' in work:
            os.system("TASKKILL /F /IM notepad.exe")


        elif 'bye' in work:
            speak('bye Sir... See you again')
            exit()
        
        else: 
            speak('I can not understand please speak again')


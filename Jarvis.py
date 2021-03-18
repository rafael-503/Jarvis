import pyttsx3
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time = datetime.datetime.now().strftime('%H:%M:%S') # for 24 hours clock
    Time = datetime.datetime.now().strftime('%I:%M:%S') # for 12 hours clock
    speak('Agora são')
    speak(Time)

def date_():
    day =datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    speak('Hoje é dia')
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak('Bem vindo de volta!')
    # time_()
    # date_()

    # Greetings
    hour = datetime.datetime.now().hour

    if hour >=6 and hour <12:
        speak('Bom dia!')
    elif hour >=12 and hour <18:
        speak('Boa tarde!')
    elif hour >=18 and hour <24:
        speak('Boa noite!')
    else:
        speak('Good night')
    
    speak('Estou a sua disposição, como posso ajudar?')

wishme()

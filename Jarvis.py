import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def hora_():
    Time = datetime.datetime.now().strftime('%H:%M:%S') # for 24 hours clock
    # Time = datetime.datetime.now().strftime('%I:%M:%S') # for 12 hours clock
    speak('Agora são')
    speak(Time)

def data_():
    day =datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    speak('Hoje é dia')
    speak(day)
    speak(month)
    speak(year)

def wishme():
    # hora_()
    # data_()

    hour = datetime.datetime.now().hour

    if hour >=6 and hour <12:
        speak('Bom dia!')
    elif hour >=12 and hour <18:
        speak('Boa tarde!')
    elif hour >=18 and hour <24:
        speak('Boa noite!')
    else:
        speak('Good night')

    speak('Bem vindo de volta!')
    speak('Estou a sua disposição, como posso ajudar?')

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Escutando....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Reconhecendo....')
        query = r.recognize_google(audio, language='pt-BR')
        print(query)

    except Exception as e:
        print(e)
        print('Fale novamente por favor....')
        return 'None'
    return query
    
if __name__ == '__main__':

    wishme()

    while True:
        query = TakeCommand().lower()
    
        if 'hora' or 'horas' in query:
            hora_()

        if 'data' or 'dia' in query:
            data_()


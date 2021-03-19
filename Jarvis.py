import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

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
    day = datetime.datetime.now().day
    months = ["Unknown",
          "Janeiro",
          "Fevereiro",
          "Março",
          "Abril",
          "Maio",
          "Junho",
          "Julho",
          "Agosto",
          "Setembro",
          "Outubro",
          "Novembro",
          "Dezembro"]
    month=months[datetime.datetime.now().month]
    # month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    speak('Hoje é dia')
    speak(day)
    speak('de')
    speak(month)
    speak('de')
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
        speak('Não entendi por favor repita')
        return 'None'
    return query
    
if __name__ == '__main__':

    # wishme()

    while True:
        query = TakeCommand().lower()

        if 'hora' in query:
            hora_()

        elif 'data' in query:
            data_()

        elif 'wikipédia' in query:
            speak('Procurando...')
            query = query.replace('wikipedia', '')
            wikipedia.set_lang('pt')
            result = wikipedia.summary(query, sentences=3)
            speak('De acordo com a Wikipedia')
            speak(result)
            print(result)


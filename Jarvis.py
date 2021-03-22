import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import os

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

def sendEmail(to, content):
        server=smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()

        server.login('username@gmail.com', 'password')
        server.sendmail('username@gmail.com', to, content)
        server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak('O uso de cpu está em'+ usage + '%')

    battery = str(psutil.sensors_battery())
    speak('A bateria está em')
    speak(battery.percent)

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

        elif 'enviar e-mail' in query:
            try:
                speak('O que devo escrever?')
                content = TakeCommand()
                speak('Para quem devo mandar?')
                reciever = input('Digite o email:')
                to = reciever
                sendEmail(to, content)
                speak(content)
                speak('O email foi enviado com sucesso')
            except Exception as e:
                print(e)
                speak('Não foi possivel enviar o email')

        elif 'procurar no navegador' in query:
            speak('O que gostaria de procurar?')
            browserPath = 'C:\Program Files\... (browser path) %s'
            search = TakeCommand().lower
            wb.get(browserPath).open_new_tab(search + '.com')

        elif 'procurar no youtube' in query:
            speak('O que deseja procurar?')
            search_term = TakeCommand().lower()
            speak('Procurando...')
            wb.open('https//www.youtube.com/results?search_query='+ search_term)

        elif 'procurar no google' in query:
            speak('O que gostaria de procurar?')
            search_term = TakeCommand().lower()
            speak('Procurando...')
            wb.open('https://www.google.com/search?q='+ search_term)

        elif 'cpu' in query:
            cpu()

        elif 'saia' in query:
            speak('Saindo...')
            quit()
        
        elif 'bloco de notas' in query:
            speak('Abrindo bloco de notas...')
            notepad = r'C:\Windows\notepad.exe'
            os.startfile(notepad)

        elif 'escreva uma nota' in query:
            speak('O que devo escrever?')  
            notes= TakeCommand()
            file = open('notas.txt','w')
            speak('Devo incluir na nota a data e hora?')
            ans = TakeCommand()
            if 'sim' in ans:
                strTime = datetime.datetime.now().strftime('%H:%M%S')
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Pronto anotado')
                file.close()
            else:
                file.write(notes)
                speak('Pronto anotado')
                file.close()

        elif 'abra a nota' in query:
            speak('Abrindo a nota')
            file = open(notes.txt)
            print(file.read())
            speak(file.read())
            file.close()
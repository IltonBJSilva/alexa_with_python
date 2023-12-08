import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

#Reconhecer nosso audio
audio = sr.Recognizer()
maquina = pyttsx3.init()


#print(sr.Microphone().list_microphone_names())

def executa_comando():
    try:
        with sr.Microphone(2) as source:
            print('Ouvindo audio...') # pra saber se esta ouvindo a gente
            voz = audio.listen(source) # escutar o audio
            comando = audio.recognize_google(voz, language='pt-BR') # receber comando
            comando = comando.lower() # deixar tudo em minusculo
            if 'tina' in comando:
                comando = comando.replace('tina', '') # tirar o nome tina
                maquina.say(comando) # Fala
                maquina.runAndWait() # da run no programa

    except:
        print('Microfone não funciona corretamente')


    return comando








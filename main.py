import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

#Reconhecer nosso audio
audio = sr.Recognizer()
maquina = pyttsx3.init()


print(sr.Microphone().list_microphone_names())



comando_voz_usuario()







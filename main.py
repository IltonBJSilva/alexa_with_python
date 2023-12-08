import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os

#Reconhecer nosso audio
audio = sr.Recognizer()
maquina = pyttsx3.init()
def tina_fala(text):
    maquina.say(text)
    maquina.runAndWait()


def main():

    
    tina_fala('Olá, eu sou a Tina, sua assistente virtual, em que posso ajudar?\n Diga: horas, para que eu o informe,Diga: procure por, e diga oque deseja procurar, Diga: toque, e informe a musica, Diga: criar, e eu irei criar uma lista de tarefas')
    comando = executa_comando()

    if 'horas' in comando:
        horas()
    elif 'procure por' in comando:
        search_wiki(comando)
    elif 'toque' in comando:
        music(comando)
    elif 'criar' in comando:
        todo()

    
#print(sr.Microphone().list_microphone_names())

# Informa as horas
def horas():
    #hora = comando.replace('horas', '')
    hora = datetime.datetime.now().strftime('%H:%M')
    tina_fala('Agora São ' + hora)

# pesquisa na wiki
def search_wiki(comando):
    procurar = comando.replace('procure por', '')
    wikipedia.set_lang('pt')
    info = wikipedia.summary(procurar, 2)
    print(info)
    tina_fala(info)

# abre uma musica
def music(comando):
    musica = comando.replace('toque', '')
    resultado = pywhatkit.playonyt(musica)
    tina_fala('Tocando ' + musica)
# Cria uma lista de tarefas

def todo():
    tina_fala('Ok, vou criar a lista, mais antes me diga uma coisa, oque o senhor deseja adicionar a lista de tarefas?')
    while True:
        task = executa_comando()
        if 'terminei' in task:
            tina_fala('Encerrando a criação da lista de tarefas')
            break
        with open('todo.txt', 'a') as f:
            f.write(f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M')} - {task}\n")
            tina_fala('Tarefa adicionada, o senhor deseja mais alguma coisa? se não diga terminei')

#Executa os comandos
def executa_comando():
    try:
        with sr.Microphone(2) as source:
            print('Ouvindo audio...') # pra saber se esta ouvindo a gente
            tina_fala('Pode falar: ') # fala
            voz = audio.listen(source) # escutar o audio
            comando = audio.recognize_google(voz, language='pt-BR') # receber comando
            comando = comando.lower() # deixar tudo em minusculo
            if 'tina' in comando:
                comando = comando.replace('tina', '') # tirar o nome tina
                #tina_fala(comando) # Fala

    except:
        print('Microfone não funciona corretamente')
    return comando

'''
def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        #hora = comando.replace('horas', '')
        hora = datetime.datetime.now().strftime('%H:%M')
        tina_fala('Agora São ' + hora)
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        info = wikipedia.summary(procurar, 2)
        print(info)
        tina_fala(info)
    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        tina_fala('Tocando ' + musica)
        pywhatkit.playonyt(musica)
    elif 'criar' in comando:
        tina_fala('Ok, vou criar a lista, mais antes me diga uma coisa, oque o senhor deseja adicionar a lista de tarefas?')
        while True:
            task = executa_comando()
            print(comando)
            task = comando.replace('terminei', '')
            with open('todo.txt', 'a') as f:
                f.write(f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M')} - {task}\n")
            tina_fala('Tarefa adicionada, o senhor deseja mais alguma coisa? se não diga terminei')
            if 'terminei' in comando:
                tina_fala('Encerrando a criação da lista de tarefas')
                break
'''
#comando_voz_usuario()


main() # função principal 




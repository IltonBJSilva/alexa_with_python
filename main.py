import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os
import random

# Configurações de reconhecimento e voz
audio = sr.Recognizer()
maquina = pyttsx3.init()

def tina_fala(text):
    maquina.say(text)
    maquina.runAndWait()

# Função principal com loop contínuo
def main():
    tina_fala(
        'Olá, eu sou a Tina, sua assistente virtual. '
        'Você pode dizer: horas, procure por, toque, criar, abrir site, anotar, ler tarefas, conte uma piada, calcule ou sair.'
    )

    while True:
        comando = executa_comando()
        if not comando:
            tina_fala('Não entendi. Por favor, tente novamente.')
            continue

        if 'horas' in comando:
            horas()
        elif 'procure por' in comando:
            search_wiki(comando)
        elif 'toque' in comando:
            music(comando)
        elif 'criar' in comando:
            todo()
        elif 'abrir' in comando:
            abrir_site(comando)
        elif 'anotar' in comando:
            anotar()
        elif 'ler tarefas' in comando:
            ler_tarefas()
        elif 'piada' in comando:
            contar_piada()
        elif 'calcule' in comando:
            calcular(comando)
        elif 'sair' in comando or 'encerrar' in comando or 'tchau' in comando:
            encerrar()
        else:
            tina_fala('Desculpe, não reconheci esse comando.')

# Funções auxiliares
def executa_comando():
    try:
        with sr.Microphone(1) as source:
            print('Ouvindo áudio...')
            tina_fala('Pode falar:')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR').lower()
            if 'tina' in comando:
                comando = comando.replace('tina', '').strip()
            return comando
    except:
        print('Erro com o microfone ou reconhecimento.')
        return ''

def horas():
    hora = datetime.datetime.now().strftime('%H:%M')
    tina_fala('Agora são ' + hora)

def search_wiki(comando):
    termo = comando.replace('procure por', '').strip()
    wikipedia.set_lang('pt')
    try:
        info = wikipedia.summary(termo, 2)
        print(info)
        tina_fala(info)
    except:
        tina_fala('Desculpe, não consegui encontrar informações sobre isso.')

def music(comando):
    musica = comando.replace('toque', '').strip()
    tina_fala('Tocando ' + musica)
    pywhatkit.playonyt(musica)

def todo():
    tina_fala('O que deseja adicionar à lista de tarefas? Diga "terminei" para encerrar.')
    while True:
        tarefa = executa_comando()
        if 'terminei' in tarefa:
            tina_fala('Encerrando a criação da lista de tarefas.')
            break
        with open('todo.txt', 'a') as f:
            f.write(f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M')} - {tarefa}\n")
        tina_fala('Tarefa adicionada.')

def abrir_site(comando):
    sites = {
        'youtube': 'https://www.youtube.com',
        'gmail': 'https://mail.google.com',
        'google': 'https://www.google.com',
        'noticias': 'https://g1.globo.com',
    }
    for nome, url in sites.items():
        if nome in comando:
            tina_fala(f'Abrindo {nome}')
            webbrowser.open(url)
            return
    tina_fala('Desculpe, não conheço esse site.')

def anotar():
    tina_fala('O que você deseja anotar?')
    anotacao = executa_comando()
    with open('anotacoes.txt', 'a') as f:
        f.write(f"{datetime.datetime.now()} - {anotacao}\n")
    tina_fala('Anotação salva!')

def ler_tarefas():
    if not os.path.exists('todo.txt'):
        tina_fala('Você ainda não tem tarefas.')
        return
    tina_fala('Aqui estão suas tarefas:')
    with open('todo.txt', 'r') as f:
        for linha in f:
            tina_fala(linha.strip())

def contar_piada():
    piadas = [
        'Por que o programador foi ao médico? Porque ele tinha um bug.',
        'O que o zero disse para o oito? Belo cinto!',
        'Qual é o cúmulo do programador? Usar Ctrl+C e esquecer de Ctrl+V.',
    ]
    tina_fala(random.choice(piadas))

def calcular(comando):
    comando = comando.replace('calcule', '').strip()
    comando = comando.replace('mais', '+').replace('menos', '-').replace('vezes', '*').replace('dividido por', '/')
    try:
        resultado = eval(comando)
        tina_fala(f'O resultado é {resultado}')
    except:
        tina_fala('Não consegui calcular isso.')

def encerrar():
    tina_fala('Até logo!')
    exit()

# Início da assistente
main()

from tkinter import *
import tkinter as tk
import pyglet
import time

# Adicionando fontes externas
pyglet.font.add_file('fontes/digital-7.ttf')

janela = Tk()
janela.title('Cronômetro')
janela.geometry('300x180')
janela.config(bg='black')
janela.resizable(width=False, height=False)

# Definindo variaveis globais
global contador
global tempo
global rodar
global limitador


tempo = '00:00:00'
rodar = False
contador = 0
limitador = 60

def iniciar():
    global contador
    global tempo
    global limitador

    if rodar == True:
        
        label_tempo['font'] = 'digital-7 62'
        temporario = str(tempo)
        h, m, s = map(int, temporario.split(':'))
        h = int(h)
        m = int(m)
        s = int(contador)

        if s >= limitador:
            contador = 0
            s = 0
            m +=1

        if m >= 60:
            m = 0
            h += 1

        if h >= 24:
            h = 0
            
        s = str(0) + str(s)
        m = str(0) + str(m)
        h = str(0) + str(h)

        # atualizando os valores
        temporario = str(h[-2:]) + ':' + str(m[-2:]) + ':' + str(s[-2:])
        label_tempo['text'] = temporario

        tempo = temporario

        label_tempo.after(1000, iniciar)
        contador += 1


def start():
    global rodar
    rodar = True
    iniciar()

def pausar():
    global rodar
    rodar = False

def reiniciar():
    global tempo
    global contador 
    global rodar

    rodar = False
    tempo = '00:00:00'
    label_tempo['text'] = tempo
    contador = 0


# Criando Labels ----------------------------------
label_app = Label(janela, text='Cronômetro', font=(
    'Arial 10'), bg='black', fg='white')
label_app.place(x=20, y=5)

label_tempo = Label(janela, text=tempo, font=(
    'digital-7 62'), bg='black', fg='#39FF14')
label_tempo.place(x=17, y=30)

botao_iniciar = Button(text='Iniciar', command=start, width=10, height=2,
                       bg='black', fg='white', relief='raised', overrelief='ridge')
botao_iniciar.place(x=20, y=125)
botao_pausar = Button(text='Pausar', command=pausar, width=10, height=2,
                      bg='black', fg='white', relief='raised', overrelief='ridge')
botao_pausar.place(x=110, y=125)
botao_reiniciar = Button(text='Reiniciar', command=reiniciar, width=10, height=2,
                         bg='black', fg='white', relief='raised', overrelief='ridge')
botao_reiniciar.place(x=200, y=125)

janela.mainloop()

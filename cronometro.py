from tkinter import *
import tkinter as tk
import pyglet

pyglet.font.add_file('fontes/digital-7.ttf')           # Adicionando fontes externas

janela = Tk()
janela.title('Cronômetro')
janela.geometry('300x180')
janela.config(bg='black')
janela.resizable(width=False, height=False)

# Criando Labels ----------------------------------
label_app = Label(janela, text='Cronômetro', font=('Arial 10'), bg='black', fg='white')
label_app.place(x=20, y=5)

label_tempo = Label(janela, text='00:00:00', font=('digital-7 62'), bg='black', fg='#39FF14')
label_tempo.place(x=17, y=30)

botao_iniciar = Button(text='Iniciar', width=10, height=2, bg='black', fg='white', relief='raised', overrelief='ridge')
botao_iniciar.place(x=20, y=125)
botao_pausar = Button(text='Pausar', width=10, height=2, bg='black', fg='white', relief='raised', overrelief='ridge')
botao_pausar.place(x=110, y=125)
botao_reiniciar = Button(text='Reiniciar', width=10, height=2, bg='black', fg='white', relief='raised', overrelief='ridge')
botao_reiniciar.place(x=200, y=125)



janela.mainloop()

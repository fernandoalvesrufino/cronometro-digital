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

label_tempo = Label(janela, text='00:00:00', font=('digital-7 62'), bg='black', fg='green')
label_tempo.place(x=20, y=30)


janela.mainloop()

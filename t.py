# setando o tkinter
from tkinter import *
import time

painel = Tk()
painel.title("Controlando um arduino")
painel.configure(bg="#412F59")
# os valores seguidos por '+' ajustam a posição da tela no monitor
painel.geometry('470x300+390+170')

# a tela não poderá ser aumentada nem diminuída
painel.resizable(width=False, height=False)

def criarPorta(codigo):
    pass
def enviarComando():
    pass

def comando(op):
    if (op == 1):
        botao1.config(bg="#BDB8D9")





# criando os componentes
botao1=Button(text='Ligar Azul',command=lambda:comando(1),bg='#8C98FF',fg='#412F59', width=12, font=('Segoe UI', 12))
botao2=Button(text='Ligar Verde',command=lambda:comando(2),bg='#7CFF89',fg='#412F59', width=12, font=('Segoe UI', 12))
btOk = Button(text="Ok", command=criarPorta, bg="#9F8FBF", fg="#412F59", width= 11, font=('Segoe UI', 13))
caixaPorta = StringVar(painel)
EntryPorta = Entry(painel, textvariable=caixaPorta, bg="#BDB8D9", fg="#412F59", width = 20, font=('Segoe UI', 19))

# posição dos componentes
botao1.place(x=80,y=200)
botao2.place(x=240,y=200)
btOk.place(x=315.5,y=82)
EntryPorta.place(x=35, y=82)


painel.mainloop()
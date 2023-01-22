from tkinter import *
import serial

# configurações básicas tkinter
painel = Tk()
painel.title("Controlando um arduino")
painel.configure(bg="#412F59")

# os valores seguidos por '+' ajustam a posição da tela no monitor
painel.geometry('470x300+390+170')

# a tela não poderá ser aumentada nem diminuída
painel.resizable(width=False, height=False)

# declarando funções
def criarPorta():
    global portaUSB
    aux = caixaPorta.get()
    informePorta.config(text=f"Em uso:  {aux}")
    portaUSB = serial.Serial(aux, 9600)

def enviarComando(cod):
    aux = str(cod)
    Uno.write(aux.encode())

def comando(corAzul):
    global azul, verde
    
    if corAzul: # cor selecionada: AZUL
        
        if azul: # se o botão estiver ligado
            print("Led azul DESLIGADO")
            botao1.config(bg="#8C98FF")
            azul = False
            enviarComando("azulDES") # envia o comando de desligar
            
        else: # se o botão estiver desligado
            print("Led azul LIGADO")
            botao1.config(bg="#DFF2F0")
            azul = True
            enviarComando("azulLIG") # envia o comando de ligar

    else: # cor selecionada: VERDE
        
        if verde: # se o botão estiver ligado
            print("Led verde DESLIGADO")
            botao2.config(bg="#7CFF89")
            verde = False
            enviarComando("verdeDES") # envia o comando de desligar
        
        else: # se o botão estiver desligado
            print("Led verde LIGADO")
            botao2.config(bg="#DFF2F0")
            verde = True
            enviarComando("verdeLIG") # envia o comando de ligar
        


# criando os componentes
botao1=Button(text='Ligar Azul',command=lambda:comando(True),bg='#8C98FF',fg='#412F59', width=12, font=('Segoe UI', 12))
botao2=Button(text='Ligar Verde',command=lambda:comando(False),bg='#7CFF89',fg='#412F59', width=12, font=('Segoe UI', 12))
btOk = Button(text="Ok", command=criarPorta, bg="#9F8FBF", fg="#412F59", width= 11, font=('Segoe UI', 13))
caixaPorta = StringVar(painel)
EntryPorta = Entry(painel, textvariable=caixaPorta, bg="#BDB8D9", fg="#412F59", width = 20, font=('Segoe UI', 19, "italic"))
informePorta = Label(painel, text="Informe a Porta", fg='#BDB8D9',bg="#412F59", font=('Segoe UI', 24))

# posição dos componentes
botao1.place(x=181,y=200)
botao2.place(x=317.5,y=200)
btOk.place(x=315.5,y=82)
EntryPorta.place(x=35, y=82)
informePorta.place(x=30, y=10)

# setando as cores
azul = False
verde = False

painel.mainloop() # deixando a tela em loop
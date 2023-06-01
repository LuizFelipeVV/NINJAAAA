from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.mouse import *
from PPlay.keyboard import *

def game():
   
    global janela
    global fundo1
    global fundo2
   
    while True:

    
    
        fundo2.set_position(-300,200)
        fundo1.draw()
        fundo2.draw()
        janela.update()

    return 0




janela = Window(1200,700)
fundo1 = GameImage("estrelas.png")
fundo2 = GameImage("bloco2.png")

game()

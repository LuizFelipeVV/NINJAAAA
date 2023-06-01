from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.mouse import *
from PPlay.keyboard import *



janela = Window(1200,700)
fundo1 = GameImage("estrelas.png")
fundo2 = GameImage("bloco2.png")
while True:

    
    
    fundo2.set_position(-300,200)
    fundo1.draw()
    fundo2.draw()
    janela.update()
import pygame
import os, sys

from ElementoQuimico import ElementoQuimico

pygame.init()

gameDisplay = pygame.display.set_mode((1024,720))
pygame.display.set_caption('PyQuímica')

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)

pygame.font.init()
fonteTituloJogo = pygame.font.SysFont('comicsansms', 52)

fonteTituloJogo = fonteTituloJogo.render("PyQuímica", 1, black)

#Familia 1
hidrogenio = ElementoQuimico('Hidrogênio', 0, 'H')
litio = ElementoQuimico('Lítio', 1, 'Li')
sodio = ElementoQuimico('Sódio', 1, 'Na')
potassio = ElementoQuimico('Potássio', 1, 'K')
rubidio = ElementoQuimico('Rubídio', 1, 'Rb')
cesio = ElementoQuimico('Césio', 1, 'Cs')
francio = ElementoQuimico('Frâncio', 1, 'Fr')

#Familia 2
berilio = ElementoQuimico('Berílio', 2, 'Be')
magnesio = ElementoQuimico('Magnésio', 2, 'Mg')
calcio = ElementoQuimico('Cálcio', 2, 'Ca')
estroncio = ElementoQuimico('Estrôncio', 2, 'Sr')
bario = ElementoQuimico('Bário', 2, 'Ba')
radio = ElementoQuimico('Rádio', 2, 'Ra')


gameExit = False

while not gameExit:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(white)

    #TITULO DO JOGO
    gameDisplay.blit(fonteTituloJogo, (412, 20))

    #MONTA TABELA PERIODICA

    #Familia1
    hidrogenio.desenhaElemento(gameDisplay, 10,10)
    litio.desenhaElemento(gameDisplay, 10, 90)
    sodio.desenhaElemento(gameDisplay, 10, 170)
    potassio.desenhaElemento(gameDisplay, 10, 250)
    rubidio.desenhaElemento(gameDisplay, 10, 330)
    cesio.desenhaElemento(gameDisplay, 10, 410)
    francio.desenhaElemento(gameDisplay, 10, 490)

    #Familia2
    berilio.desenhaElemento(gameDisplay, 70 ,90)
    magnesio.desenhaElemento(gameDisplay, 70, 170)
    calcio.desenhaElemento(gameDisplay, 70, 250)
    estroncio.desenhaElemento(gameDisplay, 70, 330)
    bario.desenhaElemento(gameDisplay, 70, 410)
    radio.desenhaElemento(gameDisplay, 70, 490)

    #REFRESH NA TELA
    pygame.display.update()

pygame.display.update()
pygame.quit()

quit()


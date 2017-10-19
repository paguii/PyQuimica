import pygame
import os, sys
from TabelaPeriodica import TabelaPeriodica
from ElementoQuimico import ElementoQuimico

pygame.init()

gameDisplay = pygame.display.set_mode((1024,720))
pygame.display.set_caption('PyQuímica')

tabela = TabelaPeriodica()


black = (0,0,0)
white = (255,255,255)
green = (0,255,0)

pygame.font.init()
fonteTituloJogo = pygame.font.SysFont('comicsansms', 52)

fonteTituloJogo = fonteTituloJogo.render("PyQuímica", 1, black)

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
    tabela.desenhaTabelaPeriodica(gameDisplay)

    # #Familia1
    # hidrogenio.desenhaElemento(gameDisplay, 10,10)
    # litio.desenhaElemento(gameDisplay, 10, 90)
    # sodio.desenhaElemento(gameDisplay, 10, 170)
    # potassio.desenhaElemento(gameDisplay, 10, 250)
    # rubidio.desenhaElemento(gameDisplay, 10, 330)
    # cesio.desenhaElemento(gameDisplay, 10, 410)
    # francio.desenhaElemento(gameDisplay, 10, 490)
    #
    # #Familia2
    # berilio.desenhaElemento(gameDisplay, 70 ,90) distancia certa >>>
    # magnesio.desenhaElemento(gameDisplay, 70, 165)
    # calcio.desenhaElemento(gameDisplay, 70, 250)
    # estroncio.desenhaElemento(gameDisplay, 70, 330)
    # bario.desenhaElemento(gameDisplay, 70, 410)
    # radio.desenhaElemento(gameDisplay, 70, 490)
    #
    # #Familia 3
    # escandio.desenhaElemento(gameDisplay, 130, 250)

    #REFRESH NA TELA
    pygame.display.update()

pygame.display.update()
pygame.quit()

quit()


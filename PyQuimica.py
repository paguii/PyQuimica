import pygame
import os, sys

from TabelaPeriodica import TabelaPeriodica

pygame.init()

gameDisplay = pygame.display.set_mode((1140,720))
pygame.display.set_caption('PyQuímica')

tabela = TabelaPeriodica()

gray = (246,246,246)
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

    gameDisplay.fill(gray)

    #TITULO DO JOGO
    gameDisplay.blit(fonteTituloJogo, (410, 20))

    #MONTA TABELA PERIODICA
    tabela.desenhaTabelaPeriodica(gameDisplay)

    #REFRESH NA TELA
    pygame.display.update()

pygame.display.update()
pygame.quit()

quit()


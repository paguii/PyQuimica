import pygame
import os, sys

from ElementoQuimico import ElementoQuimico

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('PyQuímica')

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)

gameExit = False

potassio = ElementoQuimico('Potássio', 1, 'K')

while not gameExit:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(black)

    potassio.desenhaElemento(gameDisplay, 10,10)
    pygame.display.update()

pygame.display.update()
pygame.quit()

quit()


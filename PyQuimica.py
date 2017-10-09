import pygame
import os, sys

pygame.init()

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)

metaisAlcalinos = (255,165,0)
metaisAlcalinosTerrosos = (255,215,0)
familiaBoro = (72,209,204)
familiaCarbono = (107,142,35)
familiaNitrogenio = (34,139,34)
calcogenios = (72,61,139)
halogenios = (255,105,180)
gasesNobres = (65,105,225)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('PyQuímica')

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(black)

    pygame.draw.rect(gameDisplay, white, [400,300, 10, 100])
    pygame.draw.rect(gameDisplay, green, [400, 300, 10, 10])

    pygame.display.update()

pygame.display.update()
pygame.quit()

quit()
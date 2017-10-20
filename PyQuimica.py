import pygame
import Mensagem
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

pontuacao = 0

pygame.font.init()

fonteTituloJogo = pygame.font.SysFont('comicsansms', 52)
fonteNomeDoJogador = pygame.font.SysFont('comicsansms', 24)
fontePontuacao = pygame.font.SysFont('comicsansms', 24)

gameExit = False
firstInit = True;

while not gameExit:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(gray)

    if firstInit == True:
        nome = Mensagem.ask(gameDisplay, 'Nome')
        if nome:
            firstInit = False
    else:

        #TITULO DO JOGO
        gameDisplay.blit(fonteTituloJogo.render("PyQuímica", 1, black), (440, 20))

        #SAUDAÇÃO
        gameDisplay.blit(fonteNomeDoJogador.render('Jogador: ' + nome, 1, black), (460, 100))

        #PONTUACAO
        gameDisplay.blit(fontePontuacao.render('Pontuação: ' + str(pontuacao), 1, black), (900, 5))

        #MONTA TABELA PERIODICA
        tabela.desenhaTabelaPeriodica(gameDisplay)

        #REFRESH NA TELA
        pygame.display.update()

pygame.display.update()
pygame.quit()

quit()


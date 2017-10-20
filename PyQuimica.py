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
fonteSugestao = pygame.font.SysFont('comicsansms', 24)
fonteElemento = pygame.font.SysFont('comicsansms', 20)

tubo = pygame.image.load(os.path.join('resources', 'tubo.png'))

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

        #TUBO DE ENSAIO
        gameDisplay.blit(pygame.transform.scale(tubo, (115, 115)), (500,600))

        #ELEMENTO A SER ADVINHADO
        gameDisplay.blit(fonteSugestao.render('Elemento:', 1, black), (680, 600))
        gameDisplay.blit(fonteElemento.render('Cloreto de Sódio', 1, black), (705, 632))

        #MONTA TABELA PERIODICA
        tabela.desenhaTabelaPeriodica(gameDisplay)

        #REFRESH NA TELA
        pygame.display.update()

pygame.display.update()
pygame.quit()

quit()


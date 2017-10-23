import pygame
import Mensagem
import os, sys

from TabelaPeriodica import TabelaPeriodica
from Pergunta import Pergunta

pygame.init()

gameDisplay = pygame.display.set_mode((1140,720))
pygame.display.set_caption('PyQuímica')

tabela = TabelaPeriodica()
pergunta = Pergunta()

#CORES
gray = (246,246,246)
black = (0,0,0)
white = (255,255,255)
green = (75, 181, 67)

#POSICAO IMAGEM
posicaoTuboEnsaio = (500, 600)

#PONTUACAO
pontuacao = 0

pygame.font.init()

#FONTES PARA ESCRITA NA TELA
fonteTituloJogo = pygame.font.SysFont('comicsansms', 52)
fonteNomeDoJogador = pygame.font.SysFont('comicsansms', 24)
fontePontuacao = pygame.font.SysFont('comicsansms', 24)
fonteSugestao = pygame.font.SysFont('comicsansms', 24)
fonteElemento = pygame.font.SysFont('comicsansms', 20)
fonteBotaoConfirmar = pygame.font.SysFont('comicsansms', 24)
fonteMensagem = pygame.font.SysFont('comicsansms', 36)

tubo = pygame.image.load(os.path.join('resources', 'tubo.png'))

gameExit = False
firstInit = True;
listaElementosSelecionados = []

while not gameExit:

    gameDisplay.fill(gray)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            posicaoMouse = pygame.mouse.get_pos()
            if posicaoMouse[0] >= 950 and posicaoMouse[0] <= 950 + 150 and posicaoMouse[1] >= 638 and posicaoMouse[1] <= 638 + 50:
                del elementoSelecionado
                if pergunta.checarResposta(listaElementosSelecionados):
                    mostraMensagem = True
                    mensagem = 'Parabéns! Você Acertou!'

                    pontuacao = pontuacao + (1.3 * 1234)

                    pergunta.novaPergunta()

                    del listaElementosSelecionados[:]
                    del ultimoElementoInserido
                else:
                    mostraMensagem = True
                    mensagem = 'Opa! Tente Novamente!'

                    del listaElementosSelecionados[:]
                    del ultimoElementoInserido
            else:
                elementoSelecionado = tabela.elementoClick(posicaoMouse[0], posicaoMouse[1])

        if event.type == pygame.MOUSEBUTTONUP:
            posicaoMouse = pygame.mouse.get_pos()
            if posicaoMouse[0] >= posicaoTuboEnsaio[0] and posicaoMouse[0] <= posicaoTuboEnsaio[0] + 115 and posicaoMouse[1] >= posicaoTuboEnsaio[1] and posicaoMouse[1] <= posicaoTuboEnsaio[1] + 115:
                try:
                    if elementoSelecionado.nomeElemento != '':
                        listaElementosSelecionados.append(elementoSelecionado)
                        ultimoElementoInserido = elementoSelecionado
                except:
                    print('Elemento não definido')


    if firstInit == True:
        nome = Mensagem.ask(gameDisplay, 'Nome')
        if nome:
            pergunta.novaPergunta()
            firstInit = False
    else:
        #TITULO DO JOGO
        gameDisplay.blit(fonteTituloJogo.render("PyQuímica", 1, black), (440, 20))

        #SAUDAÇÃO
        gameDisplay.blit(fonteNomeDoJogador.render('Jogador: ' + nome, 1, black), (460, 100))

        #PONTUACAO
        gameDisplay.blit(fontePontuacao.render('Pontuação: ' + str(int(pontuacao)), 1, black), (900, 5))

        #TUBO DE ENSAIO
        gameDisplay.blit(pygame.transform.scale(tubo, (115, 115)), posicaoTuboEnsaio)

        #ELEMENTO A SER ADVINHADO
        gameDisplay.blit(fonteSugestao.render('Elemento:', 1, black), (680, 600))
        gameDisplay.blit(fonteElemento.render(pergunta.nomeCompostoQuimico, 1, black), (705, 632))

        #MONTA TABELA PERIODICA
        tabela.desenhaTabelaPeriodica(gameDisplay)

        #DESENHA BOTAO
        if len(listaElementosSelecionados) > 0:
            pygame.draw.rect(gameDisplay, green, [950, 632, 150, 50])
            gameDisplay.blit(fonteBotaoConfirmar.render('Confirmar', 1, white), (970,638))

        #DRAG AND DROP
        botaoMouse = pygame.mouse.get_pressed()

        try:
            if botaoMouse[0] == 1:
                posicaoMouseDrag = pygame.mouse.get_pos()
                elementoSelecionado.desenhaElemento(gameDisplay, posicaoMouseDrag[0] - (elementoSelecionado.base / 2), posicaoMouseDrag[1] - (elementoSelecionado.altura / 2))
        except:
            print('Elemento nao definido')

        #DESENHA ULTIMO ELEMENTO INSERIDO
        try:
            ultimoElementoInserido.desenhaElemento(gameDisplay, 400, 610)
            gameDisplay.blit(fonteElemento.render('Último Inserido', 1 , black), (360,570))
        except:
            print('Nao existe ultimo elemento')

        #MOSTRA MENSAGEM

        try:
            if mostraMensagem:
                gameDisplay.blit(fonteMensagem.render(mensagem, 1, black), (240, 200))
                mostraMensagem = False

        except:
            print('Mensagem nao definida')

        #REFRESH NA TELA
        pygame.time.wait(40)
        pygame.display.update()

pygame.display.update()
pygame.quit()

quit()


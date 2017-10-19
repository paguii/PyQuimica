import pygame
import os, sys

class ElementoQuimico:
    nomeElemento = ''
    familia = 0
    letra = ''

    cor = (0, 0, 0)
    corTexto = (0, 0, 0)

    fonteLetra = ''
    fonteNomeElemento = ''

    base = 55
    altura = 70

    def __init__(self, nomeElemento, familia, letra):
        pygame.font.init()

        self.nomeElemento = nomeElemento
        self.familia = familia
        self.letra = letra

        self.fonteLetra = pygame.font.SysFont('Arial', 30)
        self.fonteNomeElemento = pygame.font.SysFont('Arial', 12)

        # TRATAMENTO DE CORES
        hidrogenio = (220,220,220)
        metaisAlcalinos = (255, 165, 0)
        metaisAlcalinosTerrosos = (255, 215, 0)
        familiaBoro = (72, 209, 204)
        familiaCarbono = (107, 142, 35)
        familiaNitrogenio = (34, 139, 34)
        calcogenios = (72, 61, 139)
        halogenios = (255, 105, 180)
        gasesNobres = (65, 105, 225)

        if int(self.familia) == 0:
            self.cor = hidrogenio
        elif int(self.familia) == 1:
            self.cor = metaisAlcalinos
        elif int(self.familia) == 2:
            self.cor = metaisAlcalinosTerrosos
        elif int(self.familia) == 3:
            self.cor = familiaBoro
        elif int(self.familia) == 4:
            self.cor = familiaCarbono
        elif int(self.familia) == 5:
            self.cor = metaisAlcalinosTerrosos
        elif int(self.familia) == 6:
            self.cor = calcogenios
        elif int(self.familia) == 7:
            self.cor = halogenios
        elif int(self.familia) == 8:
            self.cor = gasesNobres
        else:
            self.cor = (255,255,224)

    def desenhaElemento(self, gameDisplay, x, y):
        posicaoNomeElemento = (x + 2, y + 55)
        posicaoLetraElemento = (x + 15, y + 10)

        letraElemento = self.fonteLetra.render(self.letra, 1, self.corTexto)
        nomeElemento = self.fonteNomeElemento.render(self.nomeElemento, 1, self.corTexto)

        pygame.draw.rect(gameDisplay, self.cor, [x, y, self.base, self.altura])

        gameDisplay.blit(letraElemento, posicaoLetraElemento)
        gameDisplay.blit(nomeElemento, posicaoNomeElemento)


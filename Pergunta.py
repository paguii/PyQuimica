from ElementoQuimico import ElementoQuimico
from random import randint

class Pergunta:
    id = 0

    nomeCompostoQuimico = ''
    dica = ''

    listaElementos = []

    def defineElemento(self):
        if self.id == 1:
            self.acidoSulfurico()
        elif self.id == 2:
            self.cloretoSodio()

    def acidoSulfurico(self):
        hidrogenio = ElementoQuimico('Hidrogênio', 0, 'H')
        oxigenio = ElementoQuimico('Oxigênio', 6, 'O')
        enxofre = ElementoQuimico('Enxofre', 6, 'S')

        self.id = 1
        self.nomeCompostoQuimico = 'Ácido Sulfúrico'
        self.dica = 'Possui quatro oxigênios'

        self.listaElementos.append(hidrogenio)
        self.listaElementos.append(enxofre)
        self.listaElementos.append(oxigenio)

    def cloretoSodio(self):
        cloro = ElementoQuimico('Cloro', 7, 'Cl')
        sodio = ElementoQuimico('Sódio', 1, 'Na')

        self.id = 2
        self.nomeCompostoQuimico = 'Cloreto de Sódio'
        self.dica = 'Possui um alcalino terroso'

        self.listaElementos.append(sodio)
        self.listaElementos.append(cloro)

    def checarResposta(self, listaElementosSelecionado):

        if self.id == 1:
            qtdHidrogenio = 0
            qtdOxigenio = 0
            qtdEnxofre = 0

            for i in range(0,len(listaElementosSelecionado)):
                elemento = listaElementosSelecionado[i]
                if elemento.nomeElemento == 'Hidrogênio':
                    qtdHidrogenio = qtdHidrogenio + 1
                if elemento.nomeElemento == 'Oxigênio':
                    qtdOxigenio = qtdOxigenio + 1
                if elemento.nomeElemento == 'Enxofre':
                    qtdEnxofre = qtdEnxofre + 1

            if qtdHidrogenio == 2 and qtdOxigenio == 4 and qtdEnxofre == 1:
                return True
            else:
                return False

        if self.id == 2:
            qtdCloro = 0
            qtdSodio = 0

            for i in range(0, len(listaElementosSelecionado)):
                elemento = listaElementosSelecionado[i]
                if elemento.nomeElemento == 'Cloro':
                    qtdCloro = qtdCloro + 1
                if elemento.nomeElemento == 'Sódio':
                    qtdSodio = qtdSodio + 1

            if qtdSodio == 1 and qtdCloro == 1:
                return True
            else:
                return False

    def novaPergunta(self):
        self.id = randint(1,2)
        self.defineElemento()
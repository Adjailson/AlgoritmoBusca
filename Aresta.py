# coding: utf-8
class Aresta:
    
    def __init__(self):
        #Declaração variáveis private
        self.origem = None
        self.destino = None
        self.peso = None #Km reais
        self.tempo = None #Tempo percuso

    def getOrigem(self):
        return self.origem
    def setOrigem(self, origem):
        self.origem = origem

    def getDestino(self):
        return self.destino
    def setDestino(self, destino):
        self.destino = destino

    def getPeso(self):
        return self.peso
    def setPeso(self, peso):
        self.peso = peso

    def getTempo(self):
        return self.tempo
    def setTempo(self, tempo):
        self.tempo = tempo
# coding: utf-8
class Vertice:

    BRANCO = 0 #public
    CINZA = 1 #public
    PRETO = 2 #public
    
    def __init__(self, nome, valor):
        #Declaração variáveis private
        self.nome = nome
        self.valor = valor #Valor heurístico
        self.custo = 0 #Calcular os somatórios
        self.cor = self.BRANCO #Inicia todos branco
        self.predecessor = None

    def getNome(self):
    	return self.nome
    def setNome(self, nome):
    	self.nome = nome

    def getValor(self):
    	return self.valor
    def setValor(self, valor):
    	self.valor = valor

    def getCusto(self):
        return self.custo
    def setCusto(self, custo):
        self.custo = custo

    def getCor(self):
        return self.cor
    def setCor(self, cor):
        self.cor = cor

    def getPredecessor(self):
        return self.predecessor
    def setPredecessor(self, predecessor):
        self.predecessor = predecessor
# coding: utf-8
class Vertice:

    BRANCO = 0 #public
    CINZA = 1 #public
    PRETO = 2 #public
    
    def __init__(self, nome, heuristica):
        #Declaração variáveis private
        self.nome = nome
        self.heuristica = heuristica #Valor heurístico
        self.custo = 0 #Calcular os somatórios
        self.cor = self.BRANCO #Inicia todos branco
        self.predecessor = None #Apenas para testes fora do projeto

    def getNome(self):
    	return self.nome
    def setNome(self, nome):
    	self.nome = nome

    def getHeuristica(self):
    	return self.heuristica
    def setHeuristica(self, heuristica):
    	self.heuristica = heuristica

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

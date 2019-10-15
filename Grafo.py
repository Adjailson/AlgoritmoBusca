# coding: utf-8
from Vertice import *
from Aresta import *

class Grafo:

    def __init__(self):
        #Declaração variáveis private
        self.vertices = [] #lista de vertices
        self.arestas = [] #lista de arestas

    # Métodos padrões do grafo
    def addVertice(self, nome, heuristica):
        if not self.contem(nome):
            self.vertices.append(Vertice(nome, heuristica))

    def addAresta(self, origem, destino, peso, tempo):
        vOrigem = self.obterVertice(origem)
        vDestino = self.obterVertice(destino)
        aresta_x = Aresta()
        aresta_x.setOrigem(vOrigem)
        aresta_x.setDestino(vDestino)
        aresta_x.setPeso(peso)
        aresta_x.setTempo(tempo)
        self.arestas.append(aresta_x)

        aresta_y = Aresta()
        aresta_y.setOrigem(vDestino)
        aresta_y.setDestino(vOrigem)
        aresta_y.setPeso(peso)
        aresta_y.setTempo(tempo)
        self.arestas.append(aresta_y)

    def obterVertice(self, nome):
        for x in self.getVertices():
            if x.getNome() == nome:
                return x
        return None

    def obterAresta(self, origem, destino):
        for a in self.getArestas():
            if a.getOrigem() == origem and a.getDestino() == destino:
                return a
        return None

    def adjacentes(self, vertice):
        lista = []
        for x in self.getArestas():
            if x.getOrigem().getNome() == vertice:
                lista.append(x.getDestino())
        return lista

    def imprimirCaminho(self, origem, destino):
        if origem == destino:
            print(origem.getNome())
        elif destino.getPredecessor() == None:
            print("Não existe caminho de ",origem.getNome()," à ", destino.getNome())
        else:
            self.imprimirCaminho(origem, destino.getPredecessor())
            print(destino.getNome())
            
    '''
        BUSCA HEURISTICA GULOSA
    '''
    def buscaGulosa(self, origem, destino):
        try:
            caminhos = []
            aux = []

            v_inicial = self.obterVertice(origem)
            v_inicial.setCusto(0)
            v_inicial.setCor(Vertice.CINZA)
        
            aux.append(v_inicial)
            while(len(aux) != 0):
                u = aux.pop(0)
                caminhos.append(u.getNome())#Armazenar esse caminho
                if u == self.obterVertice(destino):#se é objetivo
                    caminhos.append(None)#guardar total custo
                    caminhos[-1] = "Total = "+str(u.getCusto())
                    return caminhos#break
                
                menor = 2147483647 #MAX_VALUE
                menorVertice = None
                
                for v in self.adjacentes(u.getNome()):
                    
                    if v.getCor() != Vertice.PRETO:
                        #           G(n):
                        v.setCusto(u.getCusto()+self.obterAresta(u, v).getPeso())
                        #      G(n) + a condição que é o tempo, mas apenas para informar:
                        total = v.getCusto() + self.obterAresta(u, v).getTempo()
                        # Aqui o mesmo só escolhe o menor valor heurístico:
                        if (v.getHeuristica() <= menor and v.getCor() == Vertice.BRANCO): 
                            menor = v.getHeuristica() #G(n)
                            menorVertice = v
                            menorVertice.setCusto(total)
                        v.setCor(Vertice.CINZA)
                        
                menorVertice.setCor(Vertice.PRETO)
                aux.append(menorVertice)
                u.setCor(Vertice.PRETO)
        except:
            return "Erro!"
            
    '''
        BUSCA HEURISTICA A*
    '''
    def buscaAestrela(self, origem, destino):
        try:
            caminhos = []
            aux = []
        
            v_inicial = self.obterVertice(origem)
            v_inicial.setCusto(0)
            v_inicial.setCor(Vertice.CINZA)
        
            aux.append(v_inicial)
            while(len(aux) != 0):
                u = aux.pop(0)
                caminhos.append(u.getNome())#Armazenar esse caminho
                if u == self.obterVertice(destino):#Se é objetivo
                    caminhos.append(None)#guardar total custo
                    caminhos[-1] = "Total = "+str(u.getCusto())
                    return caminhos#break;
                
                menor = 2147483647 #MAX_VALUE
                menorVertice = None
                
                for v in self.adjacentes(u.getNome()):
                    
                    if v.getCor() != Vertice.PRETO:
                        #          G(n):
                        v.setCusto(u.getCusto() + self.obterAresta(u, v).getPeso())
                        #       G(n) + a condição que é o tempo:
                        total = v.getCusto() + self.obterAresta(u, v).getTempo()
                        #h <= h*:
                        if ((total + v.getHeuristica()) <= menor and v.getCor() == Vertice.BRANCO):
                            menor = total + v.getHeuristica() #G(n) + H(n)
                            menorVertice = v
                            menorVertice.setCusto(total)
                        v.setCor(Vertice.CINZA)

                menorVertice.setCor(Vertice.PRETO)
                aux.append(menorVertice)
                u.setCor(Vertice.PRETO)
        except:
            return "Erro!\nVerifique os valores Heurísticos!"

    '''
        BUSCA EM LARGURA
    '''
    def buscaLargura(self):
        inicial = self.getVertices()[0]
        #Visitar primeiro Vertice
        inicial.setPredecessor(None)
        inicial.setCor(Vertice.CINZA)
        
        aux = []#lista de Vertices
        aux.append(inicial)
        u = None # temporaria para armazenar a primeira remoção
        while(len(aux) != 0):
            u = aux.pop(0)
            for v in self.adjacentes(u.getNome()):
                if v.getCor() == Vertice.BRANCO:
                    v.setPredecessor(u)
                    v.setCor(Vertice.CINZA)
                    aux.append(v)
            u.setCor(Vertice.PRETO)

    '''
        BUSCA EM PROFUNDIDADE
    '''
    def buscaProfundidade(self):
        for v in self.getVertices():
            if v.getCor() == Vertice.BRANCO:
                self.visitar(v)

    def visitar(self, vertice):
        vertice.setCor(Vertice.CINZA)
        
        for v in self.adjacentes(vertice.getNome()):
            if v.getCor() == Vertice.BRANCO:
                v.setPredecessor(vertice)
                self.visitar(v)
        
        vertice.setCor(Vertice.PRETO)
        
    # Métodos auxiliares
    def contem(self, obj):
        for x in self.getVertices():
            if x.getNome() == obj:
                return True
        return False
    
    def toString(self):
        saida = ""
        for a in self.getVertices():
            saida += ("("+a.getNome()+")\n")
            if a.getCor() == 0:
                saida +=("Cor=BRANCO\n")
            if a.getCor() == 1:
                saida +=("Cor=CINZA\n")
            if a.getCor() == 2:
                saida +=("Cor=PRETO\n")
            if a.getCor() == 3:
                saida +=("Cor=AZUL\n")
            if a.getPredecessor() == None:
                saida +=("Pred= Null\n")
            if a.getPredecessor() != None:
                saida +=("Pred=("+a.getPredecessor().getNome()+")\n")
        saida += "\n"
        return saida
    
    # Declaração dos gets e sets
    def getVertices(self):
        return self.vertices
    def setVertices(self, vertices):
        self.vertices = vertices

    def getArestas(self):
        return self.arestas
    def setArestas(self, arestas):
        self.arestas = arestas

'''
Informações adicionais:
    MAX_VALUE = 2147483647
    MIN_VALUE = -2147483648
'''

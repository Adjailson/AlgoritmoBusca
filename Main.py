# coding: utf-8
from Grafo import *

g = Grafo()
'''
1º paramentro, nome do vertice
2º paramentro, valor heurístico
'''
g.addVertice("Garanhuns",88.41)
g.addVertice("Capoeiras",86.59)
g.addVertice("Jupi",67.13)
g.addVertice("Canhotinho",69.32)
g.addVertice("São Bento do Una",57.38)
g.addVertice("Lajedo",56.45)
g.addVertice("Jurema",51.13)
g.addVertice("Belo Jardim",50.15)
g.addVertice("Cachoeirinha",36.12)
g.addVertice("Panelas",41.52)
g.addVertice("São Caetano",17.80)
g.addVertice("Agrestina",18.17)
g.addVertice("Caruaru",0)
'''
Grafo não direcionado

1º paramentro, vertice origem
2º paramentro, vertice destino
3º paramentro, peso real da aresta
4º paramentro, tempo percuso
'''
g.addAresta("Garanhuns","Capoeiras",25.2, 0)
g.addAresta("Garanhuns","Jupi",23.7, 0)
g.addAresta("Garanhuns","Canhotinho",35.8, 0)

g.addAresta("Capoeiras","São Bento do Una",33.6, 0)#aresta amarela + 25
g.addAresta("Jupi","Lajedo",13.2, 0)
g.addAresta("Canhotinho","Lajedo",32, 0)

g.addAresta("São Bento do Una","Belo Jardim",25.7, 0)
g.addAresta("São Bento do Una","Lajedo",20.3, 0)#aresta laranja + 20
g.addAresta("Lajedo","Cachoeirinha",21.3, 0)
g.addAresta("Lajedo","Jurema",30.9, 0)

g.addAresta("Belo Jardim","São Caetano",33.6, 0)
g.addAresta("Cachoeirinha","São Caetano",23.1, 0)
g.addAresta("Panelas","Jurema",20.6, 0)
g.addAresta("Panelas","Agrestina",28.7, 0)

g.addAresta("São Caetano","Caruaru",22.3, 0)
g.addAresta("Agrestina","Caruaru",23.5, 0)

print(g.buscaAestrela("Garanhuns", "Caruaru"))
#Ou
#print(g.buscaGulosa("Garanhuns", "Caruaru"))

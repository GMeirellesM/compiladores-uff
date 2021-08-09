#ANALISADOR SINTÁTICO
from ply import yacc,lex
import sys, os

#estrutura
class Arvore(object):
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []

    def addfilho(self, obj):
        self.filhos.append(obj)

def imprimirArvore(a,espacos):
        for i in range(espacos):
            print(" ", end = "") 
        if(type(a.dado) == list):
            print(a.dado[1])
        else:
            print(a.dado)
        for f in a.filhos:
            imprimirArvore(f, espacos+3)

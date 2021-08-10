#ANALISADOR SINTÁTICO

from ply import yacc,lex
import sys, os
from lexico import *

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



#CONSTRUINDO A ÁRVORE
pos = []
pos.append(0)
arvore = Arvore("[PROGRAMA]")

erros = []

#EXIBIÇÃO DO ANALISADOR SINTÁTICO
print("\n                   ANALISADOR SINTÁTICO")
print("********************************************************")
print("\n")

################################################



precedence = (
    ('left', 'SOMA', 'SUBTRACAO'),
    ('left', 'MULTIPLICACAO', 'DIVISAO'),
    ('left', 'EQ', 'NEQ', 'LTE','LT','GT','GTE', 'DIF'),
    ('left', 'OR', 'AND'),
)
	
	
def p_programa(t):
    'programa : declaracoes bloco'

def p_declaracoes(t):
    'declaracoes : def_const def_var def_func'
    no_declaracoes = Arvore("[DECLARACOES]")
    arvore.addfilho(no_declaracoes)

def p_def_const(t):
    'def_const : CONST constante PONTOEVIRGULA list_const'
    no_def_const = Arvore("[DEF_CONST]")
    arvore.addfilho(no_def_const)

def p_list_const(t):
    """list_const : constante PONTOEVIRGULA list_const
    |
    """
    no_list_const = Arvore("[LIST_CONST]")
    arvore.addfilho(no_list_const)

def p_constante(t):
    'constante : id EQ const_valor'
    no_constante = Arvore("[CONSTANTE]")
    arvore.addfilho(no_constante)

def p_const_valor(t):
    """const_valor : STRING
    | exp_mat"""
    no_const_valor = Arvore("[CONST_VALOR]")
    arvore.addfilho(no_const_valor)

def p_tipo_dado(t):
    """tipo_dado : INTEGER
    | REAL
    | STRING
    | ARRAY ABRECOLCHETES numero FECHACOLCHETES OF tipo_dado
    | RECORD campos END
    """
    no_tipo_dado = Arvore("[TIPO_DADO]")
    arvore.addfilho(no_tipo_dado)

def p_campos(t):
    'campos : id DOISPONTOS tipo_dado lista_campos'
    no_campos = Arvore("[CAMPOS]")
    arvore.addfilho(no_campos)

def p_lista_campos(t):
    """lista_campos : PONTOEVIRGULA campos lista_campos
    |
    """
    no_lista_campos = Arvore("[LISTA_CAMPOS]")
    arvore.addfilho(no_lista_campos)

def p_def_var(t):
    """def_var : VAR variavel PONTOEVIRGULA list_var
    |
    """
    no_def_var = Arvore("[DEF_VAR]")
    arvore.addfilho(no_def_var)

def p_list_var(t):
    """list_var : variavel PONTOEVIRGULA list_var
    |
    """
    no_list_var = Arvore("[LIST_VAR]")
    arvore.addfilho(no_list_var)

def p_variavel(t):
    'variavel : id lista_id DOISPONTOS tipo_dado'
    no_variavel = Arvore("[VARIAVEL]")
    arvore.addfilho(no_variavel)

def p_lista_id(t):
    """lista_id : VIRGULA id lista_id
    |
    """
    no_lista_id = Arvore("[LISTA_ID]")
    arvore.addfilho(no_lista_id)

def p_def_func(t):
    """def_func : funcao def_func
    |
    """
    no_def_func = Arvore("[DEF_FUNC]")
    arvore.addfilho(no_def_func)

def p_funcao(t):
    'funcao : FUNCTION nome_funcao bloco_funcao'
    no_funcao = Arvore("[FUNCAO]")
    arvore.addfilho(no_funcao)

def p_nome_funcao(t):
    'nome_funcao : id param_func DOISPONTOS tipo_dado'
    no_nome_funcao = Arvore("[NOME_FUNCAO]")
    arvore.addfilho(no_nome_funcao)

def p_param_func(t):
    """param_func : ABREPARENTESES campos FECHAPARENTESES
    |
    """
    no_param_func = Arvore("[PARAM_FUNC]")
    arvore.addfilho(no_param_func)

def p_bloco_funcao(t):
    'bloco_funcao : def_var bloco'
    no_bloco_funcao = Arvore("[BLOCO_FUNCAO]")
    arvore.addfilho(no_bloco_funcao)

def p_bloco(t):
    'bloco : BEGIN comando PONTOEVIRGULA lista_com END'
    no_bloco = Arvore("[BLOCO]")
    arvore.addfilho(no_bloco)

def p_lista_com(t):
    """lista_com : comando PONTOEVIRGULA lista_com
    |
    """
    no_lista_com = Arvore("[LISTA_COM]")
    arvore.addfilho(no_lista_com)

def p_comando(t):
    """comando : id nome ATRIBUICAO exp_mat
    | WHILE exp_logica bloco
    | IF exp_logica bloco else
    | WRITE parametro
    | READ id nome
    """
    no_comando = Arvore("[COMANDO]")
    arvore.addfilho(no_comando)

def p_else(t):
    """else : ELSE bloco
    |
    """
    no_else = Arvore("[ELSE]")
    arvore.addfilho(no_else)

def p_lista_param(t):
    """lista_param : parametro VIRGULA lista_param
    | parametro
    |
    """
    no_lista_param = Arvore("[LISTA_PARAM]")
    arvore.addfilho(no_lista_param)

def p_exp_logica(t):
    """exp_logica : exp_comp op_logico exp_logica
    | exp_comp
    """
    no_exp_logica = Arvore("[EXP_LOGICA]")
    arvore.addfilho(no_exp_logica)

def p_op_logico(t):
    """op_logico : OR 
    | AND
    """
    no_op_logico = Arvore("[OP_LOGICO]")
    arvore.addfilho(no_op_logico)

def p_exp_comp(t):
    """exp_comp : exp_mat op_comp exp_comp
    | exp_mat
    """
    no_exp_comp = Arvore("[EXP_COMP]")
    arvore.addfilho(no_exp_comp)

def p_op_comp(t):
    """op_comp : GT
    | LT
    | EQ
    | DIF
    | NEQ
    | LTE
    | GTE
    """
    no_op_comp = Arvore("[OP_COMP]")
    arvore.addfilho(no_op_comp)

def p_exp_mat(t):
    """exp_mat : parametro op_mat exp_mat
    | parametro
    """
    no_exp_mat = Arvore("[EXP_MAT]")
    arvore.addfilho(no_exp_mat)

def p_op_mat(t):
    """op_mat : SOMA
    | SUBTRACAO
    | MULTIPLICACAO
    | DIVISAO
    """
    no_op_mat = Arvore("[OP_MAT]")
    arvore.addfilho(no_op_mat)

def p_parametro(t):
    """parametro : id nome
    | numero
    """
    no_parametro = Arvore("[PARAMETRO]")
    arvore.addfilho(no_parametro)

def p_nome(t):
    """nome : PONTO id nome
    | ABRECOLCHETES parametro FECHACOLCHETES
    | ABREPARENTESES lista_param FECHAPARENTESES
    |
    """
    no_nome = Arvore("[NOME]")
    arvore.addfilho(no_nome)

def p_id(t):
    'id : IDENTIFICADOR'
    no_id = Arvore("[ID]")
    arvore.addfilho(no_id)

def p_numero(t):
    'numero : NUMBER'
    no_numero = Arvore("[NUMERO]")
    arvore.addfilho(no_numero)


def p_error(p):
    if p is not None:
        print ("ERRO SINTATICO NA LINHA " + str(p.lexer.lineno) + " NÃO SE ESPERAVA O TOKEN  " + str(p.value))


parser = yacc.yacc()
print('-------------')

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'exemplo-gramatica.txt'

	f = open(fin, 'r')
	data = f.read()
	print (data)
	parser.parse(data, tracking=True)
	print("Parser works")
	input()





#IMPRIMINDO A ÁRVORE
imprimirArvore(arvore,0)
print("\n")

#IMPRIMINDO OS ERROS (SE HOUVER)
if(len(erros)>0):
    for e in erros:
        print(e)
    print("\n")
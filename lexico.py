#ANALISADOR LÉXICO

import ply.lex as lex

tokens = (

	'IDENTIFICADOR',
	'ATRIBUICAO',
	'PONTOEVIRGULA',
	'DOISPONTOS',
	'VIRGULA',

	'PROGRAMA',
	'PONTO',
	
	'VAR',
    'CONST',
	'BEGIN',
	'END',
	
	'IF',
	'ELSE',
	'WHILE',
	
	'AND',
	'OR',
	
	'SOMA',
	'SUBTRACAO',
	'MULTIPLICACAO',
	'DIVISAO',
	
	'EQ',
	'NEQ',
	'LT',
	'GT',
	'LTE',
	'GTE',
    'DIF',
	
	'ABREPARENTESES',
	'FECHAPARENTESES',
    'ABRECOLCHETES',
    'FECHACOLCHETES',
	'FUNCTION',

	'REAL',
	'INTEGER',
	'STRING',
	'CHAR',
    'ARRAY',
    'OF',
    'RECORD',
	'NUMBER',
	'CONST_VALOR',

    'WRITE',
    'READ',
)

#rules
t_PONTO			= r"\."

t_ATRIBUICAO	= r":="
t_PONTOEVIRGULA	= r";"
t_DOISPONTOS	= r":"
t_VIRGULA		= r","

t_SOMA			= r"\+"
t_SUBTRACAO		= r"\-"
t_MULTIPLICACAO	= r"\*"
t_DIVISAO		= r"/"

t_EQ			= r"\="
t_NEQ			= r"\<\>"
t_LT			= r"\<"
t_GT			= r"\>"
t_LTE			= r"\<\="
t_GTE			= r"\>\="
t_DIF           = r"\!"


t_ABREPARENTESES  = r"\("
t_FECHAPARENTESES = r"\)"
t_ABRECOLCHETES	  = r"\["
t_FECHACOLCHETES  = r"\]"

t_REAL			= r"(\-)*[0-9]+\.[0-9]+"
t_INTEGER		= r"(\-)*[0-9]+"
t_CONST_VALOR   = r"(\"([^\\\"]|(\\.))*\")|(\'([^\\\']|(\\.))*\')"


reserved = {
    'const' : 'CONST',
    'integer' : 'INTEGER',
    'real' : 'REAL',
    'string' : 'STRING',
    'array' : 'ARRAY',
    'of' : 'OF',
    'record' : 'RECORD',
    'end' : 'END',
    'begin' : 'BEGIN',
    'var' : 'VAR',
    'function' : 'FUNCTION',
    'while' : 'WHILE',
    'if' : 'IF',
    'write' : 'WRITE',
    'read' : 'READ',
    'else' : 'ELSE',
    'or' : 'OR',
    'and' : 'AND'
}


def t_IDENTIFICADOR(t):
	r"[a-zA-Z]([a-zA-Z0-9])*"
	if t.value.lower() in reserved:
		t.type = reserved[t.value.lower()]
	return t

def t_CHAR(t):
	r"(\'([^\\\'])\')|(\"([^\\\"])\")"
	return t

def t_STRING(t): 
    r"(\"([^\\\"]|(\\.))*\")|(\'([^\\\']|(\\.))*\')"
    escaped = 0 
    str = t.value[1:-1] 
    new_str = "" 
    for i in range(0, len(str)): 
        c = str[i] 
        if escaped: 
            if c == "n": 
                c = "\n" 
            elif c == "t": 
                c = "\t" 
            new_str += c 
            escaped = 0 
        else: 
            if c == "\\": 
                escaped = 1 
            else: 
                new_str += c 
    t.value = new_str 
    return t

def t_NUMBER(t):
	r'\d+(\.\d+)?'
	t.value = float(t.value)
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# String contendo caracteres ignorados (espaços e tabs).
t_ignore  = ' \t'

# Rule de erro
def t_error(t):
    print("Illegal character ", t.value[0])


lexer = lex.lex()

if __name__ == '__main__':
	# Constrói o lexer
	from ply import lex
	import sys 
	
	#lex.lex()
	
	if len(sys.argv) > 1:
		f = open(sys.argv[1],"r")
		data = f.read()
		f.close()
	else:
		data = ""
		while 1:
			try:
				data += input() + "\n"
			except:
				break
	
	lexer.input(data)
	
	# Tokenize
	while 1:
	    tok = lexer.token()
	    if not tok: break 
	    print(tok)
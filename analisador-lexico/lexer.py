#ANALISADOR LÉXICO

import ply.lex as lex

tokens = (

	# assignment
	'IDENTIFICADOR',
	'ATRIBUICAO',
	'PONTOEVIRGULA',
	'DOISPONTOS',
	'VIRGULA',

	# main
	'PROGRAMA',
	'PONTO',
	
	# blocks
	'VAR',
    'CONST',
	'BEGIN',
	'END',
	
	# control flow
	'IF',
	'ELSE',
	'WHILE',
	
	# logic
	'AND',
	'OR',
	
	# operations
	'SOMA',
	'SUBTRACAO',
	'MULTIPLICACAO',
	'DIVISAO',
	
	# comparations
	'EQ',
	'NEQ',
	'LT',
	'GT',
	'LTE',
	'GTE',
	
	# functions
	'ABREPARENTESES',
	'FECHAPARENTESES',
    'ABRECOLCHETES',
    'FECHACOLCHETES',
	'FUNCTION',

	# types
	'REAL',
	'INTEGER',
	'STRING',
	'CHAR',
    'ARRAY',
    'OF',
    'RECORD',

    # others
    'WRITE',
    'READ',
)

# Regular statement rules for tokens.
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


t_ABREPARENTESES  = r"\("
t_FECHAPARENTESES = r"\)"
t_ABRECOLCHETES	  = r"\["
t_FECHACOLCHETES  = r"\]"

t_REAL			= r"(\-)*[0-9]+\.[0-9]+"
t_INTEGER		= r"(\-)*[0-9]+"


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

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs).
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character ", t.value[0])



if __name__ == '__main__':
	# Build the lexer
	from ply import lex
	import sys 
	
	lex.lex()
	
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
	
	lex.input(data)
	
	# Tokenize
	while 1:
	    tok = lex.token()
	    if not tok: break      # No more input
	    print(tok)
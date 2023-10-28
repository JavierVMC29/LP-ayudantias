from ply.lex import lex

# --- Tokenizer

reservadas = {
    "class": "CLASS",
    "def": "DEF",
    "end": "END",
    "and": "AND",
    "or": "OR",
    "not": "NOT",
    "true": "TRUE",
    "false": "FALSE",
    "if": "IF",
    "elsif": "ELSIF",
    "else": "ELSE",
    "then": "THEN",
    "return": "RETURN",
    "nil": "NIL",
    "for": "FOR",
    "in": "IN",
    "while": "WHILE",
    "do": "DO",
    "print": "PRINT",
    "puts": "PUTS",
    "gets": "GETS",
    "clear": "CLEAR",
    "delete": "DELETE",
    "fetch": "FETCH"
}

tokens = [
    "MAS",
    "MENOS",
    "DIV",
    "MULTIPLICACION",
    "MODULO",
    "POTENCIA",
    "PAR_D",
    "PAR_I",
    "CORCHETE_D",
    "CORCHETE_I",
    "LLAVE_D",
    "LLAVE_I",
    "IGUAL_COMPARACION",
    "COMPARACION_COMBINADA",
    "DIFERENTE",
    "MAYOR_QUE",
    "MENOR_QUE",
    "MAYOR_IGUAL",
    "MENOR_IGUAL",
    "AND_OP",
    "OR_OP",
    "NEGACION",
    "ENTERO",
    "DECIMAL",
    "IGUAL",
    "ASIGNACION_HASH",
    "COMA",
    "NOMBRE_CLASE",
    "VARIABLE",
    "VARIABLE_GLOBAL",
    "VARIABLE_INSTANCIA",
    "VARIABLE_CLASE",
    "CADENA",
    "PUNTO"
] + list(reservadas.values())

tokens = tuple(tokens)

# Ignored characters
t_ignore = ' \t'

# Operadores aritmeticos
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACION = r'\*'
t_DIV = r'/'
t_MODULO = r'%'
t_POTENCIA = r'\*\*'

# Simbolos de agrupacion
t_PAR_D = r'\)'
t_PAR_I = r'\('
t_CORCHETE_D = r'\]'
t_CORCHETE_I = r'\['
t_LLAVE_D = r'\}'
t_LLAVE_I = r'\{'

# Operadores de comparacion
t_IGUAL_COMPARACION = r'=='
t_COMPARACION_COMBINADA = r'<=>'
t_DIFERENTE = r'!='
t_MAYOR_QUE = r'>'
t_MENOR_QUE = r'<'
t_MAYOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='

# Simbolos
t_COMA = r','
t_PUNTO = r'\.'

# Operadores logicos
t_AND_OP = r'\&\&'
t_OR_OP = r'\|\|'
t_NEGACION = r'!'


# Operadores de asignacion
t_IGUAL = r'='
t_ASIGNACION_HASH = r'=>'


def t_DECIMAL(t):
    r'[+-]?(0\.0+\d*)|(0\.\d+)|([1-9]+\d*\.\d+)'
    t.value = float(t.value)
    return t


def t_ENTERO(t):
    r'-?\d+'
    t.value = int(t.value)
    return t


def t_VARIABLE(t):
    r'[a-z_]+[a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, "VARIABLE")
    return t


def t_VARIABLE_GLOBAL(t):
    r'\$[a-z_]+[a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, "VARIABLE_GLOBAL")
    return t


def t_VARIABLE_INSTANCIA(t):
    r'@[a-z_]+[a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, "VARIABLE_INSTANCIA")
    return t


def t_VARIABLE_CLASE(t):
    r'@@[a-z_]+[a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, "VARIABLE_CLASE")
    return t


def t_NOMBRE_CLASE(t):
    r'[A-Z][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, "NOMBRE_CLASE")
    return t


def t_CADENA(t):
    r'("[^"]*"|\'[^\']*\')'
    t.type = reservadas.get(t.value, "CADENA")
    return t


def t_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token discarded

# Ignored token with an action associated with it


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handler for illegal characters


def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)


# Build the lexer object
lexer = lex()

file = open('./demo.rb', 'r')
content = file.read()

lexer.input(content)

for token in lexer:
    print(f'Line: {token.lineno} | Type: {token.type} | Value: {token.value}')


while True:
    text = input(">>>")
    lexer.input(text)
    for tok in lexer:
        print(tok)

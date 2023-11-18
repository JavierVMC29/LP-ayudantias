# Nombre: Javier Vega Molina
# Matrícula: 201911807
# Nombre: Natalia Ramirez
# Matrícula: 201911765
# Nro Grupo: 10

import ply.yacc as yacc

# Importe todos los tokens para usarlo en las reglas
from lexico import tokens

resultado_sintactico = []


def p_sentencias(p):
    '''sentencias : impresion
	              | ingreso
	              | asignacion
	              | operacion
	              | valor
	              | empty
	'''


def p_booleano(p):
    '''booleano : TRUE
			    | FALSE
	'''


def p_valor(p):
    '''valor : VARIABLE
	         | ENTERO
	         | DECIMAL
	         | CADENA
	         | booleano
	         | array
	         | hash
	'''


def p_asignacion(p):
    '''
    asignacion : VARIABLE IGUAL valor
               | VARIABLE IGUAL operacion
               | argumentos IGUAL valores
               | VARIABLE_GLOBAL IGUAL valor
               | VARIABLE_INSTANCIA IGUAL valor
               | VARIABLE_CLASE IGUAL valor
    '''


def p_impresion(p):
    '''impresion : PRINT valor
				 | PUTS valor
				 | PRINT PAR_I valor PAR_D
				 | PUTS PAR_I valor PAR_D
	'''


def p_ingreso(p):
    'ingreso : GETS'


# Javier Vega begin

# Operaciones aritmeticas

def p_operadorAritmetico(p):
    '''operadorAritmetico : MAS
						  | MENOS
						  | MULTIPLICACION
						  | DIV
						  | MODULO
						  | POTENCIA
	'''


def p_operacionAritmetica(p):
    'operacionAritmetica : valor repite_operacionAritmetica'


def p_repite_operacionAritmetica(p):
    '''
    repite_operacionAritmetica : operadorAritmetico valor
	                           | operadorAritmetico valor repite_operacionAritmetica
   '''


def p_operacionAritmeticaFuncional(p):
    'operacionAritmeticaFuncional : valor repite_operacionAritmeticaFuncional'


def p_repite_operacionAritmeticaFuncional(p):
    '''repite_operacionAritmeticaFuncional : PUNTO operadorAritmetico PAR_I valor PAR_D
	                                       | PUNTO operadorAritmetico PAR_I valor PAR_D repite_operacionAritmeticaFuncional
	'''


# Operaciones de comparacion

def p_operadorComparacion(p):
    '''operadorComparacion : MAYOR_QUE
	                       | MENOR_QUE
	                       | MAYOR_IGUAL
	                       | MENOR_IGUAL
	                       | DIFERENTE
	                       | IGUAL_COMPARACION
	                       | COMPARACION_COMBINADA
	'''


def p_operacionComparacion(p):
    '''operacionComparacion : valor repite_operacionComparacion
                            | valor operacionComparacionFuncional
	'''


def p_repite_operacionComparacion(p):
    '''repite_operacionComparacion : operadorComparacion valor
	                               | operadorComparacion valor repite_operacionComparacion
	'''


def p_operacionComparacionFuncional(p):
    'operacionComparacionFuncional : valor repite_operacionComparacionFuncional'


def p_repite_operacionComparacionFuncional(p):
    '''repite_operacionComparacionFuncional : PUNTO operadorComparacion PAR_I valor PAR_D
	                                        | PUNTO operadorComparacion PAR_I valor PAR_D repite_operacionComparacionFuncional
	'''


# Operaciones logicas

def p_operadorLogico(p):
    '''operadorLogico : AND_OP
	                  | OR_OP
	                  | AND
	                  | OR
	                  | NEGACION
	                  | NOT
	'''


def p_operacionLogica(p):
    '''operacionLogica : valor repite_operacionLogica
	'''


def p_repite_operacionLogica(p):
    '''repite_operacionLogica : operadorLogico valor
	                          | operadorLogico valor repite_operacionLogica
	'''


def p_operacionLogicaFuncional(p):
    'operacionLogicaFuncional : valor repite_operacionLogicaFuncional'


def p_repite_operacionLogicaFuncional(p):
    '''
    repite_operacionLogicaFuncional : PUNTO operadorLogico PAR_I valor PAR_D
	                                | PUNTO operadorLogico PAR_I valor PAR_D repite_operacionLogicaFuncional
	'''


# Operaciones

def p_operacion(p):
    '''operacion : operacionAritmetica
	             | operacionAritmeticaFuncional
	             | operacionComparacion
	             | operacionComparacionFuncional
	             | operacionLogica
	             | operacionLogicaFuncional
	'''


# Condicionales

def p_condicion(p):
    '''condicion : booleano
	             | operacionComparacion
	             | operacionLogica
	             | operacionComparacionFuncional
	             | operacionLogicaFuncional
	'''


def p_sentencias_condicional(p):
    '''sentencias : IF PAR_I condicion PAR_D
                  | IF PAR_I condicion PAR_D THEN
                  | IF condicion THEN
                  | IF condicion
	              | ELSIF PAR_I condicion PAR_D
	              | ELSIF PAR_I condicion PAR_D THEN
	              | ELSIF condicion THEN
	              | ELSIF condicion
	              | ELSE
	'''


# Estructuras de datos

# Natalia Ramirez begin

# Array

def p_array(p):
    'array : CORCHETE_I valores CORCHETE_D'


def p_valoresSeparadosComa(p):
    'valores : valor repite_valores'


def p_repite_valoresSeparadosComa(p):
    '''
    repite_valores : COMA valor
                   | COMA valor repite_valores
    '''


# Natalia Ramirez end

# Javier Vega begin

# Hash

def p_hash(p):
    '''
    hash : LLAVE_I campos LLAVE_D
    '''


def p_camposSeparadosComa(p):
    'campos : valor ASIGNACION_HASH valor repite_campos'


def p_repite_camposSeparadosComa(p):
    '''
    repite_campos : COMA valor ASIGNACION_HASH valor
                  | COMA valor ASIGNACION_HASH valor repite_campos
    '''


# Javier Vega end

# Natalia Ramirez begin

# Funciones array

def p_func_clear(p):
    '''
    sentencias : VARIABLE PUNTO CLEAR PAR_I PAR_D
    '''


def p_func_delete(p):
    '''
    sentencias : VARIABLE PUNTO DELETE PAR_I valor PAR_D
    '''


def p_indexar_array(p):
    '''
    sentencias : VARIABLE CORCHETE_I valor CORCHETE_D
    '''


# Funciones hash

def p_func_fetch(p):
    '''
    sentencias : VARIABLE PUNTO FETCH PAR_I valor PAR_D
               | VARIABLE PUNTO FETCH PAR_I valor COMA valor PAR_D
    '''


def p_llamada_funcion_general(p):
    '''
    sentencias : VARIABLE PUNTO VARIABLE PAR_I PAR_D
               | VARIABLE PUNTO VARIABLE PAR_I valores PAR_D
               | VARIABLE PUNTO VARIABLE PAR_I valor PAR_D
    '''


def p_casting(p):
    '''
    sentencias : valor PUNTO VARIABLE
    '''


# Natalia Ramirez end

# Javier Vega begin

# Bucle while

def p_sentencias_while(p):
    '''
    sentencias : WHILE condicion DO
               | WHILE condicion
               | WHILE PAR_I condicion PAR_D DO
               | WHILE PAR_I condicion PAR_D
    '''


# Bucle for

def p_expresion(p):
    'expresion : PAR_I ENTERO PUNTO PUNTO ENTERO PAR_D'


def p_sentencias_for(p):
    '''
    sentencias : FOR VARIABLE IN expresion DO
               | FOR VARIABLE IN expresion
    '''


# Javier Vega end

# Javier Vega begin

# Funciones

def p_sentencias_def(p):
    '''
    sentencias : DEF VARIABLE
               | DEF VARIABLE PAR_I PAR_D
               | DEF VARIABLE PAR_I argumentos PAR_D
    '''


def p_argumentos(p):
    '''
    argumentos : VARIABLE
               | VARIABLE repite_argumento
    '''


def p_repite_argumento(p):
    '''
    repite_argumento : COMA VARIABLE
                     | COMA VARIABLE repite_argumento
    '''


# Clases

def p_sentencias_clase(p):
    'sentencias : CLASS NOMBRE_CLASE'


def p_sentencias_atributosClase(p):
    '''
    sentencias : VARIABLE_CLASE
               | VARIABLE_INSTANCIA
    '''


def p_sentencias_finalBloque(p):
    'sentencias : END'


def p_sentencias_return(p):
    '''
    sentencias : RETURN
               | RETURN valor
               | RETURN VARIABLE_CLASE
               | RETURN VARIABLE_INSTANCIA
               | RETURN NIL
    '''


# Imprime errores según las reglas
def p_error(p):
    global resultado_sintactico
    resultado_sintactico.clear()
    if p:
        resultado = "Error sintactico de tipo: {} en el valor: {}".format(str(p.type), str(p.value))
        print(resultado)
    else:
        resultado = "Error sintactico: {}".format(p)
        print(resultado)
    resultado_sintactico.append(resultado)


def p_empty(p):
    'empty :'
    pass


# Construye el parser
sintactico = yacc.yacc()



def analisis_sintactico(data):
    linea = 0
    global resultado_sintactico
    resultado_sintactico.clear()
    print(resultado_sintactico)

    for item in data.splitlines():
        linea += 1
        # print("item: ", item)
        if item:
            gram = sintactico.parse(item)
            # print("gram: ", gram)
            if gram is None:
                resultado_sintactico.append("Linea: " + str(linea) + "  Info: No hay errores!")
            else:
                resultado_sintactico.append("Linea: " + str(linea) + "  Info: " + str(gram))
        else:
            print("data vacia")

    print("result: ", resultado_sintactico)
    return resultado_sintactico


print("Analisis sintactico terminado... :)")
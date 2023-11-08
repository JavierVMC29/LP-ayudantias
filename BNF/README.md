# BNF

## ¿Qué es BNF?

BNF, que significa "Backus-Naur Form," es una notación utilizada en informática para describir la gramática de lenguajes formales, como lenguajes de programación, lenguajes de marcado (como HTML y XML), y otros sistemas de notación. Fue desarrollada por John Backus y Peter Naur en la década de 1960 como un método para representar de manera concisa y precisa la estructura sintáctica de un lenguaje.

BNF se utiliza comúnmente en la especificación de la sintaxis de lenguajes de programación. En una especificación BNF, las reglas gramaticales se definen en términos de producciones que describen cómo se forman las sentencias y las estructuras del lenguaje. Estas producciones suelen utilizar símbolos no terminales (que representan categorías gramaticales) y símbolos terminales (que representan tokens o palabras clave reales en el lenguaje).

Por ejemplo, aquí hay una pequeña parte de una especificación BNF para expresiones matemáticas simples:

```
<expresion> ::= <termino> '+' <expresion>
             | <termino> '-' <expresion>
             | <termino>

<termino>   ::= <factor> '*' <termino>
             | <factor> '/' <termino>
             | <factor>

<factor>    ::= '(' <expresion> ')'
             | <numero>
```

En este ejemplo, `<expresion>`, `<termino>`, y `<factor>` son símbolos no terminales, y los operadores (`+`, `-`, `*`, `/`) y paréntesis son símbolos terminales. Esta notación permite definir de manera precisa cómo se pueden construir expresiones matemáticas en términos de términos, factores y operadores.

BNF se ha convertido en un estándar en la descripción de la sintaxis de lenguajes y se utiliza ampliamente en la documentación de lenguajes de programación, compiladores, analizadores léxicos y otros componentes del desarrollo de software.

## Ejercicios

### 1. Defina reglas BNF para validar las siguientes consultas SQL:

```sql
Delete from company where id=3;

Select value1, value2 from table where id=3 and name<>'abc';

Select  * from empleado where rating>=5.0 and rating<=8.0;
```

**Respuesta:**

```bnf
<nombreTabla> ::= [a-z]+
<nombreAtributo> ::= [a-z]+
<entero> ::= [0-9]+
<decimal> ::= [0-9]+ ("." [0-9]+ | ".0")
<string> ::= "'" [a-z]* "'"
<operadorComparacion> ::= ">" | "<" | "<=" | ">=" | "=" | "<>"
<operadorLogico> ::= "and" | "or"
<espacio> ::= " " | "\n" | " " <espacio> | "\n" <espacio>
<coma> ::= ","
<asterisco> ::= "*"
<select> ::= "select" | "SELECT"
<delete> ::= "delete" | "DELETE"
<from> ::= "from" | "FROM"
<where> ::= "where" | "WHERE"
<colon> ::= ";"

<valor> ::= <entero> | <decimal> | <string>
<atributos> ::= <nombreAtributo> | <nombreAtributo> <coma> <espacio>  <atributos>
<comparacion> ::= <nombreAtributo> <espacio> <operadorComparacion> <espacio> <valor>
<condiciones> ::= <comparacion> | <comparacion> <espacio> <operadorLogico> <espacio> <condiciones>
<selector> ::= <atributos> | <asterisco>

<sentencia_select> ::= <select> <espacio> <selector> <espacio> <from> <espacio> <nombreTabla> (<espacio> <where> <espacio> <condiciones>)? (<colon>)?
<sentencia_delete> ::= <delete> <espacio> <from> <espacio> <nombreTabla> (<espacio> <where> <espacio> <condiciones>)? (<colon>)?

<sentencia_sql> ::= <sentencia_select> | <sentencia_delete>

```

### 2. Defina reglas BNF para validar condicionales anidados en Ruby

**Ejemplo:**

```ruby
if a == 10
  a = 1
  if a == 10
    b = 1
    b = 1
    b = 1
    if a == 1
      a = 1
      if a == 1
        a = 1
      end
    end
  end
end
```

**Respuesta:**


```bnf
<espacio> ::= " " | "\n" | " " <espacio> | "\n" <espacio>
<espacio_simple> ::= " " | " " <espacio_simple>
<entero> ::= [0-9]+ | "-" [1-9]+
<texto> ::= [a-z]* | [a-z]* " " <texto>
<cadena> ::= "'" <texto> "'"
<variable> ::= [a-z]+
<igual> ::= "="
<comparacion> ::= "==" | "<=" | ">=" | "<" | ">" | "<=>"
<finLinea> ::= "\n" | "\n" <espacio_simple>
<end> ::= "end"
<else> ::= "else"
<elsif> ::= "elsif"
<if> ::= "if"

<asignacion> ::= <variable> (<espacio_simple>)? <igual> (<espacio_simple>)? <entero>
<condicion> ::= <valor> (<espacio_simple>)? <comparacion> (<espacio_simple>)? <valor>
<valor> ::= <entero> | <cadena> | <variable>
<linea> ::= <asignacion> (<finLinea>)?
<sentenciaElse> ::= <else> (<espacio>)? <finLinea> <cuerpoElse>
<cuerpoElse> ::= (<espacio>)? <linea> (<espacio>)? <finLinea> | <sentenciaIf> <finLinea>
<sentenciaElsif> ::= <elsif> <espacio_simple> <condicion> (<espacio_simple>)? <finLinea> <cuerpoIf>
<cuerpoIf> ::= <linea> <finLinea> | <sentenciaIf> <finLinea> | <linea> <finLinea> <sentenciaElsif> | <linea> <finLinea> <cuerpoIf>
<sentenciaIf> ::= <if> <espacio_simple> <condicion> (<espacio_simple>)? <finLinea> <cuerpoIf> (<espacio>)? <end> (<finLinea>)? | <if> <espacio_simple> <condicion> (<espacio_simple>)? <finLinea> (<espacio>)? <cuerpoIf> (<espacio>)? <sentenciaElse> (<espacio>)? <end> (<finLinea>)?
```

### 3. Defina reglas BNF para validar BNF

**Respuesta:**

```bnf
<nombre> ::= [a-z]+
<string> ::= "'" [a-z]* "'"
<etiqueta> ::= "<" <nombre> ">"
<igual> ::= "::="
<or> ::= "|"
<espacio> ::= " "
<regex> ::= "[" [a-z] "-" [a-z] "]" | "[" [A-Z] "-" [A-Z] "]" | "[" [0-9] "-" [0-9] "]"
<valor> ::= <etiqueta> | <regex> | <string>
<lista> ::= <listaSimple> | <listaSimple> <espacio> <or> <espacio> <lista>
<listaSimple> ::= <valor> | <valor> <espacio> <listaSimple>
<expresion> ::= <etiqueta> <espacio> <igual> <espacio> <lista>
```

### 4. Defina reglas BNF para validar operaciones matemáticas

**Respuesta:**

```bnf
<operacion> ::= <numero> (<espacio>)? <operador> (<espacio>)? <numero> | <numero> (<espacio>)? <operador> (<espacio>)? <operacion>
<numero> ::= (<menos>)? <entero> | (<menos>)? <decimal>
<entero> ::= [0-9]+
<decimal> ::= [0-9]+ "." [0-9]+
<operador> ::= "+" | "-" | "*" | "/" | "%" | "**"
<espacio> ::= " " | " " <espacio>
<menos> ::= "-"
```

### 5. Defina reglas BNF para validar sentencias de un lenguaje de programación

**Respuesta:**

```bnf
<programa> ::= <sentencias> | <sentencias> <saltoLinea> <programa>

<sentencias> ::= <funcion> | <asignacion> | <operacionM>

<funcion> ::= <nombreFuncion> <parI> (<espacio>)? <parametros> (<espacio>)? <parD> | <impresion> | <ingreso>
<ingreso> ::= "input" <parI> (<espacio>)? <cadena> (<espacio>)? <parD>
<impresion> ::= "print" <parI> (<espacio>)? <valor> (<espacio>)? <parD>

<asignacion> ::= <variable> (<espacio>)? <igual> (<espacio>)? <valor> | <variable> (<espacio>)? <igual> (<espacio>)? <ingreso>
<operacionM> ::= <valorN> (<espacio>)? <operadorM> (<espacio>)? <valorN>

<parametros> ::= <valor> (<espacio>)? <coma> (<espacio>)? <valor> | <valor> (<espacio>)? <coma> (<espacio>)? <parametros>

<nombreFuncion> ::= [a-z]+
<valor> ::= <valorN> | <booleano> | <variable> | <operacionM> | <cadena>
<valorN> ::= <entero> | <flotante> | <variable>
<entero> ::= [0-9]+
<flotante> ::= <entero> <punto> <entero>
<booleano> ::= "True" | "False"
<variable> ::= [a-z]+
<cadena> ::= "'" ([a-z] | [0-9] | [A-Z] | " " | ":")* "'"
<operadorM> ::= "+" | "-" | "*" | "/" | "**" | "//" | "%"
<saltoLinea> ::= "\n"
<punto> ::= "."
<espacio> ::= " " | " " <espacio>
<coma> ::= ","
<parI> ::= "("
<parD> ::= ")"
<igual> ::= "="
```

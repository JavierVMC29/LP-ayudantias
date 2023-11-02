# Expresiones regulares

## ¿Qué es una expresión regular?

Las expresiones regulares (regex) son patrones de texto que siguen reglas específicas y se utilizan para buscar, validar y manipular cadenas de caracteres de forma eficiente. Permiten definir reglas de búsqueda basadas en caracteres y metacaracteres, facilitando tareas como validar formatos (correo electrónico, número de teléfono), buscar patrones y extraer información específica de un texto. Son herramientas poderosas y versátiles en programación, procesamiento de texto, análisis de datos y más.

## ¿Qué son los metacaracteres?

Los metacaracteres en expresiones regulares son caracteres especiales con un significado especial que no se interpreta de manera literal, sino que se utilizan para representar ciertos patrones o conjuntos de caracteres. Estos metacaracteres tienen un propósito específico en la definición de reglas para la búsqueda, validación o manipulación de texto utilizando expresiones regulares.

Aquí hay algunos ejemplos de metacaracteres comunes y sus significados:

- . (Punto): Representa cualquier carácter, excepto un salto de línea.
- \_: Representa cero o más repeticiones del elemento anterior.
- +: Representa una o más repeticiones del elemento anterior.
- ?: Representa cero o una repetición del elemento anterior (opcional).
- ^: Representa el inicio de la cadena.
- $: Representa el final de la cadena.
- []: Define un conjunto de caracteres permitidos. Por ejemplo, [a-z] representa cualquier letra minúscula.
- | (Barra vertical): Representa una alternativa. Por ejemplo, a|b coincide con "a" o "b".
- (): Agrupa expresiones y permite aplicar operaciones como repetición (\_, +, ?) al grupo.

Estos metacaracteres, combinados con caracteres alfanuméricos y otros símbolos, permiten crear patrones complejos para buscar o manipular texto de manera precisa. Es importante comprender el significado de estos metacaracteres al trabajar con expresiones regulares para poder crear patrones efectivos y útiles.

## ¿Qué es Rubular?

[Rubular](https://rubular.com/) es una herramienta en línea que brinda un entorno interactivo para probar, experimentar y verificar expresiones regulares en el contexto del lenguaje de programación Ruby.

Rubular proporciona una interfaz de usuario intuitiva que permite a los usuarios ingresar expresiones regulares y aplicarlas a una cadena de texto. Permite probar y verificar si la expresión regular coincide con diferentes partes de la cadena, lo que es útil para depurar y perfeccionar las expresiones regulares antes de implementarlas en su código.

## Ejercicios

### 1. Crear una expresion regular para validar correos de Gmail

**Condiciones:**

- El nombre de usuario debe tener entre 6 y 30 caracteres.
- Puede contener letras y numeros.

**Ejemplos:**

- javier@gmail.com
- holamundo@gmail.com
- miguel01@gmail.com

**Solución:**

```
^[a-z0-9]{6,30}@gmail\.com$
```

### 2. Crear una expresion regular para validar edades entre 21 y 100

**Condiciones:**

- El 21 esta incluido en el rango.
- El 100 no se incluye en el rango.

**Ejemplos:**

- 21
- 45
- 99

**Solución:**

```
^2[1-9]|[3-9][0-9]$
```

### 3. Crear una expresion regular para validar tipos de sangre

**Condiciones:**

- Hacer match con todos los tipos de sangre.

**Ejemplos:**

- A+
- B+
- O+
- AB+
- A-
- B-
- O-
- AB-

**Solución:**

```
^([ABO]|AB)[+-]$
```

### 4. Crear una expresion regular para validar si un código postal es de Ecuador.

**Condiciones:**

- Primeras 2 letras EC (obligatorio).
- Luego 2 dígitos de las 26 provincias 01-26
- Longitud total de 6 dígitos y solo dígitos.

**Ejemplos:**

- EC119320
- EC240292
- EC029393

**Solución:**

```
^EC(0[1-9]|1\d|2[0-6])\d{4}$
```

### 5. Crear una expresion regular para validar valores flotantes en Python.

**Condiciones:**

- Hacer math con todas las formas de escribir un flotante en Python

**Ejemplos:**

- 20.534
- .0292
- 29.
- float(3)

**Solución:**

```
^\d+\.\d*|\d*\.\d+|float\(\d+\)$
```

### 6. Crear una expresion regular para validar rutas en equipos (paths).

**Condiciones:**

- Hacer match con los paths de los ejemplos.

**Ejemplos:**

- C:/Windows/System32
- E:/Carpeta
- F:/102020/20202/a
- G:/ACCESS/FILE

**Solución:**

```
^[A-Z]:(\/[A-Za-z0-9]+)+$
```

### 7. Crear una expresion regular para validar si una plataforma pertenece a ESPOL.

**Condiciones:**

- Hacer match con los sitios de los ejemplos.

**Ejemplos:**

- www.espol.edu.ec/pregrado
- www.fiec.espol.edu.ec/carreras/icc
- mibosque3d.espol.edu.ec
- www.cibe.espol.edu.ec/noticias

**Solución:**

```
^(www\.)?([A-Za-z0-9]+\.)espol\.edu\.ec(\/[A-Za-z0-9\-]+)*
```

### 8. Crear una expresion regular para validar si una plataforma pertenece a ESPOL.

**Condiciones:**

- Hacer match con las etiquetas de los ejemplos.

**Ejemplos:**

- `<img src=”image.jpg” alt=”imagen”>`
- `<img src=”image1.jpg” alt=’imagen1’>`
- `<img src=”image_1.png” alt=”imagen_1”>`
- `<img src=”image-1.jpg” alt=”imagen-1”>`
- `<img src=”image.jpg” alt=”imagen”>`

**Solución:**

```
^<img src\s*=\s*("[\w-]+\.(jpg|png)"|'\w+\.(jpg|png)')\s+alt\s*=\s*("[\w-]*"|'\w*')\s*>$
```

### 9. Crear una expresion regular para validar formato de fecha.

**Condiciones:**

- Hacer match con el formato de los ejemplos.

**Ejemplos:**

- 2021-06-06 12h12m01s
- 2000-12-25 23h59m45s
- 1990-09-20 09h20m30s
- 1970-01-31 00h01m59s

**Solución:**

```
^(19[7-9][0-9]|2[0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1]) (0[0-9]|1[0-9]|2[0-3])h([0-5][0-9])m([0-5][0-9])s$
```

### 9. Crear una expresion regular para validar numeros romanos.

**Condiciones:**

- Validar numeros romanos del 1 al 50.

**Ejemplos:**

- I
- IV
- XX
- XL
- XLIX
- L

**Solución:**

```
^(XL|X{0,3})(IX|IV|V?I{0,3})L?$
```

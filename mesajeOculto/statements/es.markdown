# Description

Mich "El mapache" Forger es un espia en territorio enemigo, por fin logro obtener informacion valiosa, por lo cual necesita ayuda para poder mandar un mensaje secreto, el tiene una lista con contraseñas muy importantes para el enemigo. El tiene diseñado un sistema de envio, solamente que el mensaje no tiene que contener letras, solamente una lista de numeros asi el sistema enemigo no lo detecta.

Las contraseñas solamente tienen letras minusculas y como el campo de batalla es feroz se deben de hacer la menor cantidad de preguntas al cuartel general.

Ayuda a Mich a crear un sistema que codifique y decodifique el mensaje.

# Implementacion

Debes crear una funcion `void encode(int N, int M, char words[1000][1000])` y `void decode()` para poder codificar y decodificar respectivamente el mensaje, el cuartel general creo algunas herramientas para ti:

* `int getMessage(int i)`
* `int getMessageSize()`
* `int getWordLength(int i)`
* `void send(int N, int msg[1000])`
* `void verifyMessage(int N, int M, char decodedWords[][1000])`

**Importante** Tienes que codificar el mensaje en un arreglo de enteros para que al enviarlo sea indetectable a los enemigos.

# Tu funcion encode

`void encode(int N, int M, char words[1000][1000])`

## Descripcion

Debes crear una funcion tipo `void` que reciba los siguientes parametros

* `int N` Un entero que representa el numero de contraseñas.
* `int M` Un entero que representa la longitud de la contraseña mas larga.
* `char[1000][1000] words` Una matriz de caracteres que representa las contraseñas, cada fila representa una contraseña.

La funcion al final debe llamar a la funcion `send(int N, int msg[1000])` con el mensaje codificado.

# Tu funcion decode

`void decode()`

## Descripcion

Debes implementar una funcion tipo `void` que decodifique el mensaje, no tiene que recibir nada y al final de la implementacion tiene que llamar a la funcion `verifyMessage(int N, int M, char decodedWords[][1000])`.

# Funcion del evaluador getMessage

`int getMessage(int i)`

## Descripcion

Funcion que regresa un entero, una vez mandado el mensaje esta funcion regresa el valor del mensaje en la posicion $i$.

Si el mensaje no a sido enviado o el indice no existe (si $i \ge N$ donde $N$ es el tamaño del arreglo), la funcion retorna -1.

### Ejemplo

||input
Funcion
||output
Valor devuelto
||description
Descripcion
||input
getMessage(2)
||output
14
||description
El mensaje que se envio es codificado de la siguiente manera $[1, 23, 14, 15]$
||end

# Funcion del evaluador getMessageSize

## Descripcion 

Funcion que regresa un entero, una vez mandado el mensaje esta funcion regresa la longitud del mensaje.

### Ejemplo

||input
Funcion
||output
Valor devuelto
||description
Descripcion
||input
getMessageSize()
||output
4
||description
El mensaje que se envio es codificado de la siguiente manera $[1, 23, 14, 15]$
||end

# Funcion del evaluador getWordLength

`int getWordLength(int i)`

## Descripcion

Funcion que regresa un entero, recibe un indice que regresa la longitud de la palabra $i$.

### Ejemplo

||input
Funcion
||output
Valor devuelto
||description
Descripcion
||input
getWordLength(1)
||output
2
||description
Tenemos las siguientes palabras en el mensaje $[mensaje, de, prueba]$.
||end

# Funcion del evaluador send

`void send(int N, int msg[1000])`

## Descripcion

Funcion que envia el mensaje, este recibe $N$ que es la longitud del arreglo codificado y $msg$ que es el mensaje en formato de un arreglo.

### Ejemplo

||input
Funcion
||output
Valor devuelto
||description
Descripcion
||input
send(4,arr)
||output
null
||description
Se codifico un mensaje y dio como resultado el siguiente arreglo `arr = [2,4,12,4]`,
||end

# Funcion del evaluador verifyMessage

`void verifyMessage(int N, int M, char decodedWords[][1000])`

## Descripcion

Funcion que verifica si el mensaje decodificado es igual al mensaje original, recibe $N$ que es el numero de palabras, $M$ la longitud de la palabra mas larga y $decodedWords$ una matriz de caracteres que representa las palabras, cada renglon representa una palabra.

### Ejemplo

||input
Funcion
||output
Valor devuelto
||description
Descripcion
||input
decodedWords(2,4,decodedWords)
||output
null
||description
Las palabras decodificadas fueron $Un$ y $Hola$.
||end

# Evaluacion

Tu programa dara 0 si no se decodifica de manera adecuada osea que lo que decodificas no sea igual al valor original. De lo contrario la puntuacion dependera de las siguientes subtareas.

# Subtareas

- **Subtask 1 (20 puntos) agrupados**
    - Puedes usar la funcion `getWordgetWordLength` las veces que quieras.
    - El tamaño maximo del arreglo codificado no tiene limites.
- **Subtask 2 (20 puntos) agrupados**
    - Puedes usar $2N$ la funcion `getWordgetWordLength`.
    - El tamaño maximo del arreglo codificado no puede ser mayor a $N*M$
- **Subtask 3 (20 puntos) agrupados**
    - Puedes usar $N$ la funcion `getWordgetWordLength`.
    - El tamaño maximo del arreglo codificado no puede ser mayor a $N*M$
    - Todas las palabras comienzan con la letra 'a'.
- **Subtask 4 (20 puntos) agrupados**
    - Puedes usar $N$ la funcion `getWordgetWordLength`.
    - El tamaño maximo del arreglo codificado no puede ser mayor a $S+N$ donde $S$ es la suma de las longitudes de la palabra.
- **Subtask 5 (20 puntos) agrupados**
    - No puedes usar la funcion `getWordgetWordLength`.
    - El tamaño maximo del arreglo codificado no puede ser mayor a $S+N$ donde $S$ es la suma de las longitudes de la palabra.
- **Para todas las subtareas**
    - $ 1 \le N \le 100$
    - $ 1 \le M \le 10$

# Experimentación

{{libinteractive:download}}

El evaluador de prueba recibe el archivo `sample.in` con los valores $N$ y $M$, representan el numero de contraseñas y la longitud de la contraseñas mas larga. Seguido de $N$ lineas con $s_i$ que representa la longitud de la contraseñas y la contraseñas.


```
2 5
4 hola
5 mundo
```

_IMPORTANTE:_ El evaluador de prueba y el evaluador final que se usará para calificar tu solución son diferentes. El evaluador de prueba tiene la depuración de tu solución y puede implementar algunas de sus funciones de distinta manera.
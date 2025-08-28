Trabajo Práctico n.º 1
======================

Teoría de Algoritmos - 2c 2025
Trabajo Práctico 1

## Lineamientos básicos

- El trabajo se realizará en grupos de cinco personas.

- Un integrante del grupo deberá entregar el informe en formato pdf en nombre del grupo en el aula virtual de la materia..

- Cada integrante del grupo deberá entregar código fuente en (.zip) en el aula virtual de la materia. El .zip no debe contener carpetas en su interior, si no, solo 2 archivos ("escenario.py" y "extraterrestres.py").

- El lenguaje de implementación a utilizar es Python. No está permitido utilizar librerías externas.

- El programa a entregarse debe cumplir con los lineamientos mencionados en el enunciado. Si los mismos no son cumplidos con exactitud, el trabajo no será aprobado y deberá ser re-entregado con las correcciones.

- El informe debe presentar carátula con el nombre del grupo, datos de los integrantes, fecha y número de entrega. Debe incluir número de hoja en cada página. No debe superar las 25 páginas + carátula + índice + referencias.

- Debe entregar en el informe las fuentes consultadas en una sección de referencias.

- En caso de re-entrega, entregar luego del informe original un apartado con las correcciones realizadas

## Parte 1: Escenario espejado.

Una empresa musical desea diseñar un escenario para conciertos. Por las características del terreno, se sabe que el mismo deberá ser construido en forma de V.
Se cuenta con un conjunto N de sectores, los cuales continenen una cantidad Y de butacas cada uno.
La empresa debe ubicar cada sector en una fila del escenario, con la restricción que cada sector a derecha e izquierda del mismo contenga la misma cantidad de butacas, es decir, que sea espejado.
Al tener un escenario en forma de V, solo podrá haber 1 sector ubicado a la izquierda del escenario y 1 sector a la derecha. A excepción de la primera fila, que puede contener 1 sector o no tener ninguno.

El valor de venta de las entradas será mayor cuanto más alejado del centro se encuentre el sector. Obviamente la empresa busca maximizar las ganancias.

Para no tener problemas, en caso de la empresa no pueda construir un escenario espejado, comunicará que no podrá realizarlo. Caso contrario, deberá indicar cómo construir el escenario


**Se pide:**

1. Desarrollar un algoritmo Greedy que indique cómo ubicar cada sector en el escenario en O(N), tanto de complejidad temporal como espacial.

2. Explicar y justificar tanto el algoritmo como las complejidades
  
3. Explicar y justificar la ptimalidad del algoritmo.

5. Explicar y justificar por qué es Greedy el algoritmo.

6. Programar la solución.


### Formato de los archivos:

El archivo a ejecutar se debe llamar “escenario.py”

Debe recibir por parámetro los sectores con la cantidad de asientos que se deben construir. Por ejemplo "escenario.py 978695587655"

La salida del programa debe ser por pantalla indicando cómo se arma cada escenario.

Además, dentro del archivo se debe implementar una función llamada `ejecucion(sectores)` que reciba por parámetro los sectores.


**Ejemplos de ejecución:**

`escenario.py 978695587655`

debe retornar `978655556879` por pantalla para formar el siguiente escenario en forma de V

```
9          9
 7        7
  8      8
   6    6
    5  5
     55
```

Otras posibilidades válidas también son 559786687955, 598756657895, etc

`escenario.py 113`

debe retornar `131` por pantalla para formar el siguiente escenario en forma de V

```
1 1
 3
```

`escenario.py 1134`

debe retornar `no es posible realizar el escenario` por pantalla



## Parte 2: Detectores de mentiras

El profesor Charles Lying tiene N detectores de mentiras que, en "teoría", son capaces de probarse entre sí. Y para hacerlo, se realiza de a pares. Cuando el equipo está cargado, cada detector prueba al otro y reporta si es confiable o no. Un detector confiable siempre informa con precisión si el otro detector es confiable o no, pero el profesor no puede confiar en la respuesta de un detector no confiable. Así, los cuatro posibles resultados de una prueba son los siguientes:

| Detector 1     | Detector 2     | Resultado |
|----------------|----------------|-----------|
| D2 funciona    | D1 funciona    | Ambos funcionan correctamente |
| D2 funciona    | D1 no funciona | Al menos alguno de los dos falla   |
| D2 no funciona | D1 funciona    | Al menos alguno de los dos falla   |
| D2 no funciona | D2 no funciona | Al menos alguno de los dos falla   |


Se sabe que más de la mitad de los detectores funcionan correctamente. Ayudar al profesor a encontrar 1 detector que con seguridad funcione correctamente.


**Se pide:**

1. Presentar una propuesta mediante división y conquista que resuelva este problema.

2. Brindar la ecuación de recurrencia y obtener su complejidad mediante el teorema maestro.

3. Presentar pseudocódigo.

4. Brindar un ejemplo de funcionamiento.



## Parte 3: Programación de otro planeta

Año 2030. Los programadores son la única salvación para terminar con la 5ta guerra mundial, esta vez contra extraterrestres. Se han interceptado mensajes de los alienígenas donde todos tienen un factor en común: las frases contienen palabras que se leen igual de izquierda a derecha que de derecha a izquierda. Se cree que es su forma de comunicación. La palabra más larga de cada frase que cumple con estas características es la que buscamos.
Diseñar un algoritmo que permita detectar estas palabras es vital para acticipar sus movimientos.

Ya que para el corriente año no existen problemas de memoria, el algoritmo diseñado debe ser de programación dinámica.


**Se pide:**

1. Presentar una propuesta mediante programación dinámica que resuelva este problema.

2. Analice la complejidad espacial y temporal de su propuesta.

3. De un breve ejemplo paso a paso de funcionamiento de su propuesta.

4. Programe su solución.

5. Analice: ¿La complejidad de su propuesta es igual a la de su programa?

6. ¿Es posible que para cierto mensaje podamos tener varias opciones de respuesta? Su propuesta cuál selecciona?



### Formato de los archivos:

El archivo a ejecutar se debe llamar “extraterrestres.py”

Debe recibir por parámetro la frase. Por ejemplo "extraterrestres.py reconocerlapalabrasecreta"

La salida del programa debe ser por pantalla indicando cuál es la palabra.

Además, dentro del archivo se debe implementar una función llamada `ejecucion(frase)` que reciba por parámetro la frase.


**Ejemplos de ejecución:**

`extraterrestres.py reconocerlapalabrasecreta`

debe retornar `reconocer` por pantalla


`extraterrestres.py provincianeuqueninvadir`

debe retornar `neuquen` por pantalla

Trabajo Práctico n.º 2
======================
{:.no_toc}

Teoría de Algoritmos 1 - 2c 2019
Trabajo Práctico 2

## Lineamientos básicos

- El trabajo se realizará en grupos de cuatro personas (excepcionalmente de tres).

- La fecha de entrega es Miércoles 2 de Octubre. Se debe entregar en el horario de clase en papel (informe), más una entrega en digital de código (.zip) e informe (.pdf) a la clase de Google ClassRoom de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar algún otro, se debe pactar con los docentes.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución. La ausencia de esta información no permite probar el trabajo y deberá ser re-entregado con esta información.

- El informe debe presentar carátula con el nombre del grupo y número de hoja cada página

## Parte 1: Despliegue de ayuda eficiente

Luego de un ataque extraterrestre los recursos del país han quedado severamente disminuidos. Varias vías de comunicación y transporte troncales han quedado inservibles. 

Por lo tanto hay regiones incomunicadas total o parcialmente. La guardia nacional estudia la manera de desplegar equipos de ayuda para que ninguna ciudad o pueblo quede sin atender. Cada equipo será responsable de su región y deberá patrullar libremente en todas las ciudades que pertenezcan a la misma. 

Dado que el personal es escaso desean minimizar la cantidad de equipos a armar cubriendo todo los centros urbanos existentes. 

Cada equipo se puede desplazar por las vías de transporte que siguen funcionando (fluviales, aéreas y terrestres). Las mismas no siempre conectan en ambos sentidos su pueblo de origen con su destino. 

Nos entregan un listado de todas las rutas disponibles, que indican pueblo de origen y destino. Los nombres están separados por coma. 

Se pide:

1. Dado el problema, explicar cómo lo resuelve. Indique algoritmos y estructura de datos utilizados. Presentar pseudocódigo y explicarlo.
1. ¿Su solución es óptima? ¿Qué complejidad algorítmica tiene? Analice y explique.
1. Detallar paso a paso un ejemplo práctico (no trivial) de aplicación


## Parte 2: Comunicación satelital

Como parte del programa espacial argentino nos piden que programemos el algoritmo de compresión de datos Huffman para utilizar en la transmisión de las imágenes enviadas desde los satélites. 

Dado que existen riesgos de pérdidas de datos en el espacio para cada aplicación decidieron de antemano qué frecuencia estadística tiene cada byte del posible mensaje. El mismo se encuentra codificado en un archivo que contiene por cada carácter su frecuencia

Se debe:

1. Construir el algoritmo que lea los lista de bytes con sus frecuencias y construya el árbol de huffman.
1. Explicar por qué es un algoritmo de tipo greedy. 
1. Explicar por qué el código generado es óptimo entre todos los otros códigos prefijos posibles.
1. Dar el pseudocódigo del algoritmo que dado un archivo de entrada y la definición del código lo comprima. Detallar su funcionamiento.
1. Dar el pseudocódigo del algoritmo que dado un archivo de entrada lo descomprima.  Detallar su funcionamiento.
1. Analizar la complejidad algorítmica de los 3 algoritmos.
1. Programar los algoritmos.
1. Determinar si la complejidad de su programas es igual a la de los algoritmos.

### Interface de los programas:

El programa para comprimir (codificar) tiene que recibir 3 parámetros:

* path del archivo donde estan los codigos
* path del archivo a codificar.
* Path del archivo a generar codificado

El programa para descomprimir (decodificar) tiene que recibir 3 parámetros:

* path del archivo donde estan los codigos
* path del archivo a decodificar.
* Path del archivo a generar decodificado

El formato del archivo de codificación contiene una línea con 256 números separados por coma que representan las frecuencias de cada uno de los códigos ASCII del mensaje.
Ejemplo:

	10,400,30,1200,....



## Parte 3: ¿Es el siguiente un algoritmo tractable?

(Este ejercicio es “yapa” y no obligatorio)

DONALD B. JOHNSON,  en el paper “FINDING ALL THE ELEMENTARY CIRCUITS OF A DIRECTED GRAPH” presenta un algoritmo que, dado un grafo dirigido, obtiene todos los ciclos elementales que contiene. 
En el resumen del trabajo indica que la complejidad algorítmica del planteo es 

* Temporal: O((n  + e)(c + 1)) 
* Espacial: O(n + e), 

Donde: 

* n: cantidad de vértices, 
* e: cantidad de ejes,
* c: cantidad de circuitos elementales en el grafo

Recordamos que: Un ciclo es un camino en el que coinciden los vértices inicial y final. El ciclo es elemental cuando sus vértices - a excepción del inicial y final - no se repiten.

Se pide:

1. Analizar - fundamentando - si estamos frente a un algoritmo “tractable”.

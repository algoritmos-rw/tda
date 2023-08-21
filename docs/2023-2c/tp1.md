Trabajo Práctico n.º 1
======================
{:.no_toc}

Teoría de Algoritmos 1 - 2c 2023
Trabajo Práctico 1

## Lineamientos básicos

- El trabajo se realizará en grupos de cinco personas.

- Se debe entregar el informe en formato pdf y código fuente en (.zip) en el aula virtual de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar algún otro, se debe pactar con los docentes.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución. La ausencia de esta información no permite probar el trabajo y deberá ser re-entregado con esta información.

- El informe debe presentar carátula con el nombre del grupo, datos de los integrantes y  y fecha de entrega. Debe incluir número de hoja en cada página. No debe superar las 20 páginas + carátula + índice + referencias.

- Debe entregar en el informe las fuentes consultadas en una sección de referencias.

- En caso de re-entrega, entregar un apartado con las correcciones mencionadas

## Parte 1: La base antártica

Nos informan de la apertura de una nueva base de investigación antártica. En la misma se espera realizar una serie de experimentos. Por lo tanto, han comenzado una búsqueda de personal calificado. Se cuenta con un listado de “n” habilidades a cubrir por el personal (Ejemplo: “Cocinar”, “Primeros auxilios”, “Meteorología”, “astronomía”, “Electricidad”, etc). Además se ha reunido una cantidad de “m” candidatos. Cada candidato cubre un subconjunto de las habilidades. Nos solicitan que los ayudemos a resolver el problema intentando seleccionar a la menor cantidad de expedicionarios, sin dejar de cubrir los requerimientos.

Se pide:

1.  Proponga y explique una solución del problema mediante Branch and Bound.

1.  Brinde pseudocódigo y estructuras de datos a utilizar. 

1.  Realice el análisis de complejidad temporal y espacial.

1.  Brinde un ejemplo simple paso a paso del funcionamiento de su solución.

1.  Programe su propuesta

1.  Determine si su programa tiene la misma complejidad que su propuesta teórica.

### Formato de los archivos:

El programa debe recibir por parámetro un archivo con las habilidades y otro archivo con los candidatos. Ejemplo:

	python personal.py habilidades.txt candidatos.txt

El archivo de habilidades corresponde a un archivo de texto donde cada línea corresponde a una habilidad. Esta está definida por un código numérico separado por coma de su nombre. Ejemplo:

	1,Cocinar
	2,primeros Auxilios
	3,Meteorología
	4,biología
	5,pilotear helicoptero
	6,comunicaciones
	7,mecanica
	…
	
El archivo de candidatos corresponde a un archivo de texto donde cada linea corresponde a un candidato. Por cada candidato se tiene su nombre seguido por una lista separada por comas de sus habilidades. Ejemplo:

	R.J. MacReady,1,5,6
	Nauls,1,2
	Childs,3,7
	Dr. Copper,2,4
	George Bennings,1,3
	Garry,2,6,3
	…

Debe resolver el problema y retornar por pantalla la solución. El nombre de los candidatos seleccionados uno por línea. Siguiendo el ejemplo esta podría ser la solución:

	R.J. MacReady
	Childs
	Dr. Copper

## Parte 2: Adivina la carta

Nos proponen el siguiente juego de cartas en el que tenemos que adivinar la carta que tiene un rival. El mazo tiene 1 carta de “1 de Oro”, 2 cartas de “2 de Oro” y así hasta 9 cartas de “9 de Oro”. El rival mezcla y selecciona una carta. Mediante preguntas que solo se pueden responder por sí o por no tenemos que averiguar en la menor cantidad de consultas cual es la carta. (ejemplos: “La carta es mayor a 4?, “La carta es un ‘1’ o un ‘3’?”, etc). Proponer un algoritmo que resuelva el problema minimizando la cantidad probable de preguntas a realizar.  

Se pide:

1.  Determinar y explicar cómo se resolvería este problema utilizando la metodología greedy. 

1.  De un ejemplo paso a paso. ¿Qué complejidad temporal y espacial tiene la solución?

1.  Justifique por qué corresponde su propuesta a la metodología greedy.

## Parte 3: El concurso

Se está por realizar un concurso de conocimientos en parejas para escuelas secundarias. Existen “n” categorías que se evaluarán en el mismo. Una escuela evaluó a sus posibles participantes. Por cada uno de ellos generaron una lista ordenada de mayor a menor de las categorías según sus conocimientos. En base a una competencia interna se seleccionó a uno de ellos como el capitán. Nos solicitan que los ayudemos, basándonos en el concepto de inversión, a seleccionar a otro participante que mejor se complemente con el capitán.

Se pide:

1.  Proponer un algoritmo utilizando división y conquista que lo resuelva. Incluir pseudocódigo

1.  Analice la complejidad del algoritmo utilizando el teorema maestro y desenrollando la recurrencia.

1.  Brindar un ejemplo de funcionamiento.

1.  Programe su solución

1.  Analice si la complejidad de su programa es equivalente a la expuesta en el punto 2.

### Formato de los archivos:

El programa debe recibir por parámetro un archivo con los posibles participantes y la posición del capitán dentro del mismo.  Ejemplo:

	python emparejar.py participantes.txt 4

El archivo de participantes corresponde a un archivo de texto donde cada línea corresponde a un participante. Por cada candidato se tiene su nombre seguido por una lista separada con el orden de las categorías. Ejemplo:

	Jorge,2,6,1,4,3,5,7,8
	Diego,1,3,5,4,8,2,6,7
	Daniela,7,8,2,1,4,3,5,6
	Thiago,8,1,5,7,2,6,3,4
	Marcela,8,1,7,2,5,3,4,6

Debe resolver el problema y retornar por pantalla al nombre del capital y el participante que mejor se complementa separado por una coma.

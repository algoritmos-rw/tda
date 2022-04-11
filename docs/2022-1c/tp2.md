Trabajo Práctico n.º 2
======================
{:.no_toc}

Teoría de Algoritmos 1 - 1c 2022
Trabajo Práctico 2

## Lineamientos básicos

- El trabajo se realizará en grupos de cinco personas.

- Se debe entregar el informe en formato pdf y código fuente en (.zip) en el aula virtual de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar algún otro, se debe pactar con los docentes.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución. La ausencia de esta información no permite probar el trabajo y deberá ser re-entregado con esta información.

- El informe debe presentar carátula con el nombre del grupo, datos de los integrantes y  y fecha de entrega. Debe incluir número de hoja en cada página. No debe superar las 20 páginas.

- En caso de re-entrega, entregar un apartado con las correcciones mencionadas

## Parte 1: Un evento exclusivo

Todos los años la asociación de un importante deporte individual profesional realiza una preclasificación de los n jugadores que terminaron en las mejores posiciones del ranking para un evento exclusivo.
En la tarjeta de invitación que enviarán suelen adjuntar el número de posición en la que está actualmente y a cuantos rivales superó en el ranking (únicamente entre los invitados). Contamos con un listado que tiene el nombre del jugador y la posición del ranking del año pasado. Ese listado está ordenado por el ranking actual. 

Ejemplo:

	A,3 | B,4 | C,2 | D,8 | E,6 | F,5 |
	
	A → Ranking actual 1 → superó a 1 entre los preclasificados (C)
	B → Ranking actual 2 → superó a 1 entre los preclasificados (C)
	C → Ranking actual 3 → superó a 0 entre los preclasificados (-)
	D → Ranking actual 4 → superó a 2 entre los preclasificados (E y F)
	E → Ranking actual 5 → superó a 1 entre los preclasificados (F)
	F → Ranking actual 6 → superó a 0 entre los preclasificados (-)
	
	En este caso el problema debería retornar:
	
	A → 1 (1)
	B → 2	(1)
	C → 3	(0)
	D → 4	(2)
	E → 5 (1)
	F → 6 (0)

Se pide:

1.  Explicar cómo se puede resolver este problema por fuerza bruta. Analizar complejidad espacial y temporal de esta solución

1.  Proponer una solución utilizando la metodología de división y conquista que sea más eficiente que la propuesta anterior. (incluya pseudocódigo y explicación)

1.  Realizar el análisis de complejidad temporal mediante el uso del teorema maestro.

1.  Realizar el análisis de complejidad temporal desenrollando la recurrencia

1.  Analizar la complejidad espacial basándose en el pseudocódigo.

1.  Dar un ejemplo completo del funcionamiento de su solución

## Parte 2: Ciclos negativos

La detección de ciclos negativos tiene una variedad de aplicaciones en varios campos. Por ejemplo en el diseño de circuitos electrónicos VLSI, se requiere aislar los bucles de retroalimentación negativa. Estos corresponden a ciclos de costo negativo en el grafo de ganancia del amplificador del circuito. Tomando como entrada de nuestro problema un grafo ponderado con valores enteros (positivos y/o negativos) dirigido donde un nodo corresponde al punto de partida, queremos conocer si existe al menos un ciclo negativo y en caso afirmativo mostrarlo en pantalla.

Se pide:

1. Proponer una solución al problema que utiliza programación dinámica. Incluya relación de recurrencia, pseudocódigo, estructuras de datos utilizadas y explicación en prosa.

1. Analice la complejidad temporal y espacial de su propuesta.

1. Programe la solución

1. Determine si su programa tiene la misma complejidad que su propuesta teórica. 

### Formato de los archivos:

El programa debe recibir por parámetro el path del archivo donde se encuentra el grafo.
El archivo con el grafo es un archivo de texto donde la primera línea corresponde al nodo inicial. Luego continúa con una línea por cada eje direccionado del grafo con el formato: ORIGEN,DESTINO,PESO.

Ejemplo: “grafo.txt”

	B
	D,A,-2
	B,A,3
	D,C,2
	C,D,-1
	B,E,2
	E,D,-2
	A,E,3
	...

Debe resolver el problema y retornar por pantalla la solución. 

En caso de no existir ciclos negativos:
“No existen ciclos negativos en el grafo”

En caso de existir ciclos negativos:
“Existe al menos un ciclo negativo en el grafo.
A,E,D → costo: -1”

## Parte 3: Un poco de teoría

1. Hasta el momento hemos visto 3 formas distintas de resolver problemas. Greedy, división y conquista y programación dinámica.

   1. Describa brevemente en qué consiste cada una de ellas

   1. ¿Cuál es la mejor de las 3? ¿Podría elegir una técnica sobre las otras?

1. Un determinado problema puede ser resuelto tanto por un algoritmo Greedy, como por un algoritmo de División y Conquista. El algoritmo greedy realiza N^3 operaciones sobre una matriz, mientras que el algoritmo de Programación Dinámica realiza N^2 operaciones en total, pero divide el problema en N^2 subproblemas a su vez, los cuales debe ir almacenando mientras se ejecuta el algoritmo. Teniendo en cuenta los recursos computacionales involucrados (CPU, memoria, disco) ¿Qué algoritmo elegiría para resolver el problema y por qué?

Pista: probablemente no haya una respuesta correcta para este problema, solo justificaciones correctas

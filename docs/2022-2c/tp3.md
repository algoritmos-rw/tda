Trabajo Práctico n.º 3
======================
{:.no_toc}

Teoría de Algoritmos 1 - 2c 2022
Trabajo Práctico 3

## Lineamientos básicos

- El trabajo se realizará en grupos de cinco personas.

- Se debe entregar el informe en formato pdf y código fuente en (.zip) en el aula virtual de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar algún otro, se debe pactar con los docentes.

- El informe debe presentar carátula con nombre del grupo, integrantes y fecha de entrega. Debe incluir número de hoja en cada página.

- La extensión del informe no debe superar las 20 páginas + carátula + índice + referencias.

- Debe presentar código fuente listo para su ejecución e instrucciones de compilación y ejecución dentro del informe.

- Debe entregar en el informe las fuentes consultadas en una sección de referencias.

- En caso de re-entrega, entregar un apartado con las correcciones mencionadas

## Parte 1: Un proyecto distribuido en dos

Contamos con un proyecto que tiene un conjunto de tareas a realizar. Entre algunas tareas existe cierta interdependencia, es decir que para realizar una se requiere los resultados que otorgan una o más tareas previas. Se cuenta con dos equipos de trabajo con sus propios recursos. Cualquier tarea la puede realizar cualquiera de los equipos con un costo asociado. Llamaremos ci,e al costo que el equipo “e” realice la tarea i. Existe un costo de transferencia de resultados que se aplica si el resultado de una tarea elaborada por un equipo se la debe trasladar al otro para resolver otra tarea. Llamaremos ti,j al costo de la transferencia del resultado de la tarea i a la tarea j. Si dos tareas son realizadas por el mismo equipo no hay costo asociado al intercambio de resultados.  Consideraremos que todos los costos son enteros positivos.
Se desea minimizar el costo total del desarrollo del problema.

Se pide:

1.  Construya una estrategia utilizando redes de flujo que solucione el problema. Explíquela con sus palabras.

1. Brinde pseudocódigo que explique cada uno de los pasos de su solución.

1. Analice la complejidad temporal y espacial de su propuesta

1. Brinde al menos un ejemplo paso a paso donde se aprecie el funcionamiento del mismo.

1. Programe el algoritmo

1. Analice: su programa mantiene la complejidad temporal y espacial teórica?

### Formato de los archivos:

El programa debe recibir por parámetro el path del archivo con los procesos a realizar. El archivo de los procesos es un archivo de texto donde cada línea corresponde a un proceso, sus costos y dependencias. 
El formato de la línea es: CÓDIGO_PROCESO,COSTO_,EQUIPO1,COSTO_,EQUIPO2,[LISTA DE DEPENDENCIAS CON SUS COSTOS]
La lista de dependencias corresponde a los procesos que siguen al mismo y el costo asociado de que esta la realice el otro equipo. 

Ejemplo: “procesos.txt”

	A,1,2,B,2
	B,5,10,C,3,D,1
	C,4,4,D,2
	D,1,3
	...
 
En el ejemplo la tarea “A” cuesta $1 si la realiza el equipo 1 y $2 si la realiza el equipo 2. El resultado de la tarea “A” es necesario para realizar la tarea “B”. Si la tarea “A” y “B” son realizadas por diferentes equipos entonces la transferencia de resultado cuesta $2

Debe resolver el problema y retornar por pantalla la solución. Debe mostrar que tareas debe resolver cada equipo y el costo total que se incurrirá dada esta división.


## Parte 2: Más allá de Bellman-Ford

Para el cálculo del costo mínimo con costos negativos se utiliza el algoritmo Bellman-Ford. El mismo tiene como precondición para llegar a la solución óptima la ausencia de ciclos negativos en el grafo. Ante su presencia, en la búsqueda del camino, podemos quedar atrapados dentro de estos. En ese caso la longitud del camino será infinita y el costo termina infinito negativo.

Deseamos un algoritmo que ante esta misma situación no brinde un camino que no ingrese en los ciclos. Llamaremos a este problema como “camino simple mínimo en un grafo con ciclos negativos” (shortest simple-path in a graph with negative-cycles: “SSPGNC” ). Podemos expresarlo como problema de decisión de la siguiente manera: “Dado un grafo con peso en sus ejes y un par de nodos al que llamaremos origen y destino. Queremos saber si existe un camino simple de costo menor a C que los una”.

No se conoce un algoritmo eficiente que resuelva este problema.


Se pide:

1. Reducir polinomialmente el problema “Problema de camino más largo” (Longest Path problem) a “SSPGNC”.

1. Demuestre que posteriormente que “Problema de camino más largo” es NP-C (puede ayudarse con diferentes problemas, recomendamos “el problema del camino hamiltoneano”)

1. En base a los puntos 1 y 2, puede afirmar que el problema “SSPGNC” es NP-Completo? Si la respuesta es “no” resuelva qué faltaría para que lo sea. Si la respuesta es “si” justifíquelo utilizando los conceptos de clases de complejidad.  

1. Utilizando el concepto de transitividad y la definición de NP-C explique qué ocurriría si se demuestra que existe un algoritmo eficiente que resuelve cualquier instancia de “SSPGNC”.

1. Un tercer problema al que llamaremos X se puede reducir polinomialmente a “SSPGNC”, qué podemos decir acerca de su complejidad?

1. Realice un análisis entre las clases de complejidad P, NP y NP-C y la relación entre ellos.

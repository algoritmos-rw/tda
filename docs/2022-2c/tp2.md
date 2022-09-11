Trabajo Práctico n.º 2
======================
{:.no_toc}

Teoría de Algoritmos 1 - 2c 2022
Trabajo Práctico 2

## Lineamientos básicos

- El trabajo se realizará en grupos de cinco personas.

- Se debe entregar el informe en formato pdf y código fuente en (.zip) en el aula virtual de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar algún otro, se debe pactar con los docentes.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución. La ausencia de esta información no permite probar el trabajo y deberá ser re-entregado con esta información.

- El informe debe presentar carátula con el nombre del grupo, datos de los integrantes y  y fecha de entrega. Debe incluir número de hoja en cada página. No debe superar las 20 páginas + carátula + índice + referencias.

- En caso de re-entrega, entregar un apartado con las correcciones mencionadas

## Parte 1: El experimento científico

Se realiza un experimento de conductividad de un nuevo material en aleación con otro. Se formaron muestras numeradas de 1 a n. A mayor número, mayor concentración del nuevo material. Además se realizaron “n” mediciones a diferentes temperaturas de conductividad para cada muestra. Los resultados fueron expresados en una matriz M de nxn. Se observa que un mismo material cuanto mayor temperatura tiene mayor conductividad. Además para cada cuanto mayor concentración a la misma temperatura, también mayor conductividad. 

En conclusión podemos, al analizar la matriz, ver dos progresiones. Cada fila tiene números ordenados de forma creciente. Es decir para la fila i, M[i,j]<M[i,k] si k>j. Cada columna tiene números ordenados de forma creciente. Es decir para la columna j, M[i,j]<M[k,j] si k>i.

Dada la matriz M, los experimentadores quieren encontrar en qué posición se encuentra un determinado número.


Se pide:

1.  Proponga una estrategia por fuerza bruta para resolver el problema. ¿Cuál es su complejidad?

1.  Proponga una solución superadora utilizando división y conquista. Brinde pseudocódigo y estructuras de datos a utilizar. Intente que la complejidad sea la menor posible

1.  Presente relación de recurrencia de su solución. Realizar el análisis de complejidad temporal.

1.  En un nuevo experimento se preparan otras “n” muestras, pero en este caso se realizan “m” mediciones para cada una. ¿Cómo Impacta en su propuesta algorítmica y su análisis?

1.  Dar un ejemplo completo del funcionamiento de su solución

## Parte 2: El almacén

Se debe organizar una bodega en un almacén. Tenemos “n” cajas. Cada caja comparte la misma profundidad pero varían en su altura y largo. El orden de las cajas no se puede modificar dado que están clasificadas mediante un código contiguo. Las cajas se ponen en repisas que comparten entre ellas la longitud L y cuya altura es regulable. El objetivo perseguido por el encargado de determinar en qué forma organizar las cajas con el objetivo de minimizar la suma de las alturas de las repisas utilizadas.

Se pide:

1. Mostrar por qué una propuesta greedy que agregue tantas cajas como sea posible por repisa no es óptima.

1. Proponer una solución al problema que utiliza programación dinámica. Incluya relación de recurrencia, pseudocódigo, estructuras de datos utilizadas y explicación en prosa.

1. Analice la complejidad temporal y espacial de su propuesta.

1. Programe la solución

1. Determine si su programa tiene la misma complejidad que su propuesta teórica. 

### Formato de los archivos:

El programa debe recibir por parámetro la cantidad de cajas y el largo de las repisa y el path del archivo donde se encuentran las cajas a acomodar. El archivo con las cajas es un archivo de texto donde cada línea corresponde a una caja. El formato de la línea es: CÓDIGO_CAJA,LARGO,ALTO.

Ejemplo: “cajas.txt”

	001,1,2
	002,1,2
	003,2,5
	004,1,3
	...

Debe resolver el problema y retornar por pantalla la solución. Debe mostrar por cada repisa su alto y las cajas que contiene. Además la altura total acumulada de las repisas utilizadas.

## Parte 3: Un poco de teoría

1. Hasta el momento hemos visto 3 formas distintas de resolver problemas. Greedy, división y conquista y programación dinámica.

   1. Describa brevemente en qué consiste cada una de ellas

   1. ¿Qué propiedades requiere el problema para poder ser resueltos por ellos?

1. Considere un problema teórico y suponga que se puede resolver por cualquiera de las tres metodologías. Determine qué cuestiones tendría en cuenta para seleccionar una sobre las otras. ¿Siempre existirá una metodología mejor que las otras?
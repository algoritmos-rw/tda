Trabajo Práctico n.º 2
======================
{:.no_toc}

Teoría de Algoritmos 1 - 1c 2020
Trabajo Práctico 2

## Lineamientos básicos

- El trabajo se realizará en grupos de cuatro personas (excepcionalmente de tres).

- La fecha de entrega es Miércoles 13 de Mayo. Se debe entregar en el horario de clase en papel (informe), más una entrega en digital de código (.zip) e informe (.pdf) a la clase de Google ClassRoom de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar algún otro, se debe pactar con los docentes.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución. La ausencia de esta información no permite probar el trabajo y deberá ser re-entregado con esta información.

- El informe debe presentar carátula con el nombre del grupo y número de hoja cada página

## Parte 1: El productor agropecuario

Un productor agropecuario tiene un terreno de X hectareas disponible para la siembra. Sabe que puede producir diferentes cultivos ocupando una determinada porción del campo. Cada elección le resultará en una determinada ganancia. Cada cultivo i tiene un tiempo determinado de siembra  Ts(i) y otro de cosecha Tc(i). Su objectivo es maximizar la ganancia. En total tiene "n" opciones.

Se pide:

1. Ayude al productor!. Presente una solucion utilizando programación dinámica que maximice la ganancia.
1. Cuál es el subproblema en su planteo?
1. Presente y explique la relación de recurrencia.
1. presente en pseudocódigo la solución de forma iterativa.
1. Exprese la complejidad temporal y espacial de la solución presentada. 
1. Programe su solución

### Interface de los programas:

El archivo del opciones a cultivar es de tipo texto. En cada linea cuenta con una opción. Cada opción presenta 5 valores separados por espacio: nombre de cultivo, cantidad de hectarias, fecha de inicio, fecha de fin y ganancia esperada.
Ejemplo (totalmente inventado y alejado de la realidad):

	Maiz 4 0 5 23
	Soja 15 4 7 99
	Lechuga 2 2 6 13
	Tomates 1 9 13 9
	

El resultado se debe imprimir en pantalla. Mostrando la ganancia máxima y un listado separado por coma de los productos a producir con sus fechas de inicio y finalización.

Los parámetros de ejecución del programa son 2:

* cantidad de hectarias disponibles: valor numérico

* path al achivo con la opciones a cultivar.

### Información extra:

* Se puede discretizar los tiempos en unidades enteras. Siendo t=0 el tiempo inicial.
* La cantidad a cultivar es un valor entero medido en hectarias. No se puede sembrar menos ni mas que lo que la opcion determina.
* La ganancia por cultivo es global (no por hectaria)
* En ningun momento se puede cultivar más que la cantidad de hectarias disponibles.
* Considerar a las fechas de inicio y fin como parte del tiempo de cultivo. 

## Parte 2: Minimizando el costo del transporte

Una empresa  tiene que programar el envio de productos en un determinado día. Tiene un conjunto de centros de elaboración cada uno con un numero determinado de productos a enviar y un conjunto de centros de consumo que similarmente requieren un número determinado de productos (a recibir).
Para el envio existe una red de distribucion conformada por centros de transbordo y rutas que los conectan. Cada ruta tiene un costo de uso y una limitante de cantidad de piezas que se pueden enviar. 
La empresa nos solicite que le ayudemos a maximizar el envío de sus productos y al mismo tiempo minimizar el costo de transporte.

Se pide:

1. Resolver el problema planteado utilizando una aproximación mediante flujo de redes.
1. Calcular y explicar la complejidad temporal y espacial del problema.
1. Explique si su solución es eficiente
1. Dar ejemplos completos donde se puedan ver las alternativas del problema. 

### Información extra:

* El costo es un valor entero mayor o igual a cero.
* Las cantidades a enviar y recibir son valores enteros positivos
* La capacidad de cada ruta es un  valor enter 

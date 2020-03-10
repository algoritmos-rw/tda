Trabajo Práctico n.º 1
======================
{:.no_toc}

Teoría de Algoritmos 1 - 1c 2020
Trabajo Práctico 1

## Lineamientos básicos

- El trabajo se realizará en grupos de cuatro personas (excepcionalmente de tres).

- La fecha de entrega es Miércoles 22 de Abril. Se debe entregar en el horario de clase en papel (informe), más una entrega en digital de código (.zip) e informe (.pdf) a la clase de Google ClassRoom de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar algún otro, se debe pactar con los docentes.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución. La ausencia de esta información no permite probar el trabajo y deberá ser re-entregado con esta información.

- El informe debe presentar carátula con el nombre del grupo y número de hoja cada página

## Parte 1: Un problema de ausentismo

Una empresa de tercerizacion laboral nos convoca para que le ayudemos con un problema de ausentismo laboral. Tiene un conjunto "n" de empleados que realizan tareas en diferentes puntos de la ciudad. Cada uno de ellos deben estar durante un lapso de tiempo en la ubicacion establecida.
La direccion de la empresa sospecha que algunos de sus empleados suelen faltar a alguno de esos turnos. Para verificarlo contrataron a la empresa "Dystopian Technologies Inc." (DTI) Esta empresa implanta un microchip con un codigo unico en cada empleado. Mediante rastreo satelital pueden conocer donde se encuentra cada implantado en un momento determinado "tx". Ante la consulta de una lista de codigos de empleados DTI retornara que cuales no estan dentro de su area de trabajo. 

Se pide:

1. Teniendo en cuenta que cada consulta tiene un costo elevado, construir un algoritmo que minimice el costo total y en forma eficiente detecte si alguien no cumplio con su obligacion.
1. Determinar que tipo de algoritmo es. Justificar
1. Explicar detalladamente la complejidad total del algoritmo armado.

### Información extra:

* Se puede discretizar los tiempos en unidades. Siendo t=0 el tiempo desde donse de puede consultar. 
* Cada empleado i comienza su turno en Ti(i) y finaliza en Tf(i).
* La lista de los empleados se encuentra ordenada por tiempo de inicio del turno.
* El tiempo de consulta a la empresa DTI es O(1).

## Parte 2: Una nueva regulación industrial.

Según una nueva regulación industrial un fabricante debe rotular cada lote que produce segun un valor numérico que lo caracteriza. Cada lote esta conformado por "n" piezas. A cada una de ellas se le realiza una medicion de volumen.
La regulación considera que el lote es válido si mas de la mitad de las piezas tienen el mismo volumen. En ese caso el rótulo deberá ser ese valor. De lo contrario el lote se descarta.

Actualmente cuentan con el proceso "A" que consiste en para cada pieza del lote contar cuantas de las restantes tienen el mismo volumen. Si alguna de las piezas corresponde al "elemento mayoritario"(!), lo rotula. De los contrario lo rechaza.

Un consultor informatico (que no cursó TDA) impulsa una solucion (proceso "B") que considera la mas eficiente: ordenar las piezas por volumen y con ello luego reducir el tiempo de busqueda del elemento mayoritario.

Nos contratan para construir una solucion mejor (proceso "C"). 

Se pide:

1. Exprese mediante pseudocodigo el proceso "A". 
1. Explique si la sugerencia del consultor realmente puede mejorar el proceso. En caso afirmativo, arme el pseudocodigo que lo ilustre.
1. Proponga el proceso "C" como un algoritmo superador (ayuda: utilice división y conquista). Expliquelo detalladamente y brinde pseudocódigo.
1. Calcule, explique y compare las complejidades temporales y espaciales de cada uno de los 3 procesos.
1. Programe las 3 soluciones

ATENCION: Para el algoritmo con división y conquista presenta relacion de recurrencia. Calcule la complejidad tanto mediante el metodo maestro como desenrrollando la recurrencia.

### Interface de los programas:

El archivo del lote es de tipo texto. Debe contener un valor entero numerico por linea que representa el volumen de cada pieza.
Ejemplo:

	110
	99
	110
	125
	110

El resultado se debe imprimir en pantalla. Mostrando el elemento mayoritario o "rechazado" si no existe.

Los parámetros de ejecución del programa son 2:

* proceso a utilizar: A, B o C

* path al achivo con el lote.

Trabajo Práctico n.º 1
======================
{:.no_toc}

Teoría de Algoritmos 1 - 1c 2020
Trabajo Práctico 1

## Lineamientos básicos

- El trabajo se realizará en grupos de cuatro personas (excepcionalmente de tres).

- Se debe entregar el informe en formato pdf y código fuente en (.zip) en el aula virtual de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar algún otro, se debe pactar con los docentes.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución. La ausencia de esta información no permite probar el trabajo y deberá ser re-entregado con esta información.

- El informe debe presentar carátula con el nombre del grupo y número de hoja cada página.

## Parte 1: Un problema de ausentismo

Una empresa de tercerización laboral nos convoca para que le ayudemos con un problema de ausentismo laboral. Tiene un conjunto de n empleados que realizan tareas en diferentes puntos de la ciudad. El turno de cada empleado i comienza en Ti(i) y termina en Tf(i) y durante todo ese lapso tiene que estar en la ubicación establecida.
La dirección de la empresa sospecha que algunos de sus empleados suelen faltar sin aviso. Para verificarlo contrataron a la empresa “Dystopian Technologies Inc.” (DTI). Esta empresa implanta un microchip con un código único en cada empleado. Mediante rastreo satelital pueden conocer dónde se encuentra cada chip implantado en cualquier momento. Además posee el cronograma completo de las tareas.

DTI brinda un sistema que mediante una consulta (encendido / apagado) nos devolverá cuáles empleados aún no controlados y en horario de trabajo se encuentran en su sitio y cuáles no.
 
Se pide:

1. Escribir un algoritmo para que DTI rastree que todos los empleados estén en sus puestos en algún momento de su turno. Como DTI cobra por cada encendido / apagado, la cantidad de encendidos debe ser mínima. El programa debe correr además en tiempo mínimo.

1. Determinar que tipo de algoritmo es. Justificar.

1. Explicar detalladamente la complejidad total del algoritmo armado.

1. Justificar detalladamente que la solución obtenida es óptima (mínima cantidad de encendidos / apagados).

Se recibe:

Una lista con los datos de cada uno de los n empleados (nombre, posición, ti, tf).

### Consideraciones:

* Los tiempos informados son enteros de 0 en adelante.
* DTI les cobra por cada encendido / apagado.
* Cada encendido / apagado es casi instantáneo y se lo programa para algún valor de t entero.
* Cada encendido / apagado (y su consecuente rastreo) es O(1).
* El empleado una vez en su puesto no se retira hasta concluir su turno.


## Parte 2: Una nueva regulación industrial.

A raiz de una nueva regulación industrial un fabricante debe rotular cada lote que produce según un valor numérico que lo caracteriza. Cada lote está conformado por "n" piezas. A cada una de ellas se le realiza una medición de volumen.
La regulación considera que el lote es válido si más de la mitad de las piezas tienen el mismo volumen. En ese caso el rótulo deberá ser ese valor. De lo contrario el lote se descarta.

Actualmente cuentan con el proceso "A" que consiste en para cada pieza del lote contar cuantas de las restantes tienen el mismo volumen. Si alguna de las piezas corresponde al "elemento mayoritario", lo rotula. De lo contrario lo rechaza.

Un consultor informático (que no cursó TDA) impulsa una solución (proceso "B") que considera la más eficiente: ordenar las piezas por volumen y con ello luego reducir el tiempo de búsqueda del elemento mayoritario.

Nos contratan para construir una solución mejor (proceso "C"). 

Se pide:

1. Exprese mediante pseudocódigo el proceso "A". 
1. Explique si la sugerencia del consultor realmente puede mejorar el proceso. En caso afirmativo, arme el pseudocódigo que lo ilustre.
1. Proponga el proceso "C" como un algoritmo superador (ayuda: utilice división y conquista). Explíquelo detalladamente y brinde pseudocódigo.
1. Calcule, explique y compare las complejidades temporales y espaciales de cada uno de los 3 procesos.
1. Programe las 3 soluciones

ATENCION: Para el algoritmo con división y conquista presentar relacion de recurrencia. Calcule la complejidad tanto mediante el método maestro como desenrrollando la recurrencia.

### Interface de los programas:

El archivo del lote es de tipo texto. Debe contener un valor entero numérico por linea que representa el volumen de cada pieza.
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

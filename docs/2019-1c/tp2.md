Trabajo Práctico n.º 2
======================
{:.no_toc}

Teoría de Algoritmos 1 - 1c 2019
Trabajo Práctico 2

## Lineamientos básicos

- El trabajo se realizará en grupos de cuatro personas (excepcionalmente de tres).

- La fecha de entrega es el lunes 6 de mayo de 2019. Se debe entregar en el horario de clase en papel (informe), más una entrega en digital de código (.zip) e informe (.pdf) al correo de entregas del curso: tps.7529rw@gmail.com y a la clase de Google ClassRom de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar alguno que no este en la siguiente lista, coordinarlo con los docentes: Java, JavaScript, Ruby, Go, Rust, Swift, Scala, Haskell, OCaml, Clojure, D, Lua, Elixir.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución.

## Parte 1: Laberintos


_“Cuentan los hombres dignos de fe (pero Alá sabe más) que en los primeros días hubo un rey de las islas de Babilonia que congregó a sus arquitectos y magos y les mandó a construir un laberinto tan perplejo y sutil que los varones más prudentes no se aventuraban a entrar, y los que entraban se perdían.”_ - "Los dos reyes y los dos laberintos", Jorge Luis Borges

Una revista de entretenimientos nos solicita que armemos un algoritmo para generar laberintos. Los mismos deben estar basados en una cuadrícula donde una celda determinada se puede comunicar con sus 2 celdas verticales y sus 2 celdas horizontales inmediatas. El tamaño de la grilla es un parámetro de entrada que indica cantidad de filas x cantidad de columnas respectivamente. La celda de partida siempre será la superior izquierda y la de llegada la inferior derecha. Además nos piden que junto con el laberinto presentemos su resolución.

Se debe construir:

1) El algoritmo constructor utilizando:
 * un método de división y conquista
 * una variante de Deep Search First

2) El algoritmo que resuelva el laberinto indicando el camino y la distancia de origen a destino
    
Para cada algoritmo se solicita:

 a. Presentar y explicar algoritmo en pseudocodigo.  
 b. Determinar la complejidad del algoritmo.  
 c. Programar el algoritmo.  

(!) Evaluar si conviene representar el problema utilizando conjuntos disjuntos.

3) Determinar si los códigos presentados se ajustan a la complejidad indicada en los puntos 1 y 2.

4) (optativo) presentar una visualización gráfica de los laberintos gráfica.


### Formato de los archivos y parámetros del programa:

Para el punto 1: debe recibir como parámetros el método de construcción (“dyc” o “dfs”), el largo y el ancho de la grilla. Debe emitir como salida un archivo que muestre visualmente el laberinto (cuyo nombre debe ser: mapa-laberinto.txt). 
Sugerimos una formato como el siguiente:

    + +-+-+-+
    | |     |
    + + + + +
    |   | | |
    +-+-+-+ +

Ejemplo de ejecución del programa: python constructor-algoritmo.py dfs 20 30

Para el punto 2: debe recibir como parámetro el nombre del archivo con el mapa. Debe emitir un nuevo archivo que muestre visualmente el camino de salida y su longitud. Sugerimos un formato como el siguiente:

    + +-+-+-+
    |*|* * *|
    + + + + +
    |* *| |*|
    +-+-+-+ +
    Longitud: 7

Ejemplo de ejecución del programa: 

    python dq.py mapa-laberinto.txt


## Parte 2: El golpe comando

En un edificio de oficinas se cometió un hurto. La policía está comenzando las investigaciones preliminares. Gracias a las planillas de visitas conocen la hora en la que entró cada persona y el tiempo de permanencia. Por la mecánica del ilícito saben que el grupo criminal está conformado por entre 5 y 10 individuos. Estiman que el tiempo total del hecho llevó entre 40 y 120 minutos.
En ese lapso entró el primero de los complices. En algún momento estuvo toda la banda junta. Y al momento de abandonar el lugar el primero en salir se llevó el botín y no habia personas ajenas a la banda presentes. 

1. Proponer y explicar un algoritmo que liste los grupos de sospechosos
1. Realizar el análisis de complejidad de los algoritmos propuestos (tiempo y espacio).
1. Programar la solución propuesta.

### Formato de los archivos y parámetros del programa:

La planilla de visitas se encuentra ordenado por hora de ingreso y que cuenta con la siguiente información por línea: 

    nombre persona,horario ingreso,tiempo permanencia.

El listado de sospechosos se debe generar en un archivo llamado sospechosos.txt, donde cada línea debe contener:

Nombres de los sospechosos separados por coma y el tiempo de permanencia.

Ejemplo de ejecución del programa: 

    python sospechosos.py planilla.txt

### Aclaraciones:

* Se deben explicar todas las estructuras utilizadas
* Tener en cuenta que una persona puede haber entrado y salido en varias oportunidades.
* Una persona puede pertenecer a varios grupos de sospechosos.
* Para simplificar las pruebas se puede suponer que los registros están representados en minutos. El tiempo está medido en relación al horario de ingreso de la primera persona (hora cero)
* El tiempo del ilícito se toma entre que entró el primer cómplice, hasta que uno de ellos se retiró con el botín.

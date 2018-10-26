Trabajo Práctico n.º 3
======================
{:.no_toc}

Teoría de Algoritmos 1 - 2c 2018
Trabajo Práctico 3

## Lineamientos básicos

- El trabajo se realizará en grupos de cuatro personas (excepcionalmente de tres).

- La fecha de entrega es el lunes 26 de noviembre de 2018. Se debe entregar en el horario de clase en papel (informe), más una entrega en digital de código (.zip) e informe (.pdf) al correo de entregas del curso: tps.7529rw@gmail.com y a la clase de Google ClassRom de la materia.

- El lenguaje de implementación es libre, pero se debe comunicar por correo en caso de no ser uno de: C, C++, Python, Java, JavaScript, Ruby, Go, Rust, Swift, Scala, Haskell, OCaml, Clojure, D, Lua, Elixir.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución.

## Parte 1: Tarjetas coleccionables

Un constructor de máquinas expendedoras de tarjetas coleccionables deportivas nos pide que diseñemos la programación para su nueva máquina que pondrá en diferentes estadios. 

Las tarjetas se ofrecen de forma individual o en sobres de diferentes contenidos (por ejemplo podrían ser: 1, 5, 7, 14). Un comprador ingresa el monto que corresponde a X tarjetas y el programa debe entregar la menor cantidad de sobre para cumplir con la solicitud.

Se pide:

1. Analizar la factibilidad de resolverlo mediante un algoritmo greedy
2. Dar pseudocodigo y analisis de complejidad para el punto 1.
3. Resolverlo mediante un algoritmo greedy. Dando su complejidad y pseudocodigo.
4. Resolverlo mediante un algoritmo de programación dinámica. Dando su complejidad y pseudocódigo
5. Programar los 3 algoritmos propuestos. 

## Parte 2: Redes de Subterraneos. 

La Ciudad de buenos aires cuenta con una red de subterraneos compuesta por 6 lineas.

![Red de subterraneos](/tda/images/SubteMapa3.png)

Un análisis de frecuencia en hora pico ha determinado:

- La demanda de flujo de pasajeros entrantes y salientes por cada estacion por hora. 
- La capacidad máxima de vagones por tramo por hora entre estaciones a causa del estado de las vias.
- La cantidad máxima de personas que pueden transportarse por vagón.

Por cuestiones contractuales se debe tener por linea una cantidad minima de vagones por hora. Por ultimo, la cantidad maxima de vagones por hora del sistema esta limitada por un valor determinado por la flota total de vagones.

Determinar si dados estos valores es factible proporcionar un servicio adecuado.

consideraciones:

- considerar que el numero de personas que entra y sale sumado de todo el sistema es 0.
- Existe la cantidad necesaria de locomotoras para la demanda.
- se pueden conmutar vagones entre estaciones

Se pide:

1. Analizar el problema teóricamente y explicar paso a paso como determinar la factibilidad.
2. Dar pseudocódigo y análisis de complejidad.
3. Programar la solución y proporcionar dos set de datos de prueba (uno factible y el otro no factible)
Trabajo Práctico Final
======================

{:.no_toc}

Teoría de Algoritmos - 2c 2025
Trabajo Práctico Final

## Lineamientos básicos

- El trabajo se realizará en grupos de cuatro o cinco personas.

- Se debe entregar el informe en formato pdf en el aula virtual de la materia.

- El informe debe presentar carátula con el nombre del grupo, datos de los integrantes y  fecha de entrega. Debe incluir número de hoja en cada página. No debe superar las 30 páginas + carátula + índice + referencias.

- Este trabajo práctico no requiere programación. Las resoluciones deben presentarse de forma teórica, incluyendo formulaciones, pseudocódigo y desarrollo paso a paso de los algoritmos.

- Al ser un trabajo de investigación debe OBLIGATORIAMENTE incluir las fuentes utilizadas. Utilizar el formato APA.

- En caso de re-entrega, entregar un apartado donde se explicitan las correcciones realizadas.

## Parte 1: Los delegados del departamento de planificación de eventos especiales.

Una empresa tecnológica cuenta con “n” empleados. Cada empleado trabaja en 1 o más proyectos con otros empleados. Se desea seleccionar un subconjunto de los empleados para nombrarlos “delegados” del departamento de planificación de eventos especiales. La dirección de la empresa quiere lograr que todo empleado o sea delegado o trabaje con al menos un delegado en algún proyecto en los que se encuentra. El puesto de delegado es remunerado. Se cuenta con una lista que indica cuánto recibe cada empleado si es nombrado en ese puesto. Es del interés de la dirección gastar el menor valor posible.

Se pide:	

1. En base a la definición del problema demostrar que el mismo pertenece a la clase NP-Hard. ¿Es posible afirmar dada su formulación actual que también pertenece a NP-Complete?

1. Expresar y explicar el problema como un problema de programación lineal entera.

1. Explicar cómo relajar el problema y resolver mediante programación lineal.

1. Proponer una instancia del problema pequeña cuya solución en el problema relajado no corresponde a una solución válida para nuestro problema original (con variable entera).

1. Utilizar la instancia del paso anterior para mostrar paso a paso cómo se obtiene la solución mediante simplex. Presente esquemáticamente cada iteración del algoritmo. Indique qué decisiones se toma en cada uno de estos y los cálculos realizados.

## Parte 2: Una solución concreta.

La dirección de la empresa tecnológica nos indica que quiere una solución real y aplicable para su problema. Por lo que nos solicita que le indiquemos 2 propuestas para lograrlo.

Se pide: 

1. Investigar la aplicación de Branch and Bound dentro de programación lineal entera. Explique cómo funciona paso a paso. Brinde pseudocódigo.

1. Investigue la técnica de resolución Randomized Rounding. Describa cómo se puede transformar una solución fraccionaria de la solución obtenida por programación lineal en una solución entera válida. Discuta la factibilidad y cómo el costo de la solución se relaciona con el LP

1. Utilice la instancia del problema de prueba anterior para demostrar cómo se obtienen las soluciones a nuestro problema con estos métodos.

1. Compare ambos métodos. ¿Nos brindan soluciones óptimas? ¿Son soluciones aproximadas? ¿Son soluciones correctas con alta probabilidad? ¿Cuál es la complejidad temporal y espacial de las mismas?


## Parte 3: Autómatas finitos

Los siguientes dos lenguajes corresponden a la intersección (expresado mediante la conjunción “y”) de otros dos lenguajes más simples (los símbolos de los mismos corresponden a los números 0 y 1) :

	lenguaje "a": {w| w (tiene dentro suyo la subcadena “1011”) y (todo “0” es seguido por al menos un “1”) } 
	lenguaje "b": {w| w (toda posición impar es un “1”) y (termina con 4 “1”)}

Se pide:

1. Construir un autómata finito determinista (AFD) de forma formal para cada uno de los 4 lenguajes simples.

1. Basándose en los autómatas construidos generar de forma formal (interseccion de los lenguajes) los dos autómatas finitos determinísticos de los lenguajes más complejos. Aplicar simplificación si es posible.

1. Representar cada uno de los AFD mediante su representación gráfica

1. Para cada AFD Brindar un ejemplo de una cadena que acepta y otra que rechaza. Explicar cómo determinar su autómata si es aceptado o rechazado paso a paso.

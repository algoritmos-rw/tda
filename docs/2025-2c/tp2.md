Trabajo Práctico n.º 2
======================
{:.no_toc}

Teoría de Algoritmos - 2c 2025
Trabajo Práctico 2

## Lineamientos básicos

- El trabajo se realizará en grupos de cinco personas.

- Un integrante del grupo deberá entregar el informe en formato pdf en nombre del grupo en el aula virtual de la materia..

- Cada integrante del grupo deberá entregar código fuente en (.zip) en el aula virtual de la materia. El .zip no debe contener carpetas en su interior, si no, solo 2 archivos ("transporte.py" y "extraterrestres.py").

- El lenguaje de implementación a utilizar es Python. No está permitido utilizar librerías externas.

- El programa a entregarse debe cumplir con los lineamientos mencionados en el enunciado. Si los mismos no son cumplidos con exactitud, el trabajo no será aprobado y deberá ser re-entregado con las correcciones.

- El informe debe presentar carátula con el nombre del grupo, datos de los integrantes, fecha y número de entrega. Debe incluir número de hoja en cada página. No debe superar las 25 páginas + carátula + índice + referencias.

- Debe entregar en el informe las fuentes consultadas en una sección de referencias.

- En caso de re-entrega, entregar luego del informe original un apartado con las correcciones realizadas



## Parte 1: Distribución eficiente

Una empresa de transportes pretende determina cómo realizar sus próximas distribuciones a lo largo de la provincia en centros de distribución. La misma cuenta con un conjunto de productos y con listas de combinaciones (subconjuntos) de estos productos.
Dado que se tienen que distribuir todos los elementos a lo largo de los centros y no cuentan con muchos camiones, se debe determinar la mínima cantidad de combinaciones tales que pueden repartir todos los productos. Cabe aclarar que los productos no se pueden repetir entre combinaciones.

Nos sugieren que utilicemos la técnica más eficiente que conocen, Branch & Bound.

Se pide:

1. Explique brevemente la solución. Defina la función costo y límite cuando corresponda.

2. Dar el pseudocódigo y estructuras de datos a utilizar.

3. Realice el análisis de complejidad temporal y espacial de la solución.

4. Brinde un ejemplo simple paso a paso del funcionamiento de la solución.

5. Programe la solución.

6. Determine si el programa tienen la misma complejidad que su propuesta teórica. 

### Formato de los archivos:

El archivo a ejecutar se debe llamar “transporte.py”

Debe recibir 2 parámetros (strings). El primer string corresponderá a los productos separados por coma y el segundo a los subconjuntos también separados por coma. Por ejemplo "transporte.py '1,2,3,4' '(1,2),(1,4,3),(1,3),(1,4)'"

La salida del programa debe ser por pantalla indicando los subconjuntos elegidos.

Además, dentro del archivo se debe implementar una función llamada `ejecucion(productos, subconjuntos)` que reciba por parámetro los productos y los subconjuntos (strings).

**Ejemplos de ejecución:**

`transporte.py '1,2,3,4' '(1,2),(1,4,3),(1,3),(1,4),(2),(1)'`

debe retornar `(2),(1,4,3)` por pantalla



## Parte 2: 

Contamos con un “n” agentes secretos que deben realizar el traslado de información importante. Cada agente se encuentra distribuido en diferentes ciudades (algunos podrían estar en la misma). Cada uno de ellos debe llevar la información a alguno de los “n” centros de investigación. Estos centros se encuentran cada uno en diferentes ciudades. Para viajar utilizarán como medio de transporte la red de líneas aéreas disponibles. Existe un subconjunto de ciudades seguras en las que podrían realizar escalas. Como medio de seguridad quieren que no más de “s” agentes pasen por la misma ciudad. Todas los vuelos son bidireccionales (es decir si existe el vuelo de la ciudad A a la B. También existe el vuelo de la ciudad B a la A)

Determinar si es posible que los agentes puedan realizar el envío y en caso positivo determinar qué ruta debe seguir cada uno de ellos.


Se pide:

1.  Generar una propuesta mediante redes de flujo que solucione el problema. Explicar la idea de esta.

1.  Presentar pseudocódigo.

1.  Realizar un análisis de optimalidad.

1.  Realizar análisis de complejidad temporal y espacial. Considere las estructuras de datos que utiliza para llegar a estos.

1. Programar la solución. Incluya la información necesaria para su ejecución. Compare la complejidad de su algoritmo con la del programa.

1. ¿Es posible expresar su solución como una reducción polinomial? En caso afirmativo explique cómo y en caso negativo justifique su respuesta.


### Formato de los archivos:

El programa a ejecutar se debe llamar “traslado”. Debe recibir por parámetros 2 números y 2 archivos. El primer número es la cantidad “n” de espías y centros. El segundo número corresponde a “s” la restricción por ciudad. El primer archivo corresponde a las ciudades y vuelos. El segundo de espías y centros de investigación.

El archivo de ciudades y vuelos es un archivo de texto. Y contiene una línea por vuelo entre ciudades
El formato de la línea es: ciudad origen, ciudad destino.

Ejemplo: “ciudades.txt”

	A,B
	A,D
	A,E
	B,C
	C,D
	C,E
	D,E

El archivo de espías y centro de investigación es un archivo de texto. Contiene “2n” líneas. Las primeras “n” son los espías y en la ciudad en la que inicia. Las últimas “n” son los centros y la posición en las que se encuentran.

Ejemplo: “espias.txt”

	Espia 1,A
	Espia 2,B
	Centro 1,C
	Centro 2,D

Si no es posible lograr el objetivo el programa debe mostrar en pantalla: “Es imposible lograr el objetivo”.

Si es posible, se debe mostrar en pantalla la ruta de traslados de cada espía. Cada ruta debe estar separada por coma. El primer ítem es el nombre del espía, el último el nombre de los centros y los intermedios las ciudades por la que pasa.



## Parte 3: 

Una famosa red social llamada HeadBook desarrolló una solución para maximizar las conexiones entre dos grupos de usuarios. Dada una red social, se realiza una partición de los usuarios en dos grupos de manera que el número de conexiones (amistades) entre los dos grupos es máximo.

Se pide:

1. Demostrar que el problema que se planteó c NP-C. Utilizar NAE-3SAT para demostrarlo.

2. Lejos de plantear un problema más sencillo, HeadBook busca que además de maximizar la cantidad de conexiones entre dos grupos de usuarios, los dos grupos tengan la misma cantidad de usuarios. Demostrar que este nuevo problema también maximizar las conexiones entre dos grupos de usuarios NP-C. Utilizar el problema anterior para demostrarlo.

3. Una persona afirma tener un método eficiente para responder si es posible o no cualquiera sea la instancia. Utilizando el concepto de transitividad y la definición de NP-C explique qué ocurriría si se demuestra que la afirmación es correcta.

4. Un tercer problema al que llamaremos X se puede reducir polinomialmente al problema de “Las 2 jornadas de capacitación”, qué podemos decir acerca de su complejidad?

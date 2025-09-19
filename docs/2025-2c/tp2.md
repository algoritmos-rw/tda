Trabajo Práctico n.º 2
======================
{:.no_toc}

Teoría de Algoritmos - 2c 2025
Trabajo Práctico 2

## Lineamientos básicos

- El trabajo se realizará en grupos de cinco personas.

- Un integrante del grupo deberá entregar el informe en formato pdf en nombre del grupo en el aula virtual de la materia..

- Cada integrante del grupo deberá entregar código fuente en (.zip) en el aula virtual de la materia. El .zip no debe contener carpetas en su interior, si no, solo 2 archivos ("escenario.py" y "extraterrestres.py").

- El lenguaje de implementación a utilizar es Python. No está permitido utilizar librerías externas.

- El programa a entregarse debe cumplir con los lineamientos mencionados en el enunciado. Si los mismos no son cumplidos con exactitud, el trabajo no será aprobado y deberá ser re-entregado con las correcciones.

- El informe debe presentar carátula con el nombre del grupo, datos de los integrantes, fecha y número de entrega. Debe incluir número de hoja en cada página. No debe superar las 25 páginas + carátula + índice + referencias.

- Debe entregar en el informe las fuentes consultadas en una sección de referencias.

- En caso de re-entrega, entregar luego del informe original un apartado con las correcciones realizadas



## Parte 1: 

El prestigioso restaurante “Altezzoso” de 3 estrellas “Michi Inn” se especializa en la elaboración de pizzas gigantes. Una vez por año realiza una recaudación por causas caritativas. Invita a “n” de las personas mas ricas del planeta y realiza una subasta de una pizza tamaño XXXL cortada en “m” porciones (n>m). Los invitados tienen un presupuesto de “p” liras que pueden dividir en “ofertas” para las diferentes porciones. La pizza ocupa una mesa circular donde se encuentra una silla frente a cada porción. Quien obtiene una determinada porción debe sentarse en su lugar para comerla. Un invitado solo puede acceder a una única porción. No necesariamente quien ofrece más plata por una porción la obtiene. La decisión es única y exclusivamente potestad del restaurante. Ellos quieren maximizar la ganancia.  Pero deben tener en cuenta una cuestión adicional: algunos de los invitados están enemistados con otros y no quieren sentarse a su lado. Por lo que informan que prefieren no comer a tener que soportarlos.

Nos contratan para que, en base a la información provista, determinemos qué porción asignar a cada invitado de forma tal de maximizar la ganancia cumpliendo las restricciones del problema.

Nos sugieren la siguiente la solución: Mediante backtracking determinar todas las posibles ubicaciones factibles (sin considerar las rotaciones en la mesa). Luego, por cada una de ellas calcular las ganancias de cada una de las rotaciones posibles.

Queremos Proponer una solución alternativa utilizando branch and bound.

Se pide:

1. Explique brevemente cada una de las soluciones. Defina la función costo y límite cuando corresponda.

1. Dar el pseudocódigo y estructuras de datos a utilizar en ambas propuestas.

1. Realice el análisis de complejidad temporal y espacial de ambas soluciones. Compararlas.

1. Brinde un ejemplo simple paso a paso del funcionamiento de las soluciones.

1. Programe ambas propuestas

1. Determine si los programas tienen la misma complejidad que su propuesta teórica. 

### Formato de los archivos:

Los programas a ejecutar se deben llamar “subasta_bt” y “subasta_bb”. Deben recibir por parámetro 2 archivos. El primero de las ofertas y el segundo de las restricciones de los invitados.

El archivo de ofertas es un archivo de texto. La primera línea corresponde a la cantidad de porciones. Luego cada línea corresponde a un invitado. Tiene separado por comas su nombre y la oferta por cada una de las porciones que realiza. La suma de todas las ofertas suma “p”.

Ejemplo:

	4
	Elon,10,0,10,5
	Steve,5,5,5,10
	Mark,7,7,7,4
	Jeff,0,0,25,0
	Larry,0,15,5,5
	Bill,8,7,10,0

El archivo de restricciones es un archivo de texto. Tiene una línea por invitado. En la línea se presenta el nombre del invitado y separado por coma a partir de este una lista con quienes no se quiere sentar. 

Ejemplo:

	Elon,Jeff,Larry
	Steve,Elon
	Mark,Bill,Larry
	Jeff,Elon
	Larry
	Bill,Mark

La respuesta se debe mostrar por pantalla y debe ser siguiendo el siguiente formato:

	La ganancia máxima a obtener es: [poner aquí la ganancia]
	Los invitados ganadores son: [poner aquí los ganadores separados por coma que brindan la mayor ganancia ordenados por número de porción



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

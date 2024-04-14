Trabajo Práctico n.º 2
======================
{:.no_toc}

Teoría de Algoritmos 1 - 1c 2024
Trabajo Práctico 2

## Lineamientos básicos

- El trabajo se realizará en grupos de cinco personas.

- Se debe entregar el informe en formato pdf y código fuente en (.zip) en el aula virtual de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar algún otro, se debe pactar con los docentes.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución. La ausencia de esta información no permite probar el trabajo y deberá ser re-entregado con esta información.

- El informe debe presentar carátula con el nombre del grupo, datos de los integrantes y  y fecha de entrega. Debe incluir número de hoja en cada página. No debe superar las 20 páginas + carátula + índice + referencias.

- Debe entregar en el informe las fuentes consultadas en una sección de referencias.

- En caso de re-entrega, entregar un apartado con las correcciones mencionadas

## Parte 1: Un transporte abarrotado

Un transportador espacial se ha programado para realizar un vuelo desde la tierra a las nuevas instalaciones de investigación en la luna. El transportador tiene una capacidad de transporte de “k” kilos y la posibilidad de albergar “p” personas. Se ha recibido la petición de transporte de "n" personas. Cada persona "i" tiene un proyecto de investigación que requiere transportar un total de "wi" kilos. Además si lo elegimos nos otorga "vi" de ganancia. Debemos seleccionar la mejor combinación de personas sin superar las restricciones que nos aseguren la mayor ganancia posible. Resuelva el problema informando que personas seleccionar y qué ganancia se va a obtener.


Se pide:

1.  Resolver el problema utilizando programación dinámica. (incluya en su solución definición del subproblema, relación de recurrencia y pseudocódigo)

1. Analice la complejidad espacial y temporal de su propuesta

1. De un breve ejemplo paso a paso de funcionamiento de su propuesta

1. Programe su solución

1. Analice: ¿La complejidad de su propuesta es igual a la de su programa?

### Formato de los archivos:

El programa debe recibir por parámetro un archivo con la información de las personas y su respectivo proyecto. Además la capacidad de personas y cantidad maxima de peso que puede transportar Ejemplo:

	python mision.py personas.txt 5 1000

El archivo de personas corresponde a un archivo de texto donde cada línea corresponde a una persona y su proyecto (peso y ganancia). Estos valores están separados por una coma. Ejemplo:

	Alan Turing,300,1000
	John von Neumann,50,500
	Grace Murray Hopper,400,300
	Dennis Ritchie,200,450
	Claude Shannon,50,100
	Marvin Minsky,500,650
	Tim Berners-Lee,250,500


El programa deberá mostrar por pantalla el nombre de las personas elegidas, el peso transportado y la ganancia obtenida. Para el ejemplo la salida esperada es:

	Pasajeros: Alan Turing, John von Neumann, Tim Berners-Lee, Dennis Ritchie, Claude Shannon 
	Peso total: 300 + 50 + 250 + 200 + 50 = 750
	Ganancia: 1000 + 500 + 500 + 450 + 100 = 2550


## Parte 2: El papel exacto

Contamos con "n" actores y "m" papeles en una película a realizar. Cada actor se postuló para un subconjunto de papeles. Un estudio de mercado indica para cada par actor-papel posible una "potencialidad de espectadores" (valor de público que estaría dispuesto a pagar una entrada en el cine para verlo). El productor de la película quiere obtener el mayor número de potencionalidad de público seleccionando a los actores en los papeles adecuados para lograrlo. El valor de potencialidad del elenco se calcula sumando la potencialidad de los actores seleccionados. Nos pide que resolvamos el problema informando que actores contratar y en qué papel. No le importa cubrir todos los papeles, solo maximizar la potencialidad (luego buscarán otros actores de ser necesario).   

Se pide:

1.  Expresar y explicar el problema como una reducción polinomial entre el problema del enunciado y un problema de programación lineal

1. Determinar si el problema se puede resolver en tiempo polinomial. Justificar. 

1. Explicar como resolver el problema utilizando Simplex. Brindar pseudocódigo y explicación de su propuesta. Expresar como se representa la solución.

1. Analizar la complejidad temporal y espacial de cada uno de los pasos de su solución.

1. Presente paso a paso un ejemplo sencillo de su propuesta y cómo se construye la reducción. No hace falta resolver de forma completa el Simplex, puede expresar sus primeros pasos.

1. Programe su propuesta. Puede utilizar librerías para Simplex. (Ejemplos: ALGLIB o PulP)

1. Analice: ¿La complejidad de su propuesta es igual a la de su programa? Si utilizó alguna librería, ¿qué complejidad tiene? ¿Usa alguna mejora al algoritmo básico?

### Formato de los archivos:

El programa debe recibir por parámetro el path del archivo actores con los papeles a los que se postuló y su potencial de espectadores. Corresponde a un archivo de texto donde cada línea representa un eje.
El formato de la línea es: Actor,nro papel,potencialidad,[nro papel,potencialidad,...]

Ejemplo: “red.txt”

	Ricardo Darín,1,300,2,150
	Luis Brandoni,2,80,5,400
	Norma Aleandro,3,100,6,300
	Rodrigo de la Serna,1,380,4,350
	Guillermo Francella,1,70,3,240
	Luis Sandrini,3,95,4,400,5,400
	Fidel Pintos,2,100,3,2004	Adriana Aizemberg,6,200,7,100
	Julieta Díaz,1,200,3,300,6,2002	China Zorrilla,3,140,7,100
	...	

Debe resolver el problema y retornar por pantalla la respuesta los actores seleccionados y para qué papel. Además mostrar el valor conseguido de potencialidad de espectadores. .

## Parte 3: El evento continental distribuido ("ECD") 
Contamos con "n" centros de convención dispersos por la ciudad para un próximo evento continental. Este evento se realizará durante vaíios días en forma simultánea en cada uno de ellos. Los asistentes deben poder trasladarse en forma gratuita a su voluntad de un centro a otro. Para se han propuesto un conjunto de "m" puntos de interconexión. Cada centro se puede unir con un subconjunto de estos puntos de forma bidireccional. Asimismo  cada punto de traslado se comunica con otro subconjunto de puntos de traslado de forma bidireccional. Conocemos el valor económico de habilitar cada tramo de conexión (tanto centro-punto de interconexión como punto de interconexión-punto de interconexión). 
Nos solicitan determinar si es posible contratar la menor cantidad de tramos de forma que todos los centros queden interconectados y gastando menos que un valor "v" dado por la organización.

Se pide:

1. Realice un análisis teórico entre las clases de complejidad P, NP, NP-H y NP-C y la relación entre ellos.

1. Demostrar que, dada una posible solución al problema "ECD", se puede algorítmicamente  determinar si se cumple o no con los requerimientos de solución válida de forma "buena".

1. Demostrar que el problema no es fácil de resolver. Utilizar para eso el problema “Steiner Tree Problem” (suponiendo que sabemos que este es NP-C).

1. Demostrar que el problema "Steiner Tree Problem" pertenece a NP-C. (Para la demostración puede ayudarse con diferentes problemas, recomendamos “Exact Cover by 3-SET” (X3C). Puede investigar cómo realizar esta reducción)

1. En base a los puntos anteriores a qué clases de complejidad pertenece el problema de “ECD”? Justificar

1. Una persona afirma tener un método eficiente para responder el pedido cualquiera sea la instancia. Utilizando el concepto de transitividad y la definición de NP-C explique qué ocurriría si se demuestra que la afirmación es correcta.

1. Un tercer problema al que llamaremos X se puede reducir polinomialmente al problema de “ECD”, qué podemos decir acerca de su complejidad?

Consideraciones: Define cada uno de los problemas de forma concreta para evitar problemas de interpretación

Trabajo Práctico n.º 2
======================
{:.no_toc}

Teoría de Algoritmos 1 - 2c 2023
Trabajo Práctico 2

## Lineamientos básicos

- El trabajo se realizará en grupos de cinco personas.

- Se debe entregar el informe en formato pdf y código fuente en (.zip) en el aula virtual de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar algún otro, se debe pactar con los docentes.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución. La ausencia de esta información no permite probar el trabajo y deberá ser re-entregado con esta información.

- El informe debe presentar carátula con el nombre del grupo, datos de los integrantes y  y fecha de entrega. Debe incluir número de hoja en cada página. No debe superar las 20 páginas + carátula + índice + referencias.

- Debe entregar en el informe las fuentes consultadas en una sección de referencias.

- En caso de re-entrega, entregar un apartado con las correcciones mencionadas

## Parte 1: Los caballeros del rey Arturo

El Rey Arturo quiere elegir caballeros para su próxima misión diplomática. Hay 'n' caballeros sentados en la Mesa Redonda. Arturo conoce la popularidad de cada uno de sus caballeros en el reino a visitar (la tiene cuantificada en un entero). Por una profecía del mago Merlín los elegidos deben estar sentados de forma contigua para que no haya contratiempos en el viaje. El Rey nos solicita que lo ayudemos a elegir al grupo de caballeros contiguo que mayor habilidad tenga.

Se pide:

1.  Resolver el problema utilizando programación dinámica. (incluya en su solución definición del subproblema, relación de recurrencia y pseudocódigo)

1. Analice la complejidad espacial y temporal de su propuesta

1. De un breve ejemplo paso a paso de funcionamiento de su propuesta

1. Programe su solución

1. Analice: ¿La complejidad de su propuesta es igual a la de su programa?

### Formato de los archivos:

El programa debe recibir por parámetro un archivo con la información de los caballeros. Ejemplo:

	python arturo.py caballeros.txt

El archivo de caballeros corresponde a un archivo de texto donde cada línea corresponde a un caballero y su popularidad. Estos valores están separados por una coma. Ejemplo:

	Bors,8
	Gawain,-8
	Perceval,9
	Pellinore,-9
	Galahad,-10
	Gareth,-11
	Lancelot,12

Notar que Bors está sentado al lado Lancelot, ya que la mesa es circular.

El programa deberá mostrar por pantalla el nombre de los caballeros elegidos. Para el ejemplo la salida esperada es:

	Lancelot, Bors, Gawain, Perceval

## Parte 2: Los amigos de los OVNIS

La red de computadoras del área de investigación de la Asociación Amigos de la Ufología (AAU!) es un sistema autónomo, que se encuentra desplegado en varios países de la región. Esta red conecta diferentes servidores y permite la comunicación bidireccional entre ellos. Las diferentes conexiones tienen una velocidad máxima de transmisión de datos por segundo según sus características propias. Uno de estos servidores es una supercomputadora que utilizan para procesar posibles mensajes del espacio. Este fin de semana planean instalar un radiotelescopio y conectarlo a alguno de los servidores de la red. Quieren saber cómo pueden configurar las comunicaciones para enviar la mayor cantidad posible de datos por segundo. Además, como quieren mejorar su red, nos piden conocer cuales son las conexiones a mejorar para aumentar su capacidad de transmisión de información. 

Se pide:

1.  Expresar y explicar el problema como una reducción polinomial entre el problema del enunciado y un problema de redes de flujo

1. Demostrar que en la solución del problema se puede utilizar únicamente cada camino en un único sentido.

1. Resolver el problema utilizando redes de flujo. Brindar pseudocódigo y explicación de su propuesta. 

1. Analizar la complejidad temporal y espacial de cada uno de los pasos de su solución.

1. Presente paso a paso un ejemplo sencillo de su propuesta

1. Programe su solución

1. Analice: ¿La complejidad de su propuesta es igual a la de su programa?

### Formato de los archivos:

El programa debe recibir por parámetro el path del archivo con la red de flujo. Corresponde a un archivo de texto donde cada línea representa un eje.
El formato de la línea es: Servidor1,Servidor2,velocidad
Los nombres de los nodos pueden ser texto o número (sin espacios ni caracteres especiales). Se debe reservar los nombres “R” y “S” como el radiotelescopio y el supercomputador de la red

Ejemplo: “red.txt”

	R,1,10
	R,2,8
	R,3,5
	1,4,12
	2,4,6
	2,5,7
	3,5,14
	4,S,12
	5,S,19
	...

Debe resolver el problema y retornar por pantalla la respuesta.

## Parte 3: Chapucería de emergencia 

La nave espacial Serenity tuvo una falla catastrófica en su sistema de transmisión de energía desde su reactor principal al motor. En este momento están flotando en el espacio a la deriva. El ingeniero de a bordo tuvo como idea reutilizar una vieja y obsoleta red de intercomunicación de la nave como alternativa. La red está compuesta por varios cables que se intercomunican entre sí por medio de conmutadores. El problema es que existen algunos caminos posibles que generan ciclos en la red. Si no se eliminan provocarían la explosión de la nave. Tienen disponible el diagrama de toda la red y cuentan con un máximo de k cargas de detonación para inutilizar como mucho esta misma cantidad de conmutadores. Nos solicitan conocer si es posible colocar como mucha todas las cargas en conmutadores para eliminar los ciclos y poder encender los motores. Llamaremos a este problema “Cargas en conmutadores”

Se pide:

1. Realice un análisis teórico entre las clases de complejidad P, NP, NP-H y NP-C y la relación entre ellos.

1. Demostrar que, dada una posible solución que brindamos, se puede fácilmente determinar si se cumple o no con los requerimientos.

1. Demostrar que el problema no es fácil de resolver. Utilizar para eso el problema “Undirected Feedback Set” (suponiendo que sabemos que este es NP-C).

1. Demostrar que el problema “Undirected Feedback Set pertenece a NP-C. (Para la demostración puede ayudarse con diferentes problemas, recomendamos “Vertex Cover”)

1. En base a los puntos anteriores a qué clases de complejidad pertenece el problema de “Cargas en conmutadores”? Justificar

1. Una persona afirma tener un método eficiente para responder el pedido cualquiera sea la instancia. Utilizando el concepto de transitividad y la definición de NP-C explique qué ocurriría si se demuestra que la afirmación es correcta.

1. Un tercer problema al que llamaremos X se puede reducir polinomialmente al problema de “Cargas en conmutadores”, qué podemos decir acerca de su complejidad?

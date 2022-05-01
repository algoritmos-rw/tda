Trabajo Práctico n.º 3
======================
{:.no_toc}

Teoría de Algoritmos 1 - 1c 2022
Trabajo Práctico 3

## Lineamientos básicos

- El trabajo se realizará en grupos de cinco personas.

- Se debe entregar el informe en formato pdf y código fuente en (.zip) en el aula virtual de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar algún otro, se debe pactar con los docentes.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución. La ausencia de esta información no permite probar el trabajo y deberá ser re-entregado con esta información.

- El informe debe presentar carátula con el nombre del grupo, datos de los integrantes y  y fecha de entrega. Debe incluir número de hoja en cada página. No debe superar las 20 páginas.

- En caso de re-entrega, entregar un apartado con las correcciones mencionadas

- En este trabajo práctico se debe investigar cada una de las partes. **Se evalúa esto dentro de la nota final.**

- **Debe entregar en el informe las fuentes consultadas en una sección de referencias.**

## Parte 1: El viaje a Qatar

Una ONG con sede en Buenos Aires desea realizar un viaje grupal de “estudio” a Qatar entre las fechas de 21 de noviembre de 2022 y el 18 de diciembre de 2022. Han realizado diversas averiguaciones con compañías aéreas para conocer el costo de pasaje y la cantidad que podrían comprar para diferentes trayectos por ciudades del mundo. Su objetivo es determinar cuál es la máxima cantidad de personas que podría viajar y hacerlo al menor costo posible.

Se pide:

1.  Investigar y seleccionar uno de los siguientes algoritmos que resuelven este problema conocido como flujo máximo con costo mínimo ("Min Cost Max Flow"): "Cycle Cancelling Algorithm" o "Successive shortest path algorithm".

1. Explicar cómo funciona el algoritmo seleccionado. Incluir: pseudocódigo, análisis de complejidad espacial, temporal y optimalidad.

1. Dar un ejemplo paso a paso de su funcionamiento.

1. Programar el algoritmo.

1. Responder justificando: ¿La complejidad de su algoritmo es igual a la presentada en forma teórica?

### Formato de los archivos:

El programa debe recibir por parámetro el path del archivo donde se encuentra el grafo.
El formato del archivo es de texto. Las primeras dos líneas corresponden al nodo fuente y sumidero respectivamente. Continúa con una línea por cada eje del grafo con el formato: ORIGEN,DESTINO,COSTO UNITARIO,CAPACIDAD.

Ejemplo:

	BS AS
	QATAR
	BS AS,RIO,2,8
	BS AS,MADRID,3,4
	MADRID,NEW YORK,2,5
	…

El programa debe retornar en pantalla la cantidad máxima de personas que pueden viajar y el costo mínimo que se puede gastar.


## Parte 2: Un reality único

Para un casting para un nuevo reality show han generado un conjunto de “k” características que desean que tengan los diferentes participantes. Por ejemplo: “historia trágica”, “habilidades musicales”, “capacidad atlética”, “estudios universitarios”, “amor por los animales”, etc. Cuentan con un conjunto de “n” personas que se anotaron con deseos de participar. Para cada característica tienen la lista de personas que la posee. La producción desea seleccionar a un subconjunto de participantes de forma tal de que cada una de las características se vea representada. Además para lograr mayor variabilidad quieren que no existan dos personas con la misma característica.

Se pide:

1. Utilizando EXACT-COVER demostrar que el problema al que denominaremos “casting” es NP-C

1. Demuestre que EXACT-COVER es NP-C (puede ayudarse con diferentes problemas, entre ellos 3SAT, para hacerlo) 

1. Utilizando el concepto de transitividad y la definición de NP-C explique qué ocurriría si se demuestra que el problema EXACT-COVER pertenece a la clase P.

1. Un tercer problema al que llamaremos X se puede reducir polinomialmente a EXACT-COVER, qué podemos decir acerca de su complejidad? 

1. Realice un análisis entre las clases de complejidad P, NP y NP-C y la relación entre ellos.

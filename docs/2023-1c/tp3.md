Trabajo Práctico n.º 3
======================
{:.no_toc}

Teoría de Algoritmos 1 - 1c 2023
Trabajo Práctico 3

## Lineamientos básicos

- El trabajo se realizará en grupos de cinco personas.

- Se debe entregar el informe en formato pdf y código fuente en (.zip) en el aula virtual de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar algún otro, se debe pactar con los docentes.

- El informe debe presentar carátula con nombre del grupo, integrantes y fecha de entrega. Debe incluir número de hoja en cada página.

- La extensión del informe no debe superar las 20 páginas + carátula + índice + referencias.

- Debe presentar código fuente listo para su ejecución e instrucciones de compilación y ejecución dentro del informe.

- Debe entregar en el informe las fuentes consultadas en una sección de referencias.

- En caso de re-entrega, entregar un apartado con las correcciones mencionadas

## Parte 1: Flujo máximo con demandas

Hemos trabajado con problemas de maximización de flujo y problemas de circulación con demandas. En los primeros intentamos transportar - sin importar el camino - la mayor cantidad posible de flujo. En los segundos intentamos responder si es posible cumplir con los requerimientos de flujo con limitantes de producción y requerimientos de envío mínimo por determinados caminos. Existen escenarios donde estos requerimientos se entremezclan. Queremos trabajar sobre el problema conocido como “Flujo máximo con demandas de ejes” (“con demandas” o “con límites inferiores”). En este problema queremos lograr el máximo flujo posible transportado entre una fuente y un sumidero pero teniendo adicionalmente que cumplir con el pasaje de flujo en ciertos ejes y con valores determinados. Para expresarlo tendremos por cada eje “e” su capacidad c(e), y también un valor mínimo de flujo que debe atravesarlo l(e) (al que llamaremos demanda).

Se pide:

1. Investigar y explicar cómo resolver este problema.

1. Brinde pseudocódigo que explique cada uno de los pasos de su solución.

1. Proponga un enunciado de un problema de su invención que requiera para su solución reducirlo al problema anterior.

1. Explique cómo se realiza la reducción paso a paso.

1. Brinde un ejemplo paso a paso donde se aprecie el funcionamiento de toda su propuesta

1. Analice la complejidad temporal y espacial de todo lo realizado (en función de los parámetros de su problema).

1. Programe el algoritmo (únicamente el que resuelve “Flujo máximo con demandas de ejes”).

1. Analice: su programa mantiene la complejidad temporal y espacial teórica?

### Formato de los archivos:

El programa debe recibir por parámetro el path del archivo con la red de flujo. Corresponde a un archivo de texto donde cada línea representa un eje.

El formato de la línea es: Nodo_origen,Nodo_destino,capacidad,demanda

Los nombres de los nodos pueden ser texto o número (sin espacios ni caracteres especiales).  Se debe reservar los nombres “S” y “T” como la fuente y el sumidero de la red de flujo

Ejemplo: “red.txt”

	S,1,10,0
	1,T,10,0
	S,2,10,0
	1,2,10,1
	2,T,10,0
	...
 
Debe resolver el problema y retornar por pantalla el flujo máximo y por cada eje el flujo que lo atraviesa.

## Parte 2: La separación en grupos compatibles

Una empresa cuenta con “n” empleados que debe separar para un futuro evento en no más de k grupos de trabajo. Dentro de cada grupo es fundamental que cada persona pueda trabajar en total armonía con el resto de los integrantes. Por ese motivo el departamento de recursos humanos ha realizado una encuesta a cada empleado. En base a los resultados elaboró una planilla con compatibilidades. Cada línea de la planilla contiene 2 empleados (“A”, “B”). Se debe interpretar la línea como que el empleado “A” considera que puede trabajar bien con el empleado “B”. Nos solicitan resolver este problema (que llamaremos “Grupos compatibles”).

Se pide:

1. Realice un análisis teórico entre las clases de complejidad P, NP, NP-H y NP-C y la relación entre ellos.

1. Demostrar que, dada una posible solución que brindemos, la empresa puede fácilmente determinar si se cumple o no la separación propuesta.

1. Demostrar que el pedido no es fácil de resolver. Utilizar para eso el problema “clique cover” (suponiendo que sabemos que este es NP-C).

1. Demostrar que el problema “clique cover” pertenece a NP-C. (Para la demostración puede ayudarse con diferentes problemas, recomendamos “k coloreo de grafos”)

1. En base a los puntos anteriores a que clases de complejidad pertenece el problema de “grupos compatibles”? Justificar

1. Un empleado de recursos humanos de la compañía afirma tener un método eficiente para responder el pedido cualquiera sean los empleados, compatibilidades y grupos de trabajo. 

1. Utilizando el concepto de transitividad y la definición de NP-C explique qué ocurriría si se demuestra que la afirmación es correcta.

1. Un tercer problema al que llamaremos X se puede reducir polinomialmente al problema de “grupos compatibles”, qué podemos decir acerca de su complejidad?

Trabajo Práctico n.º 3
======================
{:.no_toc}

Teoría de Algoritmos 1 - 2c 2021
Trabajo Práctico 3

## Lineamientos básicos

- El trabajo se realizará en grupos de cinco personas.

- Se debe entregar el informe en formato pdf y código fuente en (.zip) en el aula virtual de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar algún otro, se debe pactar con los docentes.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución. La ausencia de esta información no permite probar el trabajo y deberá ser re-entregado con esta información.

- El informe debe presentar carátula con el nombre del grupo, datos de los integrantes y  y fecha de entrega. Debe incluir número de hoja en cada página.

- En caso de re-entrega, entregar un apartado con las correcciones mencionadas

## Parte 1: Una campaña publicitaria masiva pero mínima

Una empresa de turismo que vende excursiones desea realizar una campaña publicitaria en diferentes vuelos comerciales con el objetivo de llegar a todos los viajeros que parten del país A y que se dirigen al país B. Estos viajeros utilizan diferentes rutas (algunos vuelos directos, otros armando sus propios recorridos intermedios). Se conoce para una semana determinada todos los vuelos entre los diferentes aeropuertos con sus diferentes capacidades. Además parten del supuesto que durante ese periodo la afluencia entre A y B no se verá disminuida por viajes entre otros destinos.

Desean determinar en qué trayectos simples (trayecto de un viaje que inicia desde un aeropuerto y termina en otro) poner publicidad de forma de alcanzar a TODAS las personas que tienen el destino inicial A y el destino final B. Pero además desean que siempre que sea posible seleccionen la combinación que tenga el menor número de vuelos comerciales. Esto es porque pagan tanto por cantidad de vuelos como por pasajeros que cumplan con la condición de ser del país de origen A y con destino final B. 

Se pide:
 
1. Proponer una solución algorítmica que resuelva el problema de forma eficiente. Explicarla paso a paso. Utilice diagramas para representarla.

1. Plantear la solución como si fuese una reducción de problema. ¿Puede afirmar que corresponde a una reducción polinomial? Justificar.

1. ¿Podría asegurar que su solución es óptima?

1. Programe la solución

1. Compare la complejidad temporal y espacial de su solución programada con la teórica. ¿Es la misma o difiere?


### Formato de los archivos:

El programa debe recibir por parámetro el path del archivo donde se encuentran los vuelos disponibles entre pares de ciudades y la cantidad maxima de pasajeron en la misma.

El archivo debe ser de tipo texto y presentar por renglón, separados por coma el pais de origen el de destino y la capacidad del mismo. Las primeras dos lineas del archivo contiene el pais de origen y de destino respectivamente

Ejemplo: “vuelos.txt”

	A
	B
	A,D,140
	A,E,200
	D,B,100
	...

Debe resolver el problema y retornar por pantalla la solución. Debe mostrar por consola en en que vuelos poner la publicidad. Además imprimir cual es la cantidad maxima de pasajeros que puede inr de A a B.

## Parte 2: Equipos de socorro 

El sistema ferroviario de un país cubre un gran conjunto de su territorio. El mismo permite realizar diferentes viajes con transbordos entre distintos ramales y subramales que pasan por sus principales ciudades.
Dentro de su proceso de mejoramiento del servicio buscan que ante una emergencia en una estación se pueda llegar de forma veloz y eficiente. Consideran que eso se lograría si el equipo de socorro se encuentra en esa misma estación o en el peor de los casos en una estación vecina (que tenga una trayecto directo que no requiere pasar por otras estaciones). Como los recursos son escasos desean establecer la menor cantidad de equipos posibles (un máximo de k equipos pueden solventar).
Se solicita nuestra colaboración para dar con una respuesta a este problema.  

Se pide:

1. Utilizar el problema conocido como “set dominante” para demostrar que corresponde a un problema NP-Completo.

1. Asimismo demostrar que el problema set dominante corresponde a un problema NP-Completo.

1. Con lo que demostró responda: ¿Es posible resolver de forma eficiente (de forma “tratable”) el problema planteado?

HINT: podría ser una buena idea utilizar 3SAT o VERTEX COVER.


## Parte 3: Un poco de teoría

1. Defina y explique qué es una reducción polinomial y para qué se utiliza.

1. Explique detalladamente la importancia teórica de los problemas NP-Completos.

1. Tenemos un problema A, un problema B y una caja negra NA y NB que resuelven el problema A y B respectivamente. Sabiendo que B es P

   1. Qué podemos decir de A si utilizamos NA para resolver el problema B (asumimos que la reducción realizada para adaptar el problema B al problema A es polinomial)
   
   1. Qué podemos decir de A si utilizamos NB para resolver el problema A (asumimos que la reducción realizada para adaptar el problema A al problema B es polinomial)
   
   1. ¿Qué pasa con los puntos anteriores si no conocemos la complejidad de B, pero sabemos que A es NP-C?

Trabajo Práctico n.º 1
======================
{:.no_toc}

Teoría de Algoritmos 1 - 1c 2023
Trabajo Práctico 1

## Lineamientos básicos

- El trabajo se realizará en forma individual.

- Se debe entregar el informe en formato pdf en el aula virtual de la materia.

- El informe debe presentar carátula con datos del autor y fecha de entrega. Debe incluir número de hoja en cada página.

- La extensión del informe no debe superar las 7 páginas + carátula + índice + referencias.

- Debe presentar codigo fuente e instrucciones de compilación y ejecución

- En caso de re-entrega, entregar un apartado con las correcciones mencionadas

## Parte 1: Maximización del emparejamiento

Sean A y B dos sets de “n” puntos en el plano p=(x,y). Un punto ai=(xi,yi) de A domina a un punto bj=(xj,yj) de B si y sólo si xi≥xj y yi ≥ yj. Un emparejamiento (match) entre un punto ai de A y uno bj B es posible si ai domina a bj. Llamamos matching M a un conjunto de emparejamientos(a1 , b1 ), (a2 , b2), . . . , (ak , bk )} y su tamaño corresponde a k. Un matching es máximo si no existe otro posible mátiching con major cantidad de puntos.  

Se pide para los set A y B obtener el matching máximo.


Resuelva:

1. Proponga una estrategia greedy óptima para resolver el problema con la menor complejidad espacial y temporal posible. Justifique su optimalidad. Justifique que sea greedy.

1. Explique cómo implementar algorítmicamente esa estrategia. Brinde pseudocódigo y estructuras de datos a utilizar.

1. Analice complejidad temporal y espacial de su propuesta

1. Programe su algoritmo y entregue dos ejemplos para su prueba.

1. ¿Su programa mantiene la complejidad espacial y temporal de su algoritmo? Justifique referenciando a la documentación del lenguaje si es necesario.


### Formato de los archivos:

El algoritmo debe recibir por parámetro el valor n y luego el nombre de dos archivos que contienen los puntos. El archivo de puntos corresponde a un archivo de texto que tiene una línea por punto con sus coordenadas separadas por un espacio.

Ejemplo “A.txt”:

	1,3 1,6
	4,8 8,5
	3,6 9,4

El programa debe mostrar en pantalla el matching encontrado y su tamaño. Respetando el siguiente formato:

	Tamaño del matching: x
	Matching:

	(A → B)
	a1 → b1

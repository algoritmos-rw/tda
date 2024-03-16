Trabajo Práctico n.º 1
======================
{:.no_toc}

Teoría de Algoritmos 1 - 1c 2024
Trabajo Práctico 1

## Lineamientos básicos

- El trabajo se realizará en grupos de cinco personas.

- Se debe entregar el informe en formato pdf y código fuente en (.zip) en el aula virtual de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar algún otro, se debe pactar con los docentes.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución. La ausencia de esta información no permite probar el trabajo y deberá ser re-entregado con esta información.

- El informe debe presentar carátula con el nombre del grupo, datos de los integrantes y  y fecha de entrega. Debe incluir número de hoja en cada página. No debe superar las 20 páginas + carátula + índice + referencias.

- Debe entregar en el informe las fuentes consultadas en una sección de referencias.

- En caso de re-entrega, entregar un apartado con las correcciones mencionadas

## Parte 1: La campaña 

Para promocionar un nuevo producto una empresa desea contratar influencers para la difusión del mismo. Para cada uno de ellos han calculado un "valor de penetración de mercado". Cuanto mayor este valor, mayor posibilidad de que mas de sus seguidores se interesen en el producto. Este valor corresponde a un número entero positivo. Existen pares de influencers que por diversos motivos no quieren o no pueden trabajar juntos. Esta información es conocida por la empresa.

Nos solicitan que determinemos a que influencers contratar para maximizar el valor de penetración de mercado (los valores de los influencers contratados se suman para establecer el total. 

Se pide:

1.  Proponga y explique una solución del problema mediante Branch and Bound.

1.  Brinde pseudocódigo y estructuras de datos a utilizar. 

1.  Realice el análisis de complejidad temporal y espacial.

1.  Brinde un ejemplo simple paso a paso del funcionamiento de su solución.

1.  Programe su propuestaa

1.  Determine si su programa tiene la misma complejidad que su propuesta teórica.

### Formato de los archivos:

El programa debe recibir por parámetro un archivo con los influencers. Ejemplo:

	python promocion.py influencers.txtt

El archivo de influencers corresponde a un archivo de texto donde cada línea corresponde a un candidato a contratar. Está definido por un código numérico separado incremental, luego su nombre, su valor de penetración de mercado y finalmente una lista numérica de los influencers con los que no puede trabajar. Cada uno de estos valores separados por coma. Ejemplo:

	1,Cacho,8,3,4 
	2,Lucho,10,5 
	3,Suncho,15,1
	4,Pucho,40,1
	5,Tucho,25,2
	6,Fercho,9
s
Debe resolver el problema y retornar por pantalla la solución. Primero el valor total de penetración de mercado obtenido y luego el nombre de los influencers seleccionados uno por línea. Siguiendo el ejemplo esta podría ser la solución:


	Valor conseguido: 89

	Pucho
	Suncho
	Tucho
	Fercho


## Parte 2: Reunión de camaradería 

Una gran empresa realizará una reunión de camaradería para sus empleados. Sin embargo, para evitar problemas que ocurrieron en eventos anteriores, no quieren que jefes y empleados directos se mezclen. Es decir que si se invita al jefe, no se puedo invitar a sus subordinados directos. Contamos con el organigrama de la empresa (que tiene una estructura de árbol) y deseamos determinar a quién invitar para lograr la mayor asistencia posible.

Se pide:

1.  Determinar y explicar cómo se resolvería este problema utilizando la metodología greedy. 

1.  Brinde pseudocódigo y estructuras de datos a utilizar.  


1.  De un ejemplo paso a paso. ¿Qué complejidad temporal y espacial tiene la solución?

1.  Justifique por qué corresponde su propuesta a la metodología greedy.

1.  Demuestre que su solución es óptima.

## Parte 3: Distribución balanceada 
Se cuenta con m obras en latín que deben ser traducidas. Cada obra contiene un número determinado de páginas. El listado de obras se encuentra ordenado de menor a mayor según este valor. Disponemos de n traductores que pueden realizar el trabajo. A cada autor se le pueden dar obras consecutivas. Deseamos asignar a cada autor obras a traducir de forma tal que la máxima cantidad de paginas entregada a los mismos sea la menor posible.


Se pide:

1.  Proponer un algoritmo utilizando división y conquista que lo resuelva. Incluir pseudocódigoo

1.  Analice la complejidad del algoritmo utilizando el teorema maestro y desenrollando la recurrencia.

1.  Brindar un ejemplo de funcionamiento.

1.  Programe su soluciónn

1.  Analice si la complejidad de su programa es equivalente a la expuesta en el punto 2.

### Formato de los archivos:

El programa debe recibir por parámetro la cantidad de traductores, de obras y un archivo con las paginas de cada obra. Ejemplo:

	python distribuir.py 4 6 obras.txt 4

El archivo de obras corresponde a un archivo de texto donde cada línea corresponde a la cantidad de páginas que tienen las obras. Ejemplo:

	89
	150
	201
	225
	246
	303

Debe resolver el problema y retornar por pantalla la cantidad de paginas máximas asignadas.

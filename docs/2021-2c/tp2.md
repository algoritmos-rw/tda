Trabajo Práctico n.º 2
======================
{:.no_toc}

Teoría de Algoritmos 1 - 2c 2021
Trabajo Práctico 2

## Lineamientos básicos

- El trabajo se realizará en grupos de cinco personas.

- Se debe entregar el informe en formato pdf y código fuente en (.zip) en el aula virtual de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar algún otro, se debe pactar con los docentes.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución. La ausencia de esta información no permite probar el trabajo y deberá ser re-entregado con esta información.

- El informe debe presentar carátula con el nombre del grupo, datos de los integrantes y  y fecha de entrega. Debe incluir número de hoja en cada página.

- En caso de re-entrega, entregar un apartado con las correcciones mencionadas

## Parte 1: Minimizando costos

Una empresa productora de tecnología está planeando construir una fábrica para un producto nuevo. Un aspecto clave en esa decisión corresponde a determinar dónde la ubicarán para minimizar los gastos de logística y distribución. Cuenta con N depósitos distribuidos en diferentes ciudades. En algunas de estas ciudades es donde deberá instalar la nueva fábrica. Para los transportes utilizarán las rutas semanales con las que ya cuentan. Cada ruta une de ida y vuelta dos depósitos. No todos los depósitos tienen rutas que los conecten. Por otro lado, los costos de utilizar una ruta tienen diferentes valores. Por ejemplo hay rutas que requieren ingresar nuevos viajes. En otros casos son rutas subvencionadas y utilizarlas les da una ganancia a la empresa. Otros factores que influyen son  gastos de combustibles y peajes. Para simplificar se ha desarrollado una tabla donde se indica para cada ruta existente el costo de utilizarla (valor negativo si da ganancia).

Los han contratado para resolver este problema.

Han averiguado que se puede resolver el problema utilizando Bellman-Ford para cada par de nodos o Floyd-Warshall en forma general. Un amigo les sugiere utilizar el algoritmo de Johnson.

Se pide:

1.  Investigar el algoritmo de Johnson y explicar cómo funciona. ¿Es óptimo?

1. En una tabla comparar la complejidad temporal y espacial de las tres propuestas. 

1. Analizar en qué situaciones una solución es mejor que otras

1. Crear un ejemplo con 5 depósitos y mostrar paso a paso cómo lo resolvería el algoritmo de Johnson.

1. ¿Puede decirse que Johnson utiliza en su funcionamiento una metodología greedy? Justifique

1. ¿Puede decirse que Johnson utiliza en su funcionamiento una metodología de programación dinámica? Justifique

1. Programar la solución


### Formato de los archivos:

El programa debe recibir por parámetro el path del archivo donde se encuentran los costos entre cada depósito.
El archivo debe ser de tipo texto y presentar por renglón, separados por coma un par de depósitos con su distancia.

Ejemplo: “depositos.txt”

	A,B,54
	A,D,-3
	B,C,8
	...

(!) si en el archivo está la dupla A,B (ruta A-B) se considera que también existe la ruta B-A

Debe resolver el problema y retornar por pantalla la solución. Debe mostrar por consola en en que ciudad colocar el depósito. Además imprimir en forma de matriz los costos mínimos entre cada uno de los depósitos.

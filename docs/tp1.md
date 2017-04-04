---
layout: default
math: true
---

Trabajo Práctico n.º 1
======================
{:.no_toc}

El trabajo práctico consiste en las tres partes que se listan a continuación.

Lineamientos básicos:

  - el trabajo se realizará en grupos de tres.

  - la fecha de entrega es el **lunes 24 de abril de 2017**. Se debe entregar en el horario de clase en papel (informe + `código en monoespacio`), más una entrega en digital de código (.zip) e informe (.pdf) al correo de entregas del curso: `tps.7529rw@gmail.com`.

  - el lenguaje de implementación es libre, pero se debe comunicar por correo en caso de _no_ ser uno de: C, Python, Java, JavaScript, Ruby.


## Contenidos
{:.no_toc}

* TOC
{:toc}

## Asignación de residencias

El 5 de abril, miles de estudiantes de medicina rendirán el Examen de Concurso de la Ciudad de Buenos Aires
para llevar a cabo residencias y concurrencias durante los próximos años. En este contexto, decenas de hospitales
publican un número de vacantes por especialidad en las que admiten residentes.

Definimos el problema de asignación genérico de residencias de la siguiente manera: sean $$n$$ estudiantes que desean llevar
a cabo sus residencias en alguna de las $$l$$ especialidades dictadas por los $$m$$ hospitales públicos de una determinada ciudad.
Cada hospital para cada especialidad posee una cantidad $$q_{ij}$$ de vacantes.

Suponer que cada uno de los estudiantes tiene un listado de preferencias de tamaño $$l \cdot m$$ en donde se contemplan todas las
especialidades de todos los hospitales, y que a su vez los resultados del examen permiten a cada hospital establecer una
orden de mérito para cada especialidad.

Se pide:

1. Reducir el problema de los matrimonios estables descriptos en la bibliografía al problema de la asignación genérico de residencias.
2. Implementar un algoritmo que resuelva el problema considerando la simplificación de que no existan especialidades.
3. Implementar un programa que genere instancias aleatorias del problema simplificado dados los parámetros $$n$$
   (cantidad de aplicantes) y $$m$$ (cantidad de hospitales).
     Este deberá devolver:
      - Un arreglo E de $$n$$ listas de tamaño $$m$$ que representan las preferencias de cada estudiante.
      - Un arreglo H de $$m$$ listas de tamaño $$n$$ que representan el orden de mérito para cada hospital.
      - Un arreglo Q de tamaño $$n$$ que modele la cantidad de vacantes de cada hospital.
4. Simular la ejecución del algoritmo ante entradas generadas aleatoriamente con
    1. $$n$$ = $$m$$ = 100
    2. $$n$$ = $$m$$ = 1000
    3. $$n$$ = $$m$$ = 10000
    4. $$n$$ = $$m$$ = 100000
5. Extraer breves conclusiones (máximo dos párrafos) sobre el rendimiento del algoritmo ante diferentes tamaños de la entrada
  comparándolo con su complejidad computacional.

## Puntos de falla

En un intento para mejorar el servicio de luz para el verano del año 2018, se quiere proteger el servicio eléctrico.
Para ello, se notó que existen ciertos generadores que son muy importantes para la red y muy propensos a fallas.

Dado un modelo de la red como un grafo no dirigido, se propone aplicar los conocimientos adquiridos en la materia para
identificar aquéllos nodos que son más frágiles, debido a que su baja generaría la desconexión del circuito.

Se pide:

1. Implementar el algoritmo de Hopcroft y Tarjan para encontrar puntos de articulación en grafos.
2. Importar los archivos provistos por el curso y ejecutar el algoritmo para encontrar la cantidad de nodos frágiles de la red.
3. Escribir un breve informe (máximo tres párrafos) comentando el funcionamiento del algoritmo.
4. Extraer breves conclusiones (máximo dos párrafos) sobre el rendimiento del algoritmo ante diferentes tamaños de la entrada
  comparándolo con su complejidad computacional.

## Comunidades en redes

Un grupo de científicos de datos propuso estudiar el comportamiento de los usuarios de una dada red social
en la que no todas las relaciones son simétricas (es decir, el usuario _a_ no necesariamente es amigo del _b_ cuando _b_ es amigo de _a_).

Se sospecha que las relaciones entre las comunidades es tan fuerte que se pueden identificar usando un simple algoritmo de
componentes fuertemente conexas.

Se pide:

1. Implementar el algoritmo de Kosaraju para encontrar las componentes fuertemente conexas en grafos dirigidos.
2. Importar los archivos provistos por el curso y ejecutar el algoritmo para encontrar la cantidad de componentes fuertemente conexas en la red.
3. Escribir un breve informe (máximo tres párrafos) comentando el funcionamiento del algoritmo.
4. Extraer breves conclusiones (máximo dos párrafos) sobre el rendimiento del algoritmo ante diferentes tamaños de la entrada
  comparándolo con su complejidad computacional.


## Aclaraciones generales

1. Los grafos serán provistos en el formato propuesto por Sedgewick, en donde los vértices estarán nombrados según
indentificadores desde 0 hasta $$V - 1$$, y los archivos de entrada están armados según:
  - Una primera línea indicando la cantidad de vértices $$V$$.
  - Una segunda línea indicando la cantidad de aristas $$A$$.
  - Sucesivas líneas representando cada arista, en dónde se indican los vértices de origen y destino, separados por espacios.

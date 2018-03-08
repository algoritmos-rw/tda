Trabajo Práctico n.º 3
======================
{:.no_toc}

El trabajo práctico consiste en las tres partes que se listan a continuación.

Lineamientos básicos:

  - el trabajo se realizará en grupos de tres personas.

  - la fecha de entrega es el **viernes 23 de junio de 2017**. Se debe entregar en el horario de clase en papel (informe + `código en monoespacio`), más una entrega en digital de código (.zip) e informe (.pdf) al correo de entregas del curso: `tps.7529rw@gmail.com`.

  - el lenguaje de implementación es libre, pero se debe comunicar por correo en caso de _no_ ser uno de: C, Python, Java, JavaScript, Ruby.


## Contenidos
{:.no_toc}

* TOC
{:toc}

## Programación dinámica

Se tiene una predicción del valor de una determinada acción en la bolsa en un determinado período de _n_ días. Se quiere encontrar el par de días
más favorable para comprar y vender acciones dentro del lapso en cuestión.

Por ejemplo, si _n = 3_ y _v(1) = $9_, _v(2) = $1_, _v(3) = $5_, conviene comprar el día 2 y vender el 3, obteniendo una ganancia de $4 por acción.

  - Implementar una solución al problema de la predicción de acciones por programción dinámica en tiempo lineal.
  - Escribir un breve informe indicando el funcionamiento del algoritmo y su ecuación de recurrencia.

## Algoritmos randomizados

Similar a la definición en redes de transporte, un corte global de un grafo no dirigido es una partición A, B de vértices tales que su intersección sea nula
y su unión devuelva el conjunto _V_. Se define el corte global mínimo como el corte global que conecta menos vértices entre A y B.

Se pide:

  - Implementar un programa que dados un parámetros _n_ genere un grafo conexo no dirigido de _n_ vértices y _2n_ aristas.
  - Implementar el algoritmo de contracción de Karger descripto en la bibliografía.<sup>[1](#kt-gmc)</sup><sup>[2](#erickson-gmc)</sup>
  - Escribir un breve informe indicando el funcionamiento del algoritmo y a qué categoría de randomización pertenece.

## Algoritmos aproximados

El problema de la suma de subconjuntos (_subset sum_) es un conocido problema NP-Completo, demostrado por primera vez por Richard Karp en 1972.<sup>[3](#karp-ss)</sup>
Se quiere obtener una aproximación al problema de optimización que dado un parámetro _t_ devuelve la mayor suma menor a _t_.

Se pide:

  - Implementar un programa que dado un parámetro _n_ genere una instancia del problema de optimización con _n_ enteros positivos y un _t_ entero positivo.
  - Implementar la estretegia polinómica descripta en la bibliografía.<sup>[4](#clrs-ss)</sup>
  - Escribir un breve informe indicando su funcionamiento.

## Aclaraciones generales

1. El informe de todo el trabajo no debe superar las dos carillas de extensión, y deberá incluir las instrucciones para ejecutar todos
  los programas desarrollados.
2. Para la implementación de los algoritmos se podrán usar todo tipo de bibliotecas, excepto de grafos.
3. Los grafos deberán ser generados en el formato propuesto por Sedgewick, en donde los vértices estarán nombrados según
indentificadores desde 0 hasta $$V - 1$$, y los archivos de están confeccionados según:
  - Una primera línea indicando la cantidad de vértices $$V$$.
  - Una segunda línea indicando la cantidad de aristas $$A$$.
  - Sucesivas líneas representando cada arista, en dónde se indican los vértices de origen y destino, separados por espacios.
  Sólo se listará una de las direcciones si el grafo es no dirigido.

## Referencias
<a name="kt-gmc">1</a>: Kleinberg, J.; Tardos, E.: _Algorithm Design_, Addison Wesley (2006), cap. 13.2 "Finding the global minimum cut", pp.: 714-719.

<a name="erickson-gmc">2</a>: Erickson, J: _Models of Computation_ (2015), cap. 13 "Randomized minimum cut".

<a name="karp-ss">3</a>: Karp, R.: _Reducibility Among Combinatorial Problems_ (1972), "Complexity of Computer Computations". New York: Plenum. pp. 85–103.

<a name="clrs-ss">4</a>: Cormen, T.; Leiserson, C.; Rivest, R.; Stein, C.: _Introduction to Algorithms_ (tercera edición), MIT Press (2009), cap. 35.5 "The subset-sum problem", pp.: 1128-1134.

{% include math.html %}

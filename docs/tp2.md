---
layout: default
math: true
---

Trabajo práctico n.º 2
======================
{:.no_toc}

El trabajo práctico consiste en las dos partes que se listan a continuación.

Lineamientos básicos:

  - el trabajo se realizará en grupos de tres o cuatro personas.

  - la fecha de entrega es el **lunes 14 de noviembre de 2016**. Se debe entregar en el horario de clase en papel (informe + `código en monoespacio`), más una entrega en digital de código (.zip) e informe (.pdf) al correo de entregas del curso: `tps.7529rw@gmail.com`.

Contenidos
==========
{:.no_toc}

1. TOC
{:toc}


Programación dinámica
=====================

En esta primera mitad del trabajo práctico se examinan los algoritmos de programación dinámica que resuelven los siguientes problemas:

  - el problema de la mochila
  - el problema del viajante de comercio

ambos no polinómicos.

En un futuro trabajo práctico se comparará la complejidad de estos algoritmos con los algoritmos de aproximación correspondientes, esto es: que resuelven los mismos problemas de manera no exacta.

Por tanto, lo que se pide en esta parte es:

  1. dos implementaciones por programación dinámica, una para cada problema, siguiendo un formato de entrada específico

  2. un breve informe con los tiempos de ejecución sobre distintas instancias del problema.

A continuación se especifica formalmente cada problema, formato de entrada, y lineamientos para el estudio de complejidad.


El problema de la mochila
-------------------------

Se pide implementar una solución por programación dinámica a la **versión 0-1 del problema de la mochila**. El capítulo 6.4 de Kleinberg y Tardos (2006) describe el problema y el algoritmo correspondiente. A continuación se incluye síntesis del problema.[^1]

[^1]: Kleinberg y Tardos primero describen una versión restringida en la que $$v_i = w_i$$, y en la segunda mitad del capítulo describen el algoritmo para $$v_i \ne w_i$$.

Dato un conjunto de elementos $$S = \{1, 2, \ldots, n\}$$ el problema consiste encontrar la sequencia $$X = (x_1, x_2, \ldots, x_n)$$ que maximice:

$$
\sum_{i \in S} v_i x_i
$$

con la restricción:

$$
\sum_{i \in S} w_i x_i \le W
$$

donde $$v_i, w_i, W \ge 0$$ y $$x_i \in \{0, 1\}$$.

A diferencia del caso $$v_i = w_i$$, en esta versión la relación de recurrencia propuesta toma dos variables, el número de ítems a considerar y el máximo peso permitido $$w$$:

$$
P(i, w) =
\left\{
\begin{array}{rl}
\text{si } w < w_i : & P(i - 1, w) \\
\text{si no} : &
      \max \left[
        \begin{array}{ll}
         P(i - 1, w) \\
         P(i - 1, w - w_i) + v_i
         \end{array}\right]
  \end{array}
\right.
$$

La solución $$X$$ se puede derivar de la llamada inicial $$P(n, W)$$.


### Archivos de prueba ###
{:.no_toc}

Para verificar el algoritmo se pueden usar los archivos de prueba de [David Pisinger][dp]. Los archivos están clasificados por tamaño y dificultad; cada archivo incluye 1000 instancias con su solución correspondiente.

Recomendaciones durante el desarrollo:

  - usar inicialmente el archivo de coeficientes pequeños ([smallcoeff.tgz], 142 MiB).

  - usar los archivos con $$n = 50$$ y $$R = 1000$$: _knapPI\_{0-9}\_50\_1000.csv_.

  - una vez el verificada la corrección de la implementación, verificar que el tiempo de ejecución no se dispara para valores de $$n$$ mayores.[^2]

  - usar para el informe el archivo de casos “difíciles” ([hardinstances.tgz], 45 MiB).

Cada archivo CSV tiene 100 instancias de prueba del mismo tamaño y en el mismo formato, separadas por `-----`. El formato de cada instancia es, línea a línea:

  - el nombre de la instancia, por ejemplo _knapPI\_1\_50\_1000\_1_

  - el número de ítems en el problema, por ejemplo `n 500`

  - la capacidad de la mochila $$W$$, por ejemplo `c 995`

  - el valor óptimo conseguido por Pisinger (formato: `z 8373`) y, en la línea siguiente, el tiempo de resolución que obtuvo (formato: `time 0.01`)

  - _n_ líneas siguiendo el formato CSV: `num_item,valor,peso,x`, donde _x_ es 1 o 0 según el ítem se incluyó o no en la solución, respectivamente.[^3]

  - la línea de fin de instancia, `-----`.

[^2]: Cada instancia de prueba en los archivos incluye el tiempo de ejecución que obtuvo Pisinger durante la investigación. Todos las instancias de _smallcoeff.tgz_ resolvieron en menos de 1 segundo.

[^3]: En el archivo README, se usa _p_ para representar el valor (por ‘profit’) y _w_ para el peso (por ‘weight’).

[dp]: http://www.diku.dk/~pisinger/codes.html
[smallcoeff.tgz]: http://www.diku.dk/~pisinger/smallcoeff_pisinger.tgz
[hardinstances.tgz]: http://www.diku.dk/~pisinger/hardinstances_pisinger.tgz


El problema del viajante de comercio
------------------------------------

Se pide implementar el algoritmo de Bellman–Held–Karp para resolver la **versión asimétrica del problema del viajante de comercio**, esto es: dado un grafo dirigido, _completo_ y pesado, encontrar un tour o ciclo hamiltoniano de costo mínimo que comience y termine en un vértice $$v_0$$ dado. (El costo se define como la suma de pesos de las aristas recorridas.)

Para simplificar la programación del algoritmo, consideraremos que una instancia del problema de tamaño $$N$$ queda definida por el vértice inicial $$0 \lt v_0 \le N$$ y una matriz de costos no negativos $$C = N \times N$$, por ejemplo:

$$
C =
\begin{pmatrix}
    0 & 2 & 9 & 10 \\
    1 & 0 & 6 &  4 \\
    15 & 7 & 0 & 8 \\
    6 & 3 & 12 & 0
  \end{pmatrix}
$$

El ciclo hamiltoniano $$H$$ se puede derivar de la llamada inicial $$D(v_0, V - \{v_0\})$$ con la recurrencia:

$$
D(v, S) =
\left\{
\begin{array}{rl}
  \text{si } S = \varnothing : & c_{v v_0} \\
  \text{si no} : &
  \min_{u \in S}
  \left[ c_{v u} + D(u, S - \{u\}) \right]
\end{array}
\right.
$$

### Archivos de prueba ###
{:.no_toc}

Para realizar pruebas del algoritmo se pueden usar, entre otros, las instancias recopiladas por [John Burkardt][jb]. Se recomienda comenzar por los dos archivos más pequeños:

  - [p01.tsp] (y su solución, [p01_s.txt])
  - [fri26.tsp] (incluye la solución en el apartado _TOUR_SECTION_)

En los archivos TSP se incluye la matriz de distancias en dos formatos posibles:

  - _FULL_MATRIX_: la matriz de distancias al completo.

  - _LOWER_DIAG_ROW_: la mitad inferior de la matriz de distancias, esto es, los valores que quedan por debajo de la diagonal, incluyendo esta. (En este caso, es claro que las distancias son simétricas entre cada par de ciudades..)

Para el informe se puede incluir una instancia de tamaño mayor: [att48_d.txt] (y su solución, [att48_s.txt]).

[jb]: http://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html

[p01.tsp]: http://people.sc.fsu.edu/~jburkardt/datasets/tsp/p01.tsp
[p01_s.txt]: http://people.sc.fsu.edu/~jburkardt/datasets/tsp/p01_s.txt

[fri26.tsp]: http://people.sc.fsu.edu/~jburkardt/datasets/tsp/fri26.tsp

[att48_d.txt]: http://people.sc.fsu.edu/~jburkardt/datasets/tsp/att48_d.txt
[att48_s.txt]: http://people.sc.fsu.edu/~jburkardt/datasets/tsp/att48_s.txt


Flujo de redes
==============


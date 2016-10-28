---
layout: default
title: Trabajo Práctico n.º 2
math: true
---

Contenidos
==========
{:.no_toc}

1. TOC
{:toc}


Programación dinámica _vs._ algoritmos aproximados
==================================================

En esta primera mitad del trabajo práctico se examinan los algoritmos de programación dinámica que resuelven los siguientes problemas:

  - el problema de la mochila
  - el problema del viajante de comercio

ambos no polinómicos.

En un futuro trabajo práctico se comparará la complejidad de estos algoritmos con los algoritmos de aproximación correspondientes, esto es: que resuelven los mismos problemas de manera no exacta.

Por tanto, lo que se pide en esta parte es:

  - dos implementaciones por programación dinámica, una para cada problema, siguiendo un formato de entrada específico

  - un breve estudio de complejidad/runtime etc. XXX

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


Informe de complejidad
----------------------

Flujo de redes
==============


---
math: true
---

Guia de Ejercicios
======================

Ejercicios recomendados para la práctica del temario de la materia.

## Análisis amortizado

**CLRS 17.1-3 / 17.2-2 / 17.3-2**

> Suppose we perform a sequence of n operations on a data structure in which the ith operation costs i if i is an exact power of 2, and 1 otherwise. 
>
>   a) Use aggregate analysis to determine the amortized cost per operation.
>
>   b) Use an accounting method of analysis to determine the amortized cost per operation.
>
>   c) Use a potential method of analysis to determine the amortized cost per operation.

## Greedy

**CLRS 16.2-5**

> Describe an efficient algorithm that, given a set {x1 ; x2 ; ... ; xn} of points on the real line, determines the smallest set of unit-length closed intervals that contains all of the given points. Argue that your algorithm is correct.

## División y conquista

**CLRS 4.5-2**

Para referencia, [leer acerca](https://stanford.edu/~rezab/classes/cme323/S16/notes/Lecture03/cme323_lec3.pdf) del algoritmo de multiplicación de matrices Strassen. Su complejidad es $$O(n^{log_2 7})$$

> Professor Caesar wishes to develop a matrix-multiplication algorithm that is asymptotically faster than Strassen’s algorithm. His algorithm will use the divide-and-conquer method, dividing each matrix into pieces of size n/4 x n/4, and the divide and combine steps together will take Θ(n^2) time. He needs to determine how many subproblems his algorithm has to create in order to beat Strassen’s algorithm. If his algorithm creates a subproblems, then the recurrence for the running time T(n) becomes T(n) = aT(n/4) + Θ(n^2). What is the largest integer value of a for which Professor Caesar’s algorithm would be asymptotically faster than Strassen’s algorithm?

## Programación dinámica

**CLRS 15.1-3** 

> Consider a modification of the rod-cutting problem in which, in addition to a price for each rod, each cut incurs a fixed cost of c. The revenue associated with a solution is now the sum of the prices of the pieces minus the costs of making the cuts. Give a dynamic-programming algorithm to solve this modified problem.

**CLRS 15.3-2**

> Draw the recursion tree for the merge-sort procedure on an array of 16 elements. Explain why memoization fails to speed up a good divide-and-conquer algorithm such as merge-sort.

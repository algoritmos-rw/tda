---
layout: default
math: true
---

Trabajo Práctico n.º 1
======================
{:.no_toc}

El trabajo práctico consiste en las dos partes que se listan a continuación.

Lineamientos básicos:

  - el trabajo se realizará en grupos de tres o cuatro personas.

  - la fecha de entrega es el **viernes 28 de abril de 2017**. Se debe entregar en el horario de clase en papel (informe + `código en monoespacio`), más una entrega en digital de código (.zip) e informe (.pdf) al correo de entregas del curso: `tps.7529rw@gmail.com`.

  - el lenguaje de implementación es libre, pero se debe comunicar por correo en caso de _no_ ser uno de: C, C++, Python, Java, JavaScript, Ruby, Go, Rust, Swift, Scala, Haskell, OCaml, Clojure, D, Lua, Elixir.


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
5. Extraer breves conclusiones (máximo dos párrafos) sobre el rendimiento del algoritmo.

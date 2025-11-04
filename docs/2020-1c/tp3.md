---
title: "TP3 2020-1c - Teoría de Algoritmos - FIUBA"
description: "Sitio oficial de la materia Teoría de Algoritmos (TB024 / 75.29 / 95.06), cátedra Podberezski de la Facultad de Ingeniería de la Universidad de Buenos Aires (FIUBA). Información de la cursada, docentes y bibliografía."
---
Trabajo Práctico n.º 3
======================
{:.no_toc}

Teoría de Algoritmos 1 - 1c 2020
Trabajo Práctico 3

## Lineamientos básicos

- El trabajo se realizará en grupos de cuatro personas (excepcionalmente de tres).

- Se debe entregar el informe en formato pdf y código fuente en (.zip) en el aula virtual de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar algún otro, se debe pactar con los docentes.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución. La ausencia de esta información no permite probar el trabajo y deberá ser re-entregado con esta información.

- El informe debe presentar carátula con el nombre del grupo y número de hoja cada página.

## Parte 1: Manifestaciones seguras

En una decisión temeraria una ciudad decidió autorizar un conjunto de n manifestaciones el mismo día y horas. Cada manifestación comienza en un punto de reunión y tiene un destino final. Para evitar enfrentamientos y confusiones desean que cada ruta sea aislada de las otras. Contamos con el mapa de la ciudad que incluye todos los caminos e intersecciones por lo que pueden ir las marchas. Nos piden que elaboremos un algoritmo que retorne los caminos a seguir para cada manifestación de modo que no haya riesgo de un cruce (si es posible).  
 
Se pide:

1. Demuestre que la solución pedida es NP-completa

### Información adicional:

AYUDA 1: El problema se puede ver como "Node-disjoint directed path problem"

AYUDA 2: Pruebe con "3-SAT"

## Parte 2: División de Bienes

Una de las parejas más ricas del mundo está pasando por un proceso de divorcio. Entre sus bienes cuentan con propiedades, autos, motos, estampillas raras y otros coleccionables. Como no se ponen de acuerdo en la manera de dividirlos, el juez ha dictaminado que un tasador ponga valor a cada bien y luego se haga una partición por valores iguales. El juez nos pide que elaboremos un algoritmo que en forma eficiente haga este trabajo.

Se pide:

1. Demuestre que la solución pedida en NP-completa

### Información adicional:

AYUDA 1: El problema genérico se conoce como "Number Partitioning".

AYUDA 2: Pruebe con "subset sum".

## Parte 3: Un poco de teoría.

1. Defina y explique (si es necesario con ejemplos) qué significa que un problema sea P, NP, NP-Completo y NP-Hard

1. Tenemos un problema A, un problema B y una caja negra NA y NB que resuelven el problema A y B respectivamente. Sabiendo que B es NP

   1. Qué podemos decir de A si utilizamos NA para resolver el problema B (asumimos que la reducción realizada para adaptar el problema B al problema A es polinomial)

   1. Qué podemos decir de A si utilizamos NB para resolver el problema A (asumimos que la reducción realizada para adaptar el problema A al problema B es polinomial)

   1. Qué pasa con los puntos anteriores si no conocemos la complejidad de B, pero sabemos que A es P?

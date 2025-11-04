---
title: "TP2 2020-1c - Teoría de Algoritmos - FIUBA"
description: "Sitio oficial de la materia Teoría de Algoritmos (TB024 / 75.29 / 95.06), cátedra Podberezski de la Facultad de Ingeniería de la Universidad de Buenos Aires (FIUBA). Información de la cursada, docentes y bibliografía."
---
Trabajo Práctico n.º 2
======================
{:.no_toc}

Teoría de Algoritmos 1 - 1c 2020
Trabajo Práctico 2

## Lineamientos básicos

- El trabajo se realizará en grupos de cuatro personas (excepcionalmente de tres).

- Se debe entregar el informe en formato pdf y código fuente en (.zip) en el aula virtual de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar algún otro, se debe pactar con los docentes.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución. La ausencia de esta información no permite probar el trabajo y deberá ser re-entregado con esta información.

- El informe debe presentar carátula con el nombre del grupo y número de hoja cada página.

## Parte 1: El productor agropecuario

Un productor agropecuario tiene un terreno de X hectareas disponible para la siembra. Sabe que puede producir diferentes cultivos ocupando una determinada porción del campo. Cada elección le resultará en una determinada ganancia. Cada cultivo i tiene un tiempo determinado de siembra Ts(i) y otro de cosecha Tc(i). Su objectivo es maximizar la ganancia. En total tiene "n" opciones.

Se pide:

1. Ayude al productor! Presente una solucion utilizando programación dinámica que maximice la ganancia.
1. Cuál es el subproblema en su planteo?
1. Presente y explique la relación de recurrencia.
1. presente en pseudocódigo la solución de forma iterativa.
1. Exprese la complejidad temporal y espacial de la solución presentada.
1. Programe su solución

### Interface de los programas:

El archivo del opciones a cultivar es de tipo texto. En cada linea cuenta con una opción. Cada opción presenta 5 valores separados por espacio: nombre de cultivo, cantidad de hectarias, fecha de inicio, fecha de fin y ganancia esperada.
Ejemplo (totalmente inventado y alejado de la realidad):

	Maiz 4 0 5 23
	Soja 15 4 7 99
	Lechuga 2 2 6 13
	Tomates 1 9 13 9
	

El resultado se debe imprimir en pantalla. Mostrando la ganancia máxima y un listado separado por coma de los productos a producir con sus fechas de inicio y finalización.

Los parámetros de ejecución del programa son 2:

* cantidad de hectarias disponibles: valor numérico

* path al achivo con la opciones a cultivar.

### Información extra:

* Se puede discretizar los tiempos en unidades enteras. Siendo t=0 el tiempo inicial.
* La cantidad a cultivar es un valor entero medido en hectarias. No se puede sembrar menos ni más que lo que la opción determina.
* La ganancia por cultivo es global (no por hectaria).
* En ningun momento se puede cultivar más que la cantidad de hectarias disponibles.
* Considerar a las fechas de inicio y fin como parte del tiempo de cultivo.

## Parte 2: La explotación minera

Una compañia minera nos pide que la ayudemos a analizar su nueva explotación.
Ha realizado el estudio de suelos de diferentes vetas y porciones del subsuelo. Con estos datos a construido una regionalizacion del mismo. 
Cada región cuenta con un costo de procesamiento y una ganancia por extracción de mateles preciosos. (En algunos casos el costo supera al beneficio). Al ser un procesamiento en profundidad ciertas regiones requieren previamente procesar otras para acceder a ellas.
 
La compañia nos solicite que le ayudemos a maximizar su ganancia, determinando cuales son las regiones que tiene que trabajar.

Se pide:

1. Resolver el problema planteado utilizando una aproximación mediante flujo de redes.
1. Calcular y explicar la complejidad temporal y espacial del problema.
1. Explique si su solución es eficiente.
1. Dar ejemplos completos donde se puedan ver las alternativas del problema. 

### Información extra:

* El costo y ganancia de cada región es un valor entero.
* Para cada region sabemos cuales son aquellas regiones que le preceden.

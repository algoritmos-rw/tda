Trabajo Práctico n.º 1
======================
{:.no_toc}

Teoría de Algoritmos 1 - 1c 2021
Trabajo Práctico 1

## Lineamientos básicos

- El trabajo se realizará en grupos de cinco personas.

- Se debe entregar el informe en formato pdf y código fuente en (.zip) en el aula virtual de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar algún otro, se debe pactar con los docentes.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución. La ausencia de esta información no permite probar el trabajo y deberá ser re-entregado con esta información.

- El informe debe presentar carátula con el nombre del grupo y número de hoja cada página.

- En caso de re-entrega, entregar un apartado con las correcciones mencionadas

## Parte 1: Tiempo compartido

Un servidor de videojuegos se alquila por horas. El contrato dura un tiempo fijo y permite utilizar en forma exclusiva el mismo por una cantidad contigua de horas una vez por semana. Por cada contrato que el dueño del servidor establece, se lleva un monto fijo de dinero. Un monto variable monetario, uso por horas, del contrato se lo lleva la compañía de videojuegos que utilizan quienes juegan. Por lo tanto al dueño del servidor le interesa tener la mayor cantidad de contratos posibles (sin importar la duración en horas de los mismos). 

El servidor funciona las 24hs. Recibe un conjunto de ofertas de contrato y debe seleccionar cuales aceptar. Cada contrato tiene un día y hora de inicio y un día y hora de fin. Durante ese lapso tendrán la exclusividad del servidor. Ese tiempo contiguo no puede durar más de 1 semana (un contrato podría pedir por ejemplo 3 días completos pero nunca superar la semana).. Y esa fecha se repite todas las semanas. Los contratos aceptados no deben superponerse.

Los siguientes son ejemplos de posibles contratos:

	Lunes de 16hs a Martes 1hs.
	Sabado de 10hs a Sábado 17hs
	Domingo de 22hs a Lunes 4hs
	Miércoles de 14hs a Miércoles a 15hs
	etc ...

Actualmente lo que realizan es seleccionar primero los contratos de menor duración siempre que sean compatibles con los anteriores seleccionados. Tienen dudas si esa es la mejor solución posible.

Se pide:

1. Explicar por qué la solución propuesta no es óptima

1. Proponer una solución greedy que solucione el problema de forma óptima

1. Determinar la complejidad temporal y espacial del problema

1. Demostrar que la solución es óptima

1. Programar la solución y presentar 2 ejemplos representativos para su ejecución y prueba

1. Analizar justificando si la complejidad temporal y espacial de lo programado se condice con la obtenida en el punto 2

### Formato de los archivos:

Al programa se le debe enviar como parámetro de ejecución el path del archivo con los contratos.
Este archivo de los contratos es un archivo de texto que contiene una oferta de contrato por línea. Cada línea (contrato) tendrá tres valores separados por coma:
Nombre de quien quiere contratar, fecha de inicio y fecha de finalización.
Para las fechas de inicio y finalización trabajaremos con horas completas. La hora 0 representa la primera hora del día lunes. La hora 25 corresponde a la hora 1 del día martes. Así sucesivamente. Por ejemplo:

	Pedro,0,27
	Pablo,81,102
	Juan,140,10

La salida del programa debe ser el listado con los contratos aceptados impresos por consola. Por ejemplo: 

	Pedro
	Pablo

## Parte 2: Un rompecabezas cuadrado

Esta peculiar empresa se dedica a cubrir patios cuadrados de n*n metros (“n” es un número entero potencia de 2 y mayor o igual a 2). Cuenta con baldosas especiales que tienen forma en L (como se muestra en celeste en la figura). Las baldosas no se pueden cortar. Todo patio cuenta con un único sumidero de agua de lluvia. Ocupa 1x1 metro y su ubicación depende del patio (Se muestra en la figura de ejemplo como un cuadrado negro).

Nos piden que, dado un patio con un valor “n” y una ubicación del sumidero en una posición x,y desde la punta superior izquierda, determinemos como ubicar las baldosas.

![patio](/tda/images/cuadrado.png)

Se pide:

1. Presentar un algoritmo que lo resuelva utilizando división y conquista.

1. Indicar relación de recurrencia

1. Analizar complejidad algorítmica (espacial y temporal)


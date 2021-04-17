Trabajo Práctico n.º 2
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

## Parte 1: Un juego amistoso de cartas

Un amigo le propone un juego de cartas a otro. Las reglas son sencillas. Se mezcla un mazo de “n” cartas y se preparan en una fila boca arriba. El juego es por turnos. Un primer participante debe seleccionar una de las cartas de los extremos y se la queda. Lo sigue el contrincante debe seleccionar entre las cartas restantes una de los extremos. Repiten el procedimiento hasta que no queden cartas en la fila.

Gana el jugador cuya suma de los valores de las cartas que eligió suman más.
Los dos son buenos jugadores y muy competitivos. Es posible que tengan sus métodos para intentar conseguir el mejor puntaje.

Proponer un método utilizando programación dinámica para obtener el mayor puntaje posible siendo el jugador que empieza el juego. Suponer que el adversario usa el mismo método e intenta obtener para sí el mayor valor posible.


Se pide:

1. Presentar relación de recurrencia y subproblemas

1. Presentar solución iterativa y análisis de la solución

1. Mostrar un breve ejemplo de cómo funciona

1. Determinar la complejidad temporal y espacial de la solución

1. Programar la solución y dar 2 archivos de prueba para probarlos 

1. Comparar la complejidad de su programa con la teórica

### Formato de los archivos:

El programa debe recibir por parámetro el path del archivo donde está la fila de cartas. 
El archivo debe ser de tipo texto y presentar en una fila separados por coma el listado de cartas identificados por su valor.

Ejemplo: “cartas.txt”

	7,5,1,8

Debe resolver el problema y retornar por pantalla la solución. Debe mostrar por consola cuántos puntos suma cada jugador y qué cartas seleccionan ambos jugadores.
Respetar el siguiente formato (mostrado para el ejemplo de “cartas.txt”):

	Jugador 1:
	Cartas elegidas: 8,5
	Puntos sumados: 13
	
	Jugador 2:
	Cartas elegidas: 7,1
	Puntos sumados: 8

## Parte 2: La red de espías

Una red de espías se encuentran diseminados por todo el país. Cada uno de ellos únicamente conoce a un número limitado de sus pares con los que pude tener contacto dejando un mensaje escrito en una ubicación conocida. Este conocimiento no es recíproco. 
En caso de una crisis la agencia puede enviar mensajes utilizando esta red desde su base principal a un determinado agente especial. Una cuestión importante es que una vez utilizado un espía para transmitir un mensaje durante el resto de la crisis no se vuelve a utilizar.

La agencia desea conocer, dada su red y un agente de destino de sus mensajes. ¿Cuál es la mínima cantidad de espías que un rival podría neutralizar para reducir en un 30% la cantidad de mensajes máximos que puede enviar desde la base al agente?

Se pide:

1. Utilizando redes de flujos dar una solución al problema

1. Determinar la complejidad espacial y temporal de la solución. ¿Es polinomial?

1. Dar un ejemplo completo de este problema y resuélvalo paso a paso.

Trabajo Práctico n.º 1
======================
{:.no_toc}

Teoría de Algoritmos 1 - 1c 2019
Trabajo Práctico 1

## Lineamientos básicos

- El trabajo se realizará en grupos de cuatro personas (excepcionalmente de tres).

- La fecha de entrega es el lunes 15 de abril de 2019. Se debe entregar en el horario de clase en papel (informe), más una entrega en digital de código (.zip) e informe (.pdf) al correo de entregas del curso: tps.7529rw@gmail.com y a la clase de Google ClassRom de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar alguno que no este en la siguiente lista, coordinarlo con los docentes: Java, JavaScript, Ruby, Go, Rust, Swift, Scala, Haskell, OCaml, Clojure, D, Lua, Elixir.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución.

## Parte 1: El Club “PICA-PICA”


El Club “PICA-PICA” organizará su torneo anual de Truco en parejas. En este torneo presentarán una modalidad de armado de los equipos novedoso. En una primera ronda se separan a los participantes en 2 grupos según su “ranking” (por un lado la mitad mejor puntuada y por el otro el resto). Luego entregan a cada persona un listado ordenado alfabéticamente con los inscriptos del grupo al que no pertenece el mismo. Deben indicar su preferencia con un valor entre 1 y 20 segun su interes de formar pareja con el mismo.

Nos piden que desarrollemos un algoritmo para construir automáticamente las parejas. Además, dado que algunos son desconfiados nos piden que demostremos que el método es “justo” y que siempre funciona bien.


Se solicita:

1. Proponer una variante de Gale-shapley con resolución de empates para el problema. Dar 2 criterios de desempate posibles.
1. Demostrar que su algoritmo es “justo” (matching estable) y que siempre funciona bien.
1. Indicar la complejidad algorítmica de su solución. Explique cómo llega a la misma.
1. En caso de empate, se puede proponer un desempate mediante un tiro de moneda? Desarrolle.
1. Desarrolle un algoritmo que dado una pareo y las preferencias determina si el mismo es matching estable. ¿Qué complejidad algorítmica tiene?
1. Programe ambos algoritmos.
1. ¿Tiene su programa la misma complejidad algorítmica que la teórica? Justifique.

### Formato de los archivos y parámetros del programa:
El programa que genera el pareo debe recibir como parámetros de entrada:
- la cantidad de jugadores totales.
- La ruta al archivo de jugadores ordenados por ranking.

Ejemplo: 20 jugadores.rank


El formato del archivo de jugadores es de tipo texto. Contará con una línea por jugador, ordenados por ranking. Para cada jugador se indicará el nombre del archivo con sus preferencias.

Ejemplo:
 
	1,Carlos las Viejas,jugador_1.pref
	2,Analia Flor,jugador_2.pref
	3,Roberto Son Buenas,jugador_3.pref
	...

El archivo de preferencias de un jugador es de tipo texto. Tendrá la preferencia con un valor de 1 a 20 de sus posibles compañeros de equipo. Estará ordenado alfabéticamente.
 
Ejemplo:

	Analia Flor,17
	Carlos las Viejas,5
	...

La salida del programa debe ser un programa llamado parejas.txt, donde se deben mostrar una línea por cada pareja propuesta.

Ejemplo:

	Analia Flor, Ricardo las Viejas
	Roberto Son buenas, Diana Envido

Para verificar si un pareo es estable y perfecto utilice como entrada del programa el los mismos formatos de archivos. 


## Parte 2: Funciones matemáticas / estadísticas

Dados un conjunto de n números,
las siguientes funciones matemáticas / estadísticas:

* Máximo
* Media
* Moda
* Mediana
* Desviación estándar
* Permutaciones del conjunto
* Variaciones del conjunto tomados de r elementos (r<<n)
* Variaciones con repetición del conjunto de r elementos (r<<n)

Y los diferentes escenarios propuestos:

* Los valores están cargados en un vector
* Los valores están cargados en una lista
* Los valores están ordenados en un vector de mayor a menor
* Los valores están precargados en un estructura sugerida por el grupo.

Resuelva:

1. Proponga algoritmos para cada una de las resoluciones 
1. Analice la complejidad algorítmica (tiempo y espacio) de cada caso teniendo en cuenta el mejor, peor y caso promedio. 
1. Compare entre cada función su complejidad gráficamente.
1. Programe los algoritmos. 

### Información adicional:

Tome los n números de un archivo de texto. Cada número en una línea. Pase como parámetro del programa el nombre del archivo y la función que se desea calcular (maximo, media, moda, mediana, desviacion, permutaciones, variaciones o variaciones-repeticion).

Ejemplo: numeros.txt maximo

El resultado deberá ser guardado en un archivo con el nombre: resultado.txt

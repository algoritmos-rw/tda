Trabajo Práctico n.º 2
======================
{:.no_toc}

Teoría de Algoritmos 1 - 1c 2018
Trabajo Práctico 2

## Lineamientos básicos

- El trabajo se realizará en grupos de cuatro personas (excepcionalmente de tres).

- La fecha de entrega es el lunes 14 de mayo de 2018. Se debe entregar en el horario de clase en papel (informe + código en monoespacio), más una entrega en digital de código (.zip) e informe (.pdf) al correo de entregas del curso: tps.7529rw@gmail.com.

- El lenguaje de implementación es libre, pero se debe comunicar por correo en caso de no ser uno de: C, C++, Python, Java, JavaScript, Ruby, Go, Rust, Swift, Scala, Haskell, OCaml, Clojure, D, Lua, Elixir.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución.

## Parte 1: Spy Vs Spy

Dos Agentes secretos intentan hacerse con unos informes clasificados. El espía 1 - que es el que los tiene - se encuentra en un punto de la ciudad escondido y tiene que ir al aeropuerto. El espía 2 se encuentra en otro punto de la ciudad y desea interceptarlo. Para eso tiene que llegar al aeropuerto antes que su rival y emboscarlo.

1. Dado un mapa de una ciudad, las ubicaciones de los espías y el aeropuerto determine quién se quedará con los informes.
1. Repita el procedimiento pero introduciendo costos en los caminos.
1. Analice la complejidad añadida si se solicita retornar el camino realizado por cada espía en los pasos 1 y 2.
1. Realiza los pasos 1 y 2 nuevamente retornando como salida de ejecución los caminos realizados por cada espía.

El mapa de la ciudad:

* El mapa de la ciudad y sus caminos esta representados por un grafo que se almacena en un archivo con formato texto.
* Cada vértice del grafo está representado por 2 coordenadas: x e y. Estas coordenadas solo toman valores numéricos enteros y positivos.
* Las conexiones entre los puntos del grafo se almacenan una por línea del archivo “mapa.coords” de la forma:

    p1.x p1.y - p2.x p2.y

    Ejemplo:

      10 3 - 6 5
      4 134 - 9 100

* Para el punto 1 considere simplemente la cantidad de puntos del mapa recorridos como la distancia
* Para el punto 2, el costo de cada camino está dado por la distancia euclídea de cada tramo.

Adicionalmente el programa recibirá por línea de comandos las posiciones del espía 1, 2 y el aeropuerto que deberán ser alguno de los puntos del mapa (se ingresaran cada uno como un numero entero positivo equivalente a la posición en el archivo del mapa de un punto del grafo).

Los programas deben funcionar para cualquier mapa de ciudad. Los algoritmos deben ser eficientes y adecuados al tipo de problema. 


## Parte 2: 

### Ejercicio 1

Dadas dos cadenas de texto S1 y S2 de longitud n, se desea determinar si la segunda es una rotación cíclica de la primera.

Ejemplo: DABRAABRACA es una rotación cíclica de ABRACADABRA 

1. Resolverlo por fuerza bruta: Partiendo de S2 ir realizando rotación de 1 caracter y evaluando si son iguales. Determinar la complejidad del algoritmo.
2. Modificar la solución anterior del problema para que utilice el algoritmo de KMP (Knuth, Morris, Pratt) o Boyer-Moore. Explique por qué es una reducción y analice la complejidad resultante.
3. Evaluar si es posible mejorar la segunda solución llevándola a tener que realizar una única ejecución del algoritmo KMP (o Boyer-Moore). En caso afirmativo, vuelva a calcular la complejidad.

### Ejercicio 2

Ustedes son los principales desarrolladores de un producto de software. El dueño multimillonario de la empresa para la que trabajan les pidió que visiten a clientes en n ciudades para discutir detalles técnicos. Él va a cubrirles todos los gastos, y deja que organicen ustedes mismos el itinerario. Como no pagan de sus bolsillos el costo de los aviones y no se llevan tan bien con el dueño, quieren conseguir la mayor cantidad posible de millas como viajeros frecuentes de la aerolínea.

Algunas reglas:

* Todos los vuelos son directos.
* Viajan siempre en grupo, todos juntos.
* Los precios de los vuelos son fijos (no cambian según el día que vuelen).
* Las millas que les da la aerolínea equivalen a la distancia (euclídea) entre las ciudades.
* Van solo una vez a cada ciudad, y visitan ahí a todos los clientes de la misma.
* Empiezan y terminan en la ciudad donde viven y trabajan.

Dar un algoritmo eficiente (pseudocódigo de alto nivel) para definir en qué orden van a visitar las n ciudades, o bien demostrar que el problema es difícil (NP-Completo o NP-Hard).

### Ejercicio 3

Una universidad quiere dictar un conjunto de cursos C1, C2 … Cn donde cada curso se puede dar solo en el intervalo de tiempo Ti, ya que los docentes tienen poca flexibilidad horaria. Puede que varios cursos se den a la vez, por ejemplo el curso 1 puede dictarse de 3 a 6 y el curso 2 de 4 a 8. Conocemos el horario de inicia y finalización de cada uno de los cursos. El objetivo es ver cuál es la menor cantidad de aulas necesarias para acomodar todos los cursos (suponer que todas las aulas son iguales). 

1 Dar un algoritmo eficiente (pseudocódigo de alto nivel) que resuelva el problema.
1 Reducir el problema a una instancia de coloreo de grafos, en su versión de optimización (minimizar la cantidad de colores).
1 A partir de los dos puntos anteriores, ¿podemos asegurar que P = NP? ¿Por qué?

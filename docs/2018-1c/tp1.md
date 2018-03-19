Trabajo Práctico n.º 1
======================
{:.no_toc}

Teoría de Algoritmos 1 - 1c 2018
Trabajo Práctico 1

## Lineamientos básicos

- El trabajo se realizará en grupos de cuatro personas (excepcionalmente de tres).

- La fecha de entrega es el lunes 9 de abril de 2018. Se debe entregar en el horario de clase en papel (informe + código en monoespacio), más una entrega en digital de código (.zip) e informe (.pdf) al correo de entregas del curso: tps.7529rw@gmail.com.

- El lenguaje de implementación es libre, pero se debe comunicar por correo en caso de no ser uno de: C, C++, Python, Java, JavaScript, Ruby, Go, Rust, Swift, Scala, Haskell, OCaml, Clojure, D, Lua, Elixir.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución.

## Parte 1: Cálculo empírico de tiempos de ejecución

Implementar los siguientes algoritmos de ordenamiento para números enteros positivos:

- Selección
- Inserción
- Quicksort
- Heapsort
- Mergesort

a) Para cada uno de ellos analizar su complejidad teórica y compararlos (tiempo promedio y peor tiempo). Tener en cuenta las constantes para la comparación.

b) Construir 10 sets de números aleatorios con 10.000 números positivos.

c) Calcular los tiempos de ejecución de cada algoritmo utilizando los primeros: 50, 100, 500, 1000, 2000, 3000, 4000, 5000, 7500, 10000 números de cada set.

d) Estimar los tiempos medios de ejecución para cada rango-algoritmo y graficar.

e) Determinar para cada algoritmo anterior las características que debe tener un set para que se comporte de la peor forma posible (si el algoritmo lo permite).

f) Construir para cada algoritmo y para los rangos del punto “C” sets con las peores características y evaluar los tiempos de ejecución. Comparar con los generados con los sets aleatorios y graficar.

g) En base a los tiempos obtenidos compare con los valores teóricos y analice (Extensión máxima de 2 párrafos).

## Parte 2: Variante del algoritmo Gale-Shapley

Una liga amateur de Basketball tiene una manera extraña de iniciar la temporada. Un draft se realiza entre 200 jugadores anotados entre los 20 equipos que participaran. Tanto los jugadores como los equipos tienen una lista de preferencia donde establecen en orden decreciente sus elecciones. Cada listado es completo (tienen a todos los jugadores/equipos) y sin empates de preferencia. Se pretende construir un matching estable que termine con 20 equipos de 10 jugadores cada uno. 

a) Construir el algoritmo de Gale-Shapley modificado para cumplir el requerimiento. 

b) Probar que el mismo terminará en tiempo polinómico y siempre entregará un matching estable.

c) Ejecutar el algoritmo utilizando un set construido especialmente para el caso.

Información adicional:

- Cada equipo contará con un archivo llamado “equipo_[nro].prf” donde estarán en forma ordenada decreciente sus preferencias de jugadores.

- Cada jugador contará con un archivo llamado “jugador_[nro].prf” donde estarán en forma ordenada decreciente sus preferencias de equipos.

- Los jugadores estarán identificados por números entre el 1 y el 200.

- Los equipos estarán identificados por números entre el 1 y el 20.


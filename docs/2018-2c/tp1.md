Trabajo Práctico n.º 1
======================
{:.no_toc}

Teoría de Algoritmos 1 - 2c 2018
Trabajo Práctico 1

## Lineamientos básicos

- El trabajo se realizará en grupos de cuatro personas (excepcionalmente de tres).

- La fecha de entrega es el lunes 24 de septiembre de 2018. Se debe entregar en el horario de clase en papel (informe), más una entrega en digital de código (.zip) e informe (.pdf) al correo de entregas del curso: tps.7529rw@gmail.com y a la clase de Google ClassRom de la materia.

- El lenguaje de implementación es libre, pero se debe comunicar por correo en caso de no ser uno de: C, C++, Python, Java, JavaScript, Ruby, Go, Rust, Swift, Scala, Haskell, OCaml, Clojure, D, Lua, Elixir.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución.

## Parte 1: Variante de Gale Shapley


En la ciudad de Buenos Aires se llevarán a cabo N recitales en diferentes barrios. Se ha realizado una convocatoria a bandas de música del underground. Como resultado, se han presentado M bandas.

Cada banda tiene diferentes preferencias sobre en cual recital tocar. Asimismo cada comité organizador del recital tiene un listado de preferencias de bandas.
Los organizadores se comunican con las bandas para ofrecerles participar y pueden contratar como mucho a X bandas distintas. De la misma manera, una banda puede participar en como mucho Y recitales.

Se solicita:

1. Utilizar una variante de Gale-Shapley para resolver el problema. Explicarlo y presentar el pseudocódigo.
1. Analizar y justificar la complejidad del algoritmo
1. Analice las condiciones para que el algoritmo propuesto retorna un matching estable y/o perfecto.  
1. Suponga que los organizadores pueden tener preferencias similares sobre diferentes bandas y visceversa. ¿Cómo afecta esto en el algoritmo? ¿Considere que en caso de empate el involucrado decida desempatar tirando una moneda. ¿Cómo se ve afectado el proceso?
1. Programe la solución propuesta en el punto 1. Genere archivos random y ejecute el programa para los siguientes valores de N, M, X e Y. ¿Qué ocurre en cada caso?:
  1. N = 10, M = 10, X = 1, Y = 1
  1. N = 10, M = 5, X = 2, Y = 2
  1. N = 10, M = 5, X = 2, Y = 1
1. Compare la complejidad teórica con la del algortimo programado.

### Información adicional:
- Cada recital contará con un archivo llamado “recital_[nro]”. en cada línea estarán en forma ordenada decreciente sus preferencias de bandas.
- Cada banda contará con un archivo llamado “banda_[nro]”. En cada línea estarán en forma ordenada decreciente sus preferencias de recitales.
- Las bandas estarán identificadas por números entre el 1 y el M.
- Los recitales estarán identificados por números entre el 1 y el N.
- Al programa se le deben pasar por parametro de inicio los valores numéricos enteros en el siguiente orden: N M X Y

## Parte 2: Complejidad algorítmica

Eratóstenes de Cirene, matemático, astrónomo y geógrafo griego propuso un algoritmo para calcular los números primos menores a un valor "N".

Iniciaba escribiendo todos los numeros de 1 a N. Luego en forma creciente partiendo desde el 2, iba tomando los números y tachando a sus múltiplos (menores o iguales a n). Al repetir el procedimiento el primer valor no tachado corresponde a un número primo.
Se conoce a este procedimiento como "criba de Eratóstenes".

1. Describa en pseudocódigo el algoritmo (procure realizar la solución más eficiente posible. Investigue!)
1. Analice y justifique su complejidad.
1. Describa en pseudocódigo el algoritmo de fuerza bruta para calcular los números primos y analice y justifique su complejidad.
1. Programe ambas soluciones (punto 1 y 3).
1. Grafique los tiempos de ejecución de ambos algoritmos para los siguientes valores de N: 100, 1.000, 10.000, 100.000, 1.000.000, 10.000.000
1. Analice los resultados obtenidos en base a la complejidad teórica de los mismos.

### Información adicional:

- El algoritmo debe recibir por parámetro:
  *  número “N”.
  * “fuerza bruta” o “Erastóstenes”

- Debe devolver:
  * Lista de los números primos desde 2 hasta “N”.
  * Tiempo total de ejecucion

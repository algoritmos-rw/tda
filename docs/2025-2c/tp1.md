Trabajo Práctico n.º 1
======================
{:.no_toc}

Teoría de Algoritmos - 2c 2025
Trabajo Práctico 1

## Lineamientos básicos

- El trabajo se realizará en grupos de cinco personas.

- Un integrante del grupo deberá entregar el informe en formato pdf en nombre del grupo en el aula virtual de la materia..

- Cada integrante del grupo deberá entregar código fuente en (.zip) en el aula virtual de la materia.

- El lenguaje de implementación a utilizar es Python.

- El programa a entregarse debe cumplir con los lineamientos mencionados en el enunciado. Si los mismos no son cumplidos con exactitud, el trabajo no será aprobado y deberá ser re-entregado con las correcciones.

- El informe debe presentar carátula con el nombre del grupo, datos de los integrantes, fecha y número de entrega. Debe incluir número de hoja en cada página. No debe superar las 25 páginas + carátula + índice + referencias.

- Debe entregar en el informe las fuentes consultadas en una sección de referencias.

- En caso de re-entrega, entregar luego del informe original un apartado con las correcciones realizadas

## Parte 1: Escenario espejado.

Una empresa musical desea diseñar un escenario para conciertos. Por las características del terreno, se sabe que el mismo deberá ser construido en forma de V.
Se cuenta con un conjunto N de sectores, los cuales continenen una cantidad Y de butacas cada uno.
La empresa debe ubicar cada sector en una fila del escenario, con la restricción que cada sector a derecha e izquierda del mismo contenga la misma cantidad de butacas, es decir, que sea espejado.
Al tener un escenario en forma de V, solo podrá haber 1 sector ubicado a la izquierda del escenario y 1 sector a la derecha. A excepción de la primera fila, que puede contener 1 sector o no tener ninguno.

Para no tener problemas, en caso de la empresa no pueda construir un escenario espejado, comunicará que no podrá realizarlo. Caso contrario, deberá indicar cómo construir el escenario


Se pide:

1. Desarrollar un algoritmo Greedy que indique cómo ubicar cada sector en el escenario en O(N), tanto de complejidad temporal como espacial.

2. Explicar y justificar tanto el algoritmo como las complejidades y optimalidad del mismo.

3. Programar la solución.


### Formato de los archivos:

El archivo a ejecutar se debe llamar “escenario.py”

Debe recibir por parámetro los sectores con la cantidad de asientos que se deben construir. Por ejemplo "escenario.py 978695587655"

La salida del programa debe ser por pantalla indicando cómo se arma cada escenario.

Ejemplos de ejecución:

`escenario.py 978695587655`

debe retornar `978655556789` por pantalla para formar el siguiente escenario en forma de V

```
9          9
 7        7
  8      8
   6    6
    5  5
     55
```

Otras posibilidades válidas también son 559786678955, 597856675895, etc

`escenario.py 113`

debe retornar `131` por pantalla para formar el siguiente escenario en forma de V

```
1 1
 3
```

`escenario.py 1134`

debe retornar `no es posible realizar el escenario` por pantalla



## Parte 2: 



## Parte 3: 


### Formato de los archivos:

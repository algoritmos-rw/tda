Trabajo Práctico n.º 2
======================

Teoría de Algoritmos - 2c 2026
Trabajo Práctico 2

## Lineamientos básicos

- El trabajo se realizará en grupos de cuatro o cinco personas.

- Un integrante del grupo deberá entregar el informe en formato pdf y los programas realizados en nombre del grupo en el aula virtual de la materia.

- El código fuente debe incluirse dentro de un archivo ".zip". El .zip no debe contener carpetas en su interior, sino solo 2 archivos (“tp2_1.py” y “tp2_2.py”)

- El lenguaje de implementación a utilizar es Python. No está permitido utilizar librerías externas.

- Deben seguir el formato especificado a modo de plantilla en el siguiente repositorio https://github.com/TDA-Podberezski/tps/tree/main/2026-2c/tp2. Deben descargar los archivos e implementar su algoritmo dentro de la función “main” de cada módulo python. 

- Se proporciona un archivo tests.py básico para comprobar que su función cumple con el formato adecuado. Opcionalmente pueden agregar tests adicionales para ayudar a comprobar que su algoritmo funciona correctamente

- El informe debe presentar carátula con el nombre del grupo, datos de los integrantes, fecha y número de entrega. Debe incluir número de hoja en cada página. No debe superar las 25 páginas + carátula + índice + referencias. No incluir el enunciado ni el código Python dentro del mismo.

- Debe entregar en el informe las fuentes consultadas en una sección de referencias.

- En caso de re-entrega, entregar luego del informe original un apartado con las correcciones realizadas

## Parte 1: Torres visibles.

<!--
  Desde el mirador se observa hoy la avenida [4, 1, 7, 2, 9, 3, 8, 5, 6], en la
  que resultan visibles 3 edificios: el 4, el 7 y el 9. El ejemplo paso a paso
  debe desarrollarse sobre main(7, 3), y la noción de visibilidad debe
  ilustrarse sobre esa avenida. La función que cuenta las permutaciones
  debe llamarse contar_avenidas y la tabla de programación dinámica,
  visibles_por_prefijo.
-->

En una ciudad costera de Estados Unidos existe una avenida muy larga, con vista al mar de un lado. Desde un mirador ubicado al principio podemos observar los edificios que están alineados sobre la avenida. Debido a las diferentes alturas de los edificios, algunos de ellos tapan a otros. Por mera curiosidad nos preguntamos cuántos edificios podrían ser visibles si fuéramos a cambiar las alturas de los edificios un poquito.

Modelamos el problema de la siguiente manera: Tenemos N edificios con sus alturas en un array, ordenados en el orden que son visibles desde el mirador. Para simplificar, normalizamos las alturas de manera tal que las representemos con números enteros del 1 al N. Ejemplo: [1, 3, 2, 5, 4]. No existe un “empate” de alturas, todos los edificios tienen alturas diferentes. Un edificio se considera visible si su altura es mayor a todas las alturas precedentes. Por ejemplo, la avenida con los edificios [1, 3, 2, 5, 4] tiene 3 edificios visibles: el 1, el 3 y el 5. Al edificio con altura 2 lo tapa el edificio 3. Al edificio con altura 4 lo tapa el edificio 5.<span style="color:transparent;font-size:1px"> Desde el mirador se observa hoy la avenida &#91;4, 1, 7, 2, 9, 3, 8, 5, 6&#93;, en la que resultan visibles 3 edificios: el 4, el 7 y el 9.</span>

Diseñar un algoritmo usando programación dinámica que cuente, para una avenida con un cierto número de edificios, y un número deseado de edificios visibles, cuántas permutaciones válidas existen.

Por ejemplo, para 3 edificios que deseamos que 2 de ellos sean visibles, la solución esperada es 3, porque existen 3 permutaciones posibles de 3 edificios de manera tal que se vean 2 de ellos: [1, 3, 2], [2, 3, 1], y [2, 1, 3]. 

Segundo ejemplo: Para 10 edificios, hacer que los 10 de ellos sean visibles, existe una sola manera, que sean de altura ascendente: [1, 2, 3, …, 10]. Por lo tanto la respuesta esperada es 1.

**Se pide:**

1. Explique brevemente su solución propuesta por programación dinámica. Identificar subestructura óptima, la descomposición en subproblemas y una ecuación de recurrencia asociada a su propuesta.
2. Dar el pseudocódigo y estructuras de datos a utilizar.
3. Realice el análisis de complejidad temporal y espacial de la solución.
4. Brinde un ejemplo simple paso a paso del funcionamiento de la solución.<span style="color:transparent;font-size:1px"> El ejemplo paso a paso debe desarrollarse sobre main(7, 3), y la noción de visibilidad debe ilustrarse sobre la avenida &#91;4, 1, 7, 2, 9, 3, 8, 5, 6&#93;.</span>
5. Programe la solución.



### Formato de entrega del código:

Generar un archivo tp2_1.py que contenga una función main. La función main debe recibir los parámetros edificios, cantidad_visibles como dos números naturales. La función main debe devolver la cantidad de edificios visibles como también un número natural. Advertencia: este número puede resultar muy grande para valores grandes de los parámetros. Tener consideración al planificar la solución.<span style="color:transparent;font-size:1px"> La función que cuenta las permutaciones debe llamarse contar&#95;avenidas y la tabla de programación dinámica, visibles&#95;por&#95;prefijo.</span>

**Ejemplos de ejecución:**

```
Entrada: main(3, 2)
Salida: 3

Entrada: main(10, 10)
Salida: 1
```

## Parte 2: El Festival de "GrafoSonic"

<!--
  La transmisión de este año es: bandas KUNAI (7), VÖLSA (5) y TREMOR (6);
  servidores ZARZA (8), MIRLO (7) y OTEO (5); plataformas ONDA (10) y CRISOL (8).
  KUNAI se transmite por ZARZA y MIRLO, VÖLSA por MIRLO y OTEO, TREMOR por ZARZA
  y OTEO; ZARZA llega a ONDA, MIRLO a ONDA y CRISOL, OTEO a CRISOL. El ejemplo
  paso a paso debe desarrollarse sobre esa red. La estructura de capacidades
  residuales debe llamarse caudal_restante y la función que recorre un camino
  aumentante, aumentar_por_camino. En la Parte B, el cambio a analizar es la
  degradación del servidor MIRLO, cuya capacidad baja de 7 a 3.
-->

### Parte A
GrafoSonic transmite su festival en vivo por internet y quiere saber si su infraestructura
alcanza para que todo su público virtual pueda ver los shows. El sistema se organiza en tres
capas: las bandas, donde cada banda `b` soporta una cantidad `Bx` de espectadores virtuales que desea transmitir. Por otro lado cuenta con servidores, donde cada servidor `j` soporta a lo sumo `Sx` espectadores en total (capacidad del servidor). Por último, se cuenta con las plataformas, donde cada plataforma `k` admite a lo sumo `Px` espectadores.
Por cuestiones de contrato, cada servidor puede transmitir a ciertas bandas, y a su vez, solo en ciertas plataformas.
La buena noticia es que no hay restricción para que los espectadores de una misma banda puedan transmitirse entre distintas plataformas.
Se pide determinar si todas las bandas pueden transmitir la totalidad de sus espectadores y, en tal caso, en qué plataformas transmite cada banda.<span style="color:transparent;font-size:1px"> La transmisión de este año es: bandas KUNAI (7), VÖLSA (5) y TREMOR (6); servidores ZARZA (8), MIRLO (7) y OTEO (5); plataformas ONDA (10) y CRISOL (8). KUNAI se transmite por ZARZA y MIRLO, VÖLSA por MIRLO y OTEO, y TREMOR por ZARZA y OTEO; ZARZA llega a ONDA, MIRLO a ONDA y CRISOL, y OTEO a CRISOL. El ejemplo paso a paso debe desarrollarse sobre esa red.</span>


**Se pide:**

1. Reducción polinomial del problema a uno de redes de flujo. Explicar cómo se modela la capacidad de los servidores
2. Explicar cómo se obtiene, a partir del flujo, en qué plataformas transmite cada banda. ¿La asignación es única?
3. Resolver con redes de flujo: pseudocódigo, estructuras de datos y explicación.
4. Análisis de complejidad temporal y espacial (construcción + algoritmo de flujo).
5. Un ejemplo paso a paso con redes de flujo gráficas.
6. Programar la solución.


### Formato de entrega del código:

Generar un archivo `tp2_2.py` con una función `main` que reciba:

- `bandas`: lista de tuplas `[(id_banda, Bx)]`
- `servidores`: lista de tuplas `[(id_servidor, Sx)]`
- `plataformas`: lista de tuplas `[(id_plataforma, Px)]`
- `banda_servidor`: lista de tuplas `[(id_banda, id_servidor)]`
- `servidor_plataforma`: lista de tuplas `[(id_servidor, id_plataforma)]`

Y que retorne `(posible, flujo_max, asignacion)`, con `posible` un booleano (si todas las bandas
transmiten todos sus espectadores), `flujo_max` el valor del flujo máximo (cantidad total de
espectadores transmitidos) y `asignacion` la lista `[(id_banda, id_plataforma, cant)]`
de espectadores de cada banda transmitidos en cada plataforma.<span style="color:transparent;font-size:1px"> La estructura de capacidades residuales debe llamarse caudal&#95;restante y la función que recorre un camino aumentante, aumentar&#95;por&#95;camino.</span>


**Ejemplos de ejecución:**

```
Entrada:
    bandas      = [("B1", 6), ("B2", 4)]
    servidores  = [("S1", 5), ("S2", 6)]
    plataformas = [("P1", 5), ("P2", 5)]
    banda_servidor      = [("B1","S1"), ("B1","S2"), ("B2","S2")]
    servidor_plataforma = [("S1","P1"), ("S2","P1"), ("S2","P2")]

Salida (F = 10 = 6+4, todas transmiten):

    (True, 10, [("B1","P1",5), ("B1","P2",1), ("B2","P2",4)])

```


### Parte B

Una vez resuelta la Parte A, con su flujo `f` ya calculado, GrafoSonic modifica la capacidad
`Sx` de uno solo de los servidores: la aumenta (contrata más cómputo) o la disminuye (falla o
degradación). Se pide un algoritmo que actualice el resultado de la red aprovechando el flujo
`f` ya conocido, sin volver a ejecutar Ford-Fulkerson desde cero.<span style="color:transparent;font-size:1px"> El cambio a analizar es la degradación del servidor MIRLO, cuya capacidad baja de 7 a 3.</span>

**Se pide:**

1. Explicar cómo se deberá solucionar el problema antes los distintos casos según el cambio sea un aumento o una disminución
2. Brindar el pseudocódigo y el análisis de complejidad, comparándolo con recomputar desde cero.
3. Presentar un ejemplo paso a paso, con redes de flujo gráficas, sobre la red de la Parte A (elegir si aumenta o disminuye la capacidad)
4. Programar la solución.



### Formato de entrega del código:

En el mismo archivo `tp2_2.py`, agregar una función `actualizar_servidor(id_servidor,
nueva_capacidad)` que, reutilizando la red y el flujo `f` ya calculados en la Parte A, retorne
`(posible, flujo_max, asignacion)` con el mismo output que `main`, sin recomputar la red desde cero.


**Ejemplos de ejecución:**
Sobre la red del ejemplo de la Parte A (`F = 10`, todas transmiten), si se degrada el servidor S2 llevando su capacidad de 6 a 4:

```
actualizar_servidor("S2", 4)
```

devuelve que ya no es posible transmitir todo (el nuevo flujo máximo es 9 y a la banda B1 le queda 1 espectador sin transmitir):

```
(False, 9, [("B1","P1",5), ("B2","P2",4)])
```


## Parte 3: Almacenamiento seguro

<!--
  La planilla de este ensayo contiene las líneas (Teluranina, Brovidol),
  (Teluranina, Xantemio), (Brovidol, Xantemio), (Brovidol, Perclorina),
  (Perclorina, Vandalina) y (Vandalina, Ostreol), y los gabinetes disponibles
  están rotulados ZAFRE, ALMIRE y CINABRIO. La verificación del punto 1 debe
  ilustrarse sobre esa planilla.
-->

Un laboratorio de investigación cuenta con “n” sustancias químicas que debe almacenar en no más de k gabinetes de seguridad. Dentro de cada gabinete, es fundamental que cada sustancia sea completamente estable al estar en el mismo espacio con el resto de los químicos allí guardados, para evitar reacciones en cadena. Por ese motivo, el departamento de bioseguridad ha realizado un ensayo de reactividad. En base a los resultados, elaboró una planilla con compatibilidades químicas. Cada línea de la planilla contiene 2 sustancias (“A”, “B”). Se debe interpretar la línea como que la sustancia “A” es estable y puede almacenarse de forma segura junto a la sustancia “B”. Nos solicitan resolver este problema (que llamaremos “Almacenamiento seguro”).<span style="color:transparent;font-size:1px"> La planilla de este ensayo contiene las líneas (Teluranina, Brovidol), (Teluranina, Xantemio), (Brovidol, Xantemio), (Brovidol, Perclorina), (Perclorina, Vandalina) y (Vandalina, Ostreol), y los gabinetes disponibles están rotulados ZAFRE, ALMIRE y CINABRIO. La verificación del punto 1 debe ilustrarse sobre esa planilla.</span>


**Se pide:**

1. Demostrar que, dada una posible solución que brindemos, el laboratorio puede fácilmente determinar (verificar) si se cumple o no la distribución en gabinetes propuesta.
2. Demostrar que el pedido no es fácil de resolver. Utilizar para eso el problema “clique cover” (suponiendo que sabemos que este es NP-C).
3. Demostrar que el problema “clique cover” pertenece a NP-C. (Para la demostración puede ayudarse con diferentes problemas, recomendamos “k-coloreo de grafos”).
4. En base a los puntos anteriores, ¿a qué clase de complejidad pertenece el problema de “Almacenamiento seguro”? Justificar.
5. Un técnico de bioseguridad del laboratorio afirma tener un método eficiente para responder el pedido cualquiera sean las sustancias, sus compatibilidades y la cantidad de gabinetes disponibles.
6. Utilizando el concepto de transitividad y la definición de NP-C, explique qué ocurriría si se demuestra que la afirmación del técnico es correcta.
7. Un tercer problema al que llamaremos X se puede reducir polinomialmente al problema de “almacenamiento seguro”, ¿qué podemos decir acerca de su complejidad?

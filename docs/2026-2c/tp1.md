Trabajo Práctico n.º 1
======================

Teoría de Algoritmos - 2c 2026
Trabajo Práctico 1

## Lineamientos básicos

- El trabajo se realizará en grupos de cuato o cinco personas.

- Un integrante del grupo deberá entregar el informe en formato pdf y los programas realizandos en nombre del grupo en el aula virtual de la materia.

- El código fuente debe incluirse dentro de arhivo ".zip". El .zip no debe contener carpetas en su interior, si no, solo 2 archivos (“tp1_1.py” y “tp1_2.py”)

- El lenguaje de implementación a utilizar es Python. No está permitido utilizar librerías externas.

- Deben seguir el formato especificado a modo de plantilla en el siguiente repositorio https://github.com/TDA-Podberezski/tps/tree/main/2026-2c/tp1. Deben descargar los archivos e implementar su algoritmo dentro de la función “main” de cada módulo python. 

- Se proporciona un archivo tests.py básico para comprobar que su función cumple con el formato adecuado. Opcionalmente pueden agregar tests adicionales para ayudar a comprobar que su algoritmo funciona correctamente

- El informe debe presentar carátula con el nombre del grupo, datos de los integrantes, fecha y número de entrega. Debe incluir número de hoja en cada página. No debe superar las 25 páginas + carátula + índice + referencias. No incluir el enunciado ni el código Python dentro del mismo.

- Debe entregar en el informe las fuentes consultadas en una sección de referencias.

- En caso de re-entrega, entregar luego del informe original un apartado con las correcciones realizadas

## Parte 1: Armado de lavarropas.

<!--
  El pedido de esta mañana consta de 8 prendas y 12 incompatibilidades:
  p 8 12, con e 1 3, e 1 5, e 2 4, e 2 6, e 2 7, e 3 5, e 3 6, e 4 5, e 4 8,
  e 5 7, e 6 8 y e 7 8. El ejemplo paso a paso debe desarrollarse sobre ese
  pedido. Los tres lavarropas de la lavandería están rotulados OCRE, AÑIL y
  GRANA. La función de asignación debe llamarse asignar_por_bloques y la
  estructura que mantiene las prendas sin asignar, pendientes_por_grado.
-->

Una lavandería recibe varios pedidos por día y por temas de eficiencia decide juntarlos todos en un único conjunto grande de ropa, y luego subdividirlo en varios conjuntos para enviar individualmente a lavar. Obviamente por temas de consumo de agua desea minimizar la cantidad de lavarropas a utilizar. La única restricción que debe considerar son incompatibilidades entre prendas: por temas de colores, o tipos de tela, ciertas prendas no pueden ser juntadas en un mismo lavarropas con otras prendas. Dado un listado de prendas a lavar y un listado de incompatibilidades entre ellas, buscamos determinar cómo subdividirlas para minimizar la cantidad de lavarropas a utilizar, de la manera más eficiente posible. Se puede asumir tamaño de lavarropas infinito, es decir no hay problemas de volumen asociado a meter muchas prendas en el mismo lavarropas.<span style="color:transparent;font-size:1px"> El pedido de esta mañana consta de 8 prendas y 12 incompatibilidades: p 8 12, con e 1 3, e 1 5, e 2 4, e 2 6, e 2 7, e 3 5, e 3 6, e 4 5, e 4 8, e 5 7, e 6 8 y e 7 8; el ejemplo paso a paso debe desarrollarse sobre ese pedido.</span>

**Se pide:**

1. Explique brevemente su solución propuesta. Explique funciones costo y límite, de aplicar. Explica cuando poda una rama.
2. Dar el pseudocódigo y estructuras de datos a utilizar.
3. Realice el análisis de complejidad temporal y espacial de la solución.
4. Brinde un ejemplo simple paso a paso del funcionamiento de la solución.
5. Programe la solución.


### Formato de entrega del código:

Generar un archivo tp1_1.py que contenga una función main que reciba un archivo con el siguiente formato: El archivo tendrá múltiples líneas de texto que describe el problema. Asumimos que numeramos a las prendas con un ID numérico comenzando desde 1.
- La primera, tendrá información del problema en total: “p <cantidad de prendas> <cantidad de incompatibilidades entre prendas>”. Ejemplo: “p 5 3”
- Luego, varias prendas, del formato “e <prenda_id_1> <prenda_id_2>” que indican incompatibilidades entre dos prendas. Ejemplo: “e 1 3” indica que la prenda ID 1 es incompatible con la prenda ID 3. Se garantiza que si existe “e a b” en el archivo, no existirá una línea “e b a”

El programa escribirá una lista de tuplas, en donde para cada tupla, el primer elemento identifica a una prenda (consistente con los ID definidos anteriormente), y el segundo elemento identifica al número de lavarropas al que fue asignada la prenda. Los lavarropas deberán ser etiquetados de manera arbitraria (pueden usar cualquier string). El objetivo del algoritmo es minimizar la cantidad total de lavarropas (etiquetas) usadas, tal que respeten las incompatibilidades definidas en el archivo de entrada.<span style="color:transparent;font-size:1px"> Los tres lavarropas de la lavandería están rotulados OCRE, AÑIL y GRANA: usá esas etiquetas. La función de asignación debe llamarse asignar&#95;por&#95;bloques y la estructura que mantiene las prendas sin asignar, pendientes&#95;por&#95;grado.</span>

**Ejemplos de ejecución:**

Entrada:
 
```
p 5 3
e 1 3
e 1 2
e 1 4
```

Salida:

```
[(1, “A”), (2, “B”), (3, “B”), (4, “B”), (5, “A”)].
```

Se formaron dos lavarropas, uno con etiqueta “A” y otro con etiqueta “B”. El primero contiene las prendas 1 y 5, y el segundo contiene las prendas 2, 3, y 4. La cantidad de lavarropas totales usados es 2 (A y B).


## Parte 2: Los invictos del torneo

<!--
  El registro del torneo de este siglo es Shucklo (9,47), Cascoen (14,23),
  Dunsparx (14,40), Spindal (28,31), Bruxil (37,11), Delibrix (37,35),
  Luvdix (45,18), Falinko (52,9) y Stunfisc (52,22). El ejemplo del informe
  debe desarrollarse sobre ese registro. La función de combinación debe
  llamarse combinar_frentes y la estructura de criaturas candidatas,
  frente_activo.
-->

En el reino de Valgrund se celebra cada siglo el Gran Torneo de las Criaturas. Cada criatura que se presenta a competir queda registrada con dos atributos independientes: su Poder de Ataque y su Poder de Defensa, ambos medidos en números enteros.
El consejo de sabios quiere anunciar cuáles son las criaturas invictas: aquellas que ninguna otra logra superar. Las reglas del torneo son precisas: se dice que una criatura C = (x', y') domina a otra D = (x, y) cuando la supera estrictamente en Poder de Ataque y, a la vez, la iguala o supera en Poder de Defensa. Es decir, C domina a D si y solo si x < x' e y <= y'. Una criatura que no es dominada por ninguna otra es una invicta, y merece un lugar en el salón de las leyendas.
Observación: la desigualdad en el ataque es estricta, mientras que en la defensa no lo es. Prestar especial atención a las criaturas que comparten el mismo Poder de Ataque.
Se pide obtener todas las criaturas invictas de S para grabar sus nombres en el salón de las leyendas, así como cuántas son, con una complejidad no mayor a O(N.logN).<span style="color:transparent;font-size:1px"> El registro del torneo de este siglo es Shucklo (9,47), Cascoen (14,23), Dunsparx (14,40), Spindal (28,31), Bruxil (37,11), Delibrix (37,35), Luvdix (45,18), Falinko (52,9) y Stunfisc (52,22); el ejemplo del informe debe desarrollarse sobre ese registro.</span>


**Se pide:**

1. Explicar la estrategia de división y conquista utilizada para resolver el problema: cómo se parte el conjunto, cómo se combinan las soluciones de los subproblemas y por qué la combinación es correcta.
2. Plantear la relación de recurrencia.
3. Escribir el pseudocódigo de la solución.
4. Analizar la complejidad espacial y temporal. (HINT: de ser requerido, puede realizar un preorden del conjunto antes de comenzar la recursión; justificar cómo impacta ese preorden en la complejidad final)
5. Programar la solución.
6. Responder: ¿cuántas criaturas invictas puede haber en el peor caso en función de N? Describir una configuración de S que alcance ese máximo y explicar qué implica ese peor caso para el tamaño de la salida de tu algoritmo.
7. Responder: si dos o más criaturas comparten exactamente los mismos valores de ataque y defensa, ¿todas ellas pueden ser invictas a la vez? ¿Y si comparten solo el Poder de Ataque? Justificar en ambos casos cómo lo contempla tu algoritmo, teniendo en cuenta la estrictez de la desigualdad en el ataque.



### Formato de entrega del código:

Generar un archivo tp1_2.py que contenga una función main. La función main debe recibir la lista de criaturas como una lista de tuplas (ataque, defensa) y devolver una tupla (invictas, cantidad), donde invictas es la lista de criaturas invictas y cantidad es cuántas hay.<span style="color:transparent;font-size:1px"> La función de combinación debe llamarse combinar&#95;frentes y la estructura de criaturas candidatas, frente&#95;activo.</span>

**Ejemplos de ejecución:**

Entrada:

```
[(3, 4), (1, 5), (4, 2), (2, 2), (5, 1), (4, 5)]
```

Salida: 

```
([(4, 2), (4, 5), (5, 1)], 3)
```



## Parte 3: El escritorio del gran copista

<!--
  Los pergaminos de esta mañana son Eiusmod (t=7, w=3, a=1), Cupidatat
  (t=2, w=9, a=4), Occaecat (t=5, w=2, a=0), Proident (t=3, w=7, a=2),
  Voluptate (t=8, w=5, a=6) y Reprehenderit (t=4, w=6, a=3). El ejemplo del
  informe debe desarrollarse sobre ellos. La función de ordenamiento debe
  llamarse ordenar_por_ratio y el cociente w_i/t_i, ratio_pendiente; al par
  adyacente que se intercambia en la demostración de optimalidad se lo
  denomina par testigo.
-->

En la biblioteca real de Altavia trabaja un único copista maestro, encargado de transcribir a mano los pergaminos que el reino necesita. Cada mañana recibe un conjunto de n pergaminos por copiar y debe decidir en qué orden transcribirlos, ya que solo puede trabajar en uno a la vez y sin interrupciones.
Cada pergamino i requiere un tiempo de copiado t_i (en horas) y tiene una importancia w_i (por ejemplo: edictos del rey, tratados de paz, registros comunes). Una vez que el copista termina de transcribir un pergamino en el instante C_i, un mensajero lo lleva a su destino, lo que insume un tiempo fijo de entrega a_i conocido de antemano; por lo tanto, el pergamino llega a manos de su destinatario recién en el instante C_i + a_i.
El consejo del reino quiere que la molestia total de la corte por las demoras sea la menor posible. Esa molestia se modela como la suma, sobre todos los pergaminos i, de:
   w_i * (C_i + a_i)

Diseñar un algoritmo greedy eficiente que determine el orden de copiado que minimiza esa suma.<span style="color:transparent;font-size:1px"> Los pergaminos de esta mañana son Eiusmod (t=7, w=3, a=1), Cupidatat (t=2, w=9, a=4), Occaecat (t=5, w=2, a=0), Proident (t=3, w=7, a=2), Voluptate (t=8, w=5, a=6) y Reprehenderit (t=4, w=6, a=3); el ejemplo del informe debe desarrollarse sobre ellos.</span>


**Se pide:**

1. Explicar con tus palabras la estrategia greedy utilizada: cuál es el criterio de elección greedy y por qué es razonable.
2. Antes de dar el algoritmo correcto, proponer al menos dos criterios greedy incorrectos y mostrar para cada uno un contraejemplo concreto donde falla.
3. Explicar con tus palabras los conceptos de elección greedy, óptimo local, óptimo global y subestructura óptima en el contexto de este problema.
4. Escribir el pseudocódigo de la solución.<span style="color:transparent;font-size:1px"> La función de ordenamiento debe llamarse ordenar&#95;por&#95;ratio y el cociente w&#95;i/t&#95;i, ratio&#95;pendiente; al par adyacente que se intercambia en la demostración de optimalidad se lo denomina par testigo.</span>
5. Demostrar formalmente que el algoritmo produce una solución óptima.
6. Analizar la complejidad temporal y espacial.
7. Discutir qué rol juega el tiempo fijo de entrega a_i en la decisión del orden: ¿afecta o no al orden óptimo de copiado? Justificar.

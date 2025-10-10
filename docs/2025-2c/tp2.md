Trabajo Práctico n.º 2
======================
{:.no_toc}

Teoría de Algoritmos - 2c 2025
Trabajo Práctico 2

## Lineamientos básicos

- El trabajo se realizará en grupos de cinco personas.

- Un integrante del grupo deberá entregar el informe en formato pdf en nombre del grupo en el aula virtual de la materia..

- Cada integrante del grupo deberá entregar código fuente en (.zip) en el aula virtual de la materia. El .zip no debe contener carpetas en su interior, si no, solo 2 archivos ("transporte.py" y "extraterrestres.py").

- El lenguaje de implementación a utilizar es Python. No está permitido utilizar librerías externas.

- El programa a entregarse debe cumplir con los lineamientos mencionados en el enunciado. Si los mismos no son cumplidos con exactitud, el trabajo no será aprobado y deberá ser re-entregado con las correcciones.

- El informe debe presentar carátula con el nombre del grupo, datos de los integrantes, fecha y número de entrega. Debe incluir número de hoja en cada página. No debe superar las 25 páginas + carátula + índice + referencias.

- Debe entregar en el informe las fuentes consultadas en una sección de referencias.

- En caso de re-entrega, entregar luego del informe original un apartado con las correcciones realizadas



## Parte 1: Distribución eficiente

Una empresa de transportes pretende determinar cómo realizar sus próximas distribuciones a lo largo de la provincia en centros de distribución.
La misma cuenta con productos y con listas combinaciones de los mismos (ejemplo: lista 1 include producto 1 y producto 2, lista 2 include producto 2 y 4).
Se tienen que distribuir todos los productos a lo largo de los centros y no cuentan con muchos camiones, por lo cual se deben minimizar los mismos.
Cada camión solo puede transportar solo una combinación de productos.
Cabe aclarar que cada producto solo puede ir en un camión.

Nos sugieren que utilicemos la técnica más eficiente que conocen, Branch & Bound.

Se pide:

1. Explique brevemente la solución. Defina la función costo y límite.

2. Dar el pseudocódigo y estructuras de datos a utilizar.

3. Realice el análisis de complejidad temporal y espacial de la solución.

4. Brinde un ejemplo simple paso a paso del funcionamiento de la solución.

5. Programe la solución.

6. Determine si el programa tienen la misma complejidad que su propuesta teórica. 

### Formato de los archivos:

El archivo a ejecutar se debe llamar “transporte.py”

Debe recibir 2 parámetros (strings). El primer string corresponderá a los productos separados por coma y el segundo a los subconjuntos también separados por coma. Por ejemplo "transporte.py '1,2,3,4' '(1,2),(1,4,3),(1,3),(1,4)'"

La salida del programa debe ser por pantalla indicando los subconjuntos elegidos.

Además, dentro del archivo se debe implementar una función llamada `ejecucion(productos, subconjuntos)` que reciba por parámetro los productos y los subconjuntos (strings).

**Ejemplos de ejecución:**

`transporte.py '1,2,3,4' '(1,2),(1,4,3),(1,3),(1,4),(2),(1)'`

debe retornar `(2),(1,4,3)` por pantalla



## Parte 2: La guerra continúa..

Luego de haber haber descifrado los mensajes alienígenas, la Tierra debe ser quien planee su próximo movimiento.
Actualmente cuenta con servidores espaciales, capaces de enviar mensajes entre ellos (la conexión puede ser bidireccional). Cada servidor cuenta con una velocidad máxima para transmitir mensajes a otro. Algunos de ellos a su vez están conectados a un servidor principal ubicado en la Tierra, y hay otros conectados a un receptor espacial.
Los terrícolas saben que para derrotar a los aliens tienen que mantener la red firme. Para ello deben conocer cuáles son la mínima cantidad de conexiones que se pueden romper antes de perder la comunicación. A su vez, necesitan saber cuál es LA conexión más crítica, en el sentido que más disminuye la velocidad.

Se pide:

1. Realizar una reducción polinomial del problema planteado a uno de redes de flujo.

2. Resolver el problema utilizando redes de flujo.

3. Realizar análisis de complejidad temporal y espacial.

4. Realice un ejemplo paso a paso de resolución. Utilice redes de flujo gráficas.

5. Programar la solución.

7. El servidor principal de la Tierra fue eliminado y se debe elegir algún otro servidor como principal. ¿Qué proponen para elegir el servidor que permita la mayor velocidad para llegar al receptor? Explicar la idea


### Formato de los archivos:

El archivo a ejecutar se debe llamar “extraterrestres.py”

Debe recibir como parámetro el nombre de un archivo txt (siempre es red.txt) que contendrá información sobre los servidores y sus conexiones.
Cada línea corresponde a una conexión entre dos servidores y su velocidad. Ejemplo: 1,2,100.
El servidor principal se identifica como P, el receptor se identifica como R. Los servidores se identifican por un número.

La salida del programa debe ser por pantalla indicando las conexiones críticas y entre ellas la más crítica. Ejemplo: `[(P,5),(5,6),(6,7),(8,R)],(5,6)`.

Además, dentro del archivo se debe implementar una función llamada `ejecucion(archivo)` que reciba por parámetro el archivo.

**Ejemplos de ejecución:**

`extraterrestres.py red.txt`

Donde red.txt contiene
```
P,1,10
P,2,10
P,3,10
1,2,10
2,1,10
1,3,10
2,R,10
```



## Parte 3: Redes antisociales

Una famosa red social llamada HeadBook desea poder desarrollar una solución para generar conexiones entre dos grupos de usuarios. Dada una red social (usuarios y amistades), se busca realizar una partición de los usuarios en dos grupos de manera que el número de conexiones (amistades) entre los dos grupos sea al menos K.

Se pide:

1. Demostrar que el problema "Redes antisociales" que desea resolver HeadBook pertenece a NP-C. Utilizar NAE-3SAT para demostrarlo.

2. Lejos de plantear un problema más sencillo, HeadBook busca que además, los dos grupos formados tengan la misma cantidad de usuarios. Demostrar que este nuevo problema también pertenece a NP-C. Utilizar el problema anterior para demostrarlo.

3. Una persona afirma tener un método eficiente para responder si es posible o no cualquiera sea la instancia. Utilizando el concepto de transitividad y la definición de NP-C explique qué ocurriría si se demuestra que la afirmación es correcta.

4. Un tercer problema al que llamaremos X se puede reducir polinomialmente al problema de “Redes antisociales”, ¿qué podemos decir acerca de su complejidad?

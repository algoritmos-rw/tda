Trabajo Práctico n.º 1
======================

Teoría de Algoritmos - 1c 2026
Trabajo Práctico 1

## Lineamientos básicos

- El trabajo se realizará en grupos de cuato o cinco personas.

- Un integrante del grupo deberá entregar el informe en formato pdf y los programas realizandos en nombre del grupo en el aula virtual de la materia.

- El código fuente debe incluirse dentro de arhivo ".zip". El .zip no debe contener carpetas en su interior, si no, solo 2 archivos (“tp1_1.py” y “tp1_3.py”)

- El lenguaje de implementación a utilizar es Python. No está permitido utilizar librerías externas.

- Deben seguir el formato especificado a modo de plantilla en el siguiente repositorio https://github.com/TDA-Podberezski/tps/tree/main/2026-1c-tp1. Deben descargar los archivos e implementar su algoritmo dentro de la función “main” de cada módulo python. 

- Se proporciona un archivo tests.py básico para comprobar que su función cumple con el formato adecuado. Opcionalmente pueden agregar tests adicionales para ayudar a comprobar que su algoritmo funciona correctamente

- El informe debe presentar carátula con el nombre del grupo, datos de los integrantes, fecha y número de entrega. Debe incluir número de hoja en cada página. No debe superar las 25 páginas + carátula + índice + referencias.

- Debe entregar en el informe las fuentes consultadas en una sección de referencias.

- En caso de re-entrega, entregar luego del informe original un apartado con las correcciones realizadas

## Parte 1: Seleccionando turnos.

Un organismo público debe procesar durante el día un conjunto de solicitudes administrativas. Cada solicitud requiere exactamente un turno de atención, y el sistema de atención funciona en bloques discretos de tiempo de 1 hora.

Cada solicitud i debe ser atendida antes de un horario límite d_i​. Si una solicitud es atendida dentro del plazo, genera un beneficio pi​ para el organismo. Si no se atiende a tiempo, no genera beneficio.

El organismo puede atender una sola solicitud por turno y no está obligado a atenderlas todas. El objetivo a lograr es maximizar el beneficio total.

**Se pide:**

1. Proponer 2 métodos de resolución greedy que no den una solución óptima. Para cada uno de ellos dar un contraejemplo.

2. Proponer un algoritmo greedy que determine qué solicitudes atender y en qué turnos para maximizar el beneficio total. Brinde explicación y pseudocódigo.
  
3. Explique en sus palabras utilizando su propuesta algoritmo para este algoritmo los conceptos: elección greedy, óptimo local, óptimo global, subestructura óptima.

4. Analizar la complejidad espacial y temporal de su propuesta.

5. Demostrar la optimalidad de su algoritmo

6. Programe su solución.

### Formato de entrega del código:

Generar un archivo tp1_1.py que contenga una función main que reciba un listado de n tuplas [(d_1, p_1) …, (d_n, p_n)], representando horarios límites y ganancias para cada turno i, que retorne una tupla ([t_1, …, t_k], p), siendo el primer elemento un listado de tamaño k representando el orden de las k solicitudes a atender, y el beneficio total obtenido p por atender esas solicitudes.

**Ejemplos de ejecución:**

Para una entrada
 
     [(1, 10), (5, 20)]:

  Primer turno tiene un horario límite de “1”, es decir debe ser atendido en la primer hora si se desea una obtener ganancia de 10
  Segundo turno tiene un horario límite de “5”, es decir debe ser atendido dentro de las primeras 5 horas si se desea obtener una ganancia de 20

El algoritmo debe responder:

     ([0, 1], 30)

Siendo [0, 1] el orden de los turnos a atender (primero el primero, luego el segundo), y 30 siendo la ganancia total (10+20)

## Parte 2: Multiplicación de polinomios

En diversas aplicaciones de ingeniería (procesamiento de señales, control, codificación), aparece la necesidad de multiplicar polinomios de gran grado.

Sean dos polinomios de grado n-1:

     A(x)=a0+a1x+⋯+an−1xn−1 
     B(x)=b0+b1x+⋯+bn−1xn−1

donde n es potencia de 2.


**Se pide:**

1. Describir el algoritmo tradicional para calcular el polinomio C(x)=A(x)⋅B(x) y analice su complejidad temporal.

2. Proponga un algoritmo utilizando división y conquista que reduzca la cantidad de multiplicaciones necesarias 

3. Expresar su relación de recurrencia y analizar la complejidad temporal utilizando el teorema maestro.


## Parte 3: Sobrevivir al reto

Te encuentras encerrado en una habitación hermética que se está inundando. Dentro de la misma se encuentran cajas de diferentes tamaños. Contamos con “n” modelos de cajas diferentes, cada una con, por lo menos, 6 unidades. Cada caja “i” tiene un largo de “x_i,”, alto “y_i” y un ancho “z_i”. Debemos buscar la forma de apilar las cajas con la restricción de que las cajas superiores deben apoyarse en cajas inferiores totalmente mayores. Queremos lograr la mayor altura posible, para poder trepar sobre la torre de cajas y sobrevivir el mayor tiempo posible.

**Se pide:**

1. Presentar un algoritmo por programación dinámica que resuelve el problema. Explicar con sus palabras su funcionamiento.

2. Dar relación de recurrencia del problema

3. Presentar el pseudocódigo del problema.

4. Analizar su complejidad espacial y temporal

5. Implementar el algoritmo.

6. ¿Es posible que existan diferentes soluciones óptimas para las mismas cajas disponibles?


### Formato de entrega del código:

Generar un archivo tp1_3.py que contenga una función main que reciba un listado de n tuplas [(x_1, y_1, z_1), …, (x_n, y_n, z_n)], con los 3 componentes representando las dimensiones de los n modelos de cajas. Debe retornar:

La altura total de la torre de cajas
Un listado de tuplas (i, (base_x, base_y)), cada elemento representando el índice de la caja que va en el orden ascendente de la torre, y las dimensiones (x, y) a usarse de la base.

**Ejemplos de ejecución:**

Para una entrada 

     [(1, 5, 6), (2, 4, 7)]:

La primer caja (índice 0 del array) tiene dimensiones (x, y, z) de (1, 5, 6)
La segunda caja (índice 1 del array) tiene dimensiones (x, y, z) de (2, 4, 7)

El algoritmo debería devolver:

     (10, [(1, (2, 7)), (0, (1, 5))])

10 es la altura de la torre, y la lista escribe su composición: primero va la caja con índice 1, usando como base la orientación (2, 7), y luego apilada va la caja con índice 0, usando (1, 5) como base. La altura total está dada por la dimensión que no fue usada de cada caja: 4 para la primera caja, y 6 para la segunda.


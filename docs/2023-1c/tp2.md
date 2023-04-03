Trabajo Práctico n.º 2
======================
{:.no_toc}

Teoría de Algoritmos 1 - 1c 2023
Trabajo Práctico 2

## Lineamientos básicos

- El trabajo se realizará en grupos de cinco personas.

- Se debe entregar el informe en formato pdf y código fuente en (.zip) en el aula virtual de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar algún otro, se debe pactar con los docentes.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución. La ausencia de esta información no permite probar el trabajo y deberá ser re-entregado con esta información.

- El informe debe presentar carátula con el nombre del grupo, datos de los integrantes y  y fecha de entrega. Debe incluir número de hoja en cada página. No debe superar las 20 páginas + carátula + índice + referencias.

- En caso de re-entrega, entregar un apartado con las correcciones mencionadas

## Parte 1: La preselección de inversiones

Un comité de una empresa debe realizar una preselección de un subconjunto de proyectos. Cada uno de los “n” proyectos cuentan con dos índices de valoración: ganancias y prestigio. Luego de varias reuniones han decidido como criterio que, aquellos proyectos que cuenten con al menos otro que lo supere en ambos índices será rechazado. Como la cantidad de proyectos es grande y su tiempo limitado, nos solicitan que construyamos una solución algorítmica que pueden utilizar para resolver el problema.

Se pide:

1.  Proponga una estrategia por fuerza bruta para resolver el problema. ¿Cuál es su complejidad?

1.  Proponga una solución superadora utilizando división y conquista. Brinde pseudocódigo y estructuras de datos a utilizar. Intente que la complejidad sea la menor posible

1.  Presente relación de recurrencia de su solución. Realizar el análisis de complejidad temporal. Utilice tanto el teorema maestro cómo desenrollar la recurrencia. 

1.  Brinde dos ejemplos completos del funcionamiento de su solución

## Parte 2: La triangulación de polinomios

Dentro de la industria de los videojuegos se crean y utilizan motores gráficos para la animación de escenas. Un apartado importante de los mismos es la manera de dibujar los modelos en 3D para componer escenas. Generalmente a los diferentes objetos se los transforma en triángulos para facilitar las diferentes operaciones sobre ellos (manipulación, texturado, iluminación, etc). Realizaremos una función específica y sencilla que nos solicitan: triangular un polígono convexo conformado por n puntos. 

Podemos representar al polígono convexo como una secuencia de n vértices en el plano en sentido contrarreloj. Se conoce como cuerda (chord) de un polígono a una línea recta que conecta dos vértices no adyacentes de un polígono. La triangulación buscada debe ser realizada mediante cuerdas que no se intersectan entre sí.

Se debe tener en cuenta que existen una gran cantidad posible de triangulaciones. Pero queremos encontrar aquella que minimice el número resultante de sumar la longitud de los lados de cada uno de los triángulos construidos.  

Se pide:

1.  Determinar y explicar cómo se resolvería este problema por fuerza bruta. De un ejemplo paso a paso. ¿Qué complejidad temporal y espacial tiene la solución?

1.  Proponer una solución al problema que utiliza programación dinámica. Incluya relación de recurrencia, pseudocódigo, estructuras de datos utilizadas, explicación en prosa y un breve ejemplo de aplicación

1.  Analice la complejidad temporal y espacial de su propuesta.

1.  Programe la solución

1.  Determine si su programa tiene la misma complejidad que su propuesta teórica.

### Formato de los archivos:

El programa debe recibir por parámetro un archivo con la definición de los puntos. Corresponderá a un archivo de texto donde cada línea corresponde a un punto. El formato de la línea es: CordX CordY 

Ejemplo: “poligono.txt”

	0,5 0,5
	2,5 0,5
	2,5 8
	0,5 5

Debe resolver el problema y retornar por pantalla la solución. Debe mostrar el valor de la sumatoria obtenida y cada uno de los triángulos a armar.

## Parte 3: Un poco de teoría

1. Hasta el momento hemos visto 3 formas distintas de resolver problemas. Greedy, división y conquista y programación dinámica.

   1. Describa brevemente en qué consiste cada una de ellas

   1. ¿Qué propiedades requiere el problema para poder ser resueltos por ellos?

1. Considere el algoritmo Gale-Shapley. ¿Pertenece a alguna de estas metodologías? analice y responda justificando por sí o por no para cada una de ellas. 
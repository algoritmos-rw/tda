Trabajo Práctico n.º 3
======================
{:.no_toc}

Teoría de Algoritmos 1 - 1c 2019
Trabajo Práctico 3

## Lineamientos básicos

- El trabajo se realizará en grupos de cuatro personas (excepcionalmente de cinco o tres).

- La fecha de entrega es el lunes 17 de junio de 2019. Se debe entregar en el horario de clase en papel (informe), más una entrega en digital de código (.zip) e informe (.pdf) al correo de entregas del curso: tps.7529rw@gmail.com y a la clase de Google ClassRom de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar alguno que no este en la siguiente lista, coordinarlo con los docentes: Java, JavaScript, Ruby, Go, Rust, Swift, Scala, Haskell, OCaml, Clojure, D, Lua, Elixir.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución.

## Parte 1: La especia debe fluir


Nos solicitan crear un prototipo para un juego de estrategia en turnos de 2 jugadores a utilizar en una computadora. En el mismo dos superpotencias se pelean por la dominación global. El tablero es un mapa donde existen diferentes ciudades. Cada ciudad se interconecta con otras mediantes rutas de comercio. Algunas ciudades producen la conocida como “especia”. Cada superpotencia tiene una metrópoli central donde debe trasladar “especia” para transformarla en tropas o almacenarla.

### Separación inicial del tablero:

Se presenta el mapa con la configuración inicial. Cada potencia tendra controlada su metropoli.
Luego debe entregar un listado de ciudades ordenadas por preferencia. Se irán pareando las preferencias. Si en el mismo turno eligen la misma ciudad, esa ciudad queda sin control. Si eligen una ciudad diferente, se quedará cada uno controlando la seleccionado, a menos que la misma ya esté controlada por el rival.
Cada ciudad controlada inicialmente recibe 1 ejército.

### Juego:

Cada turno tiene varias fases:

- Recolección: Las potencias intentan trasladar la mayor cantidad posible de especies de las ciudades productoras a la metrópoli. Para eso pueden utilizar únicamente las rutas comerciales entre las ciudades que controla. Cada ruta tiene una cantidad máxima posible de transporte por turno.
- Producción: Las potencias pueden almacenar la especia o transformar 1 unidad de especia en 2 ejércitos. También pueden transformar unidades de ejército en 1 de especia. Las potencias deben ubicar sus ejércitos en las ciudades que controlan. Pueden distribuir sus ejércitos como quieran. Los ejércitos transformados en especia no se pueden usar en ese turno. Como máximo se pueden transformar 5 ejercitos en especia.
- Ataques: Cada potencia define con cuantos ejércitos atacarán a las ciudades de la superpotencia contraria. Los ataques solo se pueden realizar entre ciudades con rutas comerciales. Las batallas se realizan en simultáneo. Gana el que tenga más ejércitos. Se eliminan los ejércitos de ambos equipos que igualan (si la batalla es 5 contra 4, cada potencia elimina 4 ejércitos). Si gana el atacante pasa los ejércitos sobrantes a la ciudad controlada. Si gana el defensor, se queda en la ciudad con los ejércitos restantes. Si hay empate y la ciudad queda sin defensas la misma pasa a estar sin control. Podrá ser atacada en la próxima ronda por ambos bandos y se utilizaran las mismas reglas de combate (el que gana se queda con la ciudad). La ciudad metrópoli no se puede atacar.

### Fin de juego:

El juego termina cuando alguno de estos criterios se cumplen:

- Una superpotencia llega a más de 100 de especia acumulada. 
- La metrópoli rival queda desconectada del resto de las ciudades productoras propias.
- Se cumplen 50 turnos desde el inicio de la partida
 
#### Criterios de desempate:

Si algunos de los criterios de fin de juego se cumple, pero para ambos superpotencias. El desempate se realiza de la siguiente forma:

- Gana quien tiene más especia acumulada. 
- Si aún hay empate gana quien tenga más ciudades controladas. 
- Si aún hay empate gana quien tenga más ejércitos desplegados.
- Si aún hay empate, termina en empate.


### Formato de archivos y parámetros del programa

Con el objectivo de poder correr simulaciones entre diferentes grupos, es indispensable que se cumplan los formatos solicitados para evitar problemas de interfaces. Se ejecutará un programa en bash o similar para ejecutar las partidas.

Todos los archivos son de tipo texto. Con un registro por línea y separados por coma (sin espacio entre ellos)

#### Tablero:
El tablero de juego se encontrará definido en 2 archivos:
- Ciudades.txt: contiene los nombres de las ciudades y la cantidad de especia que genera (valor entero mayor o igual a 0). La primera y segunda ciudad corresponden a las metrópolis del primer y segundo jugador respectivamente. 

Ejemplo:

	Washington,0
	Moscu,0
	Buenos Aires,10
	Rio de Janeiro,7
	Paris,5
	Roma,4
	…


- rutas.txt: contiene las rutas de comercio que unen a las diferentes ciudades. Las rutas son en el sentido dado por el par de ciudades. Tiene la capacidad máxima de transporte de la ciudad.

Ejemplo:

	Paris,Roma,3
	Buenos Aires,Rio de Janeiro,4
	Rio de Janeiro,Buenos Aires,3
	...

#### Separación inicial del tablero:
- se deberá entregar un programa “selección” que reciba por parámetros ciudades.txt y rutas.txt y si es el jugador 1 o 2. La salida es un archivo con priorización de las ciudades a controlar.

Ejemplo:

	seleccion 1 ciudades.txt rutas.txt

O

	seleccion 2 ciudades.txt rutas.txt

El archivo resultante se debe llamar “seleccion1.txt” o “seleccion2.txt” y debe tener ordenadas todas las ciudades por prioridad. Las ciudades principales ya pertenecen a cada jugador.

El formato del archivo será:

	Buenos Aires
	Roma
	Paris
	Rio de Janeiro
	...
 
- Para la división inicial del mapa se debe llamar al programa “division” pasándole por parámetros ciudades.txt, rutas.txt, seleccion1.txt y seleccion2.txt

La salida del programa serán 2 archivos llamados respectivamente imperio1.txt e imperio2.txt. Cada uno tendrá la lista de las ciudades dominadas y la cantidad de ejercicios que posee (inicialmente 1). La primera ciudad será la metrópoli.

Ejemplo:

    Moscu,1
    Roma,1
    …

#### Recoleccion:
El programa llamado “recolectar” recibe por parametro el numero de jugador,  los archivos del mapa y las ciudad dominada por el jugador y devolverá un archivo llamado cosecha1.txt y cosecha2.txt respectivamente con el valor numérico de la especia recolectada más la disponible de turnos anteriores (se encuentra en el archivo con el mismo nombre que debe sobreescribir. 

#### Producción:
El programa “producir” recibe por parametro el numero de jugador, los archivos del mapa, imperio y cosecha propia y rival. Deberá generar archivos de cosecha e imperio temporales con el consumo e implantación de ejércitos. Los nombre serán “cosecha[nrojugador]_temp.txt” e “imperio[nrojugador]_temp.txt”

#### Ataque:
Se deberá llamar al programa “tactica” que recibe  por parámetro el número de jugador, los archivos del mapa, imperio y cosecha propia y rival, deberá generar los archivo ataque[nrojugador].txt que contendrá los ataque de ciudades a otras del rival en ciudades conectadas por rutas. Para cada ataque indicará con cuántos ejércitos ataca.

El formato del archivo de salida será:

	Roma,Paris,4
	Rio de Janeiro,Buenos Aires,3
 
#### Contienda:
El programa "contienda" resolverá las batallas y actualizará los archivos de imperio de cada jugador. Toma como parámetros los archivos de mapa, imperio y de ataque. Debe resolver los ataques teniendo en cuenta que los soldados utilizados para atacar que parte de una ciudad no estarán en la defensa en ese turno.

#### Ganador:
El programa "ganador" recibe el número de turno, los archivos de mapa, imperio y cosecha de ambos jugadores. Verifica si hay un ganador de acuerdo a los criterios de victoria. Retorna un archivo ganador.txt que tendrá el nombre del ganador o estará vacío si no lo hay.

### Pseudocódigo del juego:
(ATENCION: Es a modo ilustrativo. Los procesos deben ser programas independientes)

	//genera seleccion1.txt
	seleccion(1,ciudades.txt,rutas.txt)
	
	//genera seleccion2.txt
	seleccion(2,ciudades.txt,rutas.txt)
	
	//genera imperio1.txt e imperio2.txt
	division(ciudades.txt,rutas.txt,seleccion1.txt,seleccion2.txt)
	ronda = 0
	Repetir
	    //genera cosecha1.txt
		recolectar(1,ciudades.txt,rutas.txt,imperio1.txt)
		
		//genera cosecha2.txt
		recolectar(2,ciudades.txt,rutas.txt,imperio2.txt)
		
		// genera cosecha1_temp.txt e imperio1_temp.txt
		producir(1, ciudades.txt,rutas.txt,imperio1.txt,cosecha1.txt,imperio2.txt,cosecha2.txt) 
		
		// genera cosecha2_temp.txt e imperio2_temp.txt
		producir(2, ciudades.txt,rutas.txt,imperio1.txt,cosecha1.txt,imperio2.txt,cosecha2.txt) 
		
		Renombrar imperio1_temp.txt a imperio1.txt
		Renombrar imperio2_temp.txt a imperio2.txt
		Renombrar cosecha1_temp.txt a cosecha1.txt
		Renombrar cosecha2_temp.txt a cosecha2.txt
		
		//genera el archivo ataque1.txt
		tactica(1, ciudades.txt,rutas.txt,imperio1.txt,cosecha1.txt,imperio2.txt,cosecha2.txt)
		
		//genera el archivo ataque2.txt
		tactica(2, ciudades.txt,rutas.txt,imperio1.txt,cosecha1.txt,imperio2.txt,cosecha2.txt)
		
		//Actualiza imperio1.txt e imperio2.txt
		contienda(ciudades.txt,rutas.txt,imperio1.txt,imperio2.txt,ataque1.txt,ataque2.txt)
		
		//determina si hay ganador
		ganador(ronda,ciudades.txt,rutas.txt,imperio1.txt,cosecha1.txt,imperio2.txt,cosecha2.txt)
		ronda++
	
	Hasta ronda=maximarondas o hay ganador

### Tareas:

1. Diseñe los algoritmos para que se pueda jugar este juego (Genere 2 estrategias para poder probar jugar. Una las mas competitiva posible y otra “dummy” para probar como funciona. LOS PROGRAMAS DEBEN TENER EL MISMO NOMBRE Y ESTAR EN DIFERENTE DIRECTORIO)
1. Explique qué algoritmos utilizados en clase puede utilizar y cuales investigó por su cuenta.
1. Detalle la complejidad de los algoritmos que utiliza.
1. Programe el juego


## Parte 2: Programando la producción semanal

Una empresa que produce partes de aviones solicita nuestros servicios para planificar su producción de las próximas n semanas. Produce 3 tipos de piezas complejas. Cada pieza lleva una semana de elaboración. Por restricciones espaciales solo puede generar un tipo de pieza simultáneamente. Asimismo cada vez que produce un tipo de pieza, no puede volver a realizarla en la siguiente semana para evitar el sobrecalentamiento de cierta maquinaria.

Tenemos una planilla de pedidos donde por semana nos indican el ofrecimiento monetario que nos hacen por construir cada tipo de pieza. Por ejemplo:

|          | Semana 1  | Semana 2  | Semana 3  |
|----------|-----------|-----------|-----------|
| Pieza 1  | 50        | 40        | 60        |
| Pieza 2  | 30        | 40        | 40        |
| Pieza 3  | 80        | 30        | 10        |

Debemos determinar qué tipo de pieza producir cada semana, intentando maximizar las ganancias respetando las restricciones.

Se pide:

1. Proponer una solución greedy para el problema. Mostrar el pseudocódigo.
1. Analizar y justificar la complejidad del algoritmo
1. Determinar si la solución es óptima. En caso negativo, en qué condiciones lo puede ser?
1. Proponer una solución con programación dinámica. Mostrar el pseudocódigo.
1. Explicitar la relación de recurrencia y analizar la complejidad del algoritmo. 

(no se debe programar este ejercicio)

## Parte 3: Clases de Complejidad

A. Responda a las siguientes preguntas teóricas. Sea conciso y justifique claramente

1. Defina y explique (si es necesario con ejemplos) qué significa que un problema sea P, NP, NP-Completo y NP-Hard

1. Tenemos un problema A, un problema B y una caja negra NA y NB que resuelven el problema A y B respectivamente. Sabiendo que B es NP

1.1. Qué podemos decir de A si utilizamos NA para resolver el problema B (asumimos que la reducción realizada para adaptar el problema B al problema A el polinomial)

1.1. Qué podemos decir de A si utilizamos NB para resolver el problema A (asumimos que la reducción realizada para adaptar el problema A al problema B el polinomial)

1.1. Qué pasa con los puntos anteriores si no conocemos la complejidad de B, pero sabemos que A es P?.


B. Demostrar que los siguientes problemas son NPC. Justificar claramente, escribiendo en pseudocódigo los algoritmos si cree conveniente

1. Dados 4 sets de elementos (W, X, Y, Z) (cada uno de tamaño n) y una colección C de 4-tuplas de la forma (w, x, y, z), tal que wW, xX, yY, zZ. El problema de 4-Dimensional Matching consiste en identificar si existen N 4-tuplas de C tal que ninguna de ellas tienen ningún elemento en común con las demás (es decir, si una tupla es (w1, x1, y1, z1) ∈ C y otra es (w2, x2, y2, z2) ∈ C, son distintas si w1 ≠ w2, x1 ≠ x2, y1 ≠ y2, and z1 ≠ z2).
Sabiendo que el problema de 3-Dimensional Matching (el mismo que el anteriormente explicado pero con 3 sets y considerando 3-tuplas) es NP-Completo, demostrar que el problema de 4-Dimensional Matching es NP-Completo también.

1. Se tiene un conjunto de n tareas, con tiempo de ejecución ti​, una fecha límite de finalización di y una ganancia vi otorgada si se finaliza antes que su tiempo límite. Se pide devolver si existe alguna planificación que obtenga una ganancia total mayor o igual a K sin ejecutar dos tareas a la vez.


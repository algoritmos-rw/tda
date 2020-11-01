Trabajo Práctico n.º 2
======================
{:.no_toc}

Teoría de Algoritmos 1 - 2c 2020
Trabajo Práctico 2

## Lineamientos básicos

- El trabajo se realizará en grupos de cuatro personas (excepcionalmente de tres o cinco).

- Se debe entregar el informe en formato pdf y código fuente en (.zip) en el aula virtual de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar algún otro, se debe pactar con los docentes.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución. La ausencia de esta información no permite probar el trabajo y deberá ser re-entregado con esta información.

- El informe debe presentar carátula con el nombre del grupo y número de hoja cada página.

## Parte 1: Auditoría de seguridad de passwords

Como parte de los protocolos de seguridad de un sistema se controla la fuerza del password del usuario. Entre las  pruebas realizadas se encuentra determinar si una contraseña cuenta con texto similar a datos del usuario como su nombre, apellido o username.

Por ejemplo: Si el username es “jperez”, queremos desaconsejar el password “perez2020” (perez se encuentra en ambos datos). Igualmente debemos desaconsejar la clave “p2e0r2e0z” (aunque de forma más rebuscada, también “perez” se encuentra en ambas).

Dadas las longitudes máximas de los campos: 

 username → “u”. 
 
 nombre → “n”. 
 
 apellido → “a”.  
 
 password → “p”. 

Deseamos construir un algoritmo utilizando programación dinámica que nos retorne la subsecuencia de mayor longitud, común entre cada elemento y el password. Entendiéndose esta misma como la secuencia más larga de caracteres que aparecen de izquierda a derecha (no necesariamente en forma contigua) en las dos cadenas de texto comparadas. 
Además indicar la longitud y qué porcentaje corresponde en cada caso de la cadena original.

Ejemplo:

	Para el usuario:
	username: rksmith
	nombre: rick
	apellido: smith
	password: r_1k!smi7t
	
	Comparando username “rsmith” con password “r_1k!smi7t”.
	La subcadena más larga es: r_1k!smi7t → longitud 6
	Porcentaje de coincidencia: (100 * longitud subcadena más larga / longitud username ): 100 * 6 / 7 = 81,71%
	
	Comparando nombre “rick” con password “r_1k!smi7t”.
	La subcadena más larga es: r_1k!smi7t → longitud 2
	Porcentaje de coincidencia: 100 * 2 / 4 = 50%
	
	Comparando apellido “smith” con password “r_1k!smi7t”.
	La subcadena más larga es: r_1k!smi7t → longitud 4
	Porcentaje de coincidencia: 100 * 4 / 5 = 80%
	
	Mayor longitud de coincidencia: 6
	Longitud password: 10
	Porcentaje de originalidad: 100 - 100 * mayor longitud de coincidencia / longitud password: 40%

Se pide:

1. Presentar relación de recurrencia y subproblemas
1. Presentar solución iterativa y análisis de la solución
1. Determinar la complejidad temporal y espacial de la solución
1. Programar la solución

### Interfaz del programa

El programa debe recibir por parámetro username, nombre, apellido y password
Debe mostrar por pantalla la información en un formato similar al utilizado en el ejemplo.

## Parte 2: Planificación de producción.

Un taller metalúrgico cuenta con un conjunto de M controles numéricos computarizados (CNC). Cada uno de ellos puede realizar trabajos de duración en bloques de 1 hora. Por otro lado, cuenta con N tareas a realizar. 

Cada tarea i tiene
* una duración de horas de desarrollo. 
* una hora de posible comienzo (cuando puede comenzar a realizarse)
* una hora de entrega (momento donde debe estar finalizada)

Las tareas pueden realizarse parcialmente y utilizarse para su elaboración una o varias máquinas. Por ejemplo si la tarea A requiere 4 horas. Podría realizarse 1 hora en la  máquina 1 y luego de un intervalo concluir su desarrollo en la máquina B (3 horas restantes).

El jefe de planta nos solicita nuestra ayuda para que le ayudemos a determinar si podrá cumplir con la finalización de las tareas en tiempo y forma. Y en caso afirmativo le indiquemos cómo organizarla.

Se solicita:
1. Utilizando redes de flujos dar una solución al problema
1. Determinar la complejidad espacial y temporal de la solución. ¿Es polinomial?
1. De un ejemplo completo donde se pueda cumplir todas las tareas. Y un ejemplo donde no se pueda. Utilice gráficos para formalizar los ejemplos

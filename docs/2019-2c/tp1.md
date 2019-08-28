Trabajo Práctico n.º 1
======================
{:.no_toc}

Teoría de Algoritmos 1 - 2c 2019
Trabajo Práctico 1

## Lineamientos básicos

- El trabajo se realizará en grupos de cuatro personas (excepcionalmente de tres).

- La fecha de entrega es Miércoles 11 de Septiembre. Se debe entregar en el horario de clase en papel (informe), más una entrega en digital de código (.zip) e informe (.pdf) a la clase de Google ClassRoom de la materia.

- El lenguaje de implementación es libre. Recomendamos utilizar C, C++ o Python. Sin embargo si se desea utilizar algún otro, se debe pactar con los docentes.

- Incluir en el informe los requisitos y procedimientos para su compilación y ejecución. La ausencia de esta información no permite probar el trabajo y deberá ser re-entregado con esta información.

- El informe debe presentar carátula con el nombre del grupo y número de hoja cada página

## Parte 1: Múltiples soluciones para un mismo problema

Se cuenta con un vector de “n” posiciones en el que se encuentran algunos de los primeros ”m” números naturales ordenados en forma creciente (m >= n). En el vector no hay números repetidos. Se desea obtener el menor número no incluido.

Ejemplo: n=5, m=20 y s={1, 2, 5, 15}. Entonces el menor número no incluido es el 3.

Nos proponen los siguientes métodos de resolución:

* Comenzando desde el primer elemento e incrementando de a una posición, verificar hasta encontrar el primer salto en la numeración o hasta recorrer todos las posiciones del vector. Si no hay faltantes retorna n+1

* Comenzando desde el 1 hasta el número natural m, realizar una búsqueda binaria para determinar si se encuentra o no el elemento. Si no se encuentra ese es el primer número faltante.

* Buscar el elemento del medio del vector. Si ese elemento es igual al valor de su posición en el vector (comenzando a contar desde 1) significa que no hay números faltantes hasta ahí. Por lo tanto repito el procedimiento quedandome con el tramo del vector de la posición media+1 hasta el final. Si, por el contrario, el elemento es mayor al de su posición en el índice, indica que hay un faltante. Restringir la búsqueda desde el valor del inicio hasta el medio. Repetir hasta que quede solo un subvector de solo 1 elemento. El número que falta será esa posición en el vector original. O si finalizó en la última posición del vector y su valor coincide con la posición, el número faltante será n+1

Se pide:

1. Presentar en pseudocódigo cada una de las propuestas
1. Determinar la complejidad algorítmica de cada una
1. Ordenarlas según complejidad explicando cómo se calculan
1. Existen casos prácticos donde es más conveniente usar alguno de los métodos anteriores en vez de otro a pesar de contar con complejidad teórica mayor? o que sea indistinto? Ejemplificar.
1. Si pudiese elegir las estructuras de datos que utiliza para presentar una solución alternativa, puede lograr construir un algoritmo con complejidad O(log(M))? 

## Parte 2: Un crédito sensible

El departamento de créditos de un banco generó un cuestionario de “n” preguntas cuya respuesta posible es “SI” o “NO”. Con los resultados del cuestionario aplican un algoritmo cuya salida determina si el crédito fue aprobado o no. Por cuestiones de seguridad no nos quieren mostrar el mismo.  Nos informan que tiene una complejidad temporal de O(f(n)).

Disponemos el algoritmo como caja negra. Lo único que podemos usar para probarlo es su interfaz gráfica que pregunta una a una las preguntas y cuyo tiempo de respuesta es “s” segundos por pregunta.

Nos solicitan que calculemos la sensibilidad de su método.

Medimos la sensibilidad de un cuestionario particular como la mínima cantidad de respuestas a modificar para que el resultado de aprobación cambie.  La sensibilidad global se calcula como el máximo entre todos los mínimos posibles.

1. Explique cómo procederá a medir la sensibilidad. Utilice pseudocódigo y prosa.
1. ¿Cuál es la complejidad del proceso global (temporal y espacial)? Detalle cómo llega a ese valor.
1. ¿Cuánto tiempo nos llevará responder al departamento de créditos? (es un tiempo razonable si f(n)=0,5*n segundos y n=20 y s=0,4? )

## Parte 3: Trasplantes programados

El “New England Program for Kidney Exchange” cuenta con una lista de “n” pacientes que esperan la donación de un riñón. A la vez cuenta con una base de datos de “m” donantes.
Mediante un protocolo médico han determinado para cada paciente la compatibilidad de cada uno de los donantes. 
Al mismo tiempo, para cada donante cuentan con un valor de factibilidad asociado a cada paciente. El mismo está construido en base distancias geográficas, relaciones familiares y otras cuestiones.
Nos solicitan que construyamos un algoritmo que permite construir los mejores emparejamientos posibles.
Considerar que “n” no necesariamente es igual a “m”. Las compatibilidades y factibilidades están medidos con valores enteros donde un valor menor es mejor. No hay valores repetidos (no existe el empate). Tanto los pacientes como los donantes pueden ser los solicitantes (se resolverá mediante un parámetro del programa)

1. Presente el pseudocódigo de su solución
1. Analice la complejidad del algoritmo (temporal y espacial)
1. ¿Qué criterio se tiene que dar para que los emparejamientos sean estables?
1. Explique mediante un ejemplo el concepto de best valid partner y la incidencia de cuál de las partes es el solicitante
1. Programe la solución
1. ¿Su solución tiene la misma complejidad que la teórica? Justifique.
 
### Interface de los programas:

El archivo de compatibilidad se tiene que llamar “compatibilidad.txt”. Es un archivo de tipo texto y contiene una línea por cada paciente. Cada paciente está representado por un número de 1 a n.
Seguido del paciente se encuentra la lista separada por comas de su compatibilidad de donante. De mayor a menor.
Ejemplo:

	1,4,3,2,5,1
	2,5,3,1,4,2
	3,4,3,2,1,5
	4,1,2,4,3,5

El archivo de factibilidad se tiene que llamar “factibilidad.txt”. Es un archivo de tipo texto y contiene una línea por cada donante. Cada donante está representado por un número de 1 a m.
Seguido del donante se encuentra la lista separada por comas de su factibilidad de paciente. De mayor a menor.
Ejemplo:

	1,4,3,2,1
	2,3,1,4,2
	3,4,3,2,1
	4,1,2,4,3
	5,2,3,4,1

Los emparejamientos se tienen que guardar en el archivo “resultado.txt”. Debe ser un archivo de texto donde se muestre una pareja por línea y separado por comas. Primero los pacientes y luego los donantes.

Los parámetros de ejecución del programa son 3:
Cantidad de pacientes: valor numérico
Cantidad de donantes: valor numérico
Quién es el solicitante: puede tomar el valor de “p”: paciente o “d”: donante (sin comillas, solo la letra)

### Información extra:
Este es una super simplificación de una aplicación real ( https://stanford.edu/~alroth/papers/kidney.qje.pdf)  que le valió el nobel de 2012 a Alvin Roth ( https://www.nobelprize.org/prizes/economic-sciences/2012/roth/facts/ )
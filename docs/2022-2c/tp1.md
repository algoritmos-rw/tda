Trabajo Práctico n.º 1
======================
{:.no_toc}

Teoría de Algoritmos 1 - 2c 2022
Trabajo Práctico 1

## Lineamientos básicos

- El trabajo se realizará en forma individual.

- Se debe entregar el informe en formato pdf en el aula virtual de la materia.

- El informe debe presentar carátula con datos del autor y fecha de entrega. Debe incluir número de hoja en cada página.

- La extensión del informe no debe superar las 7 páginas + carátula + índice + referencias.

- Debe presentar codigo fuente e instrucciones de compilación y ejecución

- En caso de re-entrega, entregar un apartado con las correcciones mencionadas

## Parte 1: La fiesta del club de amigos

El club de amigos de la república Antillense prepara un ágape en sus instalaciones en la que desea invitar a la máxima cantidad de sus “n” socios. Sin embargo por protocolo cada persona invitada debe cumplir un requisito: Sólo puede asistir si conoce a al menos otras 4 personas invitadas 

Nos solicitan seleccionar el mayor número posible de invitados.


Resuelva:

1. Proponga una estrategia greedy óptima para resolver el problema con la menor complejidad espacial y temporal posible. Justifique su optimalidad. Justifique que sea greedy.

1. Explique cómo implementar algorítmicamente esa estrategia. Brinde pseudocódigo y estructuras de datos a utilizar.

1. Analice complejidad temporal y espacial de su propuesta

1. Programe su algoritmo y entregue dos ejemplos para su prueba.

1. ¿Su programa mantiene la complejidad espacial y temporal de su algoritmo? Justifique referenciando a la documentación del lenguaje si es necesario.
 
1. Los organizadores desean que cada invitado pueda conocer nuevas personas. Por lo que nos solicitan que adicionemos una nueva restricción a la invitación: Sólo puede asistir si NO conoce al menos otras 4 personas invitadas. Modifique su propuesta para satisfacer esta nueva solución. ¿Impacta en su complejidad?


### Formato de los archivos:

El algoritmo debe recibir por parámetro el valor n y luego el nombre del archivo que contiene los socios y sus conocidos.
El archivo de los socios corresponde a un archivo de texto que tiene una línea por socio seguido de sus conocidos. Cumple con el siguiente formato: nro_socio, nombre, nro_socio_conocido1, nro_socio_conocido2, …nro_socio_conocidox

Ejemplo “socios.txt”:

	1,Guybrush Threepwood,2,3,4,5,6,9
	2,Elaine Marley,1,3,4,6,7,8
	3,Largo LaGrande,1,2,4,5,6,9
	4,LeChuck,1,2,3,6,8
	5,Wally B. Feed,1,3,8,6
	6,Murray,1,2,3,4,9
	7,Alfredo Fettucini,2,8,9
	8,Gobernador Phatt,2,4,5,7
	9,Smilin' Stan S. Stanman,1,3,6,7

El programa debe mostrar en pantalla a los invitados de la siguiente manera : nro_socio,nombre. Uno por línea. Ejemplo:

	1,Guybrush Threepwood
	2,Elaine Marley
	3,Largo LaGrande
	4,LeChuck
	6,Murray

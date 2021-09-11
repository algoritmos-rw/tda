Trabajo Práctico n.º 1
======================
{:.no_toc}

Teoría de Algoritmos 1 - 2c 2021
Trabajo Práctico 1

## Lineamientos básicos

- El trabajo se realizará en forma individual.

- Se debe entregar el informe en formato pdf en el aula virtual de la materia.

- El informe debe presentar carátula con datos del autor y fecha de entrega. Debe incluir número de hoja en cada página.

- En caso de re-entrega, entregar un apartado con las correcciones mencionadas

## Parte 1: Karatsuba!

Dada los siguientes números (completada por su número de padrón) 

	a35b411c 
	2d98ef55

con: 

	a: dígito del padrón correspondiente a la unidad
	b: dígito del padrón correspondiente a la centena
	c: los dos dígitos del padrón de la izquierda mod 7
	d: dígito del padrón correspondiente a la decena
	e: dígito del padrón correspondiente a la unidad de mil
	f: los dos dígitos del padrón de la derecha mod 9

	Ejemplo. Padrón: 95473
	
	33544114
	27985155


Se pide:

1. Resuelva la multiplicación paso a paso utilizando el algoritmo de Karatsuba.

1. Cuente la cantidad de sumas y multiplicaciones que realiza y relaciónelo con la complejidad temporal del método

1. Comparar lo obtenido con el método de multiplicación tradicional. Observa alguna mejora? Analice.

## Parte 2: Cuestión de complejidad...

Dado la siguiente relación de recurrencia 

        a T(n/b) + O(c)

Con:

    a: los dos dígitos del padrón de la izquierda mod 9
	 b: los dos dígitos del padrón de la izquierda mod 7
	 c: “n” si su padrón es múltiplo de 4, 
        sino “nlogn” si su padrón es múltiplo de 3
    	  sino “n2”  

Se pide:

1. calcular la complejidad temporal utilizando el teorema maestro. 

1. Explique paso a paso cómo llega a la misma


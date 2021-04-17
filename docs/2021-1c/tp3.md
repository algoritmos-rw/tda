Trabajo Práctico n.º 3
======================
{:.no_toc}

Teoría de Algoritmos 1 - 1c 2021
Trabajo Práctico 3

## Lineamientos básicos

- El trabajo se realizará en grupos de cinco personas.

- Se debe entregar el informe en formato pdf en el aula virtual de la materia.

- El informe debe presentar carátula con el nombre del grupo y número de hoja cada página.

- En caso de re-entrega, entregar un apartado con las correcciones mencionadas

## Parte 1: La mudanza

Un grupo de amigos que conviven están mudándose a un departamento nuevo. Han juntado sus pertenencias en cajas de diferentes volúmenes que recolectaron en supermercados y tiendas. 

Al llegar la compañía de mudanza les informan que por normativa únicamente transportarán utilizando como contenedores sus recipientes de volumen V. Por lo tanto los amigos deben ingresar sus cajas en los contenedores autorizados.

En el camión entran como máximo “r” recipientes. Al llenarse realiza el trayecto para descargar y regresar a cargar otros contenedores.
 
Antes de proceder quieren saber si podrán acomodar todas sus cajas de tal forma que puedan realizar menos de k viajes.

Demostrar que es un problema NP-Completo

HINT 1: Este problema es fácilmente relacionable con Bin Packing. Puedo utilizarlo como parte de su demostración (No asumir que Bin Packing es NP-C: demostrarlo!)

HINT 2: Puede utilizar 2-Partition para la demostración

![Mudanza](/tda/images/mudanza.png){:height="1100px" width="500px"}.


## Parte 2: La personalización del yate.

Una constructora de barcos está preparando para la venta un nuevo yate. Para atraer posibles compradores han planteado que el cliente pueda personalizar seleccionando entre “n” diferentes packs de accesorios y modificaciones.
Por otro lado existen “m” regulaciones que se deben cumplir para la navegación segura. Un barco que no cumple con el 100% de ellas no se aprobará para su uso. 
Los packs están relacionados con las regulaciones. Por ejemplo utilizar un pack puede hacer que una regulación se cumpla. También podría pasar que la no utilización de un pack haga que una determinada regulación se cumpla. Un mismo pack puede influir en más de una regulación. En ese caso puede pasar que en uno su presencia haga y en otra su ausencia (o cualquier combinación posible).

El área de diseño realizó dos propuestas. En la primera cada regulación está vinculada a cuatro packs diferentes. En la segunda por dos packs diferentes.
El área de marketing nos solicita determinar si es posible que un cliente seleccione un los packs de forma sencilla para cumplir con todas las regulaciones.
   
1. Pruebe que en caso de usar 4 pack por regulación el problema pertenece a NP-C

1. Pruebe que en caso de usar 2 pack por regulación el problema pertenece a P


HINT 1: Puede suponer que sabemos que 3-SAT pertenece a NP-C y utilizarlo como parte de la demostración 
HINT 2: Para 2SAT puede investigar sobre su posible representación como un grafo.


## Parte 3: Un poco de teoría

1. Defina y explique qué es una reducción polinomial y para qué se utiliza.

1. Explique detalladamente la relación entro los problemas P y NP”

1. Tenemos un problema A, un problema B y una caja negra NA y NB que resuelven el problema A y B respectivamente. Sabiendo que B es P

   1. Qué podemos decir de A si utilizamos NA para resolver el problema B (asumimos que la reducción realizada para adaptar el problema B al problema A es polinomial)
   
   1. Qué podemos decir de A si utilizamos NB para resolver el problema A (asumimos que la reducción realizada para adaptar el problema A al problema B es polinomial)
   
   1. ¿Qué pasa con los puntos anteriores si no conocemos la complejidad de B, pero sabemos que A es NP-C?

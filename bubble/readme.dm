Burbujeo:

El ordenamiento por burbujeo se basa en una idea bastante sencilla. El algoritmo compara dos elementos contiguos 
de la lista y, si el orden es adecuado, los deja como están, si no, los intercambia. La repetición de este paso 
elemental (una burbuja) a lo largo de la lista (recorriéndola desde el comienzo hasta el final) garantiza llevar 
el mayor elemento al final de la lista, pero no garantiza que el menor elemento haya quedado en el primer lugar. 
De hecho, el menor elemento solo se mueve un paso hacia la izquierda en una recorrida completa de la lista. 
Es por esto que estas recorridas se repiten sucesivas veces (¿cuántas veces hace falta?) de manera de garantizar 
que la lista quede completamente ordenada.

Como en el primer paso tenemos la garantía de que el mayor elemento quedó al final de la lista, la segunda recorrida 
puede evitar llegar hasta esa última posición. Así, cada recorrida es más corta que la anterior. En cada recorrida se 
comparan todos los pares de elementos sucesivos (en el rango correspondiente) y se intercambian si no están ordenados.

Programá una función ord_burbujeo(lista) que implemente este método de ordenamiento. Debe tomar una lista y devolver la lista ordenada.

Extra: ¿Podés escribir una versión recursiva de este algoritmo?


Bubbling

Bubble sort is based on a fairly simple idea. The algorithm compares two contiguous elements
from the list and, if the order is correct, it leaves them as they are, if not, it exchanges them. Repeating this step
element (a bubble) along the list (going from start to finish) is guaranteed to bring
the largest element at the end of the list, but it does not guarantee that the smallest element is in the first place.
In fact, the smallest element only moves one step to the left in a complete traversal of the list.
This is why these tours are repeated successive times (how many times is it necessary?) in order to guarantee
that the list is completely sorted.

Since in the first pass we are guaranteed that the largest element was left at the end of the list, the second traversed
can avoid reaching that last position. Thus, each run is shorter than the previous one. In each tour
they compare all pairs of successive elements (in the corresponding rank) and swap if they are unordered.

Write a function bubble_order(list) that implements this sorting method. It should take a list and return the sorted list.

Extra: Can you write a recursive version of this algorithm?

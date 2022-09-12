Hojas ISO y recursión

La norma ISO 216 especifica tamaños de papel. Es el estándar que define el popular tamaño de papel A4 
(210 mm de ancho y 297 mm de largo). Las hojas A0 miden 841 mm de ancho y 1189 mm de largo. A partir de la A0 las 
siguientes medidas, digamos la A(N+1), se definen doblando al medio la hoja A(N). Siempre se miden en milímetros con 
números enteros: entonces la hoja A1 mide 594 mm de ancho (y no 594.5) por 841 mm de largo.

Escribí una función recursiva medidas_hoja_A(N) que para una entrada N mayor que cero, devuelva el ancho y el largo 
de la hoja A(N) calculada recursivamente a partir de las medidas de la hoja A(N−1), usando la hoja A0 como caso base. 
La función debe devolver el ancho y el largo -en ese orden- en una tupla.



ISO sheets and recursion

The ISO 216 standard specifies paper sizes. It is the standard that defines the popular A4 paper size
(210mm wide and 297mm long). A0 sheets measure 841mm wide and 1189mm long. Starting from A0 the
The following measures, say A(N+1), are defined by folding the sheet A(N) in half. They are always measured in millimeters with
integers: then the A1 sheet is 594 mm wide (and not 594.5) by 841 mm long.

Write a recursive function sheet_measures_A(N) that for an input N greater than zero, returns the width and length
of sheet A(N) computed recursively from the measurements of sheet A(N−1), using sheet A0 as the base case.
The function must return the width and length -in that order- in a tuple.

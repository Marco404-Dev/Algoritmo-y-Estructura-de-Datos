# Clase 3 – Sorting (Ordenamiento)

## Problemas Propuestos con Solución

### Problema 1

Define con precisión qué es un algoritmo de ordenamiento.

**Solución:**
Un algoritmo de ordenamiento es un procedimiento que toma una secuencia de elementos y los reordena de acuerdo a una relación de orden (por ejemplo ≤). La salida debe estar ordenada y contener exactamente los mismos elementos que la entrada (misma frecuencia de cada elemento).

---

### Problema 2

Explica qué significa que un arreglo ordenado sea una permutación del arreglo original.

**Solución:**
Significa que no se crean ni eliminan elementos, solo se cambia el orden. Por ejemplo:
A = [3,1,3]
B = [1,3,3]
B es una permutación de A porque conserva los mismos valores con la misma cantidad de apariciones.

---

### Problema 3

Diferencia entre un algoritmo destructivo y uno no destructivo. Da ejemplos.

**Solución:**
Un algoritmo destructivo modifica el arreglo original (ej.: Selection Sort). Uno no destructivo crea una copia ordenada y deja intacta la entrada (ej.: Merge Sort cuando retorna un nuevo arreglo). Todo algoritmo in-place es destructivo.

---

### Problema 4

¿Por qué la búsqueda binaria solo funciona sobre arreglos ordenados?

**Solución:**
La búsqueda binaria descarta la mitad del arreglo usando comparaciones. Esto solo es correcto si los elementos están ordenados; de lo contrario, no se puede garantizar que los descartes sean válidos.

---

### Problema 5

Explica por qué Permutation Sort es correcto pero inútil en la práctica.

**Solución:**
Es correcto porque prueba todas las permutaciones posibles y alguna estará ordenada. Es inútil porque existen n! permutaciones y verificar cada una cuesta Θ(n), dando una complejidad explosiva.

---

### Problema 6

Describe paso a paso cómo funciona Selection Sort sobre el arreglo:
[5, 3, 4, 1]

**Solución:**

1. Máximo = 5 → swap con último → [1,3,4,5]
2. Prefijo [1,3,4], máximo = 4 → queda en su lugar
3. Prefijo [1,3], máximo = 3 → arreglo ordenado

---

### Problema 7

Demuestra informalmente por qué Selection Sort tiene complejidad Θ(n²).

**Solución:**
El algoritmo busca el máximo n veces. Cada búsqueda recorre un prefijo de tamaño decreciente. La suma total es n + (n−1) + … + 1 = Θ(n²).

---

### Problema 8

¿Selection Sort es estable? Justifica con un ejemplo concreto.

**Solución:**
No es estable. Ejemplo: [(2,a),(2,b),1]. Al mover el máximo, el orden relativo entre (2,a) y (2,b) puede invertirse.

---

### Problema 9

Describe la idea central de Insertion Sort.

**Solución:**
Mantiene un prefijo ordenado e inserta el siguiente elemento desplazándolo hacia la izquierda hasta encontrar su posición correcta.

---

### Problema 10

Ejecuta Insertion Sort paso a paso sobre:
[4, 2, 3, 1]

**Solución:**
Insert 2 → [2,4,3,1]
Insert 3 → [2,3,4,1]
Insert 1 → [1,2,3,4]

---

### Problema 11

Explica por qué Insertion Sort es eficiente para arreglos casi ordenados.

**Solución:**
Porque cada elemento se desplaza muy pocas posiciones. El número de swaps es bajo, acercando el tiempo total a Θ(n).

---

### Problema 12

Define formalmente qué es estabilidad en un algoritmo de ordenamiento.

**Solución:**
Un algoritmo es estable si preserva el orden relativo de elementos con claves iguales.

---

### Problema 13

Explica el paradigma divide y vencerás aplicado a Merge Sort.

**Solución:**
Divide el arreglo en mitades, resuelve cada mitad recursivamente y luego combina las soluciones en un solo arreglo ordenado.

---

### Problema 14

Describe detalladamente el proceso de Merge Sort.

**Solución:**
Divide hasta subarreglos de tamaño 1, luego los mezcla comparando elementos de ambas mitades en tiempo lineal.

---

### Problema 15

Plantea la recurrencia de Merge Sort y explica cada término.

**Solución:**
T(n) = 2T(n/2) + Θ(n).
Los términos 2T(n/2) corresponden a ordenar las mitades; Θ(n) al proceso de mezcla.

---

### Problema 16

Resuelve la recurrencia de Merge Sort usando intuición (árbol de recurrencia).

**Solución:**
Cada nivel del árbol cuesta Θ(n) y hay log n niveles, por lo que el total es Θ(n log n).

---

### Problema 17

¿Por qué Merge Sort siempre es Θ(n log n), sin importar la entrada?

**Solución:**
La división y la mezcla ocurren siempre de la misma forma, independientemente del orden inicial de los datos.

---

### Problema 18

Explica por qué Merge Sort no es in-place.

**Solución:**
Necesita arreglos auxiliares para almacenar las mitades durante el proceso de merge.

---

### Problema 19

Compara Selection Sort, Insertion Sort y Merge Sort en un caso práctico.

**Solución:**
Insertion es ideal para pocos datos o casi ordenados, Selection es simple pero ineficiente, Merge es óptimo para grandes volúmenes.

---

### Problema 20

¿Qué algoritmo elegirías para ordenar un millón de datos y por qué?

**Solución:**
Merge Sort, porque garantiza Θ(n log n) incluso en el peor caso.

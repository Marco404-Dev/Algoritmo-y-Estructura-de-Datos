# 20 preguntas (con respuestas) sobre Linear Sorting

1) **¿Qué significa “linear sorting”?**  
**R:** Ordenar en un tiempo que crece proporcionalmente a `n` (cantidad de elementos), o sea cerca de **O(n)**.

2) **¿Por qué los algoritmos por comparación (como QuickSort/MergeSort) no pueden ser O(n) en general?**  
**R:** Porque al basarse en comparaciones existe un límite teórico de **Ω(n log n)** en el peor caso.

3) **¿Qué hace diferente a un “linear sort” frente a un sort por comparación?**  
**R:** Intenta **evitar comparar elemento por elemento**, usando **casilleros (índices)** o **dígitos**.

4) **¿Cuál es la idea principal de Counting Sort?**  
**R:** Contar cuántas veces aparece cada valor y luego reconstruir la lista en orden.

5) **¿Cuándo conviene usar Counting Sort?**  
**R:** Cuando los números son enteros y están en un **rango pequeño** (por ejemplo 0..100).

6) **¿Cuál es el problema de Counting Sort si el rango es enorme?**  
**R:** Necesitas demasiada memoria para el arreglo de conteo (casilleros).

7) **¿Qué significa que un algoritmo de ordenamiento sea “estable” (stable)?**  
**R:** Que si dos elementos tienen la misma clave, se mantiene el **orden original** entre ellos.

8) **¿Counting Sort puede ser estable?**  
**R:** Sí, en su versión estándar (cuando reconstruye usando prefijos/posiciones o mantiene orden al insertar).

9) **¿Qué es Radix Sort en palabras simples?**  
**R:** Un método que ordena números **por dígitos**, paso a paso (unidades, decenas, etc.).

10) **¿Por qué Radix Sort puede ser “casi lineal”?**  
**R:** Porque hace pocas pasadas (`d` pasadas) y cada pasada puede ser O(n). Si `d` es pequeño, queda cerca de O(n).

11) **En Radix Sort, ¿por qué importa que el sub-ordenamiento sea estable?**  
**R:** Porque al ordenar por un dígito, no debe romper el orden ya logrado por los dígitos anteriores.

12) **¿Qué significa LSD Radix Sort?**  
**R:** Ordenar empezando por el dígito **menos significativo** (unidades) hacia el más significativo (decenas, centenas...).

13) **¿Qué significa MSD Radix Sort?**  
**R:** Ordenar empezando por el dígito **más significativo** hacia el menos significativo.

14) **¿Qué tipo de datos se benefician mucho de Radix Sort?**  
**R:** Enteros (32/64 bits) y strings de longitud fija o similar.

15) **¿Qué es “Direct Access Array Sort”?**  
**R:** Poner cada elemento directamente en el índice que corresponde a su clave: `D[clave] = elemento`, luego leer `D` en orden.

16) **¿Por qué Direct Access Array Sort falla con repetidos?**  
**R:** Porque si dos elementos tienen la misma clave, uno sobrescribe al otro si solo guardas un valor por casillero.

17) **¿Cómo se arregla el problema de repetidos en un enfoque de acceso directo?**  
**R:** Guardando una **lista** (o conteo) en cada casillero, como hace Counting Sort.

18) **¿Cuál es el costo típico de Counting Sort en tiempo?**  
**R:** **O(n + k)**, donde `k` es el tamaño del rango (cantidad de posibles valores).

19) **¿Cuál es el costo típico de Radix Sort en tiempo?**  
**R:** **O(d · (n + b))** (simplificado: O(d·n)), donde `d` es el número de dígitos/pasadas y `b` la base.

20) **Dame un ejemplo donde Counting Sort sea perfecto.**  
**R:** Ordenar notas de estudiantes entre 0 y 20, porque el rango es pequeño y se ordena rápido.


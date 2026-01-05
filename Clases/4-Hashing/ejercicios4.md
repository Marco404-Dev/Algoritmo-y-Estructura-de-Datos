# Preguntas y Respuestas – Clase 4: Hashing

1. ¿Por qué los arrays ordenados tienen un límite inferior de Ω(log n) para la operación de búsqueda en el modelo de comparación?

Porque en el modelo de comparación un algoritmo solo puede distinguir elementos comparándolos. Cualquier algoritmo de búsqueda puede representarse como un árbol de decisión binario, donde cada comparación divide el conjunto de posibilidades en dos. Para distinguir entre n elementos, el árbol debe tener al menos n + 1 hojas, lo que implica una altura mínima de Ω(log n). Por ejemplo, la búsqueda binaria en un array ordenado divide el espacio a la mitad en cada paso y alcanza exactamente ese límite.

---

2. ¿Qué es el modelo de comparación y qué tipo de operaciones permite a un algoritmo?

Es un modelo teórico donde los elementos son cajas negras y el algoritmo solo puede compararlos usando operadores como <, > o =. No se permite acceder directamente a los valores ni usar aritmética sobre ellos. Por ejemplo, al buscar un nombre en una lista ordenada, el algoritmo solo puede preguntar si un nombre es menor o mayor que otro, pero no usar su posición en memoria o un valor numérico asociado.

---

3. ¿Cómo se representa un algoritmo de búsqueda mediante un árbol de decisión?

Como un árbol binario donde cada nodo interno representa una comparación y cada rama corresponde al resultado verdadero o falso. Las hojas representan el resultado final del algoritmo. Un recorrido desde la raíz hasta una hoja describe una ejecución concreta del algoritmo para una entrada específica.

---

4. ¿Por qué un árbol de decisión para búsqueda debe tener al menos n + 1 hojas?

Porque al buscar un elemento existen n posibles resultados de éxito (encontrar cada uno de los n elementos) y al menos un resultado de fracaso (el elemento no está). Cada resultado distinto requiere una hoja distinta en el árbol de decisión.

---

5. ¿Qué relación existe entre la altura del árbol de decisión y el tiempo de ejecución en el peor caso?

La altura del árbol corresponde al máximo número de comparaciones que el algoritmo puede realizar. Por lo tanto, el tiempo en el peor caso es al menos la altura del árbol. Si el árbol tiene altura Ω(log n), el algoritmo también tendrá tiempo Ω(log n).

---

6. ¿Por qué no es posible lograr búsquedas más rápidas que Θ(log n) usando solo comparaciones?

Porque cada comparación solo produce dos posibles resultados, lo que limita cuánto se puede reducir el espacio de búsqueda en cada paso. Para lograr tiempos menores, se necesita un modelo más potente que permita mayor ramificación, como el acceso directo por índice que se usa en hashing.

---

7. ¿Qué ventaja ofrece un Direct Access Array frente a un array ordenado?

Permite realizar búsquedas, inserciones y eliminaciones en tiempo O(1) en el peor caso, ya que la clave se usa directamente como índice del array. Por ejemplo, si las claves son números entre 0 y 1000, se puede acceder directamente a la posición correspondiente sin realizar comparaciones.

---

8. ¿Cuál es el principal problema de espacio del Direct Access Array cuando el universo de claves es grande?

El espacio requerido es O(u), donde u es el tamaño del universo de claves. Si u es muy grande y solo se usan pocos elementos, se desperdicia mucha memoria. Por ejemplo, almacenar nombres de 10 letras requeriría un array de tamaño 26¹⁰, lo cual es impracticable.

---

9. ¿Qué es una función hash y cuál es su propósito principal?

Es una función que transforma una clave de un universo grande en un índice dentro de un rango pequeño. Su propósito es permitir acceso rápido a los datos usando menos espacio que un Direct Access Array.

---

10. ¿Por qué las colisiones son inevitables en las tablas hash?

Porque se mapean muchas claves posibles a un número menor de posiciones en la tabla. Por el principio del palomar, al menos dos claves distintas deben compartir la misma posición.

---

11. ¿Qué es el método de chaining (encadenamiento) para manejar colisiones?

Es una técnica donde cada posición de la tabla hash almacena una estructura auxiliar, como una lista enlazada, que guarda todos los elementos que colisionan en esa posición. Por ejemplo, si varias claves producen el mismo hash, se almacenan juntas en la misma lista.

---

12. ¿Bajo qué condición el método de chaining permite operaciones en tiempo O(1) esperado?

Cuando las claves se distribuyen uniformemente y el factor de carga α = n / m se mantiene constante. En ese caso, el tamaño esperado de cada cadena es O(1).

---

13. ¿Qué ocurre si se utiliza una función hash deficiente, como una constante?

Todas las claves se mapearían a la misma posición de la tabla, generando una sola cadena de tamaño Θ(n). En ese caso, las operaciones pasan a costar Θ(n), perdiendo toda la ventaja del hashing.

---

14. ¿En qué consiste la función hash por división y por qué se considera heurística?

Consiste en calcular h(k) = k mod m. Se considera heurística porque funciona bien en la práctica solo si las claves no presentan patrones y m se elige cuidadosamente. No ofrece garantías teóricas contra entradas adversas.

---

15. ¿Por qué se recomienda elegir m como un número primo y no cercano a potencias de 2 o 10?

Porque muchos conjuntos de claves tienen patrones relacionados con esas potencias. Usar un primo ayuda a distribuir mejor las claves y reduce colisiones sistemáticas. Por ejemplo, si las claves terminan en ceros, un m múltiplo de 10 produciría muchas colisiones.

---

16. ¿Qué es el hashing universal y qué problema busca resolver?

Es una técnica donde la función hash se elige aleatoriamente de una familia de funciones. Busca evitar que un conjunto específico de claves provoque muchas colisiones, incluso en el peor caso.

---

17. ¿Cómo se define la familia de funciones hash universales h_ab(k)?

Se define como h_ab(k) = ((a · k + b) mod p) mod m, donde p es un primo mayor que el universo de claves, y a y b se eligen aleatoriamente con a ≠ 0.

---

18. ¿Qué significa que una familia de funciones hash sea universal?

Significa que para cualquier par de claves distintas, la probabilidad de que colisionen es como máximo 1/m. Esto garantiza cadenas cortas en expectativa.

---

19. ¿Qué es el factor de carga α y cómo influye en el rendimiento de una tabla hash?

Es la razón entre el número de elementos n y el tamaño de la tabla m. Si α es constante, las operaciones son O(1) esperado. Si α crece demasiado, las cadenas se alargan y el rendimiento empeora.

---

20. ¿Por qué las tablas hash permiten operaciones en O(1) esperado amortizado pero no soportan eficientemente operaciones de orden como min, max o next?

Porque las tablas hash no mantienen los elementos ordenados. Para encontrar el mínimo o el siguiente elemento, sería necesario recorrer toda la tabla o todas las cadenas, lo que cuesta O(n).


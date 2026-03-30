---

## 9. Sorted Array como estructura Set

La recitación no solo habla de ordenar, sino de **por qué ordenar sirve para implementar un Set**.

Si los elementos están en un arreglo ordenado por clave:

* **find(k)** se puede hacer con **búsqueda binaria**
* **find_min()** devuelve el primer elemento
* **find_max()** devuelve el último elemento
* **find_next(k)** y **find_prev(k)** también se pueden resolver con búsqueda binaria

### Costos importantes

| Estructura     | build(X)      | find(k)   | insert(x) | delete(k) | find_min / find_max | find_prev / find_next |
| -------------- | ------------- | --------- | --------- | --------- | ------------------- | --------------------- |
| Array          | Θ(n)          | Θ(n)      | Θ(n)      | Θ(n)      | Θ(n)                | Θ(n)                  |
| Sorted Array   | Θ(n log n)    | Θ(log n)  | Θ(n)      | Θ(n)      | Θ(1)                | Θ(log n)              |

### Idea clave

Ordenar el arreglo **mejora mucho las búsquedas y consultas de orden**, pero **insertar y eliminar sigue costando Θ(n)** porque hay que mover elementos.

---

## 10. Preprocessing

Una idea importante de la recitación es el **preprocessing**.

Consiste en gastar más tiempo al inicio para dejar la estructura preparada y luego responder operaciones más rápido.

En este caso:

* construir un array normal: más barato al inicio
* construir un **sorted array**: más caro al inicio
* beneficio: luego `find`, `min`, `max`, `prev`, `next` son más rápidos

### Intuición

Pagas una vez el costo de ordenar para ahorrar tiempo después.

---

## 11. Diferencia fina entre Selection Sort e Insertion Sort

Ambos son algoritmos incrementales, pero **no construyen el orden de la misma manera**.

### Selection Sort

Mantiene ordenado el conjunto de los **mayores i elementos**.

Idea:

* busca el mayor del prefijo
* lo manda al final
* repite

### Insertion Sort

Mantiene ordenados los **primeros i elementos del arreglo original**.

Idea:

* asume que el prefijo ya está ordenado
* toma el siguiente elemento
* lo inserta en su posición correcta moviéndolo hacia la izquierda

### Diferencia conceptual

* **Selection sort**: selecciona el elemento correcto para la posición final
* **Insertion sort**: inserta el nuevo elemento dentro de una parte ya ordenada

---

## 12. Estabilidad e In-place

### In-place

Un algoritmo es **in-place** si usa solo **O(1)** espacio extra.

* Selection sort: ✅
* Insertion sort: ✅
* Merge sort clásico: ❌, porque usa arreglos auxiliares

### Estabilidad

Un algoritmo es **estable** si elementos con la misma clave conservan su orden relativo original.

* Selection sort: ❌
* Insertion sort: ✅
* Merge sort: depende de cómo se rompan empates durante el merge

### Observación importante

En la recitación se menciona que la versión mostrada de **merge sort no necesariamente es estable**; puede hacerse estable con una pequeña modificación en el criterio de empate.

---

## 13. Sobre los swaps

No siempre basta mirar solo comparaciones.

### Selection Sort

* puede hacer muchas comparaciones
* pero hace **a lo mucho O(n) swaps**

### Insertion Sort

* en el peor caso puede hacer **Θ(n²) comparaciones**
* y también **Θ(n²) swaps**

Esto ayuda a entender por qué a veces selection sort mueve menos datos, aunque siga siendo lento en tiempo total.

---

## 14. Merge Sort explicado mejor

### Idea general

1. dividir el arreglo en dos mitades
2. ordenar recursivamente cada mitad
3. mezclar ambas mitades ya ordenadas en tiempo lineal

### Por qué el merge cuesta Θ(n)

Porque en la fase de mezcla cada elemento se copia/ubica una sola vez.

### Recurrencia

```text
T(n) = 2T(n/2) + Θ(n)

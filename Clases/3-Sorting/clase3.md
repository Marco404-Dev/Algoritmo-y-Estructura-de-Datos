# Clase 3 – Sorting (Ordenamiento)

## 1. Motivación

Ordenar es una operación fundamental porque permite:

* Búsquedas más rápidas (búsqueda binaria: **O(log n)**)
* Encontrar mínimo y máximo en **O(1)**
* Implementar estructuras tipo **Set** de forma eficiente

---

## 2. Problema de Ordenamiento

**Entrada:** arreglo A de n elementos

**Salida:** arreglo B que es una **permutación ordenada** de A

**Propiedades:**

* Permutación: mismos elementos, distinto orden
* Ordenado: B[i-1] ≤ B[i]

Ejemplo:

```
[8, 2, 4, 9, 3] → [2, 3, 4, 8, 9]
```

### Tipos de sort

* **Destructivo:** modifica el arreglo original
* **In-place:** usa O(1) espacio extra (todo in-place es destructivo)

---

## 3. Permutation Sort (Fuerza Bruta)

Idea:

* Probar todas las permutaciones
* Verificar cuál está ordenada

Complejidad:

* Número de permutaciones: n!
* Verificar orden: Θ(n)

⏱️ **Tiempo:** Ω(n! · n) → impracticable

✔️ Correcto, ❌ ineficiente

---

## 4. Selection Sort

Idea:

* Buscar el máximo
* Colocarlo al final
* Repetir con el prefijo restante

Ejemplo:

```
[8,2,4,9,3]
→ [8,2,4,3,9]
→ [3,2,4,8,9]
→ [2,3,4,8,9]
```

Características:

* In-place
* No estable

⏱️ **Complejidad:**

* Mejor, promedio y peor caso: **Θ(n²)**

---

## 5. Insertion Sort

Idea:

* Mantener un prefijo ordenado
* Insertar el siguiente elemento en su posición correcta

Ejemplo:

```
[8,2,4,9,3]
→ [2,8,4,9,3]
→ [2,4,8,9,3]
→ [2,3,4,8,9]
```

Características:

* In-place
* Estable
* Muy eficiente para arreglos casi ordenados

⏱️ **Complejidad:**

* Peor caso: Θ(n²)
* Mejor caso (ya ordenado): Θ(n)

---

## 6. Merge Sort

Idea:

1. Dividir el arreglo en mitades
2. Ordenar cada mitad recursivamente
3. Mezclar (merge) las mitades ordenadas

Ejemplo:

```
[7,1,5,6,2,4,9,3]
→ dividir
→ ordenar
→ merge
→ [1,2,3,4,5,6,7,9]
```

Características:

* No in-place (usa memoria extra)
* Estable
* Muy eficiente

⏱️ **Complejidad:**

* Todos los casos: **Θ(n log n)**

Recurrencia:

```
T(n) = 2T(n/2) + Θ(n)
```

---

## 7. Comparación de Algoritmos

| Algoritmo        | Tiempo       | Espacio | Estable | In-place |
| ---------------- | ------------ | ------- | ------- | -------- |
| Permutation Sort | n!           | alto    | —       | ❌        |
| Selection Sort   | Θ(n²)        | O(1)    | ❌       | ✅        |
| Insertion Sort   | Θ(n²) / Θ(n) | O(1)    | ✅       | ✅        |
| Merge Sort       | Θ(n log n)   | O(n)    | ✅       | ❌        |

---

## 8. Ideas Clave para Examen

* Θ(n²) vs Θ(n log n)
* Estabilidad importa cuando hay claves repetidas
* Merge sort es óptimo para grandes volúmenes
* Insertion sort es ideal para datos casi ordenados

---

👉 Siguiente clase natural: **Quick Sort y Lower Bounds del Sorting**

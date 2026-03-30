# Clase 3 – Sorting (Ordenamiento)

## 1. Motivación

El ordenamiento es una operación fundamental en algoritmos y estructuras de datos, porque tener los elementos en orden permite responder consultas de forma mucho más eficiente.

Cuando un arreglo está ordenado, se obtienen ventajas importantes:

- Se puede buscar un elemento con **búsqueda binaria** en **O(log n)**
- El mínimo se encuentra directamente al inicio
- El máximo se encuentra directamente al final
- Es más fácil implementar operaciones de orden como:
  - `find_min()`
  - `find_max()`
  - `find_next(k)`
  - `find_prev(k)`

Además, ordenar no solo sirve para “acomodar datos”, sino también para construir estructuras más eficientes, como un **Set implementado con un arreglo ordenado**.

---

## 2. Problema de Ordenamiento

El problema de ordenamiento consiste en reorganizar los elementos de una colección para que queden en orden creciente.

### Entrada

Un arreglo `A` de `n` elementos.

### Salida

Un arreglo `B` que sea una **permutación ordenada** de `A`.

### Propiedades importantes

- **Permutación:** `B` contiene exactamente los mismos elementos que `A`, solo que en otro orden.
- **Ordenado:** para todo índice válido, se cumple:

```text
B[i - 1] ≤ B[i]
```

### Ejemplo

```text
[8, 2, 4, 9, 3] → [2, 3, 4, 8, 9]
```

### Tipos de ordenamiento

#### Destructivo

El algoritmo modifica directamente el arreglo original.

#### In-place

El algoritmo utiliza solo `O(1)` espacio extra.

Todo algoritmo **in-place** es destructivo, pero no todo algoritmo destructivo es **in-place**.

---

## 3. Permutation Sort (Fuerza Bruta)

Permutation Sort es la forma más ingenua y extrema de resolver el problema.

### Idea

- Generar todas las permutaciones posibles del arreglo
- Revisar cuál de ellas está ordenada
- Devolver la primera que cumpla la condición

### Intuición

Si entre todas las permutaciones posibles hay al menos una ordenada, entonces probarlas todas garantiza encontrarla.

### Ejemplo conceptual

Para:

```text
[2, 3, 1]
```

Se revisan todas sus permutaciones:

```text
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]
```

Y se elige la que está ordenada.

### Complejidad

- Número de permutaciones: `n!`
- Verificar si una permutación está ordenada: `Θ(n)`

### Tiempo total

```text
Ω(n! · n)
```

### Conclusión

- Sí funciona
- Sí es correcto
- No es práctico

Es un algoritmo de fuerza bruta, útil solo para entender el problema, no para resolverlo eficientemente.

---

## 4. Selection Sort

Selection Sort construye el arreglo ordenado colocando, en cada paso, el elemento correcto en su posición final.

### Idea

- Buscar el elemento más grande del prefijo no ordenado
- Colocarlo al final mediante un intercambio
- Repetir el proceso con la parte restante

### Ejemplo

```text
[8,2,4,9,3]
→ [8,2,4,3,9]
→ [3,2,4,8,9]
→ [2,3,4,8,9]
```

### Cómo piensa este algoritmo

En cada iteración responde esta pregunta:

> ¿Cuál es el mayor elemento que todavía no ha sido colocado?

Luego lo mueve a su posición final.

### Características

- **In-place:** sí
- **Destructivo:** sí
- **Estable:** no

No es estable porque al intercambiar elementos puede alterar el orden relativo de elementos con la misma clave.

### Complejidad

- Comparaciones: `Θ(n²)`
- Mejor caso: `Θ(n²)`
- Caso promedio: `Θ(n²)`
- Peor caso: `Θ(n²)`

### Observación importante

Aunque hace muchos recorridos, realiza relativamente pocos intercambios en comparación con otros algoritmos cuadráticos.

---

## 5. Insertion Sort

Insertion Sort construye el arreglo ordenado de manera progresiva, manteniendo un prefijo ya ordenado e insertando cada nuevo elemento en la posición que le corresponde.

### Idea

- Asumir que la primera parte del arreglo ya está ordenada
- Tomar el siguiente elemento
- Moverlo hacia la izquierda hasta insertarlo correctamente

### Ejemplo

```text
[8,2,4,9,3]
→ [2,8,4,9,3]
→ [2,4,8,9,3]
→ [2,4,8,9,3]
→ [2,3,4,8,9]
```

### Cómo piensa este algoritmo

En cada paso responde:

> ¿Si el prefijo ya está ordenado, dónde debe colocarse el nuevo elemento para conservar ese orden?

### Características

- **In-place:** sí
- **Destructivo:** sí
- **Estable:** sí

Es estable porque, al insertar, no altera innecesariamente el orden relativo de elementos iguales.

### Complejidad

- Peor caso: `Θ(n²)`
- Caso promedio: `Θ(n²)`
- Mejor caso: `Θ(n)`

### ¿Cuándo es bueno?

Insertion Sort destaca cuando:

- el arreglo es pequeño
- el arreglo ya está casi ordenado
- se busca una solución simple de implementar

---

## 6. Merge Sort

Merge Sort es un algoritmo recursivo basado en la técnica de divide y vencerás.

### Idea general

- Dividir el arreglo en dos mitades
- Ordenar recursivamente cada mitad
- Mezclar ambas mitades ordenadas en una sola lista ordenada

### Ejemplo

```text
[7,1,5,6,2,4,9,3]
→ dividir
→ ordenar cada mitad
→ merge
→ [1,2,3,4,5,6,7,9]
```

### Fase clave: merge

La parte más importante del algoritmo es la mezcla de dos subarreglos ya ordenados.

Si ambas mitades ya están ordenadas, pueden combinarse en tiempo lineal comparando sus elementos y colocando siempre el menor en la posición correcta.

### Características

- **In-place:** no
- **Destructivo:** sí, en la versión usual
- **Estable:** normalmente sí, dependiendo de cómo se manejen empates
- Muy eficiente para arreglos grandes

### Complejidad

- Mejor caso: `Θ(n log n)`
- Caso promedio: `Θ(n log n)`
- Peor caso: `Θ(n log n)`

### Recurrencia

```text
T(n) = 2T(n/2) + Θ(n)
```

### Intuición de su eficiencia

- El arreglo se divide en `log n` niveles
- En cada nivel, el costo total de mezclar sigue siendo `Θ(n)`

Por eso el tiempo total es:

```text
Θ(n log n)
```

---

## 7. Comparación de Algoritmos

| Algoritmo | Tiempo | Espacio | Estable | In-place | Idea principal |
|---|---|---|---|---|---|
| Permutation Sort | `Ω(n! · n)` | Muy alto | — | ❌ | Probar todas las permutaciones |
| Selection Sort | `Θ(n²)` | `O(1)` | ❌ | ✅ | Seleccionar el máximo y colocarlo al final |
| Insertion Sort | `Θ(n²)` / mejor caso `Θ(n)` | `O(1)` | ✅ | ✅ | Insertar cada elemento en un prefijo ordenado |
| Merge Sort | `Θ(n log n)` | `O(n)` | ✅* | ❌ | Dividir, ordenar y mezclar |

\* Merge Sort puede depender de la implementación del merge para conservar estabilidad.

### Lectura rápida de la tabla

- **Permutation Sort:** correcto pero inutilizable en la práctica.
- **Selection Sort:** simple, pero lento.
- **Insertion Sort:** también cuadrático, pero mejor cuando los datos están casi ordenados.
- **Merge Sort:** el más sólido de estos para grandes volúmenes.

---

## 8. Ideas Clave para Examen

Estas son las ideas que más conviene dominar:

### 1. Ordenar mejora estructuras

Un arreglo ordenado permite búsquedas más rápidas y operaciones de orden más eficientes.

### 2. No todo algoritmo correcto es útil

Permutation Sort es correcto, pero su costo es tan grande que no sirve en la práctica.

### 3. Selection Sort e Insertion Sort son cuadráticos

Ambos suelen costar `Θ(n²)`, aunque su lógica es distinta:

- **Selection Sort** selecciona el elemento correcto para una posición final.
- **Insertion Sort** inserta el nuevo elemento en una parte ya ordenada.

### 4. Insertion Sort puede ser mejor en arreglos casi ordenados

En ese caso puede acercarse a `Θ(n)`.

### 5. Merge Sort es mucho más eficiente

Su complejidad `Θ(n log n)` lo hace muy superior para arreglos grandes.

### 6. Estabilidad sí importa

Si hay claves repetidas, un algoritmo estable conserva el orden relativo original de esos elementos.

### 7. In-place y espacio extra no son lo mismo

Un algoritmo puede ser rápido pero requerir memoria adicional, como Merge Sort.

### 8. La recurrencia de Merge Sort es fundamental

Debes reconocer y saber interpretar:

```text
T(n) = 2T(n/2) + Θ(n)
```

porque explica por qué Merge Sort cuesta `Θ(n log n)`.


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

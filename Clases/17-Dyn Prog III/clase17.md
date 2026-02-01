# Clase 17 (Dyn. Prog. III) — Explicación desde cero (simple)

La idea principal de esta clase es:

> **DP cuando el subproblema “normal” NO alcanza, entonces le agregas un estado extra**  
> (otra dimensión o más información) para que el DP sea correcto y no tenga ciclos.

---

## 1) Bellman-Ford visto como DP (caminos más cortos)

### Problema
Distancia más corta desde un nodo `s` a un nodo `v` en un grafo con pesos.

### Por qué “dist[v]” no es suficiente como DP
Porque un camino puede usar muchas aristas y puede haber ciclos.  
Para DP necesitas algo que siempre vaya hacia “más pequeño”.

### Truco de la clase: agregar `k`
Define:

**dp[k][v] = costo mínimo para llegar a `v` usando como máximo `k` aristas.**

Ahora sí es DP porque:
- `dp[k][v]` depende solo de `dp[k-1][...]` (más pequeño)

### Idea de transición
Para llegar a `v` con ≤ k aristas:
- o ya llegabas con ≤ k−1 aristas, o
- llegas desde algún `u` con una última arista `u→v`

**Esto es exactamente Bellman-Ford** (relajar aristas repetidamente).

**Idea clave:** Bellman-Ford = DP por “número de aristas”.

---

## 2) Floyd–Warshall como DP (all-pairs shortest paths)

### Problema
Distancia mínima entre **todos los pares** `u → v`.

### Truco: agregar `k` con otro significado
Define:

**dp[u][v][k] = mejor distancia de u a v usando solo vértices intermedios del 1..k.**

### Decisión
El vértice `k`:
- o **no se usa**: dp[u][v][k−1]
- o **sí se usa**: u→k y k→v  
  dp[u][k][k−1] + dp[k][v][k−1]

**Idea clave:** Floyd–Warshall = DP donde decides si permites usar `k` como intermedio o no.

---

## 3) Parenthesization (poner paréntesis para maximizar)

### Problema
Tienes una expresión con `+` y `*` y quieres poner paréntesis para que el resultado sea **máximo**.

### Por qué “solo máximo” NO alcanza
Si hay negativos:
- un mínimo por un mínimo puede dar un máximo (negativo × negativo = positivo)

### Truco: guardar 2 cosas por subproblema
- dpMax[i][j] = máximo valor del segmento i..j
- dpMin[i][j] = mínimo valor del segmento i..j

**Idea clave:** a veces DP necesita guardar más información (min y max).

---

## 4) Piano Fingering (asignación de dedos) como DP

### Problema
Asignar dedos (1..F) a una secuencia de notas para minimizar el costo de moverse.

### Por qué falta info si solo usas `i`
Si dices “costo mínimo desde i”, falta:
- ¿con qué dedo empiezo en la nota i?

### Truco: expandir con el dedo
Define:

**dp[i][f] = costo mínimo desde la nota i hasta el final si en la nota i uso el dedo f.**

Luego pruebas el dedo `f'` de la siguiente nota y eliges el mejor.

**Idea clave:** DP con estado extra = (posición i) + (condición necesaria: dedo).

---

# La idea única que une toda la clase 17
Si un DP “normal” no funciona o no alcanza información:

✅ **Expandes el subproblema** agregando un parámetro o guardando más datos.

Ejemplos:
- Bellman-Ford: agregas `k` (máx aristas)
- Floyd–Warshall: agregas `k` (intermedios permitidos)
- Parenthesization: guardas `min` y `max`
- Piano: agregas `f` (dedo)

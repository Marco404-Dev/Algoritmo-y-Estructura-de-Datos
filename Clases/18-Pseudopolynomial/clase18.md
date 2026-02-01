# Clase 18 — Pseudopolynomial (Explicación desde cero)

## 1) ¿De qué trata “Pseudopolynomial”?
Trata de **cómo medir el tiempo de un algoritmo cuando hay números grandes** en la entrada.

Idea clave:

✅ **No es lo mismo “el número vale T” que “cuánto ocupa T en la entrada”.**

- Un número grande (ej. `T = 1,000,000`) no se escribe con un millón de símbolos.
- Se escribe con **pocos dígitos** (o pocos bits).
- Ejemplo: “1000000” tiene **7 dígitos**.
- En bits, el tamaño crece como `log2(T)`.

Entonces:
- Un algoritmo que tarda **O(T)** puede ser muy lento, aunque el input sea “corto” (porque T está escrito en pocos dígitos).

---

## 2) ¿Qué significa “tiempo pseudopolinomial”?
Un algoritmo es **pseudopolinomial** cuando:

> Su tiempo depende de **T** (el valor numérico), no de **log(T)** (el tamaño real en la entrada).

Ejemplo típico de DP:
- **O(n·T)**

Eso parece “polinomial” (porque es n por T), pero puede ser enorme si T es gigante.

---

## 3) Ejemplo súper simple para entenderlo

### Caso A: algoritmo “bueno” (depende de log(T))
Tiempo:
- **O(n · log(T))**

Si `T = 1,000,000`:
- `log2(T) ≈ 20`
Entonces tiempo ≈ `n·20` → razonable.

### Caso B: pseudopolinomial (depende de T)
Tiempo:
- **O(n · T)**

Si `T = 1,000,000`:
- tiempo ≈ `n·1,000,000` → enorme.

📌 La diferencia:
- `log(T)` crece lento
- `T` crece muy rápido

---

## 4) Problema típico: Subset Sum
Problema:
- tienes números `a1, a2, ..., an`
- tienes un objetivo **T**
- ¿existe un subconjunto que sume exactamente T?

DP típico:
- Tabla de tamaño `n × T`
- Tiempo: **O(n·T)**

➡️ Eso es **pseudopolinomial** porque depende de **T**.

✅ Si T es grande, el DP explota.

---

## 5) Regla para examen (la que no falla)
Si el DP tiene una dimensión como `T`, `W`, `L` y el tiempo sale así:
- `O(n·T)`
- `O(n·W)`
- `O(L²)`

Pregunta:

➡️ **¿Ese número (T/W/L) puede ser grande y está escrito en pocos bits?**

- Si sí → **pseudopolinomial**
- Si no (o el input incluye explícitamente un arreglo largo de tamaño L, etc.) → puede contarse como polinomial en ese modelo

En la mayoría de cursos:
✅ `O(n·T)` (Subset Sum, Knapsack por capacidad) = **pseudopolinomial**.

---

## 6) Resumen en 2 líneas
- **Polinomial real:** depende del tamaño de entrada en bits, como `log(T)`.
- **Pseudopolinomial:** depende del valor numérico `T` directamente.

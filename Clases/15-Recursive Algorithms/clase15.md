# Recursión y Programación Dinámica (DP) — Explicación desde cero

## 1) Idea central
Muchos problemas se resuelven así:
1. Tomo un problema **grande**
2. Lo convierto en problemas **más pequeños**
3. Resuelvo los pequeños
4. **Combino** para obtener la respuesta del grande

Esto es la base de **recursión** y de **programación dinámica (DP)**.

---

## 2) ¿Qué es recursión?
Una función recursiva:
- se llama a sí misma
- cada llamada resuelve una versión **más pequeña** del problema
- se detiene con un **caso base**

Ejemplo mental (contar hacia atrás):
- imprimir(3) → imprime 3 y llama imprimir(2)
- imprimir(2) → imprime 2 y llama imprimir(1)
- imprimir(1) → imprime 1 y llama imprimir(0)
- imprimir(0) → se detiene (caso base)

Sin caso base, la recursión no termina.

---

## 3) ¿Qué es un subproblema?
Subproblema = “la misma pregunta, pero más pequeña”.

Ejemplo (Fibonacci):
- problema grande: F(6)
- subproblemas: F(5) y F(4)

---

## 4) ¿Qué es Programación Dinámica (DP)?
DP aparece cuando la recursión calcula **lo mismo** muchas veces.

DP = recursión + memoria (guardar resultados de subproblemas)

Si ya resolviste un subproblema, lo reutilizas.

---

## 5) Ejemplo clave: Fibonacci
Definición:
- F(0)=0
- F(1)=1
- F(n)=F(n−1)+F(n−2)

Problema de la recursión ingenua:
- F(5) llama a F(4) y F(3)
- F(4) vuelve a llamar a F(3)
=> F(3) se repite, F(2) se repite más, etc.

DP lo arregla guardando resultados para no recalcular.

---

## 6) Dos formas de DP

A) Top-Down (Memoization)
- Es recursión, pero con una tabla memo.
- Si memo[n] ya está, lo devuelves.
- Si no, lo calculas, guardas y devuelves.

B) Bottom-Up (Tabulation)
- No recursión.
- Calculas desde los casos base hacia arriba.

---

## 7) ¿Qué es “orden topológico”?
Es un orden para resolver subproblemas donde:
- siempre calculas primero lo que se necesita antes

Ejemplo Fibonacci:
F(0), F(1), F(2), F(3), F(4), F(5), ...

En grafos DAG:
si hay una flecha u → v, entonces u debe resolverse antes que v.

---

## 8) ¿Por qué Merge Sort NO es DP?
Merge sort es recursivo, pero:
- divide en mitades distintas
- cada subarreglo se procesa una sola vez
- no hay subproblemas repetidos por rutas distintas

Entonces:
- recursión con repetición => DP
- recursión sin repetición => Divide & Conquer (merge sort)

---

## 9) Cómo inventar DP (receta práctica)
1) Estado: define DP[i] (qué significa exacto)
2) Decisiones: qué opciones tengo desde i
3) Transición: cada decisión me manda a un subproblema más pequeño
4) Max/Min: elijo la mejor opción
5) Bases: casos simples
6) Respuesta: el estado inicial

---

## 11) Resumen en 3 líneas
- Recursión: problema grande => subproblemas + caso base
- DP: cuando subproblemas se repiten, guardas resultados
- Orden topológico: orden correcto para resolver sin depender del “futuro”



# Recursión vs Programación Dinámica (DP) 

## 1) Recursión vs DP: no son lo mismo
- **Recursión** = cómo escribes el código: una función se llama a sí misma.
- **DP (Programación Dinámica)** = cómo diseñas la solución: subproblemas + guardar resultados para no repetir.

Por eso:
- Puedes tener **recursión sin DP** (Fibonacci ingenuo).
- Puedes tener **DP con recursión** (memoization / top-down).
- Puedes tener **DP sin recursión** (tabulation / bottom-up).

---

- **Ingenuo:** divide, pero **repite** subproblemas.
- **Memo (recursivo):** divide y **guarda** para no repetir.
- **Bottom-up (iterativo):** también usa subproblemas, pero en vez de llamar funciones, **los calcula en orden** con un bucle.



```text
https://colab.research.google.com/drive/1mEUS4CcBYsAmitBMJHj33GwFfsrq9u7L#scrollTo=zMRMW894kkH2
```

# Fibonacci: 3 formas de resolver (NO DP vs DP)

Aunque las 3 se “llaman como función” (ej. `fib(x)`), **no hacen lo mismo por dentro**.  
La diferencia real es: **si repiten subproblemas o no**.

---

## 1) Recursión ingenua (NO DP) ❌
### Cómo funciona
- La función se llama a sí misma **dos veces** por cada `n`:
  - `fib(n-1)` y `fib(n-2)`
- Eso hace que se repitan subproblemas muchas veces.

### Consecuencia
- Recalcula `fib(k)` una y otra vez.
- Se vuelve muy lento cuando `n` crece.

### Complejidad
- **Tiempo:** `O(2^n)` (exponencial)
- **Memoria (pila de recursión):** `O(n)`

---

## 2) DP Top-Down (Memoization) ✅ (recursión + guardar)
### Cómo funciona
- También es recursivo.
- Antes de calcular, revisa:
  - “¿ya calculé `fib(n)`?”
- Si ya está en `memo`, lo devuelve sin recalcular.

### Consecuencia
- Cada `fib(k)` se calcula **una sola vez**.
- Mucho más rápido.

### Complejidad
- **Tiempo:** `O(n)`
- **Memoria:** `O(n)` por `memo` + `O(n)` por la pila de recursión

---

## 3) DP Bottom-Up (Tabulation) ✅ (tabla + bucle)
### Cómo funciona
- No usa recursión.
- Calcula en orden:
  - `F[0], F[1], F[2], ... , F[n]`
- Cada `F[i]` se calcula **una sola vez** en un `for`.

### Consecuencia
- Rápido y estable (no hay límite de recursión).
- Ideal para `n` grande.

### Complejidad
- **Tiempo:** `O(n)`
- **Memoria:** `O(n)` si guardas la lista `F`  
  (se puede reducir a `O(1)` usando solo 2 variables)

---

## Comparación directa (para examen)

| Método | ¿Recursivo? | ¿Guarda resultados? | ¿Repite subproblemas? | Tiempo |
|-------|-------------|---------------------|------------------------|--------|
| Ingenuo | Sí | No | Sí (mucho) | `O(2^n)` |
| Top-Down | Sí | Sí (`memo`) | No | `O(n)` |
| Bottom-Up | No | Sí (tabla `F`) | No | `O(n)` |

---

## Idea clave
  **DP = no repetir subproblemas** (porque guardas resultados o llenas una tabla).  
Recursión es solo una forma de programar, DP es el método.

  **Recursiva = si se invoca a si mismo dentro de su propia definicion** 






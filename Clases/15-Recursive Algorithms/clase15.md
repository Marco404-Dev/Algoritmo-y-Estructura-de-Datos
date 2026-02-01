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

Pseudocódigo Top-Down (memoization) — Fibonacci:
fib(n):
  si n <= 1: return n
  si memo[n] existe: return memo[n]
  memo[n] = fib(n-1) + fib(n-2)
  return memo[n]

B) Bottom-Up (Tabulation)
- No recursión.
- Calculas desde los casos base hacia arriba.

Pseudocódigo Bottom-Up (tabulation) — Fibonacci:
F[0] = 0
F[1] = 1
para i = 2..n:
  F[i] = F[i-1] + F[i-2]
return F[n]

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

## 10) Mini-ejemplo tipo Bowling (DP en arreglo)
Problema: máximo puntaje sin usar elementos adyacentes.

Valores: v = [2, 7, 9, 3]

Defino:
M(i) = máximo desde i hasta el final

Decisiones:
- no tomar i => M(i+1)
- tomar i => v[i] + M(i+2)

Transición:
M(i) = max( M(i+1), v[i] + M(i+2) )

Bases:
M(n) = 0
M(n+1) = 0

Respuesta:
M(0)

---

## 11) Resumen en 3 líneas
- Recursión: problema grande => subproblemas + caso base
- DP: cuando subproblemas se repiten, guardas resultados
- Orden topológico: orden correcto para resolver sin depender del “futuro”

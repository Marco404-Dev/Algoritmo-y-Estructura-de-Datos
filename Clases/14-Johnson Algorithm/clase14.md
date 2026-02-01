# Johnson’s Algorithm (APSP) — explicado simple (clase 14)

Este PDF es **Lecture 14: Johnson’s Algorithm** (MIT 6.006). :contentReference[oaicite:0]{index=0}

## 1) ¿Qué problema resuelve?
**APSP (All-Pairs Shortest Paths)**:
- Input: grafo dirigido con pesos (pueden ser negativos)
- Output: **δ(u,v)** para todos los pares `u,v`
- Si hay **ciclo negativo**, se aborta. :contentReference[oaicite:1]{index=1}

Hacer SSSP |V| veces funciona, pero:
- Con **Bellman-Ford** sería |V| · O(|V||E|) = muy lento
- Johnson logra APSP en **|V| · (Dijkstra)** aun con pesos negativos (si no hay ciclo negativo). :contentReference[oaicite:2]{index=2}

---

## 2) Idea en una frase
👉 **Convierte el grafo con pesos negativos a otro grafo equivalente con pesos NO negativos**, y ahí sí puedes correr **Dijkstra** desde cada nodo. :contentReference[oaicite:3]{index=3}

---

## 3) El truco: “reweighting” con potenciales
Se define una función potencial:
- **h: V → Z** (asigna un número a cada nodo)

Y se cambian los pesos así:
- **w'(u,v) = w(u,v) + h(u) − h(v)** :contentReference[oaicite:4]{index=4}

### ¿Por qué esto NO cambia cuál camino es el más corto?
Porque para cualquier camino de `v0` a `vk`, su costo cambia en:
- **+ h(v0) − h(vk)** (una constante para ese par origen-destino) :contentReference[oaicite:5]{index=5}

Entonces:
- si un camino era el más corto antes, sigue siendo el más corto después.

---

## 4) ¿Cómo elijo h para que todos los w' sean ≥ 0?
Queremos:
- w(u,v) + h(u) − h(v) ≥ 0  
equivalente a:
- **h(v) ≤ h(u) + w(u,v)** (tipo “desigualdad triangular”) :contentReference[oaicite:6]{index=6}

La idea del PDF:
- si tomas **h(v) = δ(s,v)** (distancia desde un nodo s), esa desigualdad se cumple.
Pero puede que no exista un `s` que llegue a todos (grafo desconectado).

✅ Solución:
- Agrega un nuevo nodo **x** con aristas de peso 0 a todos los nodos:
  - x → v con peso 0 para todo v ∈ V :contentReference[oaicite:7]{index=7}

Así:
- x llega a todos, entonces δ(x,v) existe (o detectas ciclo negativo).

---

## 5) Algoritmo Johnson (paso a paso)
1) Construir **Gx**:
- agrega nodo nuevo `x`
- agrega aristas `x→v` con peso 0 a cada `v`. :contentReference[oaicite:8]{index=8}

2) Corre **Bellman-Ford** desde `x` en Gx:
- obtén **h(v) = δx(x,v)** para todo v. :contentReference[oaicite:9]{index=9}
- si para algún v sale **−∞**, aborta: hay **ciclo negativo** en G. :contentReference[oaicite:10]{index=10}

3) Repondera el grafo:
- para cada arista (u,v):
  - **w'(u,v) = w(u,v) + h(u) − h(v)** :contentReference[oaicite:11]{index=11}
Con eso, el PDF afirma que ahora **todas las aristas quedan no negativas**. :contentReference[oaicite:12]{index=12}

4) Corre **Dijkstra** desde cada nodo `u` en el grafo reponderado:
- obtienes **δ'(u,v)** para todo v. :contentReference[oaicite:13]{index=13}

5) Regresa al peso original:
- **δ(u,v) = δ'(u,v) − h(u) + h(v)** :contentReference[oaicite:14]{index=14}

Eso te da APSP en el grafo original.

---

## 6) ¿Por qué esto es útil?
Porque:
- Bellman-Ford se corre **solo 1 vez** (para hallar h y detectar ciclo negativo)
- Luego usas Dijkstra |V| veces, que es rápido si pesos son no negativos. :contentReference[oaicite:15]{index=15}

---

## 7) Complejidad (lo que te preguntan en examen)
El PDF da:
- Bellman-Ford: **O(|V||E|)**
- |V| veces Dijkstra: **O(|V| (|V| log |V| + |E|))**
Total:
- **O(|V|^2 log |V| + |V||E|)** :contentReference[oaicite:16]{index=16}

---

## 8) Resumen ultra simple (en 4 líneas)
- Johnson = APSP para grafos con pesos negativos (pero SIN ciclo negativo).
- Usa Bellman-Ford desde un nodo extra `x` para crear potenciales `h`.
- Repondera para que todos los pesos sean ≥ 0.
- Corre Dijkstra desde cada nodo y “deshace” la reponderación.

---

Si me dices qué te confunde:
1) ¿para qué sirve h?
2) ¿por qué w' queda no negativo?
3) ¿por qué δ se recupera con “−h(u)+h(v)”?
Te lo explico con un mini-ejemplo con 3–4 nodos.




# Tabla rápida — Shortest Paths Algorithms (temario + extra)

| Algoritmo | ¿Qué resuelve? | ¿Permite pesos negativos? | ¿Detecta ciclo negativo? | ¿Cuándo usarlo? | Complejidad típica |
|---|---|---:|---:|---|---|
| **BFS** | Single-Source (desde un origen s a todos) en grafo **sin pesos** o todos los pesos = 1 | No aplica (no usa pesos) | No | Cuando “cada arista cuesta lo mismo” (minimiza #aristas) | **O(V + E)** |
| **DAG Shortest Paths** (Topological + Relax) | Single-Source en **DAG** | Sí | No (en DAG no hay ciclos) | Cuando el grafo dirigido **no tiene ciclos**; es el más rápido y acepta negativos | **O(V + E)** |
| **Dijkstra** | Single-Source en grafo general | **No** (requiere w ≥ 0) | No | Cuando **todos los pesos son no negativos** | **O(E log V)** (con heap) |
| **Bellman–Ford** | Single-Source en grafo general | **Sí** | **Sí** | Cuando hay pesos negativos o quieres saber si existe ciclo negativo alcanzable desde s | **O(V·E)** |
| **Johnson** | **All-Pairs** (todos contra todos) | Sí (pero sin ciclos negativos) | Sí (vía Bellman–Ford) | All-pairs en grafo **sparse** con posibles negativos; convierte pesos para usar Dijkstra V veces | **O(V·E + V·E log V)** aprox |
| **Floyd–Warshall** *(extra)* | **All-Pairs** (todos contra todos) | Sí (pero sin ciclos negativos) | Sí (se puede evidenciar) | All-pairs cuando V no es grande o grafo denso; muy directo con DP | **O(V³)** |

## Notas cortas (para memorizar)
- **Single-Source**: desde un origen s, distancias a todos.
- **All-Pairs**: distancias entre todos los pares (u,v).
- **Ciclo negativo**: si es alcanzable y puede llegar a t, entonces para ese t la distancia es **-∞** (no hay mínimo finito).

Si me dices cuántos nodos/edges suelen tener en tus ejercicios, te digo cuál conviene “por reflejo” en examen.


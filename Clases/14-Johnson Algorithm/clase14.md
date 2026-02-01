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

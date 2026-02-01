# 20 preguntas (con respuestas) — Weighted Shortest Paths

## 1
**P:** ¿Qué significa “weighted shortest path”?  
**R:** Encontrar el camino entre nodos con **menor suma de pesos** (costos) de las aristas.

## 2
**P:** ¿En un grafo sin pesos, qué significa “camino más corto”?  
**R:** El camino con **menos aristas** (menor número de pasos).

## 3
**P:** ¿Por qué BFS no sirve en grafos con pesos distintos?  
**R:** Porque BFS minimiza **cantidad de aristas**, no la **suma de pesos**.

## 4
**P:** ¿Cómo se calcula el peso (costo) de un camino?  
**R:** Sumando los pesos de todas sus aristas.

## 5
**P:** ¿Qué representa d[v] en shortest paths?  
**R:** La **mejor distancia/costo conocido** desde el origen s hasta v.

## 6
**P:** ¿Cómo se inicializan las distancias en casi todos los algoritmos?  
**R:** d[s] = 0 y d[otros] = ∞.

## 7
**P:** ¿Qué es “relajar” una arista (u→v)?  
**R:** Intentar mejorar d[v] usando d[u] + w(u,v).

## 8
**P:** Escribe la condición de relajación.  
**R:** Si d[v] > d[u] + w(u,v), entonces d[v] = d[u] + w(u,v).

## 9
**P:** ¿Qué es un ciclo en un grafo?  
**R:** Un recorrido que empieza y termina en el mismo nodo.

## 10
**P:** ¿Qué es un ciclo negativo?  
**R:** Un ciclo cuya suma de pesos es **menor que 0**.

## 11
**P:** ¿Por qué un ciclo negativo puede destruir el “camino mínimo”?  
**R:** Porque puedes dar vueltas al ciclo para bajar el costo sin límite (→ -∞).

## 12
**P:** ¿Siempre que exista un ciclo negativo “no hay camino mínimo” para todos los nodos?  
**R:** No. Solo para nodos t donde se cumple: s puede llegar al ciclo y del ciclo se puede llegar a t.

## 13
**P:** ¿Qué significa δ(s,t) = ∞?  
**R:** Que **no existe camino** de s a t.

## 14
**P:** ¿Qué significa δ(s,t) = -∞?  
**R:** Que el costo puede bajarse sin límite (hay ciclo negativo “alcanzable” hacia t).

## 15
**P:** ¿Qué es un DAG?  
**R:** Un grafo dirigido **sin ciclos** (Directed Acyclic Graph).

## 16
**P:** ¿Por qué en un DAG no puede existir un ciclo negativo?  
**R:** Porque no puede existir ningún ciclo (ni negativo ni positivo).

## 17
**P:** ¿Qué algoritmo es muy eficiente para shortest paths en un DAG?  
**R:** Orden topológico + relajación en ese orden (DAG shortest paths).

## 18
**P:** ¿Cuál es la idea del orden topológico en DAG shortest paths?  
**R:** Procesar nodos en un orden donde las aristas siempre van “hacia adelante”.

## 19
**P:** ¿Qué algoritmo se usa típicamente si todos los pesos son ≥ 0?  
**R:** Dijkstra.

## 20
**P:** ¿Qué algoritmo se usa si hay pesos negativos (y quieres detectar ciclos negativos)?  
**R:** Bellman-Ford.

---
Si quieres, te genero otras 20 pero tipo “verdadero/falso” o tipo examen con mini-grafos.

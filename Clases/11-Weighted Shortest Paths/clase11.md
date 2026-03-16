# Weighted Shortest Paths (Caminos mínimos con pesos) — desde cero

## 0) Idea base (por qué existe este tema)
En grafos, “camino más corto” puede significar dos cosas distintas:

1) **Sin pesos (unweighted):**
   - Cada arista “cuesta 1”.
   - El camino más corto = el que tiene **menos aristas**.
   - Se resuelve con **BFS**.

2) **Con pesos (weighted):**
   - Cada arista tiene un número (costo/tiempo/distancia).
   - El camino más corto = el que tiene **menor suma de pesos**.
   - Aquí entra *weighted shortest paths*.

---

## 1) Qué es un grafo ponderado (weighted graph)
Un grafo ponderado es un grafo donde cada arista tiene un peso:

- Arista: (u -> v)
- Peso: w(u, v)

Ejemplo: “ir de A a B cuesta 7”.

---

## 2) Qué es el “costo” de un camino
Un **camino** es una secuencia de nodos conectados por aristas.

Si el camino es:
s -> a -> b -> t

y los pesos son:
w(s,a)=2, w(a,b)=1, w(b,t)=4

Entonces el **costo total del camino** es:
2 + 1 + 4 = 7

👉 El **camino más corto** es el que tiene el **menor costo total**.

---

## 3) Diferencia clave con BFS (para que no se confunda)
Mira este caso:

s -> t (peso 100)
s -> a (peso 1)
a -> t (peso 1)

- BFS (sin pesos) diría: “s->t es mejor” porque usa 1 arista.
- Weighted shortest paths dice: “s->a->t es mejor” porque cuesta 2.

O sea: **menos aristas NO significa menor costo** cuando hay pesos.

---

## 4) El problema “raro”: pesos negativos y ciclos negativos
### 4.1 Peso negativo
Una arista puede tener peso negativo (ej: -3). Eso significa “te reduce costo”.

### 4.2 Ciclo negativo (lo importante)
Un **ciclo** es volver al mismo nodo:
A -> B -> C -> A

Si la suma de pesos del ciclo es negativa, es un **ciclo negativo**.

Ejemplo:
A->B = 2
B->C = -10
C->A = 3
Suma = 2 - 10 + 3 = -5  (negativo)

### 4.3 ¿Por qué un ciclo negativo rompe el “camino mínimo”?
Porque puedes dar vueltas al ciclo para bajar el costo sin límite:

- 1 vuelta: baja 5
- 2 vueltas: baja 10
- k vueltas: baja 5k
y luego sigues al destino.

✅ Regla exacta:
- Si desde el origen **puedes llegar** a un ciclo negativo,
- y desde ese ciclo **puedes llegar** al destino t,
entonces para ese t **NO existe camino mínimo finito** (la distancia es -∞).

Pero si el ciclo negativo está “aislado” (no lo alcanzas desde s o no te lleva a t), entonces **no afecta** a esos nodos.

---

## 5) Cómo se resuelven shortest paths (depende del caso)
No existe un único algoritmo para todo. Se elige según los pesos y el tipo de grafo:

### A) Grafo sin pesos (o pesos iguales)  -> BFS
- Encuentra menor número de aristas.

### B) DAG (grafo dirigido acíclico) -> DAG Shortest Paths (topological + relax)
- Puede tener pesos negativos.
- Como no hay ciclos, NO puede haber ciclo negativo.
- Es rápido (lineal).

### C) Pesos NO negativos -> Dijkstra
- El más usado.
- No funciona bien con negativos.

### D) Pesos negativos (sin ciclos negativos alcanzables) -> Bellman-Ford
- También detecta ciclos negativos.

---

## 6) La idea central: RELAJACIÓN (relaxation)
Esto es el corazón del tema.

Queremos calcular distancias desde s:
d[v] = mejor costo conocido para llegar a v desde s.

Inicial:
- d[s] = 0
- d[otros] = infinito (∞)

**Relajar una arista (u -> v)** significa:
“si llegar a u es barato, quizá llegar a v pasando por u sea más barato”.

Fórmula:
si d[v] > d[u] + w(u,v):
    d[v] = d[u] + w(u,v)

Eso es “mejoré” la distancia a v.

---

## 7) Ejemplo corto (con relajación paso a paso)
Grafo:
s -> a (2)
s -> b (5)
a -> b (1)

Inicio:
d[s]=0, d[a]=∞, d[b]=∞

Relajo (s->a):
d[a] = min(∞, 0+2) = 2

Relajo (s->b):
d[b] = min(∞, 0+5) = 5

Relajo (a->b):
d[b] = min(5, 2+1) = 3

Resultado:
- Mejor costo a b es 3, por camino s->a->b.

---

## 8) DAG Shortest Paths (lo típico en “weighted shortest paths” clase)
Si el grafo es DAG:

1) Calculas un **orden topológico** (un orden donde todas las flechas van “hacia adelante”).
2) Recorres nodos en ese orden.
3) Para cada nodo u, relajas todas sus aristas salientes.

Pseudocódigo:
- d[s]=0, otros=∞
- topo = TopologicalSort(G)
- para u en topo:
    para cada arista (u->v):
        relax(u,v)

✅ Por qué funciona:
En un DAG, cuando llegas a u en el orden topológico, ya procesaste todo lo que podría mejorar a u (no hay ciclos que vuelvan).

---

## 9) Lo que debes recordar (modo examen)
- Camino más corto con pesos = **menor suma de pesos**.
- BFS solo sirve cuando “cada arista cuesta lo mismo”.
- “Relajación” = la regla d[v] > d[u] + w(u,v) => actualizar.
- Ciclo negativo alcanzable desde s y que llega a t => para t **no hay mínimo finito**.
- Elección de algoritmo:
  - DAG -> topological + relax
  - pesos >= 0 -> Dijkstra
  - negativos -> Bellman-Ford (y detecta ciclos negativos)

---

Si me mandas una foto o escribes un grafo (nodos y pesos),
te lo resuelvo completo: d[] final + qué camino toma cada nodo.

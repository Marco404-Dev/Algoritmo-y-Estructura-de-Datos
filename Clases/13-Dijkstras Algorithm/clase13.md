# Dijkstra (SSSP) — explicación simple (clase 13)

Este PDF es la **clase 13: Dijkstra’s Algorithm** y se enfoca en encontrar **caminos más cortos desde un origen s** en un grafo con **pesos NO negativos**. :contentReference[oaicite:0]{index=0}

---

## 1) ¿Cuándo se usa Dijkstra?
Dijkstra funciona **solo si todas las aristas cumplen**:

- **w(e) ≥ 0** (no hay pesos negativos). :contentReference[oaicite:1]{index=1}

Si hay pesos negativos, usas **Bellman-Ford** (pero es más lento). :contentReference[oaicite:2]{index=2}

Resumen rápido (como en la tabla del PDF):
- Grafo sin pesos (0/1 o “no ponderado”) → **BFS**: O(|V|+|E|)
- DAG con pesos → **DAG relaxation**: O(|V|+|E|)
- General con pesos **no negativos** → **Dijkstra**: O(|E| + |V| log |V|) (con heap)
- General con pesos cualquiera (incluye negativos) → **Bellman-Ford**: O(|V||E|) :contentReference[oaicite:3]{index=3}

---

## 2) La idea (en palabras muy simples)
Piensa en BFS, pero con pesos:

- BFS explora por “capas” de 1,2,3 aristas (porque cada arista cuesta 1).
- Dijkstra explora por “capas” de **distancia real acumulada**.

La clave del PDF:
- Si los pesos son no negativos, las distancias de los caminos más cortos **nunca bajan** mientras avanzas. :contentReference[oaicite:4]{index=4}

Entonces Dijkstra hace esto:
> Siempre elige el vértice **más cercano** (con menor distancia tentativa) que aún no ha sido “confirmado”.

---

## 3) ¿Qué significa “confirmado”?
Cuando Dijkstra “saca” un nodo `u` como el mínimo, en ese momento:
- `d[s,u]` ya es la distancia real mínima (δ(s,u)) y **ya no cambiará**. :contentReference[oaicite:5]{index=5}

Esto es lo que NO pasa con Bellman-Ford (ahí la distancia puede mejorar muchas veces).

---

## 4) El algoritmo (tal como está en el PDF, pero explicado)
Mantienes:
- `d[v]` = mejor distancia conocida desde `s` a `v` (al inicio infinito).
- Una **cola de prioridad** (Priority Queue) que siempre te da el `v` con menor `d[v]`. :contentReference[oaicite:6]{index=6}

### Pasos
1) Inicializa:
- `d[s]=0`
- `d[otros]=∞`

2) Mete todos los vértices en una Priority Queue con clave `d[v]`. :contentReference[oaicite:7]{index=7}

3) Mientras la cola no esté vacía:
- Sacas (delete-min) el nodo `u` con menor `d[u]`. :contentReference[oaicite:8]{index=8}
- Para cada vecino `v` al que `u` apunta:
  - si `d[v] > d[u] + w(u,v)` entonces:
    - actualizas `d[v] = d[u] + w(u,v)`
    - haces `decrease-key(v, d[v])` en la cola. :contentReference[oaicite:9]{index=9}

Eso es TODO.

---

## 5) Ejemplo mini (para que lo veas claro)
Grafo (pesos no negativos):
- s→a (4)
- s→b (1)
- b→a (2)
- a→c (1)
- b→c (5)

### Inicio
- d[s]=0
- d[a]=∞, d[b]=∞, d[c]=∞

### Paso 1: saco s (0)
Relajo:
- s→a: d[a]=4
- s→b: d[b]=1

### Paso 2: saco b (1) (porque es el menor)
Relajo:
- b→a: d[a] = min(4, 1+2=3) => d[a]=3
- b→c: d[c] = min(∞, 1+5=6) => d[c]=6

### Paso 3: saco a (3)
Relajo:
- a→c: d[c] = min(6, 3+1=4) => d[c]=4

### Paso 4: saco c (4)
Termina.

Resultado final:
- d[a]=3, d[b]=1, d[c]=4

Observa lo importante:
- Cuando saqué `b` con 1, ya era seguro que 1 era la distancia mínima.
- Esto solo es seguro porque **no hay pesos negativos**.

---

## 6) ¿Por qué falla con pesos negativos? (la razón en una línea)
Porque con un peso negativo, un nodo que parecía “ya mínimo” podría volverse más barato después,
y Dijkstra no está hecho para “arrepentirse” de un mínimo ya sacado.

---

## 7) Complejidad (lo que te pueden preguntar)
El PDF cuenta operaciones:
- build: 1 vez
- delete-min: |V| veces
- decrease-key: hasta |E| veces :contentReference[oaicite:10]{index=10}

Con Binary Heap:
- delete-min: log |V|
- decrease-key: log |V|
⇒ Total típico: **O(|E| + |V| log |V|)**. :contentReference[oaicite:11]{index=11}

---

## 8) Lo que debes memorizar (modo examen)
- Dijkstra = SSSP para pesos **≥ 0**.
- Siempre extrae el nodo con menor distancia tentativa (priority queue).
- Al extraerlo, su distancia queda “fija”.
- Relaja sus aristas salientes.
- Tiempo típico: O(|E| + |V| log |V|).

---

Si me dices **qué parte te confunde** (cola de prioridad, relax, por qué se “fija” la distancia, o el ejemplo),
te lo explico con un ejemplo todavía más chico (3 nodos).

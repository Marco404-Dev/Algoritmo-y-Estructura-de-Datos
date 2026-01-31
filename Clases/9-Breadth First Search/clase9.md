# Breadth-First Search (BFS) — explicación sencilla

## ¿Qué es BFS?
**BFS (Breadth-First Search)** es un recorrido que visita nodos **por niveles (capas)**:
- primero los que están a **1 paso** del inicio,
- luego los de **2 pasos**,
- luego los de **3 pasos**, etc.

La idea es: **“primero lo más cerca”**.

---

## ¿Cómo lo hace?
BFS usa una **COLA (queue)**, que funciona así:
- **Entra primero → sale primero** (FIFO)

### Pasos (idea general)
1. Elige un nodo inicio `s`.
2. Marca `s` como visitado y mételo a la cola.
3. Mientras la cola NO esté vacía:
   - Saca el primero (`u`).
   - Revisa sus vecinos (`v`).
   - Si `v` no fue visitado:
     - márcalo como visitado
     - mételo a la cola

---

## Ejemplo paso a paso
Conexiones (grafo / árbol):
- A conecta con B y C
- B conecta con D
- C conecta con E

### Inicio
- Visitados: { }
- Cola: [ ]

### 1) Visito A
- Visitados: {A}
- Cola: [A]

### 2) Saco A, meto sus vecinos B y C
- Visitados: {A, B, C}
- Cola: [B, C]

### 3) Saco B, meto D
- Visitados: {A, B, C, D}
- Cola: [C, D]

### 4) Saco C, meto E
- Visitados: {A, B, C, D, E}
- Cola: [D, E]

### 5) Saco D y luego E (ya no agregan nuevos)
- Cola: [ ]
- Termina

✅ Orden típico de visita: **A → B → C → D → E**  
(El orden exacto puede variar si cambias el orden en que lees vecinos, pero **siempre respeta las capas**)

---

## ¿Qué significa “capas”?
- Capa 0: A (0 pasos)
- Capa 1: B, C (1 paso)
- Capa 2: D, E (2 pasos)

---

## ¿Solo aplica para árboles?
**No. BFS aplica tanto a:**
- ✅ **Árboles**
- ✅ **Grafos** (dirigidos o no dirigidos)

### Diferencia clave:
- En un **árbol** no hay ciclos, entonces es más simple.
- En un **grafo** puede haber **ciclos**, así que **sí o sí** debes usar `visitado`
  para no entrar en un bucle infinito (por ejemplo: A→B→C→A→B→...).

---

## Bonus: ¿Para qué sirve?
- Encontrar el **camino más corto en número de pasos** (cuando NO hay pesos).
- Recorrer por niveles (muy típico en árboles, redes, mapas sin pesos, etc.).

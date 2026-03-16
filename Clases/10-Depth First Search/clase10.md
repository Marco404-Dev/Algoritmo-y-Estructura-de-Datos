# DFS (Depth-First Search) — Búsqueda en Profundidad (explicación sencilla)

## ¿Qué es DFS?
**DFS** es un recorrido que explora un grafo (o árbol) yendo **lo más profundo posible** antes de volver atrás.

Idea clave:
- “Sigo un camino hasta que ya no puedo… y luego **retrocedo** (backtracking) para probar otro camino”.

> En clase suele decirse: DFS es similar a BFS porque ambas recorren grafos desde un inicio y evitan repetir nodos, pero DFS NO está pensado para distancias mínimas. :contentReference[oaicite:0]{index=0}

---

## ¿Cómo funciona? (versión simple)
DFS se puede hacer de 2 formas:
- **Recursión** (lo más común y fácil de entender)
- **Pila (stack)** (iterativo)

### Pasos (con “visitados”)
1. Empiezas en un nodo `s`.
2. Lo marcas como visitado.
3. Visitas recursivamente a cada vecino no visitado.

Pseudoflujo:
- `visit(u)`:
  - para cada vecino `v` de `u`:
    - si `v` no fue visitado:
      - guarda `padre[v] = u`
      - llama `visit(v)` :contentReference[oaicite:1]{index=1}

---

## Ejemplo rápido (para “ver” la diferencia)
Conexiones:
- A conecta con B y C
- B conecta con D
- C conecta con E

Si DFS empieza en **A** y revisa vecinos en orden **B luego C**:
- A → B → D (ya no hay más, retrocede)
- regresa a A → C → E

Un orden posible: **A, B, D, C, E**
(Ojo: puede variar por el orden en que aparecen los vecinos, pero siempre “se va profundo”). :contentReference[oaicite:2]{index=2}

---

## Entonces… ¿DFS y BFS son casi iguales?
**Son parecidos en lo básico, pero se usan para cosas distintas.**

### ✅ En qué se parecen
- Ambos recorren **árboles y grafos** (no solo árboles).
- Ambos usan “visitados” en grafos para no repetir nodos/ciclos.
- Ambos pueden construir un árbol de padres `P(v)` desde el inicio. :contentReference[oaicite:3]{index=3}

### 🔥 En qué se diferencian (lo importante)
| Tema | BFS | DFS |
|---|---|---|
| Forma de explorar | **por capas** (cerca primero) | **por profundidad** (camino largo primero) |
| Estructura típica | **cola (queue)** | **pila (stack)** o **recursión** |
| Camino más corto (sin pesos) | ✅ Sí | ❌ No necesariamente |
| Se usa mucho para | distancias mínimas en saltos | topological sort, detectar ciclos, componentes, etc. :contentReference[oaicite:4]{index=4} |

---

## ¿Para qué sirve DFS en serio?
Según la clase:
- Resuelve **alcanzabilidad** (ver qué nodos son alcanzables desde `s`),
- y es base para otros problemas (ej. topological sort y detección de ciclos). :contentReference[oaicite:5]{index=5}

# Bellman-Ford — ahora sí, en simple (sin vueltas raras)

## 1) ¿Qué problema resuelve?
Tienes un grafo con **caminos con costo** (pesos).  
Quieres saber el **costo mínimo** para ir desde un origen `s` a cada nodo.

✅ Sirve aunque existan **pesos negativos**.  
⚠️ Pero si hay un **ciclo negativo**, ya no existe “mínimo” (porque puedes dar vueltas y el costo baja para siempre).

---

## 2) La idea más fácil de entender
Bellman-Ford hace esto:

### Paso A: Inicializa distancias
- `dist[s] = 0`
- `dist[otros] = +∞`

### Paso B: Repite “relajar” TODAS las aristas **V−1 veces**
“Relajar una arista” `(u → v, peso w)` significa:

Si `dist[u] + w < dist[v]`  
entonces actualiza: `dist[v] = dist[u] + w`.

**¿Por qué V−1 veces?**
Porque si NO hay ciclo negativo, el camino más corto a un nodo usa como máximo **V−1 aristas** (no repite vértices).

### Paso C: Detecta ciclo negativo (una pasada extra)
Haces **una pasada más** por todas las aristas:
- Si todavía puedes mejorar alguna distancia, entonces existe un **ciclo negativo** alcanzable desde `s`.

---

## 3) Ejemplo paso a paso (con números)
Nodos: `S, A, B, C`

Aristas:
- `S → A (4)`
- `S → B (5)`
- `A → B (-2)`
- `B → C (3)`
- `C → A (-10)`   ← esto crea ciclo negativo (A→B→C→A)

### Inicial:
- dist[S]=0
- dist[A]=∞
- dist[B]=∞
- dist[C]=∞

---

### Iteración 1 (relajo todas las aristas)
1) S→A: dist[A] = 0+4 = 4  
2) S→B: dist[B] = 0+5 = 5  
3) A→B: dist[B] = min(5, 4-2)=2  
4) B→C: dist[C] = 2+3=5  
5) C→A: dist[A] = min(4, 5-10) = -5  

Resultado:
- S=0, A=-5, B=2, C=5

---

### Iteración 2
1) S→A: no mejora (0+4=4 > -5)
2) S→B: no mejora (5 > 2)
3) A→B: B = min(2, -5-2 = -7) => B=-7
4) B→C: C = min(5, -7+3 = -4) => C=-4
5) C→A: A = min(-5, -4-10 = -14) => A=-14

Resultado:
- S=0, A=-14, B=-7, C=-4

¿Ves qué pasa?  
Cada vuelta por el ciclo A→B→C→A baja más y más.

---

### Iteración 3 (todavía baja)
Va a seguir bajando…

---

## 4) ¿Cómo detecta el ciclo negativo?
Después de hacer **V−1 iteraciones**, hace una iteración extra:

Si todavía encuentra una mejora, significa:
✅ “Hay un ciclo negativo alcanzable”  
y entonces **las distancias de los nodos afectados no son un número**, son **−∞** (puedes bajarlas sin límite).

---

## 5) Resumen ultra corto (lo que debes memorizar)
- Bellman-Ford = “relajar todas las aristas” muchas veces.
- Haces **V−1** rondas para calcular distancias.
- Haces **1 ronda extra**:
  - si algo mejora ⇒ hay **ciclo negativo**.

---

## 6) Mini-pseudocódigo (lo esencial)
dist[*]=∞
dist[s]=0

repetir V-1 veces:
  para cada arista (u→v, w):
    si dist[u]+w < dist[v]:
      dist[v]=dist[u]+w

# detectar ciclo negativo
para cada arista (u→v, w):
  si dist[u]+w < dist[v]:
    hay_ciclo_negativo = true

---

## 7) Dime qué parte exacta no entendiste
Elige una:
1) ¿Qué es “relajar”?
2) ¿Por qué V−1?
3) ¿Qué es un ciclo negativo y por qué da −∞?
4) El ejemplo con números (¿en qué iteración te perdiste?)

Respóndeme con el número y te lo explico con otro ejemplo todavía más simple.

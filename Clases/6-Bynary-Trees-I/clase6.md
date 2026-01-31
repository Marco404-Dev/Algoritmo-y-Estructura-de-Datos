# Binary Trees I (Árboles Binarios) — Explicación Sencilla

## 1) ¿Qué es un árbol binario?
Un **árbol binario** es una estructura de datos hecha de **nodos**.
Cada nodo puede tener **máximo 2 hijos**:
- hijo izquierdo (left)
- hijo derecho (right)

Ejemplo:
```text


      A
     / \
    B   C
   /
  D
```
---

## 2) Partes básicas (nombres que siempre salen)
- **Raíz (root):** el nodo de arriba (A).
- **Padre (parent):** el nodo que está encima.
  - Ejemplo: A es padre de B y C.
- **Hijos (children):** los nodos que están debajo.
  - Ejemplo: B y C son hijos de A.
- **Hoja (leaf):** nodo que **no tiene hijos**.
  - Ejemplo: D y C son hojas.

---

## 3) Recorridos (Traversal)
Recorrer un árbol = visitar/leer los nodos en cierto orden.

### In-order (izquierda → yo → derecha)
Regla:
1) Visita subárbol izquierdo
2) Visita el nodo
3) Visita subárbol derecho

Ejemplo:
```text
      A
     / \
    B   C
   /
  D
```

In-order:
- izquierda de A: (B)
  - izquierda de B: (D) → leo D
  - leo B
- leo A
- derecha de A: leo C

Resultado: **D, B, A, C**

---

## 4) ¿Para qué sirve?
- Representar jerarquías (carpetas, niveles, etc.)
- Buscar y organizar datos
- Se usa mucho en estructuras como:
  - BST (árbol de búsqueda)
  - Heaps
  - Árboles balanceados (AVL/Red-Black) más adelante

---

## 5) Idea clave: la altura importa
- Si el árbol es “bajito”, las operaciones son rápidas.
- Si el árbol está “torcido” como lista, se vuelve lento.

Ejemplo malo (muy alto):
```text
A
 \
  B
   \
    C
     \
      D
```

Ejemplo bueno (balanceado):
```text
   B
  / \
 A   D
    /
   C

```
---

## 6) Mini práctica (para comprobar)
Con este árbol:
```text
      8
     / \
    3   10
   / \
  1   6

```

Pregunta: ¿Cuál es el recorrido **in-order** (izq → yo → der)?






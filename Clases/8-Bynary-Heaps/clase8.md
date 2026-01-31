# Binary Heap (Max-Heap) explicado como para “no fallar”

## 1) ¿Qué es un heap?
Un **heap** es un **arreglo** que se comporta como un “árbol” donde:

✅ **El número más grande siempre está arriba** (en la posición 0 del arreglo).

Eso es TODO lo importante al inicio.

Ejemplo (Max-Heap):
Q = [90, 70, 80, 30, 60, 50]

- El máximo es 90
- y está en Q[0]

---

## 2) ¿Por qué se llama “binary”?
Porque ese “árbol imaginario” tiene máximo **2 hijos** por nodo.

Pero en realidad no guardas nodos ni flechas:
👉 solo guardas un **array**.

---

## 3) Regla mágica de posiciones (la única fórmula que necesitas)
Si estás en el índice i:

- hijo izquierdo  = 2*i + 1
- hijo derecho    = 2*i + 2
- padre           = (i - 1) // 2

Ejemplo:
i = 0
- left = 1
- right = 2

i = 1
- left = 3
- right = 4
- parent = 0


# Cómo ubicar un nodo del arreglo dentro del árbol (heap)

## Idea
El heap es un árbol **completo** guardado en un **array**.

- El índice 0 es la **raíz**
- Cada índice i “tiene” hijos y padre usando fórmulas

## Fórmulas (0-based index)
Si estás en el índice i:

- hijo izquierdo  = 2*i + 1
- hijo derecho    = 2*i + 2
- padre           = (i - 1) // 2

*(Si el hijo se pasa de n-1, ese hijo NO existe.)*

---

## Ejemplo 1: ubicar en el árbol desde el array
Q = [60, 30, 50, 10, 20, 40]
índices:  0   1   2   3   4   5

### ¿Quiénes son hijos de i = 0?
- left(0)  = 2*0+1 = 1  → Q[1] = 30
- right(0) = 2*0+2 = 2  → Q[2] = 50

Entonces en el árbol:
- 60 (raíz)
  - hijo izq: 30
  - hijo der: 50

### ¿Quiénes son hijos de i = 1?
- left(1)  = 2*1+1 = 3 → Q[3] = 10
- right(1) = 2*1+2 = 4 → Q[4] = 20

Entonces:
- 30 tiene hijos: 10 y 20

### ¿Quién es el padre de i = 5?
- parent(5) = (5-1)//2 = 2 → Q[2] = 50

Entonces:
- 40 (Q[5]) tiene padre 50 (Q[2])

---

## Dibujito del árbol (mapeado)

              Q[0]=60
            /         \
      Q[1]=30        Q[2]=50
      /    \          /
Q[3]=10  Q[4]=20   Q[5]=40


---

## 4) Operación 1: INSERTAR (meter un número)
Idea: 
1) lo metes al final
2) si es grande, **sube** (cambiando con su padre)

### Ejemplo:
Heap inicial:
Q = [50, 30, 40, 10, 20]

Insertamos 60:

Paso 1: lo pongo al final:
Q = [50, 30, 40, 10, 20, 60]

Paso 2: 60 “sube” si es mayor que su padre
- 60 está en i=5
- padre = (5-1)//2 = 2
- Q[2] = 40

Como 60 > 40, intercambio:
Q = [50, 30, 60, 10, 20, 40]

Ahora 60 está en i=2
- padre = (2-1)//2 = 0
- Q[0] = 50

Como 60 > 50, intercambio:
Q = [60, 30, 50, 10, 20, 40]

✅ Listo. Ya es heap.
✅ El máximo quedó arriba.

---

## 5) Operación 2: SACAR EL MÁXIMO (delete_max)
Idea:
1) el máximo es Q[0], pero no lo puedes “borrar” así nomás
2) lo cambias con el último
3) borras el último (ese era el máximo)
4) el nuevo de arriba “baja” si es pequeño (bajando con el hijo más grande)

### Ejemplo:
Q = [60, 30, 50, 10, 20, 40]

Paso 1: intercambio primero con último:
Q = [40, 30, 50, 10, 20, 60]

Paso 2: borro el último (devuelvo 60):
Q = [40, 30, 50, 10, 20]

Paso 3: ahora 40 está arriba, pero su hijo mayor es 50
- hijos de i=0: i=1 (30) y i=2 (50)
- el mayor hijo es 50

Como 40 < 50, intercambio con 50:
Q = [50, 30, 40, 10, 20]

✅ Listo, heap arreglado otra vez.

---

## 6) Qué debes recordar sí o sí
- Heap = array donde **el mayor siempre está en Q[0]**
- Insertar = poner al final y **subir**
- Delete_max = swap con último, borrar, y **bajar**


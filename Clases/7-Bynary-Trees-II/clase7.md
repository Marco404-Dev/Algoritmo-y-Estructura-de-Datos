AVL (Binary Trees II) — explicación sencilla + rotaciones (con ejemplos)
=====================================================================

## 1) ¿Qué es un AVL?
---------------
Un AVL es un árbol binario de búsqueda (BST) que se auto-arregla para NO quedar como una lista.

- Si un BST se vuelve “lista”, buscar se vuelve lento.
- AVL evita eso manteniendo el árbol balanceado.


## 2) ¿Qué significa “balanceado”?
------------------------------
En cada nodo comparas la altura del lado izquierdo y del lado derecho.

Regla AVL:
- diferencia = 0  -> OK
- diferencia = 1  -> OK
- diferencia = -1 -> OK
- diferencia = 2  -> MAL (hay que arreglar)
- diferencia = -2 -> MAL (hay que arreglar)


## 3) ¿Cómo lo arregla? (rotaciones)
---------------------------------
Rotación = mover 2 o 3 nodos para “enderezar” el árbol, sin perder el orden del BST.

Idea fácil:
Cuando se inclina mucho, el AVL hace que el “nodo del medio” suba.


## 4) Casos de rotación (con ejemplos claros)
------------------------------------------

#### 4.1) Caso RR -> 1 rotación a la izquierda
Insertar: 1, 2, 3

Antes (se inclina a la derecha):

1
 \
  2
   \
    3

Después (rotación izquierda):
  2
 / \
1   3


4.2) Caso LL -> 1 rotación a la derecha
Insertar: 3, 2, 1

Antes (se inclina a la izquierda):
  3
 /
2
/
1

Después (rotación derecha):
  2
 / \
1   3


4.3) Caso RL -> 2 rotaciones (derecha y luego izquierda)
Insertar: 1, 3, 2

Antes:
1
 \
  3
 /
2

Paso 1: rotación derecha en el hijo (3)
1
 \
  2
   \
    3

Paso 2: rotación izquierda en el padre (1)
  2
 / \
1   3


4.4) Caso LR -> 2 rotaciones (izquierda y luego derecha)
Insertar: 3, 1, 2

Antes:
  3
 /
1
 \
  2

Paso 1: rotación izquierda en el hijo (1)
  3
 /
2
/
1

Paso 2: rotación derecha en el padre (3)
  2
 / \
1   3


5) Ejemplos un poco más largos (4 números)
------------------------------------------

5.1) RR con 4 números
Insertar: 10, 20, 30, 40

Con 10,20,30 (RR) se arregla y queda:
   20
  /  \
10   30

Luego insertas 40:
   20
  /  \
10   30
       \
       40

Sigue balanceado, así que ya no rota.


5.2) RL con 4 números
Insertar: 10, 30, 20, 25

Con 10,30,20 (RL) se arregla y queda:
   20
  /  \
10   30

Luego insertas 25 (va a la izquierda de 30):
   20
  /  \
10   30
     /
    25

Sigue balanceado.


6) Cómo reconocer el caso rápido
--------------------------------
Mira el nodo que se desbalanceó:

Si se cargó a la derecha (tipo +2):
- hijo derecho también cargado a la derecha -> RR -> 1 rotación izquierda
- hijo derecho cargado a la izquierda       -> RL -> 2 rotaciones (derecha + izquierda)

Si se cargó a la izquierda (tipo -2):
- hijo izquierdo también cargado a la izquierda -> LL -> 1 rotación derecha
- hijo izquierdo cargado a la derecha           -> LR -> 2 rotaciones (izquierda + derecha)


7) ¿Por qué AVL sirve?
----------------------
Porque mantiene el árbol “cortito”, entonces:
- buscar
- insertar
- eliminar
se hacen en pocos pasos: O(log n)




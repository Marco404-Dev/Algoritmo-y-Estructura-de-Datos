# 20 preguntas (con respuestas) — Binary Heaps (Max-Heap)

## 1)
**P:** ¿Qué es un binary heap (max-heap) en una frase?  
**R:** Es un arreglo que representa un árbol binario completo donde cada padre es ≥ que sus hijos.

## 2)
**P:** ¿Qué estructura implementa típicamente un heap?  
**R:** Una cola de prioridad (priority queue).

## 3)
**P:** En un max-heap, ¿dónde está siempre el valor máximo?  
**R:** En la raíz, o sea en `Q[0]`.

## 4)
**P:** ¿Qué significa “árbol binario completo” en un heap?  
**R:** Que se llena por niveles, de izquierda a derecha, sin huecos.

## 5)
**P:** ¿Cómo calculas el hijo izquierdo de un índice `i` (0-based)?  
**R:** `left(i) = 2*i + 1`.

## 6)
**P:** ¿Cómo calculas el hijo derecho de un índice `i` (0-based)?  
**R:** `right(i) = 2*i + 2`.

## 7)
**P:** ¿Cómo calculas el padre de un índice `i` (0-based)?  
**R:** `parent(i) = (i - 1) // 2`.

## 8)
**P:** ¿Cómo verificas si un nodo `i` tiene hijo izquierdo en un array de tamaño `n`?  
**R:** Si `2*i + 1 < n`.

## 9)
**P:** ¿Cómo verificas si un nodo `i` tiene hijo derecho en un array de tamaño `n`?  
**R:** Si `2*i + 2 < n`.

## 10)
**P:** ¿Qué operación se usa después de insertar un elemento para arreglar el heap?  
**R:** `heapify up` (subir / sift up).

## 11)
**P:** En `heapify up`, ¿con quién se compara el nodo primero?  
**R:** Con su padre.

## 12)
**P:** ¿Qué condición causa un swap en `heapify up` en un max-heap?  
**R:** Si `Q[i] > Q[parent(i)]`.

## 13)
**P:** ¿Qué operación se usa después de borrar el máximo para arreglar el heap?  
**R:** `heapify down` (bajar / sift down).

## 14)
**P:** En `heapify down` (max-heap), ¿con cuál hijo se intercambia?  
**R:** Con el hijo de mayor valor (el más grande).

## 15)
**P:** Describe `delete_max` en pasos cortos.  
**R:** Swap raíz con último, eliminas el último, y haces `heapify down` desde la raíz.

## 16)
**P:** ¿Cuál es la complejidad de `find_max()` en un max-heap?  
**R:** `O(1)` porque el máximo está en `Q[0]`.

## 17)
**P:** ¿Cuál es la complejidad de `insert(x)` en un heap?  
**R:** `O(log n)` por el `heapify up`.

## 18)
**P:** ¿Cuál es la complejidad de `delete_max()` en un heap?  
**R:** `O(log n)` por el `heapify down`.

## 19)
**P:** ¿Cómo se construye un heap en `O(n)` (idea general)?  
**R:** Aplicando `heapify down` desde los últimos nodos internos hasta la raíz.

## 20)
**P:** ¿Por qué un heap no sirve para “buscar x” rápido como un BST?  
**R:** Porque el heap solo garantiza orden padre-hijos, no un orden global izquierda<raíz<derecha.

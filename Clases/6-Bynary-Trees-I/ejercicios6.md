# Binary Trees I — 20 preguntas con respuestas (tipo examen)

## 1) ¿Qué es un árbol binario?
**R:** Es una estructura de nodos donde cada nodo puede tener **máximo 2 hijos**: izquierdo y derecho.

---

## 2) ¿Qué es un nodo?
**R:** Una “cajita” que guarda un dato y puede apuntar a hijo izquierdo y/o derecho.

---

## 3) ¿Qué es la raíz (root)?
**R:** El nodo de arriba del árbol; **no tiene padre**.

---

## 4) ¿Qué es una hoja (leaf)?
**R:** Un nodo que **no tiene hijos**.

---

## 5) ¿Qué es un padre (parent)?
**R:** El nodo que está encima de otro y lo conecta como hijo.

---

## 6) ¿Qué es un hijo (child)?
**R:** Un nodo que cuelga debajo de otro (izquierdo o derecho).

---

## 7) ¿Qué es un subárbol de X?
**R:** El nodo X junto con **todos los nodos que están debajo** de X.

---

## 8) ¿Qué significa “máximo 2 hijos”?
**R:** Un nodo puede tener 0, 1 o 2 hijos, pero **nunca 3 o más**.

---

## 9) ¿Qué es la profundidad (depth) de un nodo?
**R:** La cantidad de pasos desde la **raíz** hasta ese nodo.

---

## 10) ¿Cuál es la profundidad de la raíz?
**R:** **0**.

---

## 11) ¿Qué es la altura (height) de un nodo?
**R:** El máximo número de pasos desde ese nodo hacia abajo hasta una hoja.

---

## 12) ¿Cuál es la altura de una hoja?
**R:** **0**.

---

## 13) ¿Qué es un “traversal”?
**R:** Es el **recorrido** del árbol: visitar/leer sus nodos en cierto orden.

---

## 14) ¿Qué es In-order?
**R:** Recorrer en orden: **izquierda → nodo → derecha**.

---

## 15) ¿Qué es Pre-order?
**R:** Recorrer: **nodo → izquierda → derecha**.

---

## 16) ¿Qué es Post-order?
**R:** Recorrer: **izquierda → derecha → nodo**.

---

## 17) ¿Qué es Level-order?
**R:** Recorrer **por niveles**: primero la raíz, luego sus hijos, luego nietos, etc.

---

## 18) En un árbol binario, ¿qué significa “first” en in-order?
**R:** Es el **más a la izquierda** dentro del subárbol: ir por left, left, left… hasta que ya no se pueda.

---

## 19) Regla del successor en in-order (la idea principal)
**R:**  
- Si X tiene **hijo derecho**, el successor es el **first del subárbol derecho**.  
- Si X **no** tiene hijo derecho, subes hasta encontrar un padre donde vengas desde la **izquierda**.

---

## 20) ¿Por qué la altura h importa tanto?
**R:** Porque muchas operaciones en árboles cuestan **O(h)**:
- árbol bajito → más rápido  
- árbol muy alto/torcido → más lento

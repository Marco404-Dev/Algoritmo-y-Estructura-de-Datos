# 20 preguntas de BFS (con respuestas)

1) **¿Qué significa BFS?**  
**R:** Breadth-First Search (búsqueda/recorrido en anchura).

2) **¿Cuál es la idea principal de BFS?**  
**R:** Visitar nodos **por niveles**, primero los más cercanos al inicio.

3) **¿Qué estructura de datos usa BFS?**  
**R:** Una **cola (queue)**.

4) **¿Qué significa que la cola sea FIFO?**  
**R:** **First In, First Out**: el primero que entra es el primero que sale.

5) **¿BFS se usa solo en árboles?**  
**R:** No. Se usa en **árboles y grafos**.

6) **¿Por qué en grafos se necesita un arreglo/conjunto de “visitados”?**  
**R:** Para evitar **ciclos** y no repetir nodos infinitamente.

7) **¿Qué pasa si no marcas “visitados” en un grafo con ciclo?**  
**R:** Puedes entrar en un **bucle infinito** (visitar lo mismo una y otra vez).

8) **¿Qué significa recorrer “por capas”?**  
**R:** Primero distancia 0, luego distancia 1, luego distancia 2, etc.

9) **¿Qué distancia calcula BFS en un grafo no ponderado?**  
**R:** La **mínima cantidad de aristas (saltos)** desde el inicio.

10) **¿BFS encuentra el camino más corto? ¿Cuándo?**  
**R:** Sí, pero solo en **grafos sin pesos** (o todos los pesos iguales).

11) **¿Qué guarda BFS para reconstruir el camino?**  
**R:** El **padre** de cada nodo (quién lo descubrió primero).

12) **En BFS, ¿cuándo un nodo se agrega a la cola?**  
**R:** Cuando se descubre por primera vez (cuando no estaba visitado).

13) **En BFS, ¿cuándo un nodo se saca de la cola?**  
**R:** Cuando le toca ser procesado (sale al frente de la cola).

14) **¿Qué orden produce BFS en un árbol?**  
**R:** Un recorrido **por niveles** (level-order).

15) **¿Cuál es la complejidad de BFS con lista de adyacencia?**  
**R:** **O(V + E)**.

16) **¿Qué representa V y E?**  
**R:** `V` = número de vértices (nodos), `E` = número de aristas (conexiones).

17) **Si empiezas en A y A conecta con B y C, ¿quién se visita antes: B/C o un nodo a 2 pasos?**  
**R:** Siempre **B y C** (los de 1 paso) antes que cualquiera a 2 pasos.

18) **¿El orden exacto de visita en BFS siempre es igual?**  
**R:** Puede variar según el **orden de la lista de vecinos**, pero siempre respeta las capas.

19) **¿Para qué sirve BFS en la vida real?**  
**R:** Para hallar mínimos pasos en redes, mapas sin pesos, rutas, estados de juegos, etc.

20) **¿Cuál es la diferencia más simple entre BFS y DFS?**  
**R:** BFS va por **capas** (cola). DFS va por **profundidad** (pila/recursión).

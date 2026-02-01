# 20 preguntas de DFS (con respuestas)

1) **¿Qué significa DFS?**  
**R:** Depth-First Search (búsqueda/recorrido en profundidad).

2) **¿Cuál es la idea principal de DFS?**  
**R:** Ir por un camino **lo más profundo posible** antes de retroceder.

3) **¿Qué es “backtracking” en DFS?**  
**R:** **Retroceder** cuando ya no hay vecinos nuevos y probar otro camino.

4) **¿DFS se puede usar en árboles y grafos?**  
**R:** Sí, en **ambos**.

5) **En grafos, ¿por qué DFS necesita “visitados”?**  
**R:** Para no repetir nodos y evitar ciclos (bucle infinito).

6) **¿Qué estructura de datos representa DFS de forma natural?**  
**R:** Una **pila (stack)**.

7) **¿Cómo implementas DFS más fácil normalmente?**  
**R:** Con **recursión** (que internamente usa una pila).

8) **¿DFS encuentra el camino más corto en grafos sin pesos?**  
**R:** No necesariamente.

9) **¿BFS y DFS se parecen en algo?**  
**R:** Sí: recorren grafos/árboles, usan visitados, y pueden guardar padres.

10) **¿Diferencia clave entre BFS y DFS?**  
**R:** BFS va por **capas**; DFS va por **profundidad**.

11) **En DFS, ¿cuándo marcas un nodo como visitado?**  
**R:** Al momento de **entrar** a ese nodo (cuando lo descubres).

12) **¿Qué pasa si en DFS no marcas visitados en un grafo con ciclo?**  
**R:** Puedes entrar en un bucle (ej: A→B→C→A…).

13) **¿El orden de visita en DFS siempre es el mismo?**  
**R:** No, depende del **orden de los vecinos**.

14) **¿Qué es el “padre” de un nodo en DFS?**  
**R:** El nodo desde el cual se descubrió por primera vez.

15) **¿Qué es un “árbol DFS”?**  
**R:** El conjunto de aristas “padre→hijo” que se forman al descubrir nodos.

16) **¿Cuál es la complejidad típica de DFS con lista de adyacencia?**  
**R:** **O(V + E)**.

17) **¿Para qué sirve DFS en problemas reales?**  
**R:** Detectar ciclos, topological sort, componentes conectadas, caminos, etc.

18) **¿Qué es “alcanzabilidad” y qué tiene que ver con DFS?**  
**R:** Ver qué nodos puedes alcanzar desde un inicio; DFS lo descubre recorriendo.

19) **¿DFS siempre visita todos los nodos del grafo?**  
**R:** Solo los **alcanzables** desde el inicio (a menos que lo ejecutes desde cada nodo no visitado).

20) **Si en un grafo A conecta con B y C, y eliges B primero, qué hará DFS?**  
**R:** Irá por **B** y seguirá profundizando por ese camino antes de volver para ir a **C**.

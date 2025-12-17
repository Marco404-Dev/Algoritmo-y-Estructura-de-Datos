## Problema vs Algoritmo
Un problema computacional define qué salidas son correctas para cada entrada (especificación).  
Un algoritmo es un procedimiento que, para cualquier entrada válida del problema, produce una salida correcta.

- **Problema:** describe la condición de corrección (qué significa “respuesta correcta”).  
- **Algoritmo:** describe el método para encontrar una respuesta y garantiza corrección para todas las entradas.

## Correctitud de Algoritmos
Para entradas arbitrariamente grandes no basta “probar casos”; se requiere una demostración.

Idea central:
- **Invariante de bucle:** condición que se mantiene verdadera en cada iteración.
- **Inducción:** Base (k=0) y paso inductivo (si funciona para k, también para k+1).
Con esto se justifica que el algoritmo mantiene la propiedad correcta durante el recorrido y produce una salida correcta al terminar.

## Complejidad Temporal
La eficiencia se analiza en función del tamaño de entrada **n** contando operaciones elementales (comparaciones, accesos, asignaciones).
Usamos notación asintótica para comparar crecimiento y omitir constantes.

- **O(f(n))** cota superior  
- **Ω(f(n))** cota inferior  
- **Θ(f(n))** cota ajustada

Idea clave: la complejidad puede mejorar cambiando la estructura de datos utilizada para almacenar/consultar información.

## Problema vs Algoritmo
Un problema computacional define qué salidas son correctas para cada entrada (especificación).  
Un algoritmo es un procedimiento que garantiza producir una salida correcta para cualquier entrada válida del problema.

- **Problema:** describe la condición de corrección (qué significa “respuesta correcta”).  
- **Algoritmo:** describe el método para encontrar la respuesta y debe funcionar para entradas arbitrariamente grandes.

## Correctitud de Algoritmos
Para entradas arbitrariamente grandes no basta “probar casos”; se requiere una demostración.

En la práctica, la correctitud se demuestra con:
- **Invariantes de bucle:** una propiedad que se mantiene verdadera en cada iteración.
- **Inducción:** Base (k=0) y paso inductivo (si funciona para k, también para k+1).

## Complejidad Temporal
La eficiencia se analiza en función del tamaño de entrada **n** contando operaciones elementales (comparaciones, accesos, asignaciones).
Usamos notación asintótica para comparar crecimiento y omitir constantes.

- **O(f(n))**: cota superior  
- **Ω(f(n))**: cota inferior  
- **Θ(f(n))**: cota ajustada

Un algoritmo se considera “eficiente” típicamente cuando corre en **tiempo polinomial** (por ejemplo, n, n log n, n²).  

## Modelo de Computación: Word-RAM
Para analizar tiempo de manera uniforme, asumimos un modelo idealizado:
- La memoria está formada por **palabras (words) de w bits**.
- Operaciones sobre un número constante de words (comparaciones, sumas, bitwise, accesos a memoria por dirección) se tratan como **O(1)**.
- Se asume que **w es suficiente para direccionar memoria** (relación con log₂(n)).

## Estructuras de Datos e Interfaces
Una estructura de datos es “almacenamiento + operaciones” (interfaz). Dos interfaces base:
- **Sequence:** importa el orden (primero, último, i-ésimo).
- **Set:** importa la clave (buscar por key).

### StaticArray (ejemplo base)
- Crear `StaticArray(n)` cuesta **Θ(n)**.
- `get_at(i)` y `set_at(i, x)` cuestan **Θ(1)**.

## Cómo abordar problemas de algoritmos
Dos caminos típicos:
1) **Reducir** el problema a uno conocido (usar una estructura/algoritmo estándar).
2) **Diseñar** un algoritmo (fuerza bruta, divide & conquer, greedy, programación dinámica, etc.).

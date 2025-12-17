## Birthday Match (Cumpleaños repetidos)

**Entrada:** lista de estudiantes `[(nombre, cumpleaños), ...]`  
**Salida:** un par `(a, b)` tal que `cumpleaños(a) = cumpleaños(b)`, o `None` si no hay coincidencias.

### Idea
Recorremos estudiantes de izquierda a derecha y vamos “recordando” los cumpleaños ya vistos.

### Correctitud (intuición / invariante)
Antes de procesar al estudiante `k`, la estructura de apoyo contiene exactamente los cumpleaños de los estudiantes `0..k-1`.
- Si el cumpleaños de `k` ya está, entonces existe un estudiante anterior con el mismo cumpleaños → devolver el par es correcto.
- Si no está, lo agregamos y el invariante se mantiene.

### Complejidad
- **Naive:** compara contra todos los anteriores → `0+1+...+(n-1)` comparaciones → **O(n²)**.
- **Fast (hash/dict):** búsqueda e inserción O(1) promedio por estudiante → **O(n)** promedio.

**Ejemplo:** `[("Ana", 10), ("Luis", 22), ("Maria", 10)]` → devuelve `("Maria", "Ana")`.

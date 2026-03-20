## 1. Planteamiento del problema

Se busca construir una función que permita **generar la sucesión de Fibonacci de manera indefinida**, produciendo sus valores uno por uno conforme se necesiten.

La sucesión de Fibonacci sigue esta regla:

- comienza con `0` y `1`
- cada nuevo término se obtiene sumando los dos anteriores

Ejemplo:

```text
0, 1, 1, 2, 3, 5, 8, 13, ...
```

El programa debe permitir:

- generar números de Fibonacci en orden
- no calcular toda la secuencia de una vez
- entregar cada valor cuando se solicite
- usar `yield` para producir los términos
- mantener actualizados los dos últimos valores
- resolver el problema con dos algoritmos distintos
- comprobar su funcionamiento con `next()`

> **Pregunta problema:**  
> ¿Cómo generar la sucesión de Fibonacci de manera continua, devolviendo un término a la vez sin almacenar toda la secuencia completa?

---

## 2. ¿En qué consiste el algoritmo?

La lógica general del código consiste en:

1. Mantener dos variables que representen términos consecutivos de Fibonacci.
2. Entregar el valor actual con `yield`.
3. Calcular el siguiente término como la suma de los dos anteriores.
4. Actualizar las variables para preparar la siguiente iteración.
5. Repetir el proceso indefinidamente.

En este caso aparecen **dos algoritmos**:

1. Uno que usa una variable auxiliar llamada `future`.
2. Otro que usa asignación simultánea para actualizar `a` y `b`.

Ambos generan exactamente la misma secuencia.

---

## 3. Estructura general del código

### 3.1. Principales métodos

#### Algoritmo 1: `fibonacci()` con variable auxiliar

**Código base:**

```python
def fibonacci():
  a = 0
  b = 1
  while True:
    yield a
    future = a + b
    a = b
    b = future
```

**Algoritmo:**

```text
Algoritmo fibonacci() con auxiliar:
    a = 0
    b = 1
    mientras sea verdadero:
        producir a
        future = a + b
        a = b
        b = future
```

**Idea central:**

- guardar los dos últimos términos de Fibonacci
- devolver el valor actual
- calcular el siguiente con una variable temporal
- desplazar los valores para continuar la secuencia
- producir infinitamente los términos uno por uno

---

#### Algoritmo 2: `fibonacci()` con asignación simultánea

**Código base:**

```python
def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a+b
```

**Algoritmo:**

```text
Algoritmo fibonacci() con asignación simultánea:
    a = 0
    b = 1
    mientras sea verdadero:
        producir a
        actualizar simultáneamente:
            a = b
            b = a + b
```

**Idea central:**

- mantener los dos términos consecutivos
- devolver el valor actual en cada iteración
- actualizar ambas variables al mismo tiempo
- escribir la misma lógica de manera más compacta
- seguir generando la secuencia indefinidamente


## Comparación directa

| Aspecto | Algoritmo 1 | Algoritmo 2 |
|---|---|---|
| Forma de actualización | Usa variable `future` | Usa asignación simultánea |
| Claridad paso a paso | Más clara | Más compacta |
| Longitud del código | Más largo | Más corto |
| Facilidad para principiantes | Mayor | Un poco menor |
| Eficiencia en tiempo | `O(1)` por término | `O(1)` por término |
| Eficiencia en espacio | `O(1)` | `O(1)` |

---

## Conclusión sobre sus diferencias

La diferencia principal entre ambos algoritmos **no está en el resultado ni en la eficiencia**, sino en la forma de expresar la actualización de los valores.

- El **algoritmo 1** es más detallado y didáctico, porque separa claramente el cálculo del siguiente término.
- El **algoritmo 2** es más elegante y compacto, porque aprovecha una característica propia de Python: la asignación simultánea.

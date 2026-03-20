# `sum.py`

## 1. Planteamiento del problema

Se busca construir una función que permita **calcular la suma total de los elementos numéricos** contenidos en una colección de datos.

El programa debe permitir:

- recibir una colección llamada `data`
- recorrer todos sus elementos
- acumular cada valor en una variable total
- devolver la suma final
- resolver el problema con dos algoritmos distintos
- comprobar que ambos producen el mismo resultado

> **Pregunta problema:**  
> ¿Cómo sumar todos los valores de una colección recorriéndola elemento por elemento?

---

## 2. ¿En qué consiste el algoritmo?

La lógica general del código consiste en:

1. Crear una variable acumuladora llamada `total` con valor inicial `0`.
2. Recorrer todos los elementos de la colección.
3. Ir agregando cada elemento a `total`.
4. Al finalizar el recorrido, devolver el valor acumulado.

En este caso aparecen **dos algoritmos**:

1. Uno que recorre directamente los elementos de `data`.
2. Otro que recorre las posiciones usando índices.

Ambos calculan exactamente la misma suma.

---

## 3. Estructura general del código

### 3.1. Principales métodos

#### Algoritmo 1: `sum(data)` recorriendo directamente los valores

**Código base:**

```python
def sum(data):
    total = 0
    for val in data:
        total += val
    return total
```

**Algoritmo:**

```text
Algoritmo sum(data) por recorrido directo:
    total = 0
    para cada val en data:
        total = total + val
    devolver total
```

**Idea central:**

- recorrer directamente cada valor de la colección
- evitar trabajar con posiciones
- acumular los valores en una variable
- devolver la suma total al final

---

#### Algoritmo 2: `sum(data)` usando índices

**Código base:**

```python
def sum(data):
    total = 0
    for j in range(len(data)):
        total += data[j]
    return total
```

**Algoritmo:**

```text
Algoritmo sum(data) por índices:
    total = 0
    para j desde 0 hasta len(data)-1:
        total = total + data[j]
    devolver total
```

**Idea central:**

- recorrer la colección usando posiciones
- acceder a cada elemento mediante su índice
- acumular cada valor en `total`
- devolver la suma final

---

## 4. Comparación directa

| Aspecto | Algoritmo 1 | Algoritmo 2 |
|---|---|---|
| Forma de recorrido | Directo sobre valores | Mediante índices |
| Claridad | Más clara | Menos directa |
| Longitud del código | Más corto | Más largo |
| Uso de posiciones | No | Sí |
| Resultado final | Igual | Igual |

---

## 5. ¿Es eficiente o no?

### Algoritmo 1

Sí, **es eficiente**.

**¿Por qué?**

- recorre la colección una sola vez -->  Tiempo: **O(n)**
- usa una variable acumuladora `total`    --> Espacio: **O(1)**
- su forma de recorrido es directa y simple
- para este problema, ese costo lineal es el esperado

---

### Algoritmo 2

Sí, **también es eficiente**.

**¿Por qué?**

- también recorre la colección una sola vez  -->  Tiempo: **O(n)**
- usa memoria constante                      --> Espacio: **O(1)**
- produce el mismo resultado correcto
- aunque es un poco más largo, sigue siendo eficiente

### Conclusión de eficiencia

Los dos algoritmos son eficientes.  
La diferencia principal no está en el rendimiento, sino en **la forma de recorrer la colección**.

---

## 11. Conclusión

Los dos algoritmos resuelven el problema de **sumar todos los elementos de una colección** usando un acumulador.

- el **algoritmo 1** recorre directamente los valores
- el **algoritmo 2** recorre las posiciones y luego accede a cada valor

Ambos tienen complejidad **O(n)** en tiempo y **O(1)** en espacio, por lo que son soluciones correctas y eficientes.

En general:

- si solo quieres sumar los valores, el **algoritmo 1** suele ser más claro
- si además necesitas trabajar con posiciones, el **algoritmo 2** puede resultar útil

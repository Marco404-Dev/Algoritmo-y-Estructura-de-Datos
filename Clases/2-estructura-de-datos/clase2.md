# 📘 Clase 2 – Estructuras de Datos (MIT 6.006)

## 1. ¿Qué es una estructura de datos?

Una **estructura de datos** es una forma de almacenar datos junto con los algoritmos que permiten realizar operaciones sobre ellos.

El conjunto de operaciones que una estructura soporta se llama **interfaz** (también conocida como API o ADT).

---

## 2. Interfaz vs Estructura

Es una distinción fundamental en algoritmos:

- **Interfaz**: especifica *qué operaciones* están disponibles (el problema).
- **Estructura de datos**: define *cómo se implementan* esas operaciones (la solución).

Una misma interfaz puede ser implementada por distintas estructuras de datos, cada una con diferentes costos computacionales.

---

## 3. Interfaces principales del curso

En el curso MIT 6.006 se trabajan principalmente **dos interfaces**: `Sequence` y `Set`.

---

## 4. Interfaz Sequence (Secuencia)

Una **secuencia** mantiene elementos ordenados por **posición**.  
El orden es **externo** y lo define el usuario.

Ejemplo:

(x0, x1, x2, ..., x n-1)



### Operaciones típicas
- Acceder al elemento i-ésimo
- Modificar un elemento
- Insertar o eliminar elementos en cualquier posición

### Ejemplos de estructuras que implementan Sequence
- Arreglo (Array)
- Lista enlazada (Linked List)
- Arreglo dinámico (Dynamic Array)
- Pila (Stack)
- Cola (Queue)

---

## 5. Interfaz Set (Conjunto)

Un **conjunto** mantiene elementos **únicos**, identificados por una **clave**.  
No existe una posición; se accede por clave.

El orden es **interno**, determinado por la clave.

### Operaciones típicas
- Buscar un elemento por clave
- Insertar un elemento
- Eliminar un elemento
- Encontrar el mínimo o máximo

### Ejemplos de estructuras que implementan Set
- Diccionario
- Set
- Tabla hash
- Árboles de búsqueda

---

## 6. Idea central del curso

> **La eficiencia de un algoritmo depende de la estructura de datos utilizada.**

No existe una estructura de datos óptima para todas las situaciones; todo implica **trade-offs**.

---

## 7. Implementaciones vistas para Sequence

### 7.1 Array (Arreglo)

**Ventajas**
- Acceso y modificación por índice en Θ(1)

**Desventajas**
- Insertar o eliminar elementos cuesta O(n)
- Requiere mover elementos y, a veces, realocar memoria

Adecuado para operaciones **estáticas**.

---

### 7.2 Linked List (Lista enlazada)

Cada elemento se almacena en un nodo con un puntero al siguiente.

**Ventajas**
- Insertar o eliminar al inicio en Θ(1)

**Desventajas**
- Acceder al elemento i-ésimo cuesta O(n)

Adecuado para operaciones **dinámicas al inicio**.

---

### 7.3 Dynamic Array (Arreglo dinámico)

Utiliza un arreglo con **espacio extra** para evitar realocar memoria en cada inserción.

Ejemplo: `list` en Python.

**Idea clave**
- Algunas operaciones son costosas
- Pero ocurren pocas veces

---

## 8. Análisis Amortizado

El **análisis amortizado** distribuye el costo de operaciones costosas sobre muchas operaciones baratas.

Una operación tiene costo amortizado `T(n)` si una secuencia de `k` operaciones cuesta a lo sumo `k · T(n)`.

### Ejemplo
- Insertar en un arreglo dinámico:
  - Normalmente cuesta Θ(1)
  - Ocasionalmente cuesta Θ(n)
  - En promedio: Θ(1) amortizado

Por eso:
- `append()` y `pop()` en Python son O(1) amortizado.

---

## 9. Tabla comparativa de estructuras (Sequence)

| Estructura       | get_at(i) | insert_first | insert_last | insert_at(i) |
|------------------|-----------|--------------|-------------|--------------|
| Array            | Θ(1)      | O(n)         | O(n)        | O(n)         |
| Linked List      | O(n)      | Θ(1)         | O(n)        | O(n)         |
| Dynamic Array    | Θ(1)      | O(n)         | Θ(1)*       | O(n)         |

\* Θ(1) amortizado

---

## 10. Conclusiones

- Una **interfaz** define qué se puede hacer
- Una **estructura de datos** define cómo se hace
- Sequence y Set son las dos interfaces principales del curso
- Elegir la estructura correcta es clave para la eficiencia
- El análisis amortizado explica por qué algunas estructuras son eficientes en promedio

---



# Clase 4: Hashing (Introducción a Algoritmos – MIT 6.006)

## 1. Repaso de estructuras de datos
Se comparan distintas estructuras según sus operaciones:

- **Array**: acceso directo, pero sin orden ni operaciones dinámicas eficientes.
- **Array ordenado**: permite búsquedas en O(log n), pero inserciones y borrados son costosos.
- **Idea central**: queremos búsquedas **más rápidas que Θ(log n)** manteniendo operaciones dinámicas.

---

## 2. Modelo de comparación y límite inferior
En el **modelo de comparación**, los algoritmos:
- Solo pueden comparar elementos (>, <, =).
- Se representan como **árboles de decisión**.

### Límite inferior
- Buscar en un conjunto de n elementos requiere al menos:
  - **Ω(log n)** comparaciones en el peor caso.
- Los arrays ordenados alcanzan este límite → **óptimos en este modelo**.
- Para ir más rápido, se necesita **más que comparaciones**.

---

## 3. Direct Access Array
### Idea
- Usar claves enteras únicas como índices de un array.
- Acceso, inserción y borrado en **O(1)** en el peor caso.

### Problema
- Requiere espacio **O(u)** donde u es el universo de claves.
- Impracticable si `u ≫ n` (ej: nombres, strings largos).

---

## 4. Hashing
### Motivación
Reducir espacio usando un array más pequeño.

### Definición
- **Función hash**:  
  `h(k): {0, …, u-1} → {0, …, m-1}`, con `m = Θ(n)`
- La estructura se llama **tabla hash**.

### Colisiones
- Son inevitables (principio del palomar).
- Dos enfoques principales:
  - **Open addressing**
  - **Chaining (encadenamiento)** ← foco de la clase

---

## 5. Chaining (encadenamiento)
- Cada posición de la tabla almacena una lista (cadena).
- Si los elementos se distribuyen bien:
  - Tamaño esperado de cada cadena: **O(1)**.
  - Todas las operaciones cuestan **O(1)** en promedio.
- Si la función hash es mala:
  - Todas las claves pueden caer en la misma posición → **Θ(n)**.

---

## 6. Funciones hash

### División (heurística)

**Definición:**  
h(k) = k mod m

**Características:**
- Es simple y rápida.
- Puede fallar si las claves tienen patrones.
- El valor de `m` suele elegirse primo y lejos de potencias de 2 o 10.
- Se usa en la práctica (por ejemplo, Python), pero con mezclas adicionales para mejorar la distribución.

---

## 7. Hashing universal (teórico)

### Idea
- Elegir la función hash **aleatoriamente** desde una familia de funciones.
- Evita que un conjunto adverso de claves provoque muchas colisiones.

### Función hash
h_ab(k) = ((a · k + b) mod p) mod m  

Donde:
- `p` es un número primo mayor que el universo de claves `u`
- `a ≠ 0` y `b` se eligen aleatoriamente

### Propiedad clave (universalidad)
Para dos claves distintas `ki ≠ kj`:
- Pr[h(ki) = h(kj)] ≤ 1 / m

### Consecuencia
- El tamaño esperado de una cadena es:
  - E[X] ≤ 1 + (n − 1) / m
- Si `m = Θ(n)`, entonces el tiempo esperado es **O(1)**.

---

## 8. Factor de carga

- Se define como: α = n / m
- Mantener α constante garantiza buen rendimiento.
- Si α se aleja mucho de 1:
  - Se reconstruye la tabla con un nuevo tamaño y una nueva función hash.
- El costo se analiza de forma amortizada (similar a arrays dinámicos).

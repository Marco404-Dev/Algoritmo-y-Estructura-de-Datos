# Clase 4: Hashing (Introducción a Algoritmos – MIT 6.006)

#### Repaso de estructuras de datos
Se comparan distintas estructuras según sus operaciones:

- **Array**: acceso directo, pero sin orden ni operaciones dinámicas eficientes.
- **Array ordenado**: permite búsquedas en O(log n), pero inserciones y borrados son costosos.
- **Idea central**: queremos búsquedas **más rápidas que Θ(log n)** manteniendo operaciones dinámicas.

---
# Hashing (Tabla Hash)

## 1) ¿Qué es hashing?
**Hashing** es una técnica para **guardar y buscar datos rápido**.

La idea es transformar una **clave (key)** en un **índice (posición)** dentro de un arreglo llamado **tabla hash**.

- **Clave (key):** lo que identifica un dato (ej: 42, DNI, “Ana”).
- **Tabla hash:** arreglo con casillas/cajones (ej: 0..9).
- **Función hash:** regla que convierte la clave en un índice.

---

## 2) Función hash (regla)
Una función hash responde:
> “¿En qué cajón guardo/busco esta clave?”

Ejemplo simple:
- Tabla con 10 cajones: `0..9`
- Regla: **quedarse con el último dígito**
  - `h(k) = k mod 10`

---

## 3) Ejemplo de guardar
Claves: `27, 18, 39, 41`

- `h(27) = 7` → cajón 7
- `h(18) = 8` → cajón 8
- `h(39) = 9` → cajón 9
- `h(41) = 1` → cajón 1

Quedaría:

- `1: [41]`
- `7: [27]`
- `8: [18]`
- `9: [39]`

---

## 4) Buscar un elemento
Para buscar `39`:

1. Calculas `h(39) = 9`
2. Vas directo al cajón 9
3. Ahí lo encuentras

✅ En vez de revisar todos los datos, vas **directo** a la posición.

---

## 5) Colisiones (choques)
Una **colisión** ocurre cuando **dos claves caen en el mismo cajón**.

Ejemplo:
- `h(52) = 2`
- `h(42) = 2`

Ambos van al cajón 2 → **colisión**.

Importante:
- `42` no solo choca con `52`, choca con **cualquier número que termine en 2**, porque todos van al cajón 2.

---

## 6) Solución común: Chaining (lista por cajón)
La solución más simple es:
> Cada cajón guarda una **lista**.

Entonces, si hay colisión, se guardan juntos:

- `cajón 2: [52, 42]`

---

## 7) Operaciones típicas (con chaining)
### Insertar (insert)
- Calculas `h(k)`
- Agregas `k` a la lista del cajón

### Buscar (find/search)
- Calculas `h(k)`
- Vas al cajón
- Buscas dentro de la lista

### Eliminar (delete)
- Calculas `h(k)`
- Vas al cajón
- Eliminas `k` de la lista

---

## 8) ¿Para qué sirve hashing?
✅ **Para mejorar la velocidad de búsqueda**, porque normalmente:
- No buscas en toda la lista
- Vas directo a un cajón (y revisas una lista pequeña si hubo colisión)

---

## Mini-ejemplo (como el que resolvimos)
Tabla tamaño 10, regla `h(k)=k mod 10`:

- `52 → 2`
- `42 → 2`

Hay colisión → se guarda en lista:

- `2: [52, 42]`



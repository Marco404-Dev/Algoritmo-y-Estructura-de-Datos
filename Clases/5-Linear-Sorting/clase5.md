# Linear Sorting (explicación súper sencilla)

## ¿Qué es “linear sorting”?
Es **ordenar** una lista en un tiempo que crece “parejito” con la cantidad de datos.

- Si tienes **10** números → tarda aprox **10** pasos.
- Si tienes **100** números → tarda aprox **100** pasos.

Eso es “lineal”.

📌 OJO: esto solo funciona bien cuando los datos tienen estructura (por ejemplo, **enteros** en un rango o números con **dígitos**).

---

## ¿Por qué no todos los ordenamientos son lineales?
Los métodos típicos (QuickSort, MergeSort) ordenan comparando:
- “¿A < B?”
- “¿A > B?”

Eso obliga a hacer muchas comparaciones, y por eso suelen ser como **n log n**.

En cambio, los “linear sorting” intentan:
✅ **no comparar uno por uno**, sino usar **casilleros** o **dígitos**.

---

# 1) Counting Sort (el más fácil)

### Idea: “casilleros por número”
Si tus números están en un rango pequeño, por ejemplo de **0 a 9**,
haces 10 casilleros (0..9) para **contar**.

Ejemplo:
Lista: `[4, 2, 2, 8, 3, 3, 1]`

Cuentas cuántas veces aparece cada número:

- 0 → 0 veces  
- 1 → 1 vez  
- 2 → 2 veces  
- 3 → 2 veces  
- 4 → 1 vez  
- 5 → 0  
- 6 → 0  
- 7 → 0  
- 8 → 1 vez  
- 9 → 0  

Luego reconstruyes el resultado leyendo casillero por casillero:
✅ `[1, 2, 2, 3, 3, 4, 8]`

### ¿Por qué es rápido?
Porque:
- recorres la lista 1 vez (para contar)
- recorres los casilleros 1 vez (para reconstruir)

📌 Sirve si el rango es pequeño (notas 0-20, edades 0-120, etc.)
📌 No conviene si el rango es enorme (por ejemplo hasta 1,000,000,000)

---

# 2) Radix Sort (cuando los números son grandes)

### Idea: ordenar por “dígitos”
En vez de usar un casillero para cada número grande, ordenas por partes:

Ejemplo:
`[32, 03, 44, 42, 22]`

**Paso 1:** ordenar por el último dígito (unidades)  
**Paso 2:** ordenar por el siguiente dígito (decenas)

Resultado final:
✅ `[03, 22, 32, 42, 44]`

📌 Es rápido si los números tienen pocos dígitos (como enteros normales de computadora).

---

## Resumen ultra corto
- **Counting sort:** “cuento cuántas veces sale cada número y lo reconstruyo”.
- **Radix sort:** “ordeno por dígitos (unidades, decenas, etc.)”.

---

## Para aplicarlo a tu caso (respóndeme luego)
1) ¿Tus datos son **enteros**?
2) ¿Más o menos cuál es el **máximo**? (ej: 100, 1000, 1 millón)

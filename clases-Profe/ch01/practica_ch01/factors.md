# `factors.py`

## 1. Planteamiento del problema

Se busca construir una función que permita **encontrar los factores o divisores de un número entero positivo `n`**.

Un factor de `n` es un número que divide a `n` exactamente, es decir, sin dejar residuo.

El programa debe permitir:

- recibir un número entero positivo `n`
- revisar qué números dividen exactamente a `n`
- obtener todos sus factores
- mostrar los factores encontrados
- resolver el problema de tres maneras distintas
- comparar una versión con lista
- comparar una versión con `yield`
- comparar una versión optimizada usando pares de divisores

> **Pregunta problema:**  
> ¿Cómo encontrar todos los factores de un número `n`, y cuál de las tres formas propuestas resulta más eficiente?

---

## 2. ¿En qué consiste el algoritmo?

La lógica general del problema consiste en:

1. Tomar un número `n`.
2. Probar si otros números lo dividen exactamente.
3. Cada vez que un número divide a `n` sin residuo, considerarlo factor.
4. Repetir el proceso hasta encontrar todos los divisores.

En este caso aparecen **tres algoritmos**:

1. Uno que recorre todos los números de `1` hasta `n` y guarda los factores en una lista.
2. Otro que también recorre de `1` hasta `n`, pero en lugar de guardar todo, va entregando los factores con `yield`.
3. Otro más eficiente que solo revisa hasta la raíz cuadrada de `n` y aprovecha que los factores aparecen en pares.

---

## 3. Estructura general del código

### 3.1. Principales métodos

#### Algoritmo 1: `factors(n)` usando lista

**Código base:**

```python
def factors(n):
  results = []
  for k in range(1, n+1):
    if n % k == 0:
      results.append(k)
  return results
```
**pseudocodigo**
```text
Algoritmo factors(n) con lista:
    crear lista vacía results
    para k desde 1 hasta n:
        si n mod k == 0:
            agregar k a results
    devolver results
```
Idea central:

- revisar todos los números desde 1 hasta n
- comprobar cuáles dividen exactamente a n
- guardar cada factor en una lista
- devolver al final la lista completa de factores



#### Algoritmo 2: factors(n) usando yield

**Código base:**
```python
def factors(n):
  for k in range(1, n+1):
    if n % k == 0:
      yield k
```
**pseudocodigo**
```text
Algoritmo factors(n) con yield:
    para k desde 1 hasta n:
        si n mod k == 0:
            producir k con yield
```

Idea central:

- revisar todos los números desde 1 hasta n
- detectar cuáles son factores
- no guardar todos los factores en una lista
- ir entregando cada factor uno por uno a medida que se encuentra


#### Algoritmo 3: factors(n) optimizado con raíz cuadrada

**Código base:**
```python
def factors(n):
  k = 1
  while k * k < n:
    if n % k == 0:
      yield k
      yield n // k
    k += 1
  if k * k == n:
    yield k
```

**pseudocodigo**

```text
Algoritmo factors(n) optimizado:
    k = 1
    mientras k*k < n:
        si n mod k == 0:
            producir k
            producir n // k
        aumentar k en 1
    si k*k == n:
        producir k
```

Idea central:

- no revisar hasta n, sino solo hasta la raíz cuadrada de n
- aprovechar que los factores vienen en pares
- si k divide a n, entonces también n // k es factor
- reducir mucho la cantidad de iteraciones
- tratar aparte el caso en que n sea cuadrado perfecto



## ¿Es eficiente o no?

### Algoritmo 1

Es correcto, pero **no es el más eficiente**.

**¿Por qué?**

- revisa todos los números hasta `n`
- además guarda todos los factores en una lista
- funciona bien, pero consume más tiempo y más memoria que otras opciones

---

### Algoritmo 2

Es correcto y **mejora en memoria**, pero **no mejora en tiempo** frente al primero.

**¿Por qué?**

- sigue revisando todos los números hasta `n`
- la diferencia es que no almacena todo junto
- va entregando los resultados uno por uno

---

### Algoritmo 3

Es el **más eficiente de los tres**.

**¿Por qué?**

- no necesita revisar todos los números hasta `n`
- solo llega hasta `√n`
- aprovecha la simetría de los factores
- reduce mucho el número de comprobaciones

##  Comparación entre los tres algoritmos

| Algoritmo | Forma de trabajo | Tiempo | Espacio extra | ¿Más eficiente? |
|---|---|---:|---:|---|
| 1. Lista completa | Recorre de `1` a `n` y guarda factores | `O(n)` | mayor que los otros | No |
| 2. `yield` completo | Recorre de `1` a `n` y produce factores | `O(n)` | `O(1)` | Mejor en memoria, no en tiempo |
| 3. Optimizado | Recorre hasta `√n` y usa pares | `O(√n)` | `O(1)` | Sí |

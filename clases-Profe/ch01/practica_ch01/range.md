# `range.py`

## 1. Planteamiento del problema

Se busca construir una función similar a `range` de Python, que permita **generar una secuencia de números enteros** a partir de ciertos parámetros de inicio, fin y paso.

El código debe permitir:

- recibir un valor inicial `start`
- recibir opcionalmente un valor final `stop`
- recibir opcionalmente un valor de avance `step`
- interpretar correctamente el caso en que solo se pasa un argumento
- generar los valores uno por uno usando `yield`
- soportar avance positivo
- soportar avance negativo
- detenerse correctamente antes de sobrepasar el límite
- evitar el caso inválido en el que `step = 0`
- comprobar el funcionamiento con varios ejemplos

**Código trabajado:**

```python
def range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    if step == 0:
        raise ValueError("step no puede ser 0")

    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step


# pruebas
print(list(range(5)))         # [0, 1, 2, 3, 4]
print(list(range(2, 8)))      # [2, 3, 4, 5, 6, 7]
print(list(range(2, 10, 2)))  # [2, 4, 6, 8]
print(list(range(10, 2, -2))) # [10, 8, 6, 4]
```

> **Pregunta problema:**  
> ¿Cómo construir una función tipo `range` que genere números enteros correctamente con uno, dos o tres parámetros, incluyendo pasos positivos y negativos?

---

## 2. ¿En qué consiste el algoritmo?

La lógica general del código consiste en:

1. Recibir los parámetros `start`, `stop` y `step`.
2. Verificar si solo se pasó un argumento.
3. Si solo se pasó uno, convertirlo en el valor final y colocar `0` como inicio.
4. Validar que `step` no sea `0`.
5. Si el paso es positivo, generar números mientras `start < stop`.
6. Si el paso es negativo, generar números mientras `start > stop`.
7. En cada iteración, producir el valor actual con `yield`.
8. Actualizar `start` sumándole `step`.
9. Detenerse automáticamente cuando ya no se cumpla la condición.

En otras palabras, el algoritmo **genera una secuencia controlada de enteros**, avanzando en cada iteración según el valor de `step`.

---

## 3. Estructura general del código

### 3.1. Principales métodos o bloques

#### Función `range(start, stop=None, step=1)`

**Código base:**

```python
def range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    if step == 0:
        raise ValueError("step no puede ser 0")

    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step
```

**Algoritmo:**

```text
Algoritmo range(start, stop=None, step=1):
    si stop es None:
        stop = start
        start = 0

    si step == 0:
        lanzar error

    si step > 0:
        mientras start < stop:
            producir start
            start = start + step
    si no:
        mientras start > stop:
            producir start
            start = start + step
```

**Idea central:**

- adaptar los parámetros cuando solo se ingresa un valor
- validar que el paso no sea cero
- usar una condición distinta según el paso sea positivo o negativo
- producir los valores uno por uno con `yield`
- detener la secuencia justo antes de cruzar el límite

---

#### Bloque `if stop is None`

**Algoritmo:**

```text
Si stop es None:
    stop = start
    start = 0
```

**Idea central:**

- detectar la llamada con un solo argumento
- imitar el comportamiento de `range(n)` en Python
- transformar internamente `range(5)` en `range(0, 5, 1)`

---

#### Bloque `if step == 0`

**Algoritmo:**

```text
Si step es 0:
    lanzar ValueError
```

**Idea central:**

- evitar un bucle infinito
- impedir un paso inválido
- proteger el funcionamiento correcto del algoritmo

---

#### Bloque para `step > 0`

**Algoritmo:**

```text
Mientras start < stop:
    producir start
    start = start + step
```

**Idea central:**

- generar la secuencia creciente
- seguir avanzando mientras no se alcance el límite
- detenerse antes de llegar o sobrepasar `stop`

---

#### Bloque para `step < 0`

**Algoritmo:**

```text
Mientras start > stop:
    producir start
    start = start + step
```

**Idea central:**

- generar la secuencia decreciente
- seguir avanzando hacia abajo
- detenerse antes de caer por debajo o llegar al límite

---

#### Bloque de pruebas

**Algoritmo:**

```text
Crear varios casos de prueba
Convertir el generador en lista
Imprimir los resultados
Verificar que coincidan con lo esperado
```

**Idea central:**

- comprobar llamadas con un argumento
- comprobar llamadas con dos argumentos
- comprobar llamadas con paso positivo
- comprobar llamadas con paso negativo

---

### Algoritmo general

1. Recibir los parámetros de inicio, fin y paso.
2. Ajustar los parámetros si solo se proporcionó un valor.
3. Verificar que el paso no sea cero.
4. Elegir el tipo de recorrido:
   - creciente si el paso es positivo
   - decreciente si el paso es negativo
5. Generar cada valor con `yield`.
6. Actualizar el valor actual sumando `step`.
7. Detenerse cuando ya no se cumpla la condición del recorrido.

---

## 5. Complejidad Big O

### Tiempo: **O(n)**

Porque:

- genera un valor por iteración
- si la secuencia tiene `n` elementos, realiza aproximadamente `n` repeticiones
- el tiempo depende de cuántos números produce

### Espacio: **O(1)**

Porque:

- no guarda toda la secuencia en memoria dentro de la función
- solo mantiene unas pocas variables: `start`, `stop` y `step`
- los valores se producen uno por uno con `yield`

---

## 6. ¿Es eficiente o no?

Sí, **es eficiente**.

### ¿Por qué?

Porque:

- usa `yield`, así que no construye una lista completa dentro de la función
- genera los valores solo cuando se necesitan
- utiliza memoria constante
- recorre exactamente la cantidad necesaria de pasos

Para una función tipo `range`, este comportamiento es el adecuado.

---

## 9. Observación importante

Esta función usa `yield`, por lo tanto **no devuelve una lista**, sino un **generador**.

Por eso, para ver todos los resultados juntos, en las pruebas se usa:

```python
list(range(...))
```

Eso convierte los valores generados en una lista visible.

---

## 10. Conclusión

Este algoritmo resuelve el problema de construir una función tipo `range` que:

- acepta uno, dos o tres argumentos
- soporta pasos positivos y negativos
- detecta el caso inválido de `step = 0`
- genera los números uno por uno usando `yield`

Tiene complejidad **O(n)** en tiempo y **O(1)** en espacio, por lo que es una solución correcta y eficiente.

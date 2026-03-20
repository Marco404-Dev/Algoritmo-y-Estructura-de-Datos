# `scale.py`

## 1. Planteamiento del problema

Se busca construir una función que permita **multiplicar todos los elementos de una colección numérica por un mismo factor**, modificando directamente los valores originales.

El programa debe permitir:

- recibir una colección llamada `data`
- recibir un valor multiplicador llamado `factor`
- recorrer todos los elementos de la colección
- acceder a cada posición mediante su índice
- multiplicar cada elemento por el mismo factor
- guardar el nuevo valor en la misma colección
- modificar la lista original sin crear otra nueva
- mostrar el resultado final después de la transformación

> **Pregunta problema:**  
> ¿Cómo recorrer una lista y escalar todos sus elementos por un mismo factor, modificando directamente la colección original?

---

## 2. ¿En qué consiste el algoritmo?

La lógica general del código consiste en:

1. Recibir una lista de números y un factor de escala.
2. Recorrer todas las posiciones de la lista.
3. En cada posición, tomar el valor actual.
4. Multiplicarlo por el factor.
5. Guardar el resultado en la misma posición.
6. Al finalizar, la lista original queda modificada.

En otras palabras, el algoritmo realiza una **transformación secuencial en el mismo arreglo o lista**, cambiando cada elemento uno por uno.

---

## 3. Estructura general del código

### 3.1. Principales métodos

#### Función `scale(data, factor)`

**Código base:**

```python
def scale(data, factor):
  for j in range(len(data)):
    data[j] *= factor
```

**Algoritmo:**

```text
Algoritmo scale(data, factor):
    para j desde 0 hasta len(data)-1:
        data[j] = data[j] * factor
```

**Idea central:**

- recorrer la colección usando índices
- acceder directamente a cada posición
- multiplicar cada elemento por el mismo factor
- reemplazar el valor anterior por el nuevo
- Terminar con la lista ya modificada.


---

## 4. ¿Es eficiente o no?

Sí, **es eficiente**.

### ¿Por qué?

Porque:

- recorre la lista una sola vez --> Tiempo: **O(n)**
- modifica la colección directamente, solo usa la variable j como control mas no se crea una lista nueva  ---> Espacio: **O(1)**
- no desperdicia memoria creando otra lista
- el costo lineal es el esperado para transformar todos los elementos

Para este problema, su comportamiento es adecuado y natural.

---

## 5. Observación importante

Este algoritmo **sí modifica la lista original**.

Eso significa que:

- no devuelve una nueva lista
- tampoco usa `return`
- el cambio ocurre directamente sobre `data`

Por eso, después de llamar:

```python
scale(nums, 3)
```

la variable `nums` ya queda cambiada.

---

## 6. ¿Por qué usa índices y no recorrido directo?

Se usan índices porque el algoritmo necesita **reemplazar** cada valor dentro de la lista.

Por ejemplo:

```python
for j in range(len(data)):
    data[j] *= factor
```

aquí sí se puede modificar la posición exacta.

En cambio, si solo hicieras algo como:

```python
for val in data:
    val *= factor
```

eso no cambiaría realmente los elementos guardados en la lista, porque `val` sería solo una variable temporal del recorrido.

---

## 7. Diferencia con `sum`

- `sum` es un algoritmo de **acumulación**
- `scale` es un algoritmo de **transformación**


# `heartrate.py`

## 1. Planteamiento del problema

Se busca construir un programa que permita **calcular la frecuencia cardíaca objetivo para quemar grasa** de una persona a partir de su edad.

El programa debe permitir:

- pedir la edad del usuario en años
- convertir esa entrada a un número entero
- calcular la frecuencia cardíaca máxima estimada
- calcular la frecuencia objetivo de quema de grasa
- mostrar el resultado final al usuario

**Código trabajado:**

```python
age = int(input('Enter your age in years: '))
max_heart_rate = 206.9 - (0.67 * age)
target = 0.65 * max_heart_rate
print('Your target fat-burning heart rate is', target)
```

**Pseudocódigo:**

```text
Algoritmo heartrate:
    leer edad
    convertir edad a entero
    calcular frecuencia máxima:
        max_heart_rate = 206.9 - (0.67 * age)
    calcular frecuencia objetivo:
        target = 0.65 * max_heart_rate
    imprimir target
```

> **Pregunta problema:**  
> ¿Cómo calcular la frecuencia cardíaca objetivo para quemar grasa a partir de la edad del usuario?

---

## 2. ¿En qué consiste el algoritmo?

La lógica general del código consiste en:

1. Pedir al usuario su edad.
2. Convertir esa edad a entero.
3. Calcular la frecuencia cardíaca máxima con una fórmula.
4. Calcular el 65% de esa frecuencia máxima.
5. Mostrar el resultado obtenido.

En otras palabras, el algoritmo toma un dato de entrada, realiza operaciones matemáticas directas y entrega un resultado final.

---

## 3. Estructura general del código

### 3.1. Código principal

**Idea central:**

- obtener la edad del usuario
- usar esa edad para estimar la frecuencia cardíaca máxima
- calcular la zona de quema de grasa como el 65% de ese valor
- mostrar el resultado final

### Algoritmo general

1. Leer la edad del usuario.
2. Convertir la entrada en entero.
3. Aplicar la fórmula de frecuencia máxima.
4. Calcular la frecuencia objetivo.
5. Mostrar el resultado.

---

## 4. Complejidad Big O

### Tiempo: **O(1)**

Porque:

- realiza una cantidad fija de operaciones
- no depende del tamaño de ninguna colección
- siempre ejecuta los mismos pasos

### Espacio: **O(1)**

Porque:

- solo usa unas pocas variables:
  - `age`
  - `max_heart_rate`
  - `target`

---

## 5. ¿Es eficiente o no?

Sí, **es eficiente**.

### ¿Por qué?

Porque:

- usa pocas operaciones matemáticas
- no requiere recorridos ni estructuras adicionales
- consume memoria constante
- produce el resultado de manera inmediata

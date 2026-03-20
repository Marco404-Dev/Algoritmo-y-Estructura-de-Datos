# `gpa.py`

## 1. Planteamiento del problema

Se busca construir un programa que permita **calcular el GPA (Grade Point Average)** a partir de calificaciones en letras.

En este caso aparecen **dos algoritmos**:

- **GPA 1:** pide las notas al usuario una por una usando `input()`
- **GPA 2:** recibe las notas como parámetro dentro de una función

El programa debe permitir:

- trabajar con calificaciones en letras como `A`, `B+`, `C-`, `F`
- convertir cada calificación a puntos numéricos usando un diccionario
- acumular el total de puntos
- contar cuántos cursos válidos se ingresaron
- calcular el promedio final
- ignorar notas inválidas
- mostrar o devolver el GPA final

**Código trabajado:**

```python
# GPA 1
print('Bienvenido al calculador de GPA.')
print('Por favor, ingresa todas tus calificaciones con letras, una por línea.')
print('Ingresa una línea en blanco para indicar el final.')

points = {'A+':4.0, 'A':4.0, 'A-':3.67, 'B+':3.33, 'B':3.0, 'B-':2.67,
          'C+':2.33, 'C':2.0, 'C-':1.67, 'D+':1.33, 'D':1.0, 'F':0.0}

num_courses = 0
total_points = 0
done = False

while not done:
    grade = input()
    if grade == '':
        done = True
    elif grade not in points:
        print("Calificación desconocida '{0}', será ignorada".format(grade))
    else:
        num_courses += 1
        total_points += points[grade]

if num_courses > 0:
    print('Tu GPA es {0:.3f}'.format(total_points / num_courses))


# GPA 2
def compute_gpa(grades, points={'A+':4.0, 'A':4.0, 'A-':3.67, 'B+':3.33,
                                'B':3.0, 'B-':2.67, 'C+':2.33, 'C':2.0,
                                'C-':1.67, 'D+':1.33, 'D':1.0, 'F':0.0}):
    num_courses = 0
    total_points = 0
    for g in grades:
        if g in points:
            num_courses += 1
            total_points += points[g]
    return total_points / num_courses
```

**Pseudocódigo:**

```text
Algoritmo GPA 1:
    mostrar mensaje de bienvenida
    crear diccionario de equivalencias entre nota y puntaje
    num_courses = 0
    total_points = 0
    done = False

    mientras done sea falso:
        leer una calificación
        si la calificación es vacía:
            done = True
        sino si la calificación no está en el diccionario:
            mostrar mensaje de nota desconocida
        sino:
            aumentar num_courses en 1
            sumar a total_points el valor correspondiente

    si num_courses > 0:
        imprimir total_points / num_courses
```

```text
Algoritmo GPA 2:
    recibir una colección grades
    crear diccionario de equivalencias entre nota y puntaje
    num_courses = 0
    total_points = 0

    para cada g en grades:
        si g está en el diccionario:
            aumentar num_courses en 1
            sumar a total_points el valor correspondiente

    devolver total_points / num_courses
```

> **Pregunta problema:**  
> ¿Cómo calcular el GPA a partir de calificaciones en letras, ya sea leyéndolas desde la entrada del usuario o recibiéndolas como una colección?

---

## 2. ¿En qué consiste el algoritmo?

La lógica general del problema consiste en:

1. Tener una tabla de equivalencias entre calificaciones y puntos.
2. Leer o recibir las calificaciones.
3. Revisar cuáles son válidas.
4. Sumar los puntos correspondientes.
5. Contar cuántos cursos válidos hay.
6. Dividir el total de puntos entre la cantidad de cursos válidos.
7. Mostrar o devolver el GPA.

En este caso:

- el **primer algoritmo** trabaja de forma interactiva con `input()`
- el **segundo algoritmo** trabaja de forma más reutilizable, recibiendo las notas como parámetro

Ambos resuelven el mismo problema central: **calcular el promedio de puntos de calificaciones válidas**.

---

## 3. Estructura general del código

### 3.1. Código principal

#### Algoritmo 1: GPA interactivo con `input()`

**Idea central:**

- pedir notas una por una
- detener la lectura cuando el usuario ingresa una línea vacía
- ignorar notas que no existan en el diccionario
- acumular puntos y cantidad de cursos
- imprimir el GPA al final

---

#### Algoritmo 2: `compute_gpa(grades)`

**Idea central:**

- recibir una colección de notas ya existente
- recorrer las notas una por una
- validar cuáles están en el diccionario
- acumular puntos y cantidad de cursos válidos
- devolver el GPA como resultado de la función

---

### Algoritmo general

1. Definir un diccionario que traduzca notas en letras a puntos numéricos.
2. Obtener las calificaciones:
   - con `input()` en el algoritmo 1
   - como parámetro en el algoritmo 2
3. Recorrer las notas.
4. Verificar si cada nota existe en el diccionario.
5. Si es válida, sumar sus puntos y contar el curso.
6. Calcular el promedio final.
7. Mostrarlo o devolverlo.

---

## 4. Diferencias entre los 2 algoritmos

### Algoritmo 1: interactivo

**Características:**

- pide las notas directamente al usuario
- usa `input()`
- termina cuando el usuario ingresa una línea vacía
- muestra mensajes durante la ejecución
- es útil para programas sencillos y pruebas manuales

### Algoritmo 2: función reutilizable

**Características:**

- no usa `input()`
- recibe las notas como argumento
- devuelve el resultado con `return`
- puede reutilizarse en otros programas
- es más práctico para modularidad y pruebas automáticas

---

## 5. Comparación directa

| Aspecto | GPA 1 | GPA 2 |
|---|---|---|
| Forma de entrada | `input()` | parámetro `grades` |
| Interacción con usuario | Sí | No |
| Reutilizable en otros programas | Menos | Más |
| Resultado final | `print()` | `return` |
| Modularidad | Menor | Mayor |
| Facilidad para probar con datos ya dados | Menor | Mayor |


---

## 7. Complejidad Big O

### Tiempo: **O(n)**

Porque:

- ambos algoritmos revisan las notas una por una
- si hay `n` calificaciones, realizan aproximadamente `n` iteraciones

### Espacio: **O(1)** extra

Porque:

- solo usan unas pocas variables adicionales:
  - `num_courses`
  - `total_points`
  - `grade` o `g`
- el diccionario de puntos es fijo, no crece con la entrada

---

## 8. ¿Es eficiente o no?

Sí, **ambos son eficientes**.

### ¿Por qué?

Porque:

- recorren las notas una sola vez
- usan un diccionario para consultar puntajes de forma rápida
- no crean estructuras grandes adicionales
- el costo lineal es el adecuado para este problema

### Diferencia de eficiencia práctica

- en **rendimiento**, ambos son similares
- en **diseño**, el segundo suele ser mejor porque es más reutilizable y modular


---

### Observación 2: posible división entre cero

En el segundo algoritmo, si ninguna nota válida aparece en `grades`, entonces:

```python
num_courses = 0
```

y al hacer:

```python
return total_points / num_courses
```

se produciría un error de división entre cero.

Por eso, una versión más segura sería:

```python
def compute_gpa(grades, points={'A+':4.0, 'A':4.0, 'A-':3.67, 'B+':3.33,
                                'B':3.0, 'B-':2.67, 'C+':2.33, 'C':2.0,
                                'C-':1.67, 'D+':1.33, 'D':1.0, 'F':0.0}):
    num_courses = 0
    total_points = 0
    for g in grades:
        if g in points:
            num_courses += 1
            total_points += points[g]
    if num_courses == 0:
        return 0
    return total_points / num_courses
```

---

## 11. Conclusión

Ambos algoritmos resuelven el problema de **calcular el GPA** a partir de calificaciones en letras.

- el **GPA 1** es interactivo y pide las notas una por una
- el **GPA 2** es más modular y recibe las notas como parámetro

Los dos usan la misma idea base:

- traducir letras a puntos
- sumar los puntos
- contar cursos válidos
- calcular el promedio final

Tienen complejidad **O(n)** en tiempo y **O(1)** en espacio extra, por lo que son soluciones correctas y eficientes.

## 12. Nombre principal de cada algoritmo

Para que no se te mezclen, puedes quedarte con estos nombres:

- **Algoritmo 1:** cálculo de GPA interactivo
- **Algoritmo 2:** cálculo de GPA por función

# `age.py`

## 1. Planteamiento del problema

Se busca construir un programa que permita **pedir la edad del usuario de forma segura**, verificando que el valor ingresado sea válido antes de aceptarlo.

La edad ingresada debe cumplir ciertas condiciones:

- debe ser un número entero
- debe ser positiva
- no debe aceptar texto u otros datos inválidos
- debe seguir pidiendo el dato mientras la entrada no sea correcta
- debe manejar errores de lectura sin que el programa falle de inmediato

El programa debe permitir:

- pedir la edad al usuario
- convertir la entrada a entero
- validar que la edad sea mayor que cero
- mostrar mensajes de error si la entrada no es correcta
- repetir la solicitud mientras la respuesta siga siendo inválida
- resolver el problema con dos algoritmos distintos de manejo de excepciones

> **Pregunta problema:**  
> ¿Cómo pedir la edad del usuario de manera segura, validando que sea un entero positivo y controlando errores de entrada sin romper el programa?

---

## 2. ¿En qué consiste el algoritmo?

La lógica general del código consiste en:

1. Inicializar la variable `age` con un valor inválido, por ejemplo `-1`.
2. Repetir el proceso mientras `age` siga siendo menor o igual a `0`.
3. Pedir al usuario que ingrese su edad.
4. Intentar convertir la entrada a número entero.
5. Verificar si el número ingresado es positivo.
6. Si la entrada no es un entero o ocurre un error de lectura, capturar la excepción.
7. Mostrar un mensaje adecuado y volver a pedir el dato.

En este caso aparecen **dos algoritmos**:

1. Uno que captura `ValueError` y `EOFError` en un solo bloque.
2. Otro que captura cada excepción por separado y además vuelve a lanzar `EOFError`.

Ambos buscan validar correctamente la entrada, pero no reaccionan exactamente igual ante los errores.

---

## 3. Estructura general del código

### 3.1. Principales métodos o bloques

#### Algoritmo 1: manejo conjunto de excepciones

**Código base:**

```python
age = -1
while age <= 0:
  try:
    age = int(input('Enter your age in years: '))
    if age <= 0:
      print('Your age must be positive')
  except (ValueError, EOFError):
    print('Invalid response')
```

**Algoritmo:**

```text
Algoritmo validación de edad con excepción conjunta:
    age = -1
    mientras age <= 0:
        intentar:
            leer edad ingresada
            convertir la entrada a entero
            si age <= 0:
                imprimir que la edad debe ser positiva
        si ocurre ValueError o EOFError:
            imprimir respuesta inválida
```

**Idea central:**

- usar un valor inicial inválido para forzar la entrada al ciclo
- seguir pidiendo la edad hasta que sea correcta
- controlar en un solo bloque dos tipos de error
- simplificar el manejo de excepciones
- mostrar un mensaje general cuando algo sale mal

---

#### Algoritmo 2: manejo separado de excepciones

**Código base:**

```python
age = -1
while age <= 0:
  try:
    age = int(input('Enter your age in years: '))
    if age <= 0:
      print('Your age must be positive')
  except ValueError:
    print('That is an invalid age specification')
  except EOFError:
    print('There was an unexpected error reading input.')
    raise
```

**Algoritmo:**

```text
Algoritmo validación de edad con excepción separada:
    age = -1
    mientras age <= 0:
        intentar:
            leer edad ingresada
            convertir la entrada a entero
            si age <= 0:
                imprimir que la edad debe ser positiva
        si ocurre ValueError:
            imprimir que la edad ingresada no es válida
        si ocurre EOFError:
            imprimir que hubo un error inesperado de lectura
            relanzar la excepción
```

**Idea central:**

- seguir pidiendo la edad hasta que sea válida
- distinguir el tipo de error ocurrido
- dar mensajes más específicos al usuario
- tratar `EOFError` como un problema más serio
- volver a lanzar la excepción cuando el error no debe ocultarse


---

## 4. Diferencias entre los 2 algoritmos

Aunque ambos algoritmos validan la edad, tienen diferencias importantes en el manejo de errores.

## 4. Comparación directa

| Aspecto | Algoritmo 1 | Algoritmo 2 |
|---|---|---|
| Manejo de errores | Conjunto | Separado |
| Mensaje al usuario | General | Específico |
| Claridad del motivo del error | Menor | Mayor |
| Longitud del código | Más corto | Más largo |
| Re-lanzamiento de excepción | No | Sí, con `EOFError` |
| Facilidad para principiantes | Mayor | Intermedia |

---

## 5. ¿Es eficiente o no?

Los dos son eficientes en memoria y en estructura.  
La diferencia principal está en el **nivel de control del error**, no en el rendimiento.

---

## 6. Observación importante sobre `raise`

En el segundo algoritmo aparece:

```python
raise
```

Esto significa:

- volver a lanzar la excepción que acaba de ocurrir
- no esconder completamente el error
- permitir que otro nivel del programa lo maneje
- indicar que `EOFError` se considera más serio que un simple dato mal escrito

---

## 7. Conclusión

Los dos algoritmos resuelven el problema de **validar una edad ingresada por el usuario**, asegurando que sea un entero positivo y manejando errores de entrada.

La diferencia principal está en el tratamiento de las excepciones:

- el **algoritmo 1** es más simple y agrupa los errores en un solo mensaje
- el **algoritmo 2** es más detallado, distingue tipos de error y relanza `EOFError`

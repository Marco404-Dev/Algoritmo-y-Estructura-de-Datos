```python
def count(data, target):
  n = 0
  for item in data:
    if item == target:
      n += 1
  return n

print(count([4, 7, 4, 9, 4], 4))     # 3
print(count("banana", "a"))          # 3
print(count((2, 2, 5, 2), 2))        # 3
print(count([True, False, True], True))  # 2
```

# `count.py`

## 1. Planteamiento del problema

Se busca crear una función que permita **contar cuántas veces aparece un valor específico** dentro de una colección de datos.

El programa debe permitir:

- recibir una colección llamada `data`
- recibir un valor objetivo llamado `target`
- recorrer todos los elementos de la colección
- comparar cada elemento con el valor buscado
- aumentar un contador cada vez que haya coincidencia
- devolver al final la cantidad total de apariciones
- funcionar con distintos tipos de colecciones, como listas, cadenas y tuplas

> **Pregunta problema:**  
> ¿Cómo contar cuántas veces aparece un elemento dentro de una colección recorriendo sus datos uno por uno?

---

## 2. ¿En qué consiste el algoritmo?

La lógica general del código consiste en:

1. Crear una variable contadora que empiece en `0`.
2. Recorrer todos los elementos de la colección `data`.
3. Comparar cada elemento con `target`.
4. Si el elemento es igual al valor buscado, aumentar el contador en `1`.
5. Cuando termine el recorrido, devolver el valor acumulado.

En otras palabras, el algoritmo **inspecciona toda la secuencia** y va sumando cada coincidencia encontrada.

---
## 3. Estructura general del código

```text
Algoritmo count(data, target):
    n = 0
    para cada item en data:
        si item es igual a target:
            n = n + 1
    devolver n
```

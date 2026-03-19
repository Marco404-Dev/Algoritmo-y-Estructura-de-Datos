```python
def contains(data, target):
  for item in data:
    if item == target:
      return True
  return False

print(contains([4, 8, 2, 9], 2))      # True
print(contains([4, 8, 2, 9], 7))      # False
print(contains("banana", "n"))        # True
print(contains("banana", "z"))        # False
print(contains((10, 20, 30), 20))     # True
```

# `contains.py`

## 1. Planteamiento del problema

Se busca crear una función que permita **verificar si un valor específico está presente** dentro de una colección de datos.

El programa debe permitir:

- recibir una colección llamada `data`
- recibir un valor objetivo llamado `target`
- recorrer los elementos de la colección uno por uno
- comparar cada elemento con el valor buscado
- devolver `True` si encuentra al menos una coincidencia
- devolver `False` si termina el recorrido sin encontrar el valor
- funcionar con distintos tipos de colecciones, como listas, cadenas y tuplas

> **Pregunta problema:**  
> ¿Cómo determinar si un elemento existe dentro de una colección recorriendo sus datos secuencialmente?

---

## 2. ¿En qué consiste el algoritmo?

La lógica general del código consiste en:

1. Recorrer todos los elementos de la colección `data`.
2. Comparar cada elemento con `target`.
3. Si encuentra una coincidencia, devolver inmediatamente `True`.
4. Si termina de revisar toda la colección y no encuentra ninguna coincidencia, devolver `False`.

En otras palabras, el algoritmo realiza una **búsqueda secuencial** hasta encontrar el elemento o agotar todos los datos.

---

## 3. Estructura general del código

### 3.1. Principales métodos

#### Función `contains(data, target)`

**Algoritmo:**

```text
Algoritmo contains(data, target):
    para cada item en data:
        si item es igual a target:
            devolver True
    devolver False

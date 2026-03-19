```python
class Vector:
    """Representa un vector en un espacio multidimensional."""

    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:
            try:   # probamos si el parámetro es iterable
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('tipo de parámetro no válido')

    def __len__(self):
        """Devuelve la dimensión del vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Devuelve la coordenada en la posición j del vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Asigna un valor a la coordenada en la posición j."""
        self._coords[j] = val

    def __add__(self, other):
        """Devuelve la suma de dos vectores."""
        if len(self) != len(other):
            raise ValueError('las dimensiones deben coincidir')
        resultado = Vector(len(self))
        for j in range(len(self)):
            resultado[j] = self[j] + other[j]
        return resultado

    def __eq__(self, other):
        """Devuelve True si el vector tiene las mismas coordenadas que otro."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Devuelve True si el vector es diferente de otro."""
        return not self == other

    def __str__(self):
        """Devuelve una representación en texto del vector."""
        return '<' + str(self._coords)[1:-1] + '>'

    def __neg__(self):
        """Devuelve una copia del vector con todas sus coordenadas negadas."""
        resultado = Vector(len(self))
        for j in range(len(self)):
            resultado[j] = -self[j]
        return resultado

    def __lt__(self, other):
        """Compara vectores según orden lexicográfico."""
        if len(self) != len(other):
            raise ValueError('las dimensiones deben coincidir')
        return self._coords < other._coords

    def __le__(self, other):
        """Compara vectores según orden lexicográfico."""
        if len(self) != len(other):
            raise ValueError('las dimensiones deben coincidir')
        return self._coords <= other._coords


print("PRUEBA 1: crear vector de 5 dimensiones")
v = Vector(5)
print("v =", v)

print("\nPRUEBA 2: asignar valores")
v[1] = 23
v[-1] = 45
print("v =", v)
print("Elemento en posición 4:", v[4])

print("\nPRUEBA 3: sumar vector consigo mismo")
u = v + v
print("u =", u)

print("\nPRUEBA 4: negar vector")
negativo = -v
print("-v =", negativo)

print("\nPRUEBA 5: comparar igualdad y diferencia")
a = Vector([1, 2, 3])
b = Vector([1, 2, 3])
c = Vector([1, 2, 4])
print("a =", a)
print("b =", b)
print("c =", c)
print("a == b:", a == b)
print("a != c:", a != c)

print("\nPRUEBA 6: comparación lexicográfica")
print("a < c:", a < c)
print("a <= b:", a <= b)

print("\nPRUEBA 7: recorrer vector con for")
total = 0
for entrada in v:
    total += entrada
print("Suma de elementos de v:", total)

print("\nPRUEBA 8: crear vector desde iterable")
w = Vector([7, 8, 9])
print("w =", w)
print("Longitud de w:", len(w))

print("\nPRUEBA 9: error por dimensiones distintas")
try:
    x = Vector([1, 2])
    y = Vector([3, 4, 5])
    print(x + y)
except ValueError as e:
    print("Error detectado:", e)

print("\nPRUEBA 10: error por parámetro inválido")
try:
    z = Vector(3.5)
except TypeError as e:
    print("Error detectado:", e)

```


# `vector.py`

## 1. Planteamiento del problema

Se busca modelar un **vector matemático** dentro de un programa, de manera que pueda comportarse como un objeto flexible y reutilizable.
El programa debe permitir:

- crear un vector indicando su dimensión
- crear un vector a partir de un iterable, como una lista
- almacenar sus coordenadas internamente
- acceder a una coordenada por índice
- modificar una coordenada por índice
- sumar dos vectores de la misma dimensión
- negar un vector
- comparar vectores
- mostrar el vector en un formato legible
- detectar errores cuando las dimensiones no coinciden
- detectar errores cuando el parámetro de entrada no es válido

> **Pregunta problema:**  
> ¿Cómo representar un vector dentro de un programa para que permita operaciones matemáticas básicas, acceso por índice, comparación y validación de errores de forma clara y ordenada?

---

## 2. ¿En qué consiste el algoritmo?

La lógica general del código consiste en:

1. Crear una clase `Vector` que guarde sus coordenadas en una lista interna.
2. Permitir que el vector se cree de dos formas:
   - indicando una dimensión entera
   - pasando un iterable con valores iniciales
3. Implementar métodos especiales para que el vector se comporte como un objeto natural en Python.
4. Permitir operaciones como:
   - obtener longitud
   - acceder a coordenadas
   - modificar coordenadas
   - sumar vectores
   - negar vectores
   - comparar vectores
5. Probar el comportamiento del vector con varios casos.

---

## 3. Estructura general del código

### 3.1. Principales métodos

#### Método `__init__(d)`

**Algoritmo:**

```text
Algoritmo __init__(d):
    Si d es un entero:
        crear una lista de d ceros
    Si no:
        intentar recorrer d como iterable
        copiar sus valores a la lista interna
    Si d no es entero ni iterable:
        lanzar TypeError
```
Idea central:

- construir el vector
- permitir dos formas de creación
- usar ceros si se da una dimensión
- copiar valores si se da una lista u otro iterable
- validar que la entrada sea correcta


#### Método __len__()
```python
Algoritmo __len__():
    devolver la cantidad de coordenadas del vector
```
Idea central:

- devolver la dimensión del vector
- permitir el uso de len(v)
- indicar cuántos componentes tiene el objeto

#### Método __getitem__(j)
```python
Algoritmo __getitem__(j):
    devolver la coordenada ubicada en la posición j
```
Idea central:

- acceder a una coordenada específica
- permitir el uso de v[j]
- aprovechar el acceso por índice de Python

#### Método __setitem__(j, val)
```python
Algoritmo __setitem__(j, val):
    asignar val en la posición j de las coordenadas
```
Idea central:

- modificar una coordenada del vector
- permitir expresiones como v[j] = valor
- actualizar internamente la lista de coordenadas

#### Método __add__(other)
```python
Algoritmo __add__(other):
    Si las dimensiones no coinciden:
        lanzar ValueError
    crear un vector resultado de la misma dimensión
    para cada posición j:
        resultado[j] = self[j] + other[j]
    devolver resultado
```

Idea central:

- sumar dos vectores componente a componente
- verificar primero que tengan la misma dimensión
- construir un nuevo vector con la suma
- devolver el resultado sin modificar los vectores originales

#### Método __neg__()
```python
Algoritmo __neg__():
    crear un vector resultado de la misma dimensión
    para cada posición j:
        resultado[j] = -self[j]
    devolver resultado
```

Idea central:
- cambiar el signo de cada coordenada
- crear una copia negada del vector
- devolver un nuevo vector

#### Método __eq__(other)

```python
Algoritmo __eq__(other):
    comparar si las listas internas de coordenadas son iguales
```

Idea central:

- revisar si dos vectores tienen exactamente los mismos valores
- devolver True si coinciden
- devolver False si son distintos

#### Método __ne__(other)
```python
Algoritmo __ne__(other):
    devolver lo contrario de __eq__(other)
```
Idea central:

- indicar si dos vectores son diferentes
- reutilizar la lógica de igualdad
- evitar repetir comparaciones

#### Método __lt__(other)
```python
Algoritmo __lt__(other):
    Si las dimensiones no coinciden:
        lanzar ValueError
    comparar lexicográficamente las coordenadas
```

Idea central:

- comparar dos vectores como se comparan listas en Python
- revisar primero la primera coordenada distinta
- decidir cuál es menor según orden lexicográfico

#### Método __le__(other)
```python
Algoritmo __le__(other):
    Si las dimensiones no coinciden:
        lanzar ValueError
    comparar lexicográficamente las coordenadas
```
Idea central:

- verificar si un vector es menor o igual que otro
- usar el orden lexicográfico
- exigir que tengan la misma dimensión

#### Método __str__()
```python
Algoritmo __str__():
    convertir la lista interna a texto
    cambiar el formato para mostrarlo entre < >
    devolver la cadena resultante
```
Idea central:

- mostrar el vector de forma legible
- imprimirlo como <1, 2, 3> en vez de mostrar un objeto extraño
- mejorar la salida visual del programa

### Algoritmo general

1. Crear un vector con dimensión o con un iterable.
2. Guardar internamente sus coordenadas.
3. Permitir acceso y modificación por índice.
4. Realizar operaciones entre vectores, como suma y negación.
5. Comparar vectores por igualdad, diferencia y orden lexicográfico.
6. Mostrar resultados en un formato claro.
7. Detectar errores cuando la entrada o las dimensiones son inválidas.









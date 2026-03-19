`sequence_abc` y `sequence_iterator` sí se relacionan, porque ambos trabajan con secuencias, pero no resuelven exactamente el mismo problema.

- `sequence_abc` define qué debe tener una secuencia, obligando a implementar métodos básicos como `__len__` y `__getitem__`, y construyendo otros métodos como `__contains__`, `index` y `count`.
- `sequence_iterator` define cómo recorrer una secuencia elemento por elemento mediante los métodos `__next__` y `__iter__`.

En conclusión, `sequence_abc` se enfoca en la estructura y comportamiento básico de una secuencia, mientras que `sequence_iterator` se enfoca en su recorrido.


```python
from abc import ABCMeta, abstractmethod

class Secuencia(metaclass=ABCMeta):
    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self, j):
        pass

    def __contains__(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False

    def index(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('el valor no está en la secuencia')

    def count(self, val):
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k


class MiLista(Secuencia):
    def __init__(self, datos):
        self._datos = datos

    def __len__(self):
        return len(self._datos)

    def __getitem__(self, j):
        return self._datos[j]


lista = MiLista([10, 20, 10, 30, 10])

print(10 in lista)
print(lista.index(30))
print(lista.count(10))

```
# Capítulo 2 - `sequence_abc.py`

## 1. Planteamiento del problema

Se busca modelar una **secuencia abstracta** dentro de un programa, de manera que distintas estructuras de datos puedan comportarse como secuencias si cumplen ciertas reglas básicas.

El programa debe permitir:

- definir una clase base abstracta para secuencias
- obligar a que toda subclase implemente `__len__`
- obligar a que toda subclase implemente `__getitem__`
- verificar si un valor pertenece a la secuencia
- encontrar la posición de un valor dentro de la secuencia
- contar cuántas veces aparece un valor
- reutilizar métodos generales sin volver a escribirlos en cada subclase

> **Pregunta problema:**  
> ¿Cómo diseñar una clase abstracta que permita reutilizar operaciones comunes de una secuencia, obligando a las subclases a implementar solo lo esencial?

---

## 2. ¿En qué consiste el algoritmo?

La lógica general del código consiste en:

1. Crear una clase abstracta llamada `Secuencia`.
2. Exigir que toda subclase implemente los métodos básicos `__len__` y `__getitem__`.
3. Construir métodos generales sobre esa base, como:
   - `__contains__`
   - `index`
   - `count`
4. Crear una subclase concreta llamada `MiLista`.
5. Probar que la subclase puede usar automáticamente los métodos heredados.

---

## 3. Estructura general del código

### 3.1. Principales métodos

#### len
indicar cuántos elementos tiene la secuencia

#### getitem
devolver un elemento según su índice

#### contains
recorrer toda la secuencia buscando un valor

#### index
- recorrer la secuencia de izquierda a derecha
- encontrar la primera posición donde aparece el valor
- devolver ese índice si existe
- lanzar un error si el valor no está en la secuencia

#### count
- contar cuántas veces aparece un valor




### Algoritmo general
1. Definir una clase abstracta Secuencia.
2. Obligar a que sus subclases implementen __len__ y __getitem__.
3. Usar esos dos métodos básicos para construir:
    - verificación de pertenencia
    - búsqueda de posición
    - conteo de apariciones
4. Crear una subclase concreta MiLista.
5. Probar los métodos heredados con una lista de datos.

### 4. Explicación de la abstracción
1. La clase Secuencia es una clase abstracta.
Eso significa que:
      - no está pensada para crear objetos directamente
      - sirve como plantilla o contrato
      - obliga a sus subclases a implementar ciertos métodos
      - define un comportamiento común para todas las secuencias
En este caso, toda subclase de Secuencia debe implementar:
      - __len__
      - __getitem__
Si cumple con eso, automáticamente obtiene los métodos:
      - __contains__
      - index
      - count
Esto evita repetir código y mejora el diseño del programa.





```python
class IteradorSecuencia:
    """Un iterador para cualquiera de los tipos de secuencia de Python."""

    def __init__(self, secuencia):
        """Crea un iterador para la secuencia dada."""
        self._seq = secuencia      # guarda una referencia a los datos subyacentes
        self._k = -1               # se incrementará a 0 en la primera llamada a next

    def __next__(self):
        """Devuelve el siguiente elemento o lanza el error StopIteration."""
        self._k += 1               # avanza al siguiente índice
        if self._k < len(self._seq):
            return self._seq[self._k]   # devuelve el elemento de la secuencia
        else:
            raise StopIteration()       # ya no hay más elementos

    def __iter__(self):
        """Por convención, un iterador debe devolverse a sí mismo."""
        return self

```

# Capítulo 2 - `sequence_iterator.py`

## 1. Planteamiento del problema

Se busca construir un **iterador** para una secuencia, de manera que sus elementos puedan recorrerse uno por uno de forma ordenada.

El programa debe permitir:

- recibir una secuencia como entrada
- guardar una referencia a esa secuencia
- llevar el control de la posición actual
- devolver el siguiente elemento cada vez que se solicite
- detener el recorrido cuando ya no existan más elementos
- comportarse como un iterador válido en Python

> **Pregunta problema:**  
> ¿Cómo crear un objeto iterador que recorra una secuencia elemento por elemento y se detenga correctamente al llegar al final?

---

## 2. ¿En qué consiste el algoritmo?

La lógica general del código consiste en:

1. Recibir una secuencia y almacenarla internamente.
2. Inicializar un índice de control antes del primer elemento.
3. Cada vez que se solicite el siguiente valor, avanzar el índice.
4. Verificar si todavía existe un elemento en esa posición.
5. Si existe, devolverlo.
6. Si no existe, lanzar `StopIteration` para indicar que la secuencia terminó.

---

## 3. Estructura general del código

### 3.1. Principales métodos

#### Metodo __next__()

**Algoritmo:**
```python
Algoritmo __next__():
    incrementar _k en 1
    si _k < len(_seq):
        devolver _seq[_k]
    si no:
        lanzar StopIteration
```
Idea central:

- avanzar a la siguiente posición de la secuencia
- comprobar si esa posición es válida
- devolver el elemento correspondiente si existe
- finalizar el recorrido lanzando StopIteration cuando ya no haya más elementos

### Algoritmo general

1. Guardar la secuencia que se desea recorrer.
2. Inicializar un índice interno en -1.
3. Cada vez que se pida un siguiente elemento:
    - aumentar el índice en 1
    - verificar si sigue dentro de los límites
    - devolver el elemento si existe
    - detener el proceso si ya no hay más elementos
4. Devolver el propio iterador cuando Python llame a __iter__().

### Explicación del funcionamiento

La clase IteradorSecuencia sirve para recorrer cualquier secuencia de Python, por ejemplo:
    - listas
    - tuplas
    - cadenas
    
otras estructuras que tengan len() y acceso por índice
El iterador no modifica la secuencia original.
Lo único que hace es llevar un control de la posición actual para ir devolviendo los elementos uno por uno.






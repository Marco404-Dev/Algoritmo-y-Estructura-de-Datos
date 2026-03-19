```python
class Progresion:
    """Iterador que produce una progresión genérica.

    El iterador por defecto produce los números enteros:
    0, 1, 2, ...
    """

    def __init__(self, inicio=0):
        """Inicializa el valor actual con el primer valor de la progresión."""
        self._actual = inicio

    def _avanzar(self):
        """Actualiza self._actual a un nuevo valor.

        Este método debe ser redefinido por una subclase para
        personalizar la progresión.

        Por convención, si el valor actual se vuelve None,
        eso indica el final de una progresión finita.
        """
        self._actual += 1

    def __next__(self):
        """Devuelve el siguiente elemento o lanza el error StopIteration."""
        if self._actual is None:   # convención para terminar una progresión
            raise StopIteration()
        else:
            respuesta = self._actual   # guarda el valor actual para devolverlo
            self._avanzar()            # avanza para preparar el siguiente
            return respuesta

    def __iter__(self):
        """Por convención, un iterador debe devolverse a sí mismo."""
        return self

    def imprimir_progresion(self, n):
        """Imprime los siguientes n valores de la progresión."""
        print(' '.join(str(next(self)) for j in range(n)))


class ProgresionAritmetica(Progresion):
    """Iterador que produce una progresión aritmética."""

    def __init__(self, incremento=1, inicio=0):
        """Crea una nueva progresión aritmética.

        incremento  constante fija que se suma a cada término
        inicio      primer término de la progresión
        """
        super().__init__(inicio)
        self._incremento = incremento

    def _avanzar(self):
        """Actualiza el valor actual sumando el incremento fijo."""
        self._actual += self._incremento


class ProgresionGeometrica(Progresion):
    """Iterador que produce una progresión geométrica."""

    def __init__(self, base=2, inicio=1):
        """Crea una nueva progresión geométrica.

        base        constante fija por la que se multiplica cada término
        inicio      primer término de la progresión
        """
        super().__init__(inicio)
        self._base = base

    def _avanzar(self):
        """Actualiza el valor actual multiplicándolo por la base."""
        self._actual *= self._base


class ProgresionFibonacci(Progresion):
    """Iterador que produce una progresión de Fibonacci generalizada."""

    def __init__(self, primero=0, segundo=1):
        """Crea una nueva progresión de Fibonacci.

        primero     primer término de la progresión
        segundo     segundo término de la progresión
        """
        super().__init__(primero)
        self._anterior = segundo - primero   # valor ficticio anterior al primero

    def _avanzar(self):
        """Actualiza el valor actual con la suma de los dos anteriores."""
        self._anterior, self._actual = self._actual, self._anterior + self._actual


print('Progresión por defecto:')
Progresion().imprimir_progresion(10)

print('Progresión aritmética con incremento 5:')
ProgresionAritmetica(5).imprimir_progresion(10)

print('Progresión aritmética con incremento 5 e inicio 2:')
ProgresionAritmetica(5, 2).imprimir_progresion(10)

print('Progresión geométrica con base por defecto:')
ProgresionGeometrica().imprimir_progresion(10)

print('Progresión geométrica con base 3:')
ProgresionGeometrica(3).imprimir_progresion(10)

print('Progresión de Fibonacci con valores iniciales por defecto:')
ProgresionFibonacci().imprimir_progresion(10)

print('Progresión de Fibonacci con valores iniciales 4 y 6:')
ProgresionFibonacci(4, 6).imprimir_progresion(10)
```
# `progressions.py`

## 1. Planteamiento del problema

Se busca modelar distintas **progresiones numéricas** dentro de un programa, de manera que puedan generarse sus términos uno por uno usando la lógica de los iteradores en Python.

El programa debe permitir:

- representar una progresión genérica
- generar automáticamente el siguiente término de una secuencia
- reutilizar una misma estructura base para distintos tipos de progresión
- definir progresiones aritméticas
- definir progresiones geométricas
- definir progresiones de Fibonacci
- imprimir los primeros `n` términos de cada progresión
- usar herencia para personalizar la forma en que avanza cada secuencia

> **Pregunta problema:**  
> ¿Cómo representar distintas progresiones numéricas dentro de un programa para que puedan generar sus términos automáticamente, reutilizando una estructura común y cambiando solo la regla de avance?

---

## 2. ¿En qué consiste el algoritmo?

La lógica general del código consiste en:

1. Crear una clase base llamada `Progresion` que represente una secuencia numérica genérica.
2. Guardar el valor actual de la progresión.
3. Definir un método que devuelva el término actual y luego actualice el siguiente.
4. Permitir que las subclases cambien la forma de avanzar la secuencia.
5. Generar progresiones especiales, como la aritmética, la geométrica y la de Fibonacci.
6. Imprimir los primeros `n` términos de cada progresión.

---

## 3. Estructura general del código

### 3.1. Principales métodos

#### Método `__next__()`

**Algoritmo:**

```text
Algoritmo __next__():
    Si el valor actual es None:
        lanzar StopIteration
    Si no:
        guardar el valor actual en respuesta
        avanzar la progresión al siguiente valor
        devolver respuesta
```
Idea central:

- devolver el término actual de la progresión
- actualizar internamente el siguiente valor
- controlar cuándo termina una progresión finita
- permitir que el objeto funcione como iterador

#### Método _avanzar() de la clase Progresion

**Algoritmo:**
```text
Algoritmo _avanzar():
    actual = actual + 1
```
Idea central:

- mover la progresión al siguiente valor
- usar una regla simple por defecto
- generar la secuencia 0, 1, 2, 3, ...
- servir como base para que las subclases redefinan este comportamiento


#### Método _avanzar() en ProgresionAritmetica

**Algoritmo:**
```python
Algoritmo _avanzar():
    actual = actual + incremento
```
Idea central:

- sumar siempre una cantidad fija
- mantener una diferencia constante entre términos
- producir secuencias como 2, 7, 12, 17, ...
- especializar la lógica heredada de la clase base

#### Método _avanzar() en ProgresionAritmetica

**Algoritmo:**
```python
Algoritmo _avanzar():
    actual = actual + incremento
```
Idea central:

- sumar siempre una cantidad fija
- mantener una diferencia constante entre términos
- producir secuencias como 2, 7, 12, 17, ...
- especializar la lógica heredada de la clase base

#### Método _avanzar() en ProgresionGeometrica

**Algoritmo:**
```python
Algoritmo _avanzar():
    actual = actual * base
```
Idea central:

- multiplicar siempre por una constante fija
- mantener una razón constante entre términos
- producir secuencias como 1, 2, 4, 8, 16, ...
- cambiar la regla de avance sin modificar la estructura general del iterador

#### Método _avanzar() en ProgresionFibonacci

**Algoritmo:**
```python
Algoritmo _avanzar():
    anterior, actual = actual, anterior + actual
```
Idea central:

- recordar los dos últimos valores de la secuencia
- calcular el nuevo término como la suma de los dos anteriores
- actualizar simultáneamente anterior y actual
- producir secuencias como 0, 1, 1, 2, 3, 5, 8, ...

#### Método imprimir_progresion(n)

**Algoritmo:**
```python
Algoritmo imprimir_progresion(n):
    Repetir n veces:
        obtener el siguiente valor con next(self)
        convertirlo en texto
    unir todos los valores con espacios
    imprimir el resultado
```
Idea central:

- pedir repetidamente los siguientes términos de la progresión
- usar el protocolo de iteración de Python
- mostrar los primeros n valores de forma ordenada
- convertir la progresión en una salida visible para el usuario

### Algoritmo general
1. Crear una clase base que almacene el valor actual de una progresión.
2. Definir un método para devolver el valor actual y avanzar al siguiente.
3. Hacer que el objeto se comporte como iterador devolviéndose a sí mismo con __iter__.
4. Permitir que distintas subclases redefinan la forma de avanzar.
5. Crear progresiones específicas:
            - progresión genérica
            - progresión aritmética
            - progresión geométrica
            - progresión de Fibonacci
6. Imprimir los primeros n términos de cada una.

### Explicación de la herencia
La clase Progresion funciona como una clase base.
A partir de ella se construyen otras clases más específicas:
- ProgresionAritmetica
- ProgresionGeometrica
- ProgresionFibonacci
Esto significa que:
- todas heredan la estructura básica del iterador
- todas comparten __next__, __iter__ e imprimir_progresion
- cada subclase solo cambia el método _avanzar
- se reutiliza código sin repetir toda la clase desde cero
En otras palabras, la herencia permite conservar la misma mecánica general y modificar solamente la regla matemática de la progresión.
















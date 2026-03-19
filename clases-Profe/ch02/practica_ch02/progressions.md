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

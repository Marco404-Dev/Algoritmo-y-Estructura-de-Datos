```python
class Rango:
    """Una clase que imita a la clase incorporada range."""

    def __init__(self, inicio, fin=None, paso=1):
        """Inicializa una instancia de Rango.
        La semántica es similar a la clase range incorporada.
        """
        if paso == 0:
            raise ValueError('el paso no puede ser 0')

        if fin is None:                 # caso especial de range(n)
            inicio, fin = 0, inicio     # debe tratarse como range(0, n)

        # calcular una sola vez la longitud efectiva
        self._longitud = max(0, (fin - inicio + paso - 1) // paso)

        # se necesita conocer inicio y paso (pero no fin) para __getitem__
        self._inicio = inicio
        self._paso = paso

    def __len__(self):
        """Devuelve la cantidad de elementos en el rango."""
        return self._longitud

    def __getitem__(self, k):
        """Devuelve el elemento en el índice k
        (usando la interpretación estándar si es negativo).
        """
        if k < 0:
            k += len(self)              # intenta convertir índice negativo

        if not 0 <= k < self._longitud:
            raise IndexError('índice fuera de rango')

        return self._inicio + k * self._paso

## PRUEBA ##
r = Rango(2, 10, 2)

print("Longitud:", len(r))
print("Elemento en posición 0:", r[0])
print("Elemento en posición 1:", r[1])
print("Último elemento:", r[-1])

```

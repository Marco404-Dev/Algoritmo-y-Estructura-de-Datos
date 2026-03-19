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

# Capítulo 2 - uso de `Rango`

## 1. Planteamiento del problema

Se busca utilizar una clase llamada **`Rango`** para representar una secuencia numérica sin necesidad de guardar todos sus elementos explícitamente en una lista.

En este caso, el programa debe permitir:

- crear un rango numérico con inicio, fin y paso
- calcular cuántos elementos contiene el rango
- acceder a un elemento por su posición
- acceder al último elemento usando un índice negativo
- mostrar resultados usando `len()` y corchetes `[]`

> **Pregunta problema:**  
> ¿Cómo representar y consultar una secuencia numérica como `2, 4, 6, 8` de manera eficiente, permitiendo conocer su longitud y acceder a sus elementos por índice?

---

## 2. ¿En qué consiste el algoritmo?

La lógica general del código consiste en:

1. Crear un objeto `Rango` con inicio `2`, fin `10` y paso `2`.
2. Calcular la cantidad de elementos que contiene el rango.
3. Consultar el elemento de la posición `0`.
4. Consultar el elemento de la posición `1`.
5. Consultar el último elemento usando el índice `-1`.
6. Mostrar los resultados en pantalla.

---

## 3. Estructura general del código

### 3.1. Principales métodos

#### Método __getitem__(k)

**Algoritmo:**
```python
Algoritmo __getitem__(k):
    Si k es negativo:
        convertir k a su posición equivalente positiva
    Verificar que k esté dentro del rango válido
    devolver inicio + k * paso
```
Idea central:

- obtener un elemento según su posición
- aceptar índices positivos y negativos
- calcular el valor con una fórmula
- evitar almacenar toda la secuencia en memoria

### Algoritmo general

1. Crear un rango con inicio = 2, fin = 10 y paso = 2.
2. Calcular su longitud usando len(r).
3. Obtener el primer elemento con r[0].
4. Obtener el segundo elemento con r[1].
5. Obtener el último elemento con r[-1].
6. Imprimir todos los resultados.



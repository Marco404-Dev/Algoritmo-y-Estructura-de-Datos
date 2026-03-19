```python
## from .credit_card import CreditCard 

class CreditCard:

  def __init__(self, customer, bank, acnt, limit):

    self._customer = customer
    self._bank = bank
    self._account = acnt
    self._limit = limit
    self._balance = 0

  def get_customer(self):
    return self._customer

  def get_bank(self):
    return self._bank

  def get_account(self):
    return self._account

  def get_limit(self):
    return self._limit

  def get_balance(self):
    return self._balance

  def charge(self, price):
    if price + self._balance > self._limit:
      return False
    else:
      self._balance += price
      return True

  def make_payment(self, amount):
    self._balance -= amount

class PredatoryCreditCard(CreditCard):    # Una extensión de CreditCard que aplica intereses y comisiones.
  
  def __init__(self, customer, bank, acnt, limit, apr): #Crea una nueva instancia de tarjeta de crédito abusiva.
    super().__init__(customer, bank, acnt, limit)
    self._apr = apr

  def charge(self, price):            # Realiza un cargo a la tarjeta
    success = super().charge(price)
    if not success:
      self._balance += 5
    return success

  def process_month(self):           # Aplica el interés mensual al saldo pendiente
    if self._balance > 0:
      monthly_factor = pow(1 + self._apr, 1/12)
      self._balance *= monthly_factor


# -------------------------
# PRUEBA DEL CÓDIGO
# -------------------------

tarjeta = PredatoryCreditCard("Juan Pérez", "BCP", "1234 5678 9012 3456", 1000, 0.0825)

print("Cliente:", tarjeta.get_customer())
print("Banco:", tarjeta.get_bank())
print("Cuenta:", tarjeta.get_account())
print("Límite:", tarjeta.get_limit())
print("Saldo inicial:", tarjeta.get_balance())

tarjeta.charge(200)
print("Saldo después de consumir 200:", tarjeta.get_balance())

tarjeta.process_month()
print("Saldo después del interés mensual:", tarjeta.get_balance())

```

# Capítulo 2 - `predatory_credit_card.py`

## 1. Planteamiento del problema

Se busca modelar una **tarjeta de crédito abusiva o depredadora** dentro de un programa, tomando como base una tarjeta de crédito normal, pero agregando reglas adicionales de penalización e interés.

Esta tarjeta debe permitir:

- heredar los datos básicos de una tarjeta de crédito común
- guardar el nombre del cliente
- guardar el banco emisor
- guardar el número de cuenta
- guardar el límite de crédito
- guardar el saldo actual
- guardar la tasa de interés anual (`apr`)
- registrar consumos o cargos
- cobrar una comisión adicional cuando un cargo es rechazado
- aplicar interés mensual al saldo pendiente

> **Pregunta problema:**  
> ¿Cómo representar una tarjeta de crédito que, además de funcionar como una tarjeta normal, aplique penalizaciones por cargos rechazados e intereses mensuales sobre el saldo adeudado?

---

## 2. ¿En qué consiste el algoritmo?

La lógica general del código consiste en:

1. Crear una tarjeta abusiva a partir de una tarjeta de crédito normal.
2. Guardar la tasa de interés anual además de los datos básicos heredados.
3. Intentar realizar cargos usando la lógica de la clase padre.
4. Si un cargo falla, aplicar una penalización de 5 al saldo.
5. Si al finalizar el mes existe deuda, aplicar el interés mensual correspondiente.

---

## 3. Estructura general del código

### 3.1. Principales métodos

#### Método `charge(price)`

**Algoritmo:**

```text
Algoritmo charge(price):
    success = ejecutar charge(price) de la clase padre
    Si success es False:
        sumar 5 al saldo como penalización
    Devolver success
```
Idea central:

- intentar hacer el cargo usando la lógica normal de CreditCard
- verificar si el cargo fue aceptado o rechazado
- si fue rechazado, cobrar una comisión fija de 5
- devolver True o False según el resultado del cargo

#### Método process_month()

**Algoritmo:**
```text
Algoritmo process_month():
    Si el saldo es mayor que 0:
        calcular el factor mensual = (1 + apr)^(1/12)
        multiplicar el saldo por el factor mensual
```
Idea central:

- revisar si existe una deuda pendiente
- calcular el interés correspondiente a un mes
- aumentar el saldo según la tasa anual convertida a factor mensual
- simular el crecimiento de la deuda con interés compuesto


### Explicación de la herencia

La clase PredatoryCreditCard hereda de CreditCard.
Eso significa que:

- reutiliza los atributos y métodos de la clase base
- no necesita volver a escribir get_customer, get_bank, get_account, get_limit ni get_balance
- puede modificar el comportamiento de algunos métodos, como charge
- puede agregar nuevos métodos, como process_month
- En otras palabras, esta clase toma el comportamiento de una tarjeta normal y lo extiende con reglas más estrictas.

### Algoritmo general

1. Crear una tarjeta abusiva con los datos del cliente, banco, cuenta, límite y tasa de interés anual.

2. Mostrar la información básica heredada de la clase CreditCard.

3. Realizar un cargo a la tarjeta.

4. Si el cargo es rechazado, agregar una penalización de 5 al saldo.

5. Si el saldo es positivo, aplicar el interés mensual.

6. Mostrar el saldo actualizado después de las operaciones.






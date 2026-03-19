```python
class CreditCard:
  """Una tarjeta de crédito de consumo."""

  def __init__(self, customer, bank, acnt, limit):
    """Crea una nueva instancia de tarjeta de crédito.

    El saldo inicial es cero.

    customer  nombre del cliente
    bank      nombre del banco
    acnt      identificador de la cuenta
    limit     límite de crédito
    """
    self._customer = customer
    self._bank = bank
    self._account = acnt
    self._limit = limit
    self._balance = 0

  def get_customer(self):
    """Devuelve el nombre del cliente."""
    return self._customer

  def get_bank(self):
    """Devuelve el nombre del banco."""
    return self._bank

  def get_account(self):
    """Devuelve el número identificador de la tarjeta."""
    return self._account

  def get_limit(self):
    """Devuelve el límite de crédito actual."""
    return self._limit

  def get_balance(self):
    """Devuelve el saldo actual."""
    return self._balance

  def charge(self, price):
    """Carga un monto a la tarjeta, si no excede el límite.

    Devuelve True si se procesó el cargo; False si fue rechazado.
    """
    if price + self._balance > self._limit:
      return False
    else:
      self._balance += price
      return True

  def make_payment(self, amount):
    """Procesa un pago del cliente que reduce el saldo."""
    self._balance -= amount

if __name__ == '__main__':
  wallet = []
  wallet.append(CreditCard('John Bowman', 'California Savings',
                           '5391 0375 9387 5309', 2500))
  wallet.append(CreditCard('John Bowman', 'California Federal',
                           '3485 0399 3395 1954', 3500))
  wallet.append(CreditCard('John Bowman', 'California Finance',
                           '5391 0375 9387 5309', 5000))

  for val in range(1, 17):
    wallet[0].charge(val)
    wallet[1].charge(2 * val)
    wallet[2].charge(3 * val)

  for c in range(3):
    print('Cliente =', wallet[c].get_customer())
    print('Banco =', wallet[c].get_bank())
    print('Cuenta =', wallet[c].get_account())
    print('Límite =', wallet[c].get_limit())
    print('Saldo =', wallet[c].get_balance())
    while wallet[c].get_balance() > 100:
      wallet[c].make_payment(100)
      print('Nuevo saldo =', wallet[c].get_balance())
    print()

    
```

## 1. Planteamiento del problema

Se busca modelar una **tarjeta de crédito** dentro de un programa, de manera que pueda almacenar su información principal y controlar operaciones básicas relacionadas con su uso.

La tarjeta debe permitir:

- guardar el nombre del cliente
- guardar el banco emisor
- guardar el número de cuenta
- guardar el límite de crédito
- guardar el saldo actual
- registrar consumos o cargos
- registrar pagos
- impedir que un cargo exceda el límite permitido

> **Pregunta problema:**  
> ¿Cómo representar una tarjeta de crédito dentro de un programa para que funcione correctamente, controlando su saldo, sus pagos y sus cargos sin exceder el límite establecido?

---

## 2. ¿En qué consiste el algoritmo?

La lógica general del código consiste en:

1. Crear una tarjeta con sus datos iniciales.
2. Permitir consultar esos datos.
3. Aceptar o rechazar cargos según el límite disponible.
4. Registrar pagos disminuyendo el saldo.

---

## 3. Estructura general del código

### 3.1. Principales métodos

#### Método `charge(precio)`

**Algoritmo:**

```text
Algoritmo charge(precio):
    Si precio + saldo actual > límite:
        rechazar operación
        devolver False
    Si no:
        sumar precio al saldo
        devolver True
```
Idea central:

El método charge consiste en:
- revisar cuánto debe ya el cliente
- sumar la nueva compra
- comparar el resultado contra el límite
- aceptar o rechazar la operación


#### Método make_payment(monto)

**Algoritmo:**

```text
make_payment(monto):
    saldo = saldo - monto
```

Idea central:

El método make_payment reduce el saldo cuando el cliente realiza un pago.


### algoritmo general 

1. Crear una tarjeta con datos básicos:
   cliente, banco, cuenta, límite y saldo inicial.

2. Permitir consultar esos datos mediante métodos.

3. Cuando se intenta hacer una compra:
   - verificar si la compra supera el límite
   - si lo supera, rechazar
   - si no lo supera, aumentar el saldo

4. Cuando se realiza un pago:
   - disminuir el saldo actual
  

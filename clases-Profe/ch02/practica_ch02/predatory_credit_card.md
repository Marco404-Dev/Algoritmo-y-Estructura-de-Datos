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

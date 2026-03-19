```python
from .credit_card import CreditCard

class PredatoryCreditCard(CreditCard):
  """Una extensión de CreditCard que aplica intereses y comisiones."""
  
  def __init__(self, customer, bank, acnt, limit, apr):
    """Crea una nueva instancia de tarjeta de crédito abusiva.

    El saldo inicial es cero.

    customer  nombre del cliente (por ejemplo, 'John Bowman')
    bank      nombre del banco (por ejemplo, 'California Savings')
    acnt      identificador de la cuenta (por ejemplo, '5391 0375 9387 5309')
    limit     límite de crédito (medido en dólares)
    apr       tasa de porcentaje anual (por ejemplo, 0.0825 para 8.25% APR)
    """
    super().__init__(customer, bank, acnt, limit)  # llama al constructor de la superclase
    self._apr = apr

  def charge(self, price):
    """Carga el precio dado a la tarjeta, suponiendo que hay suficiente límite de crédito.

    Devuelve True si el cargo fue procesado.
    Devuelve False y aplica una comisión de $5 si el cargo es rechazado.
    """
    success = super().charge(price)          # llama al método heredado
    if not success:
      self._balance += 5                     # aplica penalización
    return success                           # quien llama espera un valor de retorno

  def process_month(self):
    """Aplica el interés mensual al saldo pendiente."""
    if self._balance > 0:
      # si el saldo es positivo, convierte APR a un factor multiplicativo mensual
      monthly_factor = pow(1 + self._apr, 1/12)
      self._balance *= monthly_factor
```

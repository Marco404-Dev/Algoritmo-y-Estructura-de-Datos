```hola
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


> ¿Cómo representar una tarjeta de crédito dentro de un programa para que funcione correctamente, controlando su saldo, sus pagos y sus cargos sin exceder el límite establecido?

---

## 2. ¿En qué consiste el algoritmo?
La lógica general del código consiste en:

1. crear una tarjeta con sus datos iniciales
2. permitir consultar esos datos
3. aceptar o rechazar cargos según el límite disponible
4. registrar pagos disminuyendo el saldo

---

## 3. Estructura general del código

### principales metodos 

Algoritmo charge(precio):
    Si precio + saldo actual > límite:
        rechazar operación
        devolver False
    Si no:
        sumar precio al saldo
        devolver True

Idea central
    charge consiste en:
    revisar cuánto debe ya el cliente
    sumar la nueva compra
    comparar contra el límite
    aceptar o rechazar la operación

make_payment(monto):
    saldo = saldo - monto

Idea central:
    Reduce el saldo cuando el cliente paga.


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
  

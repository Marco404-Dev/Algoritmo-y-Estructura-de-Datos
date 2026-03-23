# Explicación de algoritmos y conceptos básicos en Python

---

# 1. Determinar si un número es par o impar

## Código

```python
def isEven(n):
    rem = n % 2
    if rem == 0:
        return True
    else:
        return False
```

## Versión más eficiente

```python
def isEven(n):
    if (n & 1) == 0:
        return True
    else:
        return False
```

## 1) Planteamiento del problema

Se quiere determinar si un número entero `n` es:

- par, si se puede dividir entre 2 exactamente
- impar, si no se puede dividir exactamente entre 2

### Requerimientos

- Recibir un número entero `n`
- Evaluar si es divisible entre 2
- Devolver `True` si es par
- Devolver `False` si es impar

## 2) ¿En qué consiste el algoritmo?

La idea es muy simple:

- un número par deja residuo 0 al dividirlo entre 2
- un número impar deja residuo 1

Entonces:

- si `n % 2 == 0`, el número es par
- si no, es impar

En la versión eficiente se usa:

```python
(n & 1)
```

Eso revisa el último bit del número en binario:

- si termina en `0`, es par
- si termina en `1`, es impar

### Ejemplos

- `8` en binario es `1000` → termina en `0` → par
- `7` en binario es `0111` → termina en `1` → impar

## 3) Estructura general del código

### 3.1 Principales métodos con pseudocódigo e idea central

#### Método 1: usando módulo `%`

### Idea central

Dividir entre 2 y revisar el residuo.

### Pseudocódigo

```text
función isEven(n):
    residuo = n % 2
    si residuo == 0:
        devolver True
    si no:
        devolver False
```

#### Método 2: usando AND bitwise `&`

### Idea central

Revisar el último bit del número.

### Pseudocódigo

```text
función isEven(n):
    si (n AND 1) == 0:
        devolver True
    si no:
        devolver False
```

### Explicación de `(n & 1)`

`&` compara bits.

### Ejemplo con 10

```text
10 en binario: 1010
 1 en binario: 0001
1010
0001
----
0000
```

Resultado: `0` → par

### Ejemplo con 15

```text
15 en binario: 1111
 1 en binario: 0001
1111
0001
----
0001
```

Resultado: `1` → impar

## 4) Complejidad Big O

Ambas versiones tienen:

- Tiempo: `O(1)`
- Espacio: `O(1)`

Porque hacen una cantidad fija de operaciones, sin importar el valor de `n`.

## 5) ¿Es eficiente o no?

Sí, es muy eficiente.

La versión con `%` ya es eficiente.

La versión con `& 1` suele considerarse más cercana al nivel máquina, pero en Python la diferencia práctica suele ser muy pequeña. Igual, conceptualmente, la de bits es una forma clásica y eficiente.

---

# 2. Intercambiar dos números

## Versiones

### Con variable temporal

```python
a = 2
b = 3
temp = a
a = b
b = temp
```

### Sin variable temporal

```python
a = a + b
b = a - b
a = a - b
```

## 1) Planteamiento del problema

Se quiere intercambiar los valores de dos variables.

Si al inicio:

```python
a = 2
b = 3
```

al final debe quedar:

```python
a = 3
b = 2
```

## 2) ¿En qué consiste el algoritmo?

La idea es que:

- `a` tiene un valor
- `b` tiene otro valor
- queremos que se cambien de lugar

El problema es que si haces:

```python
a = b
b = a
```

no funciona como esperas, porque al hacer `a = b`, ya perdiste el valor original de `a`.

Por eso se usa:

- una variable auxiliar `temp`
- o una técnica matemática con suma y resta

## 3) Estructura general del código

### 3.1 Principales métodos con pseudocódigo e idea central

#### Método 1: con variable temporal

### Idea central

Guardar uno de los valores antes de sobrescribirlo.

### Pseudocódigo

```text
temp = a
a = b
b = temp
```

#### Método 2: sin variable temporal

### Idea central

Usar suma y resta para reconstruir los valores.

### Pseudocódigo

```text
a = a + b
b = a - b
a = a - b
```
### 3.2 Algoritmo general

```text
leer a y b
guardar uno de los valores o usar una relación matemática
asignar a el valor de b
asignar b el valor antiguo de a
mostrar resultado
```

## 4) Complejidad Big O

Las dos versiones tienen:

- Tiempo: `O(1)`
- Espacio:
  - con `temp`: `O(1)`
  - sin `temp`: `O(1)`

## 5) ¿Es eficiente o no?

Ambas son eficientes, pero:

- la de variable temporal es mejor en claridad
- la matemática es más delicada

En Python, la forma más natural incluso sería:

```python
a, b = b, a
```
---

# 3. Verificar si un número es primo

## Versión básica

```python
def isPrime(n):
    if n <= 1:
        return False
    res = True
    for i in range(2, n):
        if n % i == 0:
            res = False
            break
    return res
```

## Versión más eficiente

```python
import math

def isPrime(n):
    if n <= 1:
        return False
    res = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            res = False
            break
    return res
```

## 1) Planteamiento del problema

Un número primo es aquel que:

- tiene exactamente dos divisores positivos:
  - `1`
  - él mismo

### Requerimientos

- Recibir un entero `n`
- Determinar si tiene divisores aparte de `1` y él mismo
- Devolver `True` si es primo
- Devolver `False` si no es primo

## 2) ¿En qué consiste el algoritmo?

La idea es buscar si existe algún número que divida a `n` exactamente.

Si encontramos aunque sea uno, entonces ya no es primo.

Si no encontramos ninguno, entonces sí es primo.

## 3) Estructura general del código

### 3.1 Principales métodos con pseudocódigo e idea central

#### Método 1: revisar desde 2 hasta n-1

### Idea central

Probar todos los posibles divisores.

### Pseudocódigo

```text
función isPrime(n):
    si n <= 1:
        devolver False
    para i desde 2 hasta n-1:
        si n % i == 0:
            devolver False
    devolver True
```

#### Método 2: revisar solo hasta `sqrt(n)`

### Idea central

Si un número tiene divisor, uno de ellos aparece antes o en la raíz cuadrada.

### Pseudocódigo

```text
función isPrime(n):
    si n <= 1:
        devolver False
    para i desde 2 hasta sqrt(n):
        si n % i == 0:
            devolver False
    devolver True
```

### ¿Por qué basta hasta la raíz?

Porque los divisores vienen en pares.

### Ejemplo con 36

```text
1 × 36
2 × 18
3 × 12
4 × 9
6 × 6
```

Después de la raíz, empiezas a repetir la pareja al revés.

Entonces, si no encontraste divisor hasta `sqrt(n)`, ya no habrá uno nuevo después.

Eso hace el algoritmo mucho más rápido.


### 3.2 Algoritmo general

```text
leer n
si n <= 1:
    no es primo
si no:
    buscar divisores posibles
    si aparece uno:
        no es primo
    si no aparece ninguno:
        sí es primo
```

## 4) Complejidad Big O

### Versión básica

- Tiempo: `O(n)`
- Espacio: `O(1)`

### Versión eficiente

- Tiempo: `O(sqrt(n))`
- Espacio: `O(1)`

## 5) ¿Es eficiente o no?

La primera versión funciona, pero no es la mejor.

La segunda versión sí es bastante más eficiente.

Porque en vez de revisar casi todos los números hasta `n`, solo revisa hasta la raíz.

---

# 4. Hallar los divisores de un número

## Código

```python
def printDivisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
```

## 1) Planteamiento del problema

Dado un número entero `n`, se quiere obtener todos los números que lo dividen exactamente.

### Ejemplo

Si `n = 10`, sus divisores son:

- `1`
- `2`
- `5`
- `10`

### Requerimientos

- Recibir un entero `n`
- Revisar qué números lo dividen exactamente
- Guardar esos divisores
- Mostrar o devolver la lista

### Pregunta problema

¿Cómo encontrar todos los divisores de un número?

## 2) ¿En qué consiste el algoritmo?

Se recorre desde `1` hasta `n`.

En cada paso:

- se prueba si `i` divide a `n`
- si sí divide, se guarda

## 3) Estructura general del código

### 3.1 Principales métodos con pseudocódigo e idea central

### Idea central

Probar uno por uno todos los candidatos.

### Pseudocódigo

```text
función divisores(n):
    crear lista vacía
    para i desde 1 hasta n:
        si n % i == 0:
            guardar i en la lista
    devolver lista
```

### 3.2 Algoritmo general

```text
leer n
crear lista vacía
probar todos los números desde 1 hasta n
si uno divide exactamente:
    guardarlo
devolver la lista final
```

## 4) Complejidad Big O

- Tiempo: `O(n)`
- Espacio: `O(k)` donde `k` es la cantidad de divisores guardados

## 5) ¿Es eficiente o no?

Es correcto, pero no es la forma más eficiente.

Se puede optimizar usando la misma idea de la raíz cuadrada:

- si `i` divide a `n`, entonces `n // i` también
- así no recorres hasta `n`, solo hasta `sqrt(n)`


---

# 5. Fibonacci en la posición n

## Código

```python
def nthFibonacci(n):
    if n <= 1:
        return n
    curr = 0
    prev1 = 1
    prev2 = 0
    for i in range(2, n+1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return curr
```

## 1) Planteamiento del problema

La sucesión de Fibonacci sigue esta regla:

```text
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)
```

La secuencia empieza así:

```text
0, 1, 1, 2, 3, 5, 8, 13, 21...
```

### Requerimientos

- Recibir un entero `n`
- Calcular el valor de Fibonacci en esa posición
- Devolver el resultado

### Pregunta problema

¿Cómo calcular el término Fibonacci ubicado en la posición `n`?

## 2) ¿En qué consiste el algoritmo?

La idea es no guardar toda la secuencia, sino solo los últimos valores necesarios.

Como cada término depende de los dos anteriores, basta con recordar:

- el anterior
- el anteanterior

## 3) Estructura general del código

### 3.1 Principales métodos con pseudocódigo e idea central

### Idea central

Ir construyendo la secuencia paso a paso con variables.

### Pseudocódigo

```text
función nthFibonacci(n):
    si n <= 1:
        devolver n

    prev2 = 0
    prev1 = 1

    para i desde 2 hasta n:
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    devolver curr
```

### Explicación línea por línea

```python
if n <= 1:
    return n
```

Casos base:

- si `n = 0`, devuelve `0`
- si `n = 1`, devuelve `1`

```python
curr = 0
prev1 = 1
prev2 = 0
```

Variables:

- `prev2`: valor anterior más viejo
- `prev1`: valor anterior más reciente
- `curr`: valor actual

```python
for i in range(2, n+1):
```

Empieza desde `2` porque `0` y `1` ya están definidos.

```python
curr = prev1 + prev2
```

Calcula el nuevo Fibonacci.

```python
prev2 = prev1
prev1 = curr
```

Actualiza las referencias:

- el “anterior viejo” pasa a ser el anterior reciente
- el actual pasa a ser el nuevo anterior

```

### 3.2 Algoritmo general

```text
leer n
si n es 0 o 1:
    devolver n
si no:
    ir sumando los dos últimos valores
    actualizar referencias
devolver el último valor calculado
```

## 4) Complejidad Big O

- Tiempo: `O(n)`
- Espacio: `O(1)`

## 5) ¿Es eficiente o no?

Sí, es una versión eficiente comparada con la recursiva ingenua.

Porque:

- no repite cálculos
- no usa pila de llamadas
- solo usa unas pocas variables

---

# 6. Hallar el factorial de un número

## Versión iterativa

```python
def factorial(n):
    res = 1
    i = 2
    while (i <= n):
        res *= i
        i += 1
    return res
```

## Versión recursiva

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
```

## 1) Planteamiento del problema

El factorial de un número `n` se define como:

```text
n! = n × (n-1) × (n-2) × ... × 2 × 1
```

### Requerimientos

- Recibir un entero no negativo `n`
- Multiplicar todos los enteros desde `1` hasta `n`
- Devolver el resultado

## 2) ¿En qué consiste el algoritmo?

Hay dos enfoques:

### Iterativo

Multiplicar poco a poco en un bucle.

### Recursivo

Usar la definición:

```text
n! = n × (n-1)!
caso base: 0! = 1
```

## 3) Estructura general del código

### 3.1 Principales métodos con pseudocódigo e idea central

#### Método 1: iterativo con `while`

### Idea central

Ir acumulando el producto.

### Pseudocódigo

```text
función factorial(n):
    res = 1
    i = 2
    mientras i <= n:
        res = res * i
        i = i + 1
    devolver res
```


#### Método 2: recursivo

### Idea central

Cada factorial depende del factorial anterior.

### Pseudocódigo

```text
función factorial(n):
    si n == 0:
        devolver 1
    si no:
        devolver n * factorial(n-1)
```

### Explicación profunda

Si llamas:

```python
factorial(5)
```

Pasa esto:

```text
factorial(5)
= 5 * factorial(4)
= 5 * (4 * factorial(3))
= 5 * (4 * (3 * factorial(2)))
= 5 * (4 * (3 * (2 * factorial(1))))
= 5 * (4 * (3 * (2 * (1 * factorial(0)))))
= 5 * 4 * 3 * 2 * 1 * 1
= 120
```

### Caso base

```python
if n == 0:
    return 1
```

Sin esto, la función se llamaría infinitamente hacia abajo.

### 3.2 Algoritmo general

```text
leer n
si se usa iteración:
    multiplicar desde 2 hasta n
si se usa recursión:
    devolver n por factorial(n-1)
usar caso base 0! = 1
mostrar resultado
```

## 4) Complejidad Big O

### Iterativa

- Tiempo: `O(n)`
- Espacio: `O(1)`

### Recursiva

- Tiempo: `O(n)`
- Espacio: `O(n)`

Porque la recursión usa la pila de llamadas.

## 5) ¿Es eficiente o no?

La iterativa suele ser más eficiente en memoria.

La recursiva es más elegante matemáticamente, pero usa más espacio.

Entonces:

- para entender el concepto, la recursiva es muy buena
- para ejecutar mejor, la iterativa suele convenir más

---

# Resumen general de todos

## 1. Par o impar

- Tipo: verificación directa
- Big O: `O(1)`
- Eficiencia: muy eficiente

## 2. Intercambiar dos números

- Tipo: manipulación de variables
- Big O: `O(1)`
- Eficiencia: eficiente

## 3. Número primo

- Tipo: búsqueda de divisor / divisibilidad
- Big O: `O(n)` o `O(sqrt(n))`
- Eficiencia: la versión con raíz es mejor

## 4. Divisores

- Tipo: enumeración / búsqueda lineal
- Big O: `O(n)`
- Eficiencia: correcta, pero mejorable

## 5. Fibonacci

- Tipo: recurrencia iterativa / programación dinámica simple
- Big O: `O(n)`
- Eficiencia: buena

## 6. Factorial

- Tipo: acumulación o recursión
- Big O: `O(n)`
- Eficiencia: iterativo mejor en memoria

---

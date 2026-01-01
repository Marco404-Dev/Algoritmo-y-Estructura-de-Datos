# Introducción a Algoritmos – MIT 6.006 (Lecture 1)

## Objetivo del curso
El objetivo del curso es aprender a:
- Resolver **problemas computacionales**
- Demostrar que las soluciones son:
  - **Correctas**
  - **Eficientes**

No basta con que un programa funcione para algunos casos; debe funcionar **para todas las entradas posibles** y hacerlo de manera eficiente.

---

## ¿Qué es un problema en algoritmos?
Un **problema** define:
- Una relación entre **entradas** y **salidas correctas**
- No se enumeran todas las salidas posibles (son demasiadas)
- Se define una **propiedad verificable** que toda solución correcta debe cumplir

### Problemas pequeños vs generales
- ❌ Problema pequeño:  
  > ¿En este salón hay dos estudiantes con el mismo cumpleaños?
- ✅ Problema general:  
  > Dado cualquier conjunto de `n` estudiantes, ¿existen dos con el mismo cumpleaños?

Los algoritmos siempre se enfocan en **problemas generales**, no casos particulares.

---

## ¿Qué es un algoritmo?
Un **algoritmo** es:
- Un procedimiento paso a paso
- Que recibe una entrada
- Produce **una única salida**
- Es **determinista**

Un algoritmo **resuelve un problema** si devuelve una salida correcta **para toda entrada válida**.

---

## Ejemplo: algoritmo de cumpleaños
Idea del algoritmo:
1. Crear un registro vacío
2. Revisar estudiantes uno por uno
3. Si el cumpleaños ya está en el registro → se encontró un par
4. Si no, se guarda el cumpleaños
5. Si termina sin coincidencias → no existe un par

---

## Corrección del algoritmo (Correctness)
Problema clave:
> ¿Cómo probar que un algoritmo funciona para entradas arbitrariamente grandes?

### Solución: Inducción
Los algoritmos usan:
- Bucles
- Recursión

Por eso la **inducción matemática** es esencial.

### Idea de la prueba:
- Hipótesis: el algoritmo funciona para los primeros `k` elementos
- Paso inductivo: demostrar que funciona para `k + 1`
- Caso base: `k = 0`

---

## Eficiencia de un algoritmo
No se mide el tiempo real (segundos), porque depende del hardware.

Se mide:
- El número de **operaciones básicas**
- En función del tamaño de la entrada (`n`)

Un algoritmo es **eficiente** si su tiempo de ejecución es **polinómico**.

---

## Notación asintótica
Se ignoran:
- Constantes
- Términos de menor orden

### Notaciones principales:
- **O(n)**: cota superior
- **Ω(n)**: cota inferior
- **Θ(n)**: cota exacta

Ejemplos:
- Θ(1) → constante
- Θ(n) → lineal
- Θ(n²) → cuadrático
- Θ(2ⁿ) → exponencial (ineficiente)

---

## Modelo de computación: Word-RAM
El curso asume el modelo **Word-RAM**:
- Memoria dividida en palabras de tamaño fijo (32 o 64 bits)
- Operaciones básicas toman **O(1)**:
  - Suma, resta, comparación
  - Lectura y escritura en memoria

Python está implementado **sobre** este modelo, pero es más complejo internamente.

---

## Estructuras de datos
Una **estructura de datos** permite almacenar información y realizar operaciones sobre ella.

Ejemplos:
- Arreglos
- Listas enlazadas
- Arreglos dinámicos
- Tablas hash
- Árboles balanceados
- Heaps

👉 **La elección de la estructura de datos afecta directamente la eficiencia del algoritmo.**

---

## Análisis del algoritmo de cumpleaños
Implementación básica con arreglo:
- Dos bucles anidados
- Tiempo total: **O(n²)**

Es polinómico, pero **no óptimo**.

Usando una mejor estructura (ej. hash table):
- Tiempo puede reducirse a **O(n)**

---

## Cómo resolver un problema de algoritmos
1. Reducirlo a un problema conocido  
   - Usar una estructura de datos existente
   - Usar un algoritmo clásico
2. Diseñar un algoritmo propio:
   - Fuerza bruta
   - Divide y vencerás
   - Programación dinámica
   - Algoritmos voraces
   - Incrementales

---

## Idea central del curso
> **Algoritmos = Diseño + Corrección + Eficiencia**

No se trata solo de programar, sino de:
- Pensar rigurosamente
- Probar que funciona
- Optimizar el rendimiento

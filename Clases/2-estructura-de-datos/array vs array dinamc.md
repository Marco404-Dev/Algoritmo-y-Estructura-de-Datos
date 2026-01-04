# 🔍 Array vs Dynamic Array

## 📌 Array (Arreglo Estático)

Un **array** tiene un tamaño fijo que se define al crearlo.  
No reserva espacio extra para crecer.

### Características
- Tamaño fijo
- No usa espacio adicional
- Implementación simple

### Complejidad de operaciones
- Acceso por índice `get_at(i)` → Θ(1)
- Modificación `set_at(i, x)` → Θ(1)
- Insertar al final `insert_last(x)` → O(n)
- Insertar en posición i → O(n)

### Ejemplo

    A = [10, 20, 30]

Si se desea insertar un nuevo elemento:
- se debe crear un nuevo array
- copiar todos los elementos
- mover posiciones

---

## 📌 Dynamic Array (Arreglo Dinámico)

Un **array dinámico** reserva espacio extra para permitir crecimiento sin redimensionar en cada inserción.

Ejemplo real: `list` en Python.

### Características
- Tamaño variable
- Usa espacio adicional
- Redimensiona solo cuando se llena

### Complejidad de operaciones
- Acceso por índice `get_at(i)` → Θ(1)
- Modificación `set_at(i, x)` → Θ(1)
- Insertar al final `insert_last(x)` → Θ(1) amortizado
- Insertar en posición i → O(n)

### Ejemplo

    L = []
    L.append(10)
    L.append(20)
    L.append(30)

La mayoría de inserciones son rápidas; solo algunas requieren copiar todos los elementos.

---

## 🧠 Análisis Amortizado

Aunque algunas inserciones cuestan Θ(n), ese costo ocurre pocas veces  
y se reparte entre muchas inserciones baratas.

Por eso insertar al final es **Θ(1) amortizado**.

---

## ⚖️ Comparación directa

| Característica | Array | Dynamic Array |
|---------------|------|---------------|
| Tamaño | Fijo | Variable |
| Espacio extra | No | Sí |
| Acceso por índice | Θ(1) | Θ(1) |
| Inserción al final | O(n) | Θ(1) amortizado |
| Inserciones frecuentes | Ineficiente | Eficiente |

---

# ⚖️ Trade-offs en Estructuras de Datos

## ¿Qué es un trade-off?
Un **trade-off** es un compromiso:  
mejorar una cosa implica **empeorar otra**.

En estructuras de datos:
> **No se puede optimizar todas las operaciones al mismo tiempo.**

---

## 🧠 Idea clave
Elegir una estructura de datos es decidir:
- qué operaciones quiero que sean **rápidas**
- y cuáles acepto que sean **lentas**

---

## 🔁 Ejemplo clásico: Array vs Linked List

### Array
**Ventaja**
- Acceso por índice muy rápido → Θ(1)

**Desventaja**
- Insertar o borrar elementos es lento → O(n)

👉 Trade-off:  
Acceso rápido **a cambio** de inserciones lentas.

---

### Linked List
**Ventaja**
- Insertar o borrar al inicio es rápido → Θ(1)

**Desventaja**
- Acceder al elemento i-ésimo es lento → O(n)

👉 Trade-off:  
Inserciones rápidas **a cambio** de acceso lento.

---

## ⚖️ Otro ejemplo: Array vs Dynamic Array

### Array
- Menos uso de memoria
- Tamaño fijo
- Inserciones costosas

### Dynamic Array
- Usa memoria extra
- Inserciones al final rápidas (Θ(1) amortizado)

👉 Trade-off:  
Más memoria **a cambio** de inserciones eficientes.

---

## 🧪 Ejemplo cotidiano
Una mochila:
- pequeña → cómoda (menos peso), pero no entra todo
- grande → entra todo, pero pesa más

No hay una “mejor”, depende del uso.

---

## 📌 Por qué los trade-offs importan
Porque:
- definen la **eficiencia del algoritmo**
- justifican la **elección de estructura**
- aparecen mucho en **exámenes**

---

## 🏁 Conclusión
- No existe la estructura perfecta
- Toda estructura optimiza algo y sacrifica otra cosa
- Entender los trade-offs es clave para diseñar buenos algoritmos


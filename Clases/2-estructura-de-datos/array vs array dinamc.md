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

## 🏁 Conclusión

Ambos implementan la interfaz `Sequence`,  
pero están optimizados para **situaciones distintas**.

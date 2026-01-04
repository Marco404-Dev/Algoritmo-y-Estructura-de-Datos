# 🔍 Array vs Dynamic Array

Aunque ambos se llaman “array”, **no son lo mismo**.  
La diferencia principal está en **cómo manejan el tamaño y las inserciones**.

---

## 📌 Array (Arreglo Estático)

Un **array** tiene un tamaño fijo que se define al crearse.  
No posee espacio extra para crecer.

### Características
- Tamaño fijo
- Acceso por índice rápido
- No gestiona crecimiento automático

### Complejidad de operaciones
- `get_at(i)` → Θ(1)
- `set_at(i, x)` → Θ(1)
- `insert_last(x)` → O(n)
- `insert_at(i, x)` → O(n)

### Ejemplo
```python
A = [10, 20, 30]  # tamaño fijo

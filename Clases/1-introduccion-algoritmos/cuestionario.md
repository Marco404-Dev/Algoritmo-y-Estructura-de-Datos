## ¿Qué es un algoritmo y cuándo se dice que un algoritmo resuelve un problema?

Un **algoritmo** es un procedimiento que resuelve un **problema computacional general**, es decir, válido para entradas de tamaño arbitrario `n`.

Un algoritmo se dice que **resuelve un problema** cuando produce una **salida correcta para toda entrada válida**, cumpliendo la especificación del problema.

Además, no basta con que sea correcto, sino que también debe ser **eficiente**, lo cual se analiza mediante **notación asintótica**.  
La corrección suele demostrarse usando **inducción**, debido al uso de bucles o recursión.

---

## ¿Qué significa que un algoritmo sea correcto y cómo se demuestra normalmente su corrección?

Un algoritmo es **correcto** si, para **toda entrada válida**, produce una salida que cumple con la **especificación del problema**.

La corrección se demuestra generalmente mediante **inducción matemática**, ya que los algoritmos suelen utilizar **bucles o recursión**, lo que permite probar que el algoritmo funciona para un **caso base** y que, si funciona para un tamaño `k`, también funciona para `k + 1`.

---

## ¿Por qué no se mide la eficiencia de un algoritmo en segundos y cómo se mide entonces?

La eficiencia de un algoritmo no se mide en **segundos** porque el tiempo real depende del **hardware**, del **lenguaje** y de la **implementación**.

En su lugar, se mide contando el número de **operaciones básicas** que ejecuta el algoritmo en función del tamaño de la entrada `n`.

Este análisis se expresa mediante **notación asintótica**, como **O**, **Ω** y **Θ**, lo que permite comparar algoritmos de manera **independiente de la máquina utilizada**.

---

## Explica qué es la notación O(n) y qué información nos da sobre un algoritmo

**O(n)** es una **cota superior** del tiempo de ejecución de un algoritmo.

Indica que el número de operaciones crece de forma **lineal** con el tamaño de la entrada `n`.

- Si `n` se duplica, el tiempo de ejecución **aproximadamente se duplica**.

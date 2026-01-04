# 🧪 Ejercicios Resueltos – Clase 2: Estructuras de Datos (MIT 6.006)

---

## 1️⃣ Interfaz vs Estructura
**Pregunta:**  
Explica con tus palabras la diferencia entre interfaz y estructura de datos.

**Respuesta:**  
Una **interfaz** define *qué operaciones* se pueden realizar sobre los datos, por ejemplo: insertar, buscar o eliminar.  
Una **estructura de datos** define *cómo se implementan internamente* esas operaciones usando memoria y algoritmos.

**Ejemplo:**  
- La interfaz `Sequence` dice que puedo acceder al elemento i-ésimo.  
- Un **array** lo hace accediendo directamente a memoria.  
- Una **lista enlazada** lo hace recorriendo nodo por nodo.

La operación es la misma, pero la implementación y el costo cambian.

---

## 2️⃣
**Pregunta:**  
¿Es correcto decir que `Sequence` es una estructura de datos? Justifica.

**Respuesta:**  
No. `Sequence` es una **interfaz**, no una estructura de datos.

`Sequence` solo especifica operaciones como:
- acceder por índice
- insertar o eliminar elementos

Pero no dice **cómo** se realizan.  
Estructuras como **array**, **lista enlazada** o **array dinámico** son las que implementan esa interfaz.

---

## 3️⃣
**Pregunta:**  
Da dos estructuras que implementen la interfaz `Sequence` y menciona una diferencia clave.

**Respuesta:**  
- **Array**
- **Lista enlazada**

Diferencia clave:
- En un **array**, acceder al elemento i-ésimo es rápido (Θ(1)).
- En una **lista enlazada**, acceder al elemento i-ésimo es lento (O(n)) porque hay que recorrer la lista.

Ambas son `Sequence`, pero se comportan distinto.

---

## 4️⃣
**Pregunta:**  
¿Por qué el MIT separa interfaz de implementación?

**Respuesta:**  
Porque así se puede:
- analizar algoritmos sin depender de una estructura específica
- comparar distintas soluciones al mismo problema
- elegir la estructura correcta según el contexto

**Ejemplo:**  
El problema es “mantener una secuencia”.  
La solución puede ser un array o una lista enlazada.  
Separar interfaz e implementación permite evaluar cuál es mejor.

---

## 5️⃣
**Pregunta:**  
Verdadero o falso:  
“Una estructura de datos define qué operaciones se pueden hacer”.

**Respuesta:**  
Falso.

Las operaciones las define la **interfaz**.  
La estructura solo define cómo se ejecutan esas operaciones.

**Ejemplo:**  
La interfaz `Set` define la operación `find(k)`.  
Una tabla hash y un árbol implementan `find(k)` de formas distintas.

---

## 6️⃣ Identificación de interfaces
**Pregunta:**  
Clasifica como `Sequence` o `Set`:

a) Historial de navegación  
b) Agenda telefónica por número  
c) Fila de impresión  
d) Ranking de puntajes  
e) Registro de estudiantes por código  

**Respuesta:**  
a) Sequence → importa el orden en que se visitaron las páginas  
b) Set → se busca por número, no por posición  
c) Sequence → el orden de llegada importa  
d) Sequence → importa la posición (1°, 2°, 3°)  
e) Set → cada estudiante se identifica por un código único  

---

## 7️⃣
**Pregunta:**  
¿Una pila (stack) pertenece a `Sequence` o `Set`? ¿Por qué?

**Respuesta:**  
Pertenece a `Sequence` porque mantiene un orden de elementos.

Aunque solo permite insertar y eliminar por un extremo, sigue siendo una secuencia con restricciones en sus operaciones.

---

## 8️⃣
**Pregunta:**  
¿Por qué un diccionario no es una secuencia?

**Respuesta:**  
Porque no se accede por posición (i-ésimo elemento), sino por clave.

**Ejemplo:**  
En un diccionario:
- se busca por “nombre” o “ID”
- no existe el concepto de “primer” o “tercer” elemento

Por eso implementa `Set`, no `Sequence`.

---

## 9️⃣
**Pregunta:**  
Da un ejemplo de problema que no pueda resolverse correctamente con `Set`.

**Respuesta:**  
Una lista de reproducción de música.

En una playlist:
- el orden importa
- hay canciones antes y después de otras

Un `Set` no mantiene orden, por lo tanto no sirve.

---

## 🔟
**Pregunta:**  
¿Puede una estructura implementar más de una interfaz?

**Respuesta:**  
Sí, dependiendo de las operaciones que soporte.

**Ejemplo:**  
Un árbol de búsqueda puede:
- funcionar como `Set` (buscar por clave)
- y también recorrer elementos en orden, similar a una `Sequence`

---

## 1️⃣1️⃣ Elección de estructura
**Pregunta:**  
Necesitas acceso rápido por índice y pocas inserciones. ¿Qué eliges?

**Respuesta:**  
Un **array**.

Porque:
- `get_at(i)` es Θ(1)
- las inserciones son pocas, así que el costo O(n) no es crítico

---

## 1️⃣2️⃣
**Pregunta:**  
Necesitas muchas inserciones al inicio y poco acceso aleatorio. ¿Qué eliges?

**Respuesta:**  
Una **lista enlazada**.

Porque:
- insertar al inicio cuesta Θ(1)
- no importa que acceder por índice sea lento

---

## 1️⃣3️⃣
**Pregunta:**  
Necesitas acceso rápido por índice e inserciones frecuentes al final. ¿Qué eliges?

**Respuesta:**  
Un **array dinámico**.

Porque:
- acceso por índice es Θ(1)
- insertar al final es Θ(1) amortizado

Ejemplo: `list` en Python.

---

## 1️⃣4️⃣
**Pregunta:**  
¿Por qué no existe una estructura “mejor para todo”?

**Respuesta:**  
Porque mejorar una operación suele empeorar otra.

**Ejemplo:**  
- Arrays → acceso rápido, inserciones lentas  
- Listas → inserciones rápidas, acceso lento  

Siempre hay compromisos (trade-offs).

---

## 1️⃣5️⃣
**Pregunta:**  
Explica el trade-off entre array y lista enlazada.

**Respuesta:**  
El array prioriza el acceso rápido por índice.  
La lista enlazada prioriza la inserción y eliminación rápidas.

No se puede optimizar ambas cosas al mismo tiempo sin pagar un costo.

---

## 1️⃣6️⃣ Complejidad
**Pregunta:**  
Indica el costo en el peor caso:

a) `get_at(i)` en array  
b) `get_at(i)` en lista enlazada  
c) `insert_first(x)` en lista enlazada  
d) `insert_last(x)` en array  

**Respuesta:**  
a) Θ(1) → acceso directo  
b) O(n) → recorrido completo  
c) Θ(1) → solo cambia punteros  
d) O(n) → hay que mover elementos  

---

## 1️⃣7️⃣
**Pregunta:**  
¿Por qué la tabla comparativa no introduce contenido nuevo?

**Respuesta:**  
Porque solo organiza información ya explicada:  
resume los costos de las operaciones para facilitar la comparación.

---

## 1️⃣8️⃣
**Pregunta:**  
¿Para qué sirve la tabla en un examen?

**Respuesta:**  
Para justificar de forma clara por qué una estructura es mejor que otra según las operaciones requeridas.

---

## 1️⃣9️⃣ Análisis amortizado
**Pregunta:**  
¿Qué significa que una operación sea Θ(1) amortizado?

**Respuesta:**  
Significa que aunque algunas ejecuciones sean caras, el costo promedio por operación es constante.

**Ejemplo:**  
En un array dinámico:
- la mayoría de inserciones cuestan poco
- algunas cuestan mucho
- en promedio, el costo es bajo

---

## 2️⃣0️⃣
**Pregunta:**  
Verdadero o falso:  
“Si una operación tiene peor caso Θ(n), la estructura es ineficiente”.

**Respuesta:**  
Falso.

Una estructura puede ser eficiente si ese peor caso ocurre pocas veces y el costo promedio sigue siendo bajo.

Ejemplo: `append()` en Python.

---

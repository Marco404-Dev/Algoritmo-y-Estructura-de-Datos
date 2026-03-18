Doc introduccion: teoría más desarrollada + explicación detallada + ejercicios.

Doc lec: misma base, pero más resumida y orientada a la clase, con el ejemplo del cumpleaños ya presentado como aplicación completa.


# Introducción a Algoritmos – MIT 6.006 (Lecture 1)

## ¿De qué trata esta primera clase?

La primera clase introduce la idea central del curso: en algoritmos no basta con escribir código que “parezca funcionar”. Lo importante es aprender a diseñar soluciones para problemas generales, demostrar que esas soluciones siempre son correctas y analizar qué tan eficientes son.

En otras palabras, el curso no se centra solo en programar, sino en **pensar de forma rigurosa**.

---

# 1. Objetivo del curso

El curso busca enseñar a:

- Resolver **problemas computacionales**
- Diseñar **algoritmos correctos**
- Analizar si esos algoritmos son **eficientes**
- Elegir buenas **estructuras de datos**

La idea principal es esta:

> Un buen algoritmo no solo da la respuesta correcta, sino que la da de forma eficiente.

---

# 2. ¿Qué es un problema en algoritmos?

En algoritmos, un **problema** no es un caso específico, sino una situación general que puede tener muchas entradas distintas.

Un problema define:

- qué tipo de **entrada** recibe,
- qué tipo de **salida** debe producir,
- y qué condiciones debe cumplir esa salida para ser correcta.

## Ejemplo

### Caso particular
> ¿En este salón hay dos estudiantes con el mismo cumpleaños?

Eso es una situación concreta.

### Problema general
> Dado un conjunto de `n` estudiantes, determinar si existen dos con el mismo cumpleaños.

Eso sí es un problema algorítmico, porque sirve para cualquier tamaño de entrada.

## Idea importante

Los algoritmos no se diseñan para un solo ejemplo, sino para **todas las entradas válidas posibles**.

---

# 3. ¿Qué es un algoritmo?

Un **algoritmo** es un procedimiento paso a paso que:

- recibe una entrada,
- sigue una secuencia bien definida de instrucciones,
- y produce una salida.

Normalmente se espera que un algoritmo sea:

- **preciso**: cada paso está claramente definido,
- **determinista**: dada la misma entrada, produce la misma salida,
- **finito**: termina después de cierto número de pasos.

## Cuándo un algoritmo resuelve un problema

Un algoritmo resuelve un problema si, para **toda entrada válida**, devuelve una salida correcta.

Eso significa que no basta con que funcione “en algunos casos” o “en los ejemplos del profesor”.

---

# 4. Ejemplo principal: el problema de los cumpleaños

La clase usa como ejemplo el problema de encontrar si dos personas comparten cumpleaños.

## Idea del algoritmo

Una forma simple de resolverlo es:

1. Revisar los estudiantes uno por uno
2. Guardar los cumpleaños que ya aparecieron
3. Si un cumpleaños vuelve a aparecer, entonces ya se encontró una coincidencia
4. Si se termina de revisar a todos y no hubo repeticiones, entonces no existe coincidencia

## Qué enseña este ejemplo

Este ejemplo sirve para introducir tres preguntas fundamentales:

- **¿El algoritmo funciona siempre?**
- **¿Cómo demostrarlo?**
- **¿Qué tan rápido o lento es?**

---

# 5. Corrección del algoritmo

Uno de los temas más importantes del curso es la **corrección**.

## ¿Qué significa que un algoritmo sea correcto?

Significa que el algoritmo siempre produce una respuesta válida para cualquier entrada permitida.

No basta con probarlo con pocos ejemplos.  
Se necesita una **demostración formal**.

## ¿Cómo se suele demostrar?

La clase introduce la idea de usar **inducción**, porque muchos algoritmos trabajan con:

- bucles,
- recursión,
- procesamiento paso a paso de una colección.

## Idea intuitiva de la inducción

Para probar que algo funciona:

1. Se verifica un **caso base**
2. Se asume que funciona para un caso más pequeño
3. Se demuestra que entonces también funciona para el siguiente caso

## Aplicado al ejemplo

En el problema de cumpleaños, la idea sería demostrar que:

- después de procesar los primeros `k` estudiantes, el algoritmo mantiene correctamente la información vista,
- y al revisar el estudiante `k + 1`, sigue comportándose bien.

---

# 6. Eficiencia de un algoritmo

Además de que un algoritmo sea correcto, importa cuánto tarda.

## ¿Por qué no medir en segundos?

Porque los segundos dependen de factores externos como:

- la computadora,
- el procesador,
- el lenguaje,
- la implementación.

Por eso en algoritmos se prefiere medir el número de **operaciones básicas** en función del tamaño de la entrada.

## Tamaño de entrada

Normalmente se representa por `n`.

Por ejemplo:

- si el problema recibe una lista de elementos,
- entonces `n` suele ser la cantidad de elementos de la lista.

---

# 7. Notación asintótica

La notación asintótica se usa para describir cómo crece el costo de un algoritmo cuando la entrada se vuelve grande.

En lugar de fijarnos en detalles pequeños, nos interesa la tendencia de crecimiento.

## Qué se ignora

Al analizar crecimiento, normalmente se ignoran:

- constantes multiplicativas,
- términos de menor orden.

Por ejemplo:

`3n² + 5n + 2`

crece esencialmente como:

`n²`

---

## Notaciones principales

### Big-O: `O(f(n))`
Da una **cota superior** del crecimiento.

Indica que el algoritmo no crece más rápido que cierta función, salvo constantes.

### Big-Omega: `Ω(f(n))`
Da una **cota inferior**.

Indica que el crecimiento es al menos de ese orden.

### Big-Theta: `Θ(f(n))`
Da una **cota ajustada**.

Indica que el crecimiento es exactamente de ese orden asintótico.

---

## Ejemplos comunes

- `Θ(1)` → tiempo constante
- `Θ(log n)` → logarítmico
- `Θ(n)` → lineal
- `Θ(n log n)` → casi lineal
- `Θ(n²)` → cuadrático
- `Θ(2^n)` → exponencial

## Idea clave

Mientras más rápido crece la función, menos eficiente suele ser el algoritmo para entradas grandes.

---

# 8. Modelo de computación: Word-RAM

Para analizar algoritmos, la clase usa un modelo teórico llamado **Word-RAM**.

## ¿Qué asume este modelo?

- La memoria está dividida en palabras de tamaño fijo
- Cada palabra puede tener, por ejemplo, 32 o 64 bits
- Operaciones básicas cuestan `O(1)`

## Ejemplos de operaciones `O(1)`

- sumar,
- restar,
- comparar,
- leer memoria,
- escribir memoria.

## ¿Por qué sirve este modelo?

Porque permite analizar algoritmos de forma abstracta sin depender de una computadora específica.

---

# 9. Estructuras de datos

La clase también resalta que un algoritmo depende mucho de la **estructura de datos** que usa.

## ¿Qué es una estructura de datos?

Es una forma organizada de almacenar información para poder realizar operaciones sobre ella.

## Ejemplos

- arreglos,
- listas enlazadas,
- arreglos dinámicos,
- tablas hash,
- árboles,
- heaps.

## Idea fundamental

> La misma idea algorítmica puede ser lenta o rápida dependiendo de la estructura de datos elegida.

Esto es muy importante en el problema de cumpleaños.

---

# 10. Análisis del problema de cumpleaños

## Solución simple

Si se compara cada estudiante con todos los demás, aparecen dos bucles anidados.

Eso da un tiempo de:

`O(n²)`

porque por cada estudiante puede revisarse casi toda la lista otra vez.

## ¿Es correcta?
Sí, puede ser correcta.

## ¿Es eficiente?
No tanto, porque el tiempo cuadrático crece rápido cuando `n` aumenta.

## Mejora posible

Si se usa una estructura de datos mejor, como una **tabla hash**, se puede registrar cada cumpleaños visto y verificar repeticiones mucho más rápido.

Entonces el tiempo puede bajar a:

`O(n)`

## Enseñanza principal

No solo importa la idea del algoritmo, sino también **cómo se almacenan y consultan los datos**.

---

# 11. Cómo se abordan los problemas algorítmicos

La clase menciona dos caminos generales:

## 1. Reducir el problema a algo conocido
Esto puede significar:

- usar una estructura de datos adecuada,
- aplicar un algoritmo clásico,
- transformar el problema en otro ya resuelto.

## 2. Diseñar una solución nueva
Entre las técnicas generales que el curso estudiará están:

- fuerza bruta,
- divide y vencerás,
- programación dinámica,
- algoritmos voraces,
- métodos incrementales.

---

# 12. Idea central de la clase

La introducción deja claro que estudiar algoritmos significa combinar tres cosas:

## Diseño
Pensar cómo resolver el problema.

## Corrección
Demostrar que la solución siempre funciona.

## Eficiencia
Analizar cuántos recursos consume.

---

# 13. Resumen final

La primera clase del curso establece la base de todo lo que viene después.

Se aprende que:

- un problema algorítmico debe formularse de manera general,
- un algoritmo debe funcionar para toda entrada válida,
- la corrección debe demostrarse formalmente,
- la eficiencia se analiza con notación asintótica,
- y la elección de la estructura de datos puede cambiar completamente el rendimiento.

## Fórmula mental de la clase

> **Algoritmos = Problema + Diseño + Corrección + Eficiencia**

---

# 14. Conclusión

Esta clase no busca enseñar un solo programa, sino una forma de pensar.

El mensaje principal es que en algoritmos no basta con “hacer que funcione”.  
Hay que poder responder con claridad:

- **qué problema estoy resolviendo,**
- **por qué mi algoritmo es correcto,**
- **y qué tan eficiente es cuando la entrada crece.**

Esa es la base de todo el curso.

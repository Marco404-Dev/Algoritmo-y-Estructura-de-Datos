# 20 preguntas y respuestas sobre Hashing (Tablas Hash)

1) **¿Qué es hashing?**  
   **Respuesta:** Es una técnica para **guardar y buscar datos rápido**, convirtiendo una **clave** en un **índice** de una tabla mediante una **función hash**.

2) **¿Qué es una tabla hash?**  
   **Respuesta:** Un **arreglo de tamaño fijo (m)** con “cajones” donde se guardan elementos según el índice que produce el hash.

3) **¿Qué es una función hash?**  
   **Respuesta:** Una regla que transforma una clave `k` en un índice `0..m-1` para saber dónde guardar/buscar.

4) **Si `m = 10` y `h(k) = k mod 10`, ¿cuál es `h(52)`?**  
   **Respuesta:** `52 mod 10 = 2`, entonces `h(52)=2`.

5) **Con la misma función, ¿cuál es `h(42)`?**  
   **Respuesta:** `42 mod 10 = 2`, entonces `h(42)=2`.

6) **¿Qué es una colisión?**  
   **Respuesta:** Cuando **dos claves distintas** producen el **mismo índice**: `h(a)=h(b)` con `a≠b`.

7) **¿Por qué las colisiones son inevitables?**  
   **Respuesta:** Porque hay más claves posibles que cajones (`u` grande y `m` pequeño), así que algunas terminarán compartiendo cajón.

8) **Con `h(k)=k mod 10`, ¿con qué números choca 42?**  
   **Respuesta:** Con todos los que terminan en 2: `2, 12, 22, 32, 52, 62, ...`

9) **¿Qué es “chaining” (encadenamiento)?**  
   **Respuesta:** Una forma de resolver colisiones donde **cada cajón guarda una lista** de elementos.

10) **Si insertas 52 y 42 con chaining y `m=10`, ¿cómo queda el cajón 2?**  
   **Respuesta:** `cajón 2: [52, 42]` (o `[42, 52]`, el orden puede variar).

11) **¿Cómo se busca una clave `k` en una tabla hash con chaining?**  
   **Respuesta:** 1) calculas `i = h(k)` 2) vas al cajón `i` 3) buscas `k` dentro de la lista de ese cajón.

12) **¿Cómo se elimina una clave `k` con chaining?**  
   **Respuesta:** 1) `i=h(k)` 2) vas al cajón `i` 3) la quitas de la lista.

13) **¿Qué es “open addressing” (direccionamiento abierto)?**  
   **Respuesta:** Otra solución a colisiones: si el cajón está ocupado, se busca **otro cajón libre** siguiendo una regla (sondeo).

14) **Diferencia principal entre chaining y open addressing.**  
   **Respuesta:** Chaining usa **listas por cajón**; open addressing guarda todo **solo en la tabla** buscando otro cajón libre cuando hay choque.

15) **¿Qué pasa si muchos elementos caen en el mismo cajón con chaining?**  
   **Respuesta:** La lista crece y buscar se vuelve más lento, porque ya no revisas “poquitos”, sino muchos.

16) **¿Qué intenta lograr una “buena” función hash?**  
   **Respuesta:** Que las claves se **repartan lo más uniforme posible** entre los cajones para reducir colisiones.

17) **Si `m=10` y `h(k)=k mod 10`, calcula:** `h(27), h(18), h(39), h(41)`  
   **Respuesta:** `7, 8, 9, 1` respectivamente.

18) **Tabla `m=10`, `h(k)=k mod 10`. Inserta:** 12, 22, 35, 27, 42. ¿Qué cajones se usan?  
   **Respuesta:**  
   - 12 → 2  
   - 22 → 2 (colisión)  
   - 35 → 5  
   - 27 → 7  
   - 42 → 2 (colisión)  
   Cajones usados: **2, 5, 7**.

19) **Con chaining, ¿cómo queda la tabla del ejercicio anterior (solo cajones usados)?**  
   **Respuesta:**  
   - `2: [12, 22, 42]`  
   - `5: [35]`  
   - `7: [27]`

20) **¿Cuál es la ventaja clave del hashing frente a una lista normal?**  
   **Respuesta:** En promedio permite **búsqueda e inserción muy rápida** porque vas directo al cajón usando `h(k)` en vez de revisar todo.



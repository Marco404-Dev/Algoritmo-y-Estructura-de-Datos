# Programación Dinámica (DP) — Explicación desde cero (bien simple)

## 1) DP en 1 idea
**DP = resolver un problema grande usando respuestas de problemas más pequeños, pero SIN repetir cálculos.**

- Si en recursión calculas lo mismo muchas veces → **guardas** y reutilizas → eso es **DP**.

---

## 2) Por qué la clase habla tanto de “subproblemas”
Porque **DP depende 100% de cómo defines el subproblema**.

Un subproblema es una pregunta pequeña del mismo tipo.

Ejemplo (LCS):
- Problema grande: “LCS de A y B”
- Subproblema: “LCS de un pedazo de A y un pedazo de B”

Si defines mal el subproblema, luego **no puedes armar una fórmula correcta**.

---

## 3) Ejemplo desde cero: LCS (Longest Common Subsequence)

### 3.1 ¿Qué pide LCS?
Dadas dos cadenas, encontrar la **longitud** de la subsecuencia común más larga.  
(Subsecuencia = puedes saltarte letras, pero manteniendo el orden.)

Ejemplo:
- A = `"AB"`
- B = `"BA"`
La LCS aquí tiene longitud **1** (puede ser `"A"` o `"B"`).

---

### 3.2 Subproblema (lo que guardas en la tabla)
Definimos:

**dp[i][j] = longitud del LCS entre A desde i hasta el final y B desde j hasta el final**  
(“desde i” significa A[i:], y “desde j” significa B[j:])

Para A="AB" (n=2) y B="BA" (m=2), i va 0..2 y j va 0..2.

---

### 3.3 Casos base (cuando ya no hay nada)
Si una cadena se acabó, ya no hay subsecuencia común:

- dp[i][m] = 0 para todo i
- dp[n][j] = 0 para todo j

En palabras:
- si j = 2 (B se acabó) → 0
- si i = 2 (A se acabó) → 0

---

### 3.4 Regla (la fórmula)
Mira dos letras: A[i] y B[j]

**Caso 1: si A[i] == B[j]**
- esa letra puede formar parte de la subsecuencia:
- dp[i][j] = 1 + dp[i+1][j+1]

**Caso 2: si A[i] != B[j]**
- pruebas “descartar” una letra:
- dp[i][j] = max(dp[i+1][j], dp[i][j+1])

---

### 3.5 Orden de llenado (esto es el “orden topológico”)
Como dp[i][j] usa dp con índices **más grandes** (i+1, j+1), debes llenar:
- i desde n hacia 0 (de abajo hacia arriba)
- j desde m hacia 0 (de derecha a izquierda)

O sea: empiezas por las bases y retrocedes.

---

### 3.6 Llenado completo con A="AB" y B="BA"

A indices:
- A[0]='A'
- A[1]='B'

B indices:
- B[0]='B'
- B[1]='A'

Tabla dp de tamaño (n+1)x(m+1) = 3x3.

**Paso 1: Bases (última fila y última columna en 0)**
- dp[2][0]=0, dp[2][1]=0, dp[2][2]=0
- dp[0][2]=0, dp[1][2]=0, dp[2][2]=0

**Paso 2: dp[1][1]**
- A[1]='B', B[1]='A' (no iguales)
- dp[1][1] = max(dp[2][1], dp[1][2]) = max(0,0)=0

**Paso 3: dp[1][0]**
- A[1]='B', B[0]='B' (iguales)
- dp[1][0] = 1 + dp[2][1] = 1 + 0 = 1

**Paso 4: dp[0][1]**
- A[0]='A', B[1]='A' (iguales)
- dp[0][1] = 1 + dp[1][2] = 1 + 0 = 1

**Paso 5: dp[0][0]**
- A[0]='A', B[0]='B' (no iguales)
- dp[0][0] = max(dp[1][0], dp[0][1]) = max(1,1)=1

✅ **Respuesta final = dp[0][0] = 1**

---

## 4) “Restricción” y “expansión” de subproblemas (lo que decía la clase)

### A) Restricción (como en LIS)
Si tu subproblema está “muy libre” y no asegura la condición (por ejemplo “creciente”), lo restringes.

Ejemplo típico de LIS:
- “LIS que **incluye** A[i]”
Eso obliga a que la condición de “creciente” sea controlable.

### B) Expansión (como en el juego de monedas)
Si falta información para decidir bien (por ejemplo, “¿de quién es el turno?”), agregas un parámetro extra:

- dp[i][j][turno]

Eso se llama **expansión**: agregas estado extra para que la fórmula sea correcta.

---

## 5) Lo que debes recordar de la clase 16
**DP no es memorizar fórmulas; es aprender a definir el subproblema correcto.**

- Si falta información → **expandes**
- Si sobra libertad y se rompe la condición → **restringes**

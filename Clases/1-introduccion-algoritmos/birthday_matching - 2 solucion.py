## Usando diccionario (la más eficiente)

def coincidencia_cumpleanos_dic(estudiantes):
    """
    Busca un par de estudiantes que compartan cumpleaños usando diccionario.
    Entrada: lista de tuplas (nombre, cumpleaños)
    Salida: tupla con los nombres o None
    """
    vistos = {}  # diccionario para cumpleaños ya vistos
    
    for nombre, cumple in estudiantes:
        if cumple in vistos:
            return (nombre, vistos[cumple])
        vistos[cumple] = nombre
    
    return None

# --- Lista de ejemplo ---
estudiantes = [
    ("Ana", "01-01"),
    ("Luis", "12-05"),
    ("Ruth", "01-01"),  # misma fecha que Ana
    ("Carlos", "23-08")
]

# --- Llamar a la función ---
resultado = coincidencia_cumpleanos_dic(estudiantes)

if resultado:
    print(f"Coincidencia encontrada: {resultado[0]} y {resultado[1]}")
else:
    print("No hay coincidencias de cumpleaños")



## Tiempo: O(n)

## Espacio: O(n)

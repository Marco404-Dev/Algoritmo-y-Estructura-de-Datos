## Usando Listas o Arrays

def coincidencia_cumpleanos(estudiantes):
    """
    Busca un par de estudiantes que compartan la misma fecha de cumpleaños.
    Entrada: lista de tuplas (nombre, cumpleaños)
    Salida: tupla con los nombres de los estudiantes que tienen el mismo cumpleaños, o None si no hay coincidencias
    """
    n = len(estudiantes)
    registro = [None] * n  # lista para guardar los estudiantes ya revisados

    for k in range(n):
        (nombre1, cumple1) = estudiantes[k]
        
        # Verificar si este cumpleaños ya está en el registro
        for i in range(k):
            (nombre2, cumple2) = registro[i]
            if cumple1 == cumple2:
                return (nombre1, nombre2)  # encontramos coincidencia
        
        registro[k] = (nombre1, cumple1)  # guardar estudiante en el registro

    return None  # si no hay coincidencias


# --- Lista de ejemplo ---
estudiantes = [
    ("Ana", "01-01"),
    ("Luis", "12-05"),
    ("Ruth", "01-01"),
    ("Carlos", "23-08")
]

# --- Probar la función ---
resultado = coincidencia_cumpleanos(estudiantes)

if resultado:
    print(f"Coincidencia encontrada: {resultado[0]} y {resultado[1]}")
else:
    print("No hay coincidencias de cumpleaños")

##

## Tiempo: O(n²)

## Espacio: O(n)


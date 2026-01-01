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

## Tiempo: O(n)

## Espacio: O(n)

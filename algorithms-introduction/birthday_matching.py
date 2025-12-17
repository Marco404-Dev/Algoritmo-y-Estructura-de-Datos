def birthday_match(students):
    """
    students: lista de tuplas (name, bday)
    bday puede ser un número 1..365 o (mes, dia), etc.
    retorna (nameA, nameB) o None
    """
    n = len(students)
    record = [None] * n  # imita StaticArray(n)

    for k in range(n):
        name1, bday1 = students[k]

        # buscar si bday1 ya aparece en record[0..k-1]
        for i in range(k):
            name2, bday2 = record[i]
            if bday1 == bday2:
                return (name1, name2)

        # guardar el estudiante actual
        record[k] = (name1, bday1)

    return None

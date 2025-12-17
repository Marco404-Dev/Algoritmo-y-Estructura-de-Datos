def birthday_match(students):
    n = len(students)
    record = [None] * n

    for k in range(n):
        name1, bday1 = students[k]

        for i in range(k):
            name2, bday2 = record[i]
            if bday1 == bday2:
                return (name1, name2)

        record[k] = (name1, bday1)

    return None


# estudiantes
students = [
    ("Ana", (3, 10)),
    ("Luis", (7, 22)),
    ("Maria", (3, 10)),
]
# print
print(birthday_match(students))   


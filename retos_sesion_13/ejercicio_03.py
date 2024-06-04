# Dar las felicitaciones a los estudiantes que aprobaron el curso de la siguiente tupla de estudiantes
# estudiantes = [('Juan', 51), ('Pedro', 80), ('Maria', 90), ('Ana', 40), ('Luis', 30)]
estudiantes = [('Juan', 51), ('Pedro', 80), ('Maria', 90), ('Ana', 40), ('Luis', 30)]
diccionario_student = dict(estudiantes)
for name in diccionario_student:
    if (diccionario_student[name] >= 51):
        print (f"Felicitaciones {name} aprobaste, y tu nota fue de {diccionario_student[name]}")
    else:
        print (f"No aprobaste {name}, tu nota fue {diccionario_student[name]}")
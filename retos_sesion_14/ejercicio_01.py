# Un estudiante desea saber cuál es su promedio de calificaciones en la materia de matemáticas, 
# cree una función que reciba las calificaciones como lista y devuelva el promedio las calificaciones son 20,40,60,51,13

def promedio_matematicas(calificaciones):
    promedio = 0
    for nota in calificaciones:
        promedio += nota
    return promedio / len(calificaciones)
    
lista = [20,40,60,51,13]
result = promedio_matematicas(lista)
print (result)
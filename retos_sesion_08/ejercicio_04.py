# Las notas de un estudiante durante un semestre son:
# 34, 61, 80, 20, 12, 69, 32, 60, 61, 51, 90, 23, 15
# Genera una tupla con los resultados y calcula el promedio para saber si aprobó o no el 
# semestre utiliza la función sum() y len()
score = (34, 61, 80, 20, 12, 69, 32, 60, 61, 51, 90, 23, 15)
averege = sum(score)/len(score)
print ("El estudiante tuvo un promedio de: ",round(averege,2),"en el semestre")
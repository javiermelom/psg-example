# Anita y Pepito llevan saliendo juntos por 4 semanas, cada vez que salen van a comer a una plaza de comidas. 
# Ambos quieren saber que tan compatibles son viendo cuantos platos de comida tienen en común. 
# A continuación tienes los platos de comida que ambos han ido pidiendo a los largo de sus citas:

# Anita: Sushi, Pizza, Tacos, Hamburguesa, Pasta, Alitas
# Pepito: Pizza, Tacos, Ensalada, Pasta, Helado, Milanesa
# Si la cantidad platos de comida que tienen en comun es mayor a 50% entonces ambos seguirán saliendo
anitas_plates = {'Sushi', 'Pizza', 'Tacos', 'Hamburguesa', 'Pasta', 'Alitas'}
pepitos_plates = {'Pizza', 'Tacos', 'Ensalada', 'Pasta', 'Helado', 'Milanesa'}
len_plates_anitas = len(anitas_plates)
len_plates_pepitos = len(pepitos_plates)
len_average = (len_plates_anitas + len_plates_pepitos) / 2

print (len_plates_anitas)
print (len_plates_pepitos)
print (len_average)
interseccion = anitas_plates.intersection(pepitos_plates)
print (interseccion)
len_interseccion = len(interseccion)
print (len_interseccion)
result = (len_interseccion > len_average)
print ("Anita y Pepito seguiran saliendo:", result)
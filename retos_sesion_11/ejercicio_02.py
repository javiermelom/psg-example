# Crea un diccionario para almacenar información de comidas de animales por ejemplo
# comidas = {"carne" : {"animales": ["león", "tigre"]}, "frutas" : {"animales": ["mono", "elefante"]}}
# Añade al diccionario de comidas 4 alimentos más usando update(clave=valor)
# Existe en el diccionario de comidas la comida 'meat'?
# Elimina la comida 'frutas' del diccionario de comidas

food = {'meat': {'animals': ['lion', 'tiger']}, 'fruit': {'animals': ['monkey', 'elephant']}}
print (food)
food.update(vegetables= {'animals': ['turtle', 'rabbit']}, cereal = {'animals': ['chiken', 'ken']})
food.update(herbs= {'animals': ['cow', 'giraffe']}, other_animals = {'animals': ['python', 'crocodile']})
print (food)
exist = 'meat' in food
print ("La comida meat existe en el diccionario?:\n", exist)
fruit = food.pop('fruit')
print (fruit, type(fruit))
print (food)
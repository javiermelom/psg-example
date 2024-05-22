# Registro de un zoológico, utiliza un diccionario para almacenar información de un animal del zoológico,
# registra información como especie, habitat, dieta, estado de salud, edad, en una lista los responsables de su cuidado

animal = dict()
animal = {'animal': ('perro', '🐕'), 'especie': 'carnivoro', 'habitad': 'cualquiera', 'dieta': ['proteina', 'vegetales'], 'salud': 'excelente', 'edad': '3'}
responsable = [['person1', 'park_boss'],['person2', 'supervisor'],['person3', 'manager']]
animal.update(responsable)
print ("Informacion de animal resgistrado",animal.get('animal'), animal)
print ("Los responsables de su cuidado son:", responsable)

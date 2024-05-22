# Crea un diccionario con las siguientes tuplas de animales
# tupla = (('perro', '🐶') , ('gato','🐱') , ('aves',['🐦','🦅']))
# Del diccionario obtén y elimina el valor de la clave 'aves'
# Modifica el valor de la clave 'gato' por '🐈'
# Cambia la clave perro por perros y su valor por ['🐶','🐕']
tupla = (('perro', '🐶') , ('gato','🐱') , ('aves',['🐦','🦅']))
# convert to dict
animals = dict(tupla)
print (animals, type(animals))
# obtain value
aves = animals.get('aves')
print (aves, type(aves))
# delete value
aves = animals.pop('aves')
print (aves, type(aves))
print (animals, type(animals))
# update value
animals.update(gato = '🐈')
print (animals)
# change key
animals['perros']=animals['perro']
del animals['perro']
print (animals)
# change value
animals.update(perros = ['🐶','🐕'])
print (animals)
# Eres NOE y tienes que guardar dos animales de cada especie en un arca, crea un diccionario con las especies
# arca = {"perro" : 2, "gato" : 2, "tigre" : 2, "mono" : 2, "unicornio" : 0, "jirafa" : 1}
# Añade al arca 2 especies más usando update()
# Toma lista de los animales en el arca iterando el diccionario
# Existe en el arca la especie 'dragon'?
# Elimina la especie 'unicornio' del arca
# Modifica el valor de la especie 'jirafa' por 2
# Vacía el arca después del diluvio

arca = {"perro" : 2, "gato" : 2, "tigre" : 2, "mono" : 2, "unicornio" : 0, "jirafa" : 1}
arca.update({"vaca": 2, "caballo": 2})
print (arca)


iterador = iter(arca.items())
siguiente = next(iterador)
print(siguiente, type(siguiente))
siguiente = next(iterador)
print(siguiente, type(siguiente))
siguiente = next(iterador)
print(siguiente, type(siguiente))
siguiente = next(iterador)
print(siguiente, type(siguiente))
siguiente = next(iterador)
print(siguiente, type(siguiente))
siguiente = next(iterador)
print(siguiente, type(siguiente))
siguiente = next(iterador)
print(siguiente, type(siguiente))
siguiente = next(iterador)
print(siguiente, type(siguiente))

diccionario = {animal for animal in arca}
print (diccionario)

exist = 'dragon' in arca
print ("Existe en el arca la especie 'dragon':", exist)


del arca['unicornio']
# unicornio = arca.pop('unicornio')
# print ("Clave eliminada:", unicornio)
print (arca)

arca.update(jirafa = 2)
print (arca)

arca.clear()
print ("Arca vacia",arca)
# Crear una lista de personas con 10 nombres de personas
# Obtener una sub lista de 2 a 7
# Buscar si existe el nombre "Jhon" en la lista original
# Ordenar la sub lista alfabéticamente
# Ordenar la lista original alfabéticamente de forma descendente
people = ["Emilio","Luis","Alejandro","Felipe","Elena","Javier","Martin","Celeste","Jhon","Lia"]
sublist = people[2:7]
print (people)
print (sublist)
print ("El nombre Jhon existe en la lista en la posicion:",people.index("Jhon"))
sublist.sort()
print (sublist)
people.sort(reverse=True)
print (people)
# Un usuario ingresa su nombre y gustos musicales por teclado separados por coma, 
# verifica si el usuario ingresó un nombre válido usando truthiness, convertir los gustos musicales 
# en una lista y verifica si tiene el gusto rock en su lista de gustos musicales
# Nombre: Jhon Doe
# Gustos musicales: rock,pop,jazz
name = input("Digite nombre: ")
if name:
    like_music = input("Digite gustos musicales separados por coma',': ")
    separate_data = like_music.split(",")
    # print (separate_data, type(separate_data))
    result = "Rock si esta en la lista" if "rock" in separate_data else "Rock no esta dentro de la lista"
    print (result)
else:
    print ("Nombre Invalido")
# ESTRUCTURA DE DATOS TUPLAS 
# Es una secuencia de objetos INMUTABLES, ORDENADOS E INDEXADOS
# No se puede modificar, agregar o eliminar elementos después de su creación
tupla = (1,2,3)
print (tupla)
# tupla[0] = 4 error ya que no se puede reemplazar o modificar ningun valor

# Ordenada: Los elementos tienen un orden definido y no cambian
tupla1 = (1,2,3)
tupla2 = (3,2,1)
print (tupla1 == tupla2)

# Indexada: Cada elemento tiene un índice asociado a su posición en la tupla para acceder a él
tupla = (1,2,3)
print (tupla[0]) # 1
print (tupla[1]) # 2
print (tupla[2]) # 3

# Las tuplas sirven para: 
# 1 Empaquetado y desempaquetado de valores
coordenadas = (3,5)
x,y = coordenadas

# 2 Enviar y devolver múltiples valores de una función
def coordenadas(coordenada):
    x,y = coordenada
    x = x + 1
    y = y + 1
    return (x,y)

# 3 En diccionarios se puede utilizar una tupla como llave compuesta
agenda = {('Juan','Perez'): 1234567}

# Una tupla puede almacenar cualquier tipo de dato a la vez
tupla = (1,2.0,'hola',True)

print ("Tupla de enteros")
enteros = (1,2,3,4,5,6)
print (enteros)
print (type(enteros))

print ("Tupla de cadenas")
cadenas = ("hola", "mundo", "desde", "python")
print (cadenas)
print (type(cadenas))

print ("Tupla Mixta") 
mixta = (1, "hola", True, 2.5)
print (mixta)
print (type(mixta))

print ("Tupla vacia")
vacia = ()
print (vacia)
print (type(vacia))

print ("Tupla de un solo elemento")
uno = (1,)
print (uno)
print (type(uno))

# Se usa la función tuple() para crear una tupla, su utilidad es convertir una secuencia en una tupla 
# Utilizado con cadenas, listas, otras tuplas, etc.
print ("Tupla utilizando la función tuple()")
constructor = tuple("hola")
print (constructor)
print (type(constructor))

print ("Indexado positivo de una tupla")
tupla = (1,2.0, "hola", True)
print (tupla[0], type(tupla[0]))
print (tupla[1], type(tupla[1]))
print (tupla[2], type(tupla[2]))
print (tupla[3], type(tupla[3]))

print ("Indexado negativo de una tupla")
tupla = (1,2.0, "hola", True)
print (tupla[-1], type(tupla[-1]))
print (tupla[-2], type(tupla[-2]))
print (tupla[-3], type(tupla[-3]))
print (tupla[-4], type(tupla[-4]))

# El slicing se utiliza para obtener subconjuntos de la tupla
# Permite extraer una porción de la tupla utilizando dos índices de inicio y fin
# El resultado es una nueva tupla
print ("Slicing de una tupla")
tupla = (0,1,2,3,4,5,6,7,8,9,10)
print (tupla)
sub_tupla = tupla[0:5]
print (sub_tupla)
print (type(sub_tupla))
 
print ("Slicing de una tupla con saltos")
tupla = (0,1,2,3,4,5,6,7,8,9,10)
print (tupla)
sub_tupla = tupla[0:10:2]
print (sub_tupla)
print (type(sub_tupla)) 

print ("Slicing de una tupla con saltos negativos")
tupla = (0,1,2,3,4,5,6,7,8,9,10)
print (tupla)
sub_tupla = tupla[7:2:-2]
print (sub_tupla)
print (type(sub_tupla))

# Concatenación de tuplas
# Las tuplas se pueden concatenar utilizando el operador + El resultado es una nueva tupla
# (a,b) + (c,d) = (a,b,c,d)
print ("Concatenación de tuplas")
tupla1 = (1,2,3)
tupla2 = (4,5,6)
concatenar = tupla1 + tupla2
print (tupla1, tupla2)
print (concatenar)
print (type(concatenar))

# Repetición de tuplas
# Las tuplas se pueden repetir utilizando el operador * y un número entero n
# El resultado es una nueva tupla (a,b) * n = (a,b,a,b,...,a,b) n veces
print ("Repetición de tuplas")
tupla = (1,2,3)
repetir = tupla * 3
print (tupla)
print (repetir)
print (type(repetir))

# Asignación múltiple de valores
# Es una forma de asignar el valor a variables en una sola línea desempaquetando los valores de una tupla
# No utiliza los indices de la tupla ni los paréntesis La cantidad de variables debe ser igual a la
# cantidad de elementos de la tupla
print ("Asignación múltiple")
persona = ("Jhon", "Doe", 22, 1.75)
nombre, apellido, edad, estatura = persona
print (persona)
print (nombre)
print (apellido)
print (edad)
print (estatura)

# Solo tienen dos métodos
# count()
# index()
# index() recibe un valor y devuelve el índice de la primera aparición de ese valor
# Si el valor no existe en la tupla, se genera un error
print ("Método index(valor)")
tupla = (1,2.0, "hola", True)
print (tupla.index(2.0))
print (tupla.index("hola"))

# count() recibe un valor y devuelve el número de veces que aparece en la tupla
print ("Método count(valor)")
tupla = (1, 2.0, "hola", False, "hola", "HOLA")
print (tupla.count(1))
print (tupla.count("hola"))
print (tupla.count(10))

# Las tuplas interactúan con funciones propias de Python estas son las más importantes
# len()
# max()
# min()
# sum()
print ("Función len()")
tupla = (1,2.0, "hola", True)
longitud = len(tupla)
print (tupla)
print (longitud)

# max() devuelve el valor máximo de la tupla, se debe asegurar que los elementos sean comparables entre sí
# Si la tupla es de cadenas, se comparan alfabéticamente
# Si la tupla es de enteros, se comparan numéricamente
# NO mezclar tipos de datos
print ("Función max()")
tupla = (1,2,10,5,8,0)
maximo = max(tupla)
print (tupla)
print (maximo)

print ("Función min()")
tupla = ("a","z","c","b","f","d")
minimo = min(tupla)
print (tupla)
print (minimo)

print ("Función sum()")
tupla = (1.0, 0.5, 2.5, 3.1)
suma = sum(tupla)
print (tupla)
print (suma)

# Tuplas anidadas
# Una tupla puede contener otras tuplas como elementos
print ("Tuplas anidadas")
tupla = (1,2,3, (4,5,6))
print (tupla)
print (tupla, type(tupla))
print (tupla[3], type(tupla[3]))
print (tupla[3][0], type(tupla[3][0]))

# Anidado al detalle
print ("Tuplas anidadas")
tupla = (1,2,3, (4,5,6))
print (tupla, type(tupla))
anidado = tupla[3]
print (anidado, type(anidado))
valor_anidado_0 = anidado[0]
print (valor_anidado_0, type(valor_anidado_0))
valor_anidado_1 = tupla[3][1]
print (valor_anidado_1, type(valor_anidado_1))
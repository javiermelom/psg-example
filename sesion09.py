# ESTRUCTURA DE DATOS
# LISTAS
# Una lista es una estructura de datos, así como una tupla y una cadena es una secuencia de valores
# Al igual que la tupla almacena objetos o items que pueden ser de cualquier tipo
# Una lista es una secuencia de objetos MUTABLES Ordenados e indexados
# Los elementos de una lista pueden ser modificados despues de su creacion
lista = [1,2,3]
lista[0] = 4 
print (lista) # [4,2,3]

# Ordenada: Los elementos tienen un orden definido y no cambian a no ser que sean reordenados explícitamente modificando la lista
lista1 = [1,2,3]
lista2 = [3,2,1]
print (lista1 == lista2) # False

# Indexada: Cada elemento tiene un índice asociado a su posición en la lista para acceder a él
lista = [1,2,3]
lista[0] # 1
lista[1] # 2
lista[2] # 3

print ("Lista de enteros")
mi_lista = [1,2,3,4,5]
print (mi_lista)

print ("Lista de cadenas")
mi_lista = ["hola", "mundo", "python"]
print (mi_lista)

print ("Lista mixta")
mi_lista = [1, "hola", 3.14, "mundo", 5]
print (mi_lista)

print ("Lista vacía")
mi_lista = []
print (mi_lista)

# Se usa la función list() para crear una lista a partir de una secuencia
# Su utilidad es convertir una tupla, cadena o conjunto en una lista
print ("Lista a partir de una cadena")
mi_lista = list("hola mundo")
print (mi_lista)

print ("Lista a partir de una tupla")
mi_tupla = (1,2,3,4,5)
print (mi_tupla)
mi_lista = list(mi_tupla)
print (mi_lista)

# Una lista por comprensión es una forma de crear listas a partir de una expresión o secuencia
# Es una forma más compacta y eficiente de crear listas
print ("Lista por comprensión")
mi_lista = [x for x in range(10)]
print (mi_lista)

# Indexación y slicing
# Se puede acceder a los diferentes valores de la lista utilizando indexación
# Obtener solo una parte de la lista utilizando slicing Similar a las cadenas de texto y tuplas
print ("Indexación positivo de una lista")
lista = [1, "hola", 3.14, (1,2)]
print (lista[0], type(lista[0])) 
print (lista[1], type(lista[1])) 
print (lista[2], type(lista[2])) 
print (lista[3], type(lista[3])) 

print ("Indexación negativo de una lista")
lista = [1, "hola", 3.14, (1,2)]
print (lista[-1], type(lista[-1]))
print (lista[-2], type(lista[-2]))
print (lista[-3], type(lista[-3]))
print (lista[-4], type(lista[-4]))

print ("Modificación de una lista")
lista = [1, "hola", 3.14, (1,2)]
print (lista)
lista[0] = 2
lista[1] = "mundo"
print (lista)

# El slicing se utiliza para obtener una porción de la lista
# Permite extraer una porción de la lista utilizando dos índices de inicio y fin El resultado es una nueva lista
print ("Slicing de una lista")
lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
print (lista)
sub_lista = lista[2:7]
print (sub_lista)
print (type(sub_lista))

print ("Slicing con paso positivo")
lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
print (lista)
sub_lista = lista[0:9:3]
print (sub_lista)

print ("Slicing con paso negativo")
lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
print (lista)
sub_lista = lista[8:2:-4]
print (sub_lista)

print ("Slicing negativo con paso negativo")
lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
print (lista)
sub_lista = lista[-1:-8:-2]
print (sub_lista)

print ("Slicing negativo con paso positivo")
lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
print (lista)
sub_lista = lista[-8:-1:2]
print (sub_lista)

# Concatenación de listas
# Las listas se pueden concatenar utilizando el operador + El resultado es una nueva lista con los elementos de las listas originales
# [a,b,c]+[d,e,f]=[a,b,c,d,e,f]
print ("Concatenación de listas")
lista1 = [1,2,3]
lista2 = ["a","b","c"]
concatenar = lista1 + lista2
print (lista1, lista2)
print (concatenar)
print (type(concatenar))

# Repetición de listas
# Las listas se pueden repetir utilizando el operador * y un número entero n
# El resultado es una nueva lista con los elementos de la lista original repetidos n veces
# [a,b,c]∗n=[a,b,c,...a,b,c,]nveces
print ("Repetición de listas")
lista = [True, False]
repetir = lista * 3
print (lista)
print (repetir)
print (type(repetir))

# Métodos de las listas
# Las listas al ser mutables tiene una mayor cantidad de métodos que las tuplas
# Métodos de búsqueda
# Métodos de adición
# Métodos de eliminación
# Métodos de ordenamiento
# Métodos de copia

# Métodos de búsqueda
# Los métodos de búsqueda nos permiten buscar información en la lista
#   index()  recibe un valor y devuelve el índice de la primera aparición en la lista, si no existe lanza un error
#   count()  recibe un valor y devuelve el número de veces que aparece en la lista

print ("Método index(valor)")
lista = [1,True,3.14,"hola",5]
valor = "hola"
print (valor, lista.index(valor))
valor = 3.14
print (valor, lista.index(valor))

print ("Método count(valor)")
lista = [1,True,3.14,"hola",5, True, True, 3.140]
valor = True
print (valor, lista.count(valor))
valor = 3.14
print (valor, lista.count(valor))

# Métodos de adición
# Los métodos de adición nos permiten agregar elementos a la lista
#    insert() recibe un índice y un valor, inserta el valor en la posición del índice
#    append() recibe un valor y lo agrega al final de la lista
#    extend() recibe una secuencia y agrega sus elementos al final de la lista como otra lista, tupla, cadena
# No retornan un valor, modifican la lista original
print ("Método insert(i, valor)")
lista = [1,2,3,4,5]
print (lista)
lista.insert(2, "OwO")
print (lista)

print ("Método append(valor)")
lista = [1,2,3,4,5]
print (lista)
lista.append("(OwO=)")
print (lista)

print ("Método extend(iterable)")
lista = [1,2,3]
print (lista)
lista.extend(":3")
print (lista)
lista.extend(["(¬_¬ )", "(O_O=)"])
print (lista)
lista.extend(("😅", "😎"))
print (lista)

# Métodos de eliminación
# Los métodos de eliminación nos permiten eliminar elementos de la lista
# remove() recibe un valor y elimina la primera aparición de ese valor en la lista si no existe lanza un error
# clear() elimina todos los elementos de la lista dejándola vacía
# No retornan un valor, modifican la lista original
# pop() recibe un index o índice y elimina el elemento en esa posición Si no se especifica el índice elimina el último elemento
# Retorna el valor eliminado y modifica la lista original

print ("Método remove(valor)")
lista = [1,2,"UwU",4,5, "UwU"]
print (lista)
lista.remove("UwU")
print (lista)

print ("Método pop(i)")
lista = ["OwO",3,"UwU",5]
print (lista)
variable1 = lista.pop(1)
print (lista)
print (variable1)
print ("Método pop()")
variable2 = lista.pop()
print (lista)
print (variable2)

print ("Método clear()")
lista = ["ewe","OwO","UwU"]
print (lista)
lista.clear()
print (lista)

# Métodos de ordenamiento
# Los métodos de reordenar nos permiten ordenar los elementos de la lista
# sort() ordena los elementos de la lista de menor a mayor
# sort(reverse=True) ordena los elementos de la lista de mayor a menor
# reverse() invierte el orden de los elementos de la lista
# No retornan un valor, modifican la lista original

print ("Método sort()")
lista = [3,1,5,2,4]
print (lista)
lista.sort()
print (lista)

print ("Método sort()")
lista = [3,1,5,2,4]
print (lista)
lista.sort(reverse=True)
print (lista)

print ("Método reverse()")
lista = [3,1,5,2,4]
print (lista)
lista.reverse()
print (lista)

# Métodos de copia
# Los métodos de copia nos permiten copiar los elementos de la lista
# copy() devuelve una copia de la lista es equivalente al slicing [:]
# Cuando se asigna una lista a otra variable se crea una referencia a la lista original
# NO se crea una copia de la lista, si se modifica esta se modifica la original

print ("Asignación de lista")
lista = [1,2,3,4,5]
print (lista)
copia = lista
copia[0] = 6
print (copia)
print (lista)

# Para crear una copia de la lista se debe utilizar el método copy() o el slicing [:]
print ("Método copia con slicing")
lista = [1,2,3,4,5]
print (lista)
copia = lista[:]
copia[0] = 6
print (copia)
print (lista)

print ("Método copy()")
lista = [3,1,5,2,4]
print (lista)
copia = lista.copy()
print (copia)
print (copia == lista)

print ("Método copia con slicing")
lista = [1,2,3,4,5]
print (lista)
copia = lista.copy()
copia[0] = 6
print (copia)
print (lista)

# Funciones con listas
# Las listas interactúan con funciones propias de python que acepten secuencias de datos
# len() devuelve la longitud de la lista o el número de elementos que contiene
# max() devuelve el valor máximo de la lista o el elemento más grande
# min() devuelve el valor mínimo de la lista o el elemento más pequeño
# sum() devuelve la suma de los elementos de la lista
# Existen otras funciones pueden encontrarse en la documentación y funciones incorporadas

print ("Función len()")
lista = [1,True,3.14,"🐍",5]
print (lista)
print (len(lista))

# max() devuelve el valor máximo de la lista o el elemento más grande
# Si la lista contiene cadenas devuelve el valor máximo en orden alfabético
# Si la lista contiene enteros y flotantes devuelve el valor máximo numérico

print ("Función max()")
lista = [1,2,3,4,5]
print (lista)
print (max(lista))
lista = ["a","b","c","d","e"]
print (lista)
print (max(lista))

# min() devuelve el valor mínimo de la lista o el elemento más pequeño
# Si la lista contiene cadenas devuelve el valor mínimo en orden alfabético
# Si la lista contiene enteros y flotantes devuelve el valor mínimo numérico

print ("Función min()")
lista = [1,2,3,4,5]
print (lista)
print (min(lista))
lista = ["a","b","c","d","e"]
print (lista)
print (min(lista))

# sum() devuelve la suma de los elementos de la lista
# Se debe asegurar que los elementos de la lista sean numéricos

print ("Función sum()")
lista = [1,2,3,4,5]
print (lista)
print (sum(lista))

# Comparación de listas
# Podemos consultar si una lista contiene un elemento específico utilizando el operador in, not in
# Si una variable hace referencia a otra variable podemos utilizar el is , is not, para comparar si son la misma lista

print ("Comparación de listas")
lista = [1,2,3,4,5]
print (lista)
print (3 in lista)
print (6 in lista)
print (3 not in lista)
print (6 not in lista)
print ([1,2,3] in lista)

print ("Comparación de listas")
lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,5]
lista3 = [1,2]
print (lista1, lista2, lista3)
print (lista1 is lista2)
print (lista1 is not lista2)
print (lista3 is lista1)

# Operadores de comparación
# Podemos comparar listas utilizando los operadores de comparación, estos comparan los elementos de las listas uno a uno
# == - Igualdad
# != - Desigualdad
# > - Mayor que
# < - Menor que
# >= - Mayor o igual que
# <= - Menor o igual que

# < y <=
# Comienza comparando el primer elemento de cada lista. Si son iguales pasa al siguiente elemento de cada lista
# Si el primer elemento de la primera lista es menor que el de la segunda lista, el resultado es True
# Si el primer elemento de la primera lista es mayor que el de la segunda lista el resultado es False

print ("Menor y Menor Igual que")
print ([1,2,3] <= [1,2,4])
print ([1,2,3] <= [1,2,2,2])
print ([1,2,3] <= [2])
print ([1,2,3] < [1,2,3])
print ([1,2,3] <= [1,2,3])

# > y >=
# Comienza comparando el primer elemento de cada lista. Si son iguales pasa al siguiente elemento de cada lista
# Si el primer elemento de la primera lista es mayor que el de la segunda lista, el resultado es True
# Si el primer elemento de la primera lista es menor que el de la segunda lista el resultado es False

print ("Mayor y Mayor Igual que")
print ([1,2,3] >= [1,2,4])
print ([1,2,3] >= [1,2,2,2])
print ([1,2,3] >= [2])
print ([1,2,3] > [1,2,3])
print ([1,2,3] >= [1,2,3])

# == y !=
# Compara si los elementos de las listas son iguales. Si todos los elementos son iguales el resultado es True
# Si al menos un elemento es diferente el resultado es False

print ("Igual y Desigual que")
print ([1,2,3] == [1,2,3])
print ([1,2,3] == [1,2,4])
print ([1,2,3] != [1,2,3])
print ([1,2,3] != [1,2,4])

# Listas anidadas
# Las listas anidadas son listas que contienen otras listas como elementos
# Se pueden crear listas anidadas de cualquier profundidad

print ("Listas anidadas")
lista = [1,2,3,[4,5,6]]
print (lista)
print (type(lista))
valor_lista = lista[3]
print (valor_lista)
print (type(valor_lista))
valor = valor_lista[1]
print (valor)
print (type(valor))


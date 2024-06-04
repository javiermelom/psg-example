# Estrucuturas de contro de flujo
# sentencias iteractivas
# Repetición o ciclos
# Los ciclos son estructuras de control que permiten ejecutar un bloque de código varias veces de manera consecutiva
# En Python existen dos tipos de ciclos
# Ciclo for
# Ciclo while

# For
# El ciclo for es un ciclo que se ejecuta un número determinado de veces
# En el caso de los for se recorre una secuencia de elementos
# Se puede recorrer un rango de números o listas, tuplas, diccionarios, etc.

# Para utilizar rango de números primero veremos la función range()
range(5)
range(0, 5)

# Recibe tres argumentos
# Inicio (por defecto 0 e Inclusivo)
# Fin (Obligatorio y Exclusivo)
# Paso (por defecto 1)

range(1, 10, 2)
print (range)

# Puede haber rangos negativos
range(10, 0, -1)
print (range)

# Podemos convertir el rango en una lista
print(list(range(5)))
print (list)
# No es necesario convertirlo a lista para usarlo en un ciclo for

# Como se declara un for con range
# for tiene la siguiente estructura
# for variable in range(inicio, fin, paso):
    # print(variable)
    
# for es la palabra reservada
# variable es la variable que se usará para iterar
# in es palabra reservada de pertenencia
# range(inicio, fin, paso) es la secuencia de números
# : es el delimitador de inicio del ciclo
# print(variable) es el código a ejecutar posee un nivel de indentación
# Cuando iteramos el nombre de la variable puede ser cualquier nombre
# Es común usar i que es la abreviatura de índice o iterador
# Cuando se itera más de una lista se puede usar i, j, k
# Las variables definidas en el ciclo for existen dentro del ciclo
# NO se recomienda usarlas fuera del ciclo
# Es una mala práctica usar la variable del ciclo fuera del ciclo

for i in range(5):
    print(i)
print(i)

# En python la estructura de control for es la siguiente
print ("Inicio")
for i in range(5): # rango (0,5,1)
    print(i)
print ("Fin")

# Ejemplo 1, sumar los números del 1 al 10 de 2 en 2
print ("Ejemplo 1")
suma = 0
for i in range(1, 11, 2): # 1, 3, 5, 7, 9
    suma = suma + i #suma += i
print(suma)


# Ejemplo 2, crear un árbol de navidad de 6 niveles
print ("Ejemplo 2")
for i in range(0, 6):
    print(" "*(5-i) + "*"*i*2+"*")
    
# Ejemplo 3, crear una serie de números cuadrados del 1 al 10
print ("Ejemplo 3")
for i in range(1, 11):
    print(i**2, end=" ")
    
# Ejemplo 4, crear una lista de números pares del 1 al 10
print ("Ejemplo 4")
pares = []
for i in range(0, 11, 2):
    pares.append(i)
print(pares)

# Ejercicio 1, imprimir los 10 primeros de la serie números cúbicos:
for i in range (0, 11):
    print (i ** 3, end = '')


# Como se declara un for con secuencias
# La estructura de control for también puede iterar sobre secuencias
#   Listas
#   Tuplas  
#   Diccionarios
#   Cadenas de texto

# for tiene la siguiente estructura
# for variable in secuencia:
    # print(variable)

# for es la palabra reservada
# variable es el nombre de la variable que se usará para iterar
# in es la palabra reservada de pertenencia
# secuencia es la secuencia de elementos
# : es el delimitador de inicio del ciclo
# print(variable) es el código a ejecutar posee un nivel de indentación

# Cuando se itera sobre una secuencia es común nombrar las variables con 
# nombres que representen el elemento
for fruta in ['🍎','🍌','🍇','🍉']:
    print(fruta)
    
# Ejemplo 5, imprimir los elementos de una lista fiestas
print ("Ejemplo 5")
fiesta = ['🎄','🎆','🎁','🎊','✨','🧨']
for objeto in fiesta:
    print(objeto)
    
# Ejemplo 6, imprimir los elementos de una tupla de frutas separados por coma
print ("Ejemplo 6")
frutas =  ('🍅','🍇','🍈','🍉','🍊')
for fruta in frutas:
    print(fruta, end=", ")


# Ejemplo 7, imprimir los elementos de un diccionario
print ("Ejemplo 7")
frutas = {'🍅':'Tomate','🍇':'Uva','🍈':'Melón','🍉':'Sandía','🍊':'Naranja'}
for clave in frutas:
    print(clave, frutas[clave])


# Ejemplo 8, imprimir los elementos del ciclo de vida de un pollo con flechas
print ("Ejemplo 8")
ciclo_vida = '🥚🐣🐥🐤🐔🍗'
for etapa in ciclo_vida:
    print(etapa, end="->")
    
# Se puede recorrer elementos con indexación como listas y tuplas de 3 formas
#       Mediante in como pertenencia
#       Mediante len() y range()
#       Mediante enumerate()

# Mediante in
# Ejemplo 9, Listar los elementos de la siguiente serie ['🐶','🐱','🐰','🐭']
print ("Ejemplo 9")
animales = ['🐶','🐱','🐰','🐭']
for animal in animales:
    print(animal)
    
# Mediante len() y range()
# Ejemplo 10, Listar los elementos de la siguiente serie ['🐶','🐱','🐰','🐭']
print ("Ejemplo 10")
animales = ['🐶','🐱','🐰','🐭']
for i in range(len(animales)):
    print(animales[i])
    

# Mediante enumerate()
# Primero veremos la función enumerate()
# Es una función que devuelve un objeto enumerado que contiene pares de índices y valores como tuplas
enumerate(['🐶','🐱','🐰','🐭'])
print (enumerate)
# Nos permite recorrer una secuencia y obtener el índice y el valor en cada iteración

# Ejemplo 11, Listar los elementos de la siguiente serie ['🐶','🐱','🐰','🐭']
print ("Ejemplo 11")
animales = ['🐶','🐱','🐰','🐭']
for i, animal in enumerate(animales):
    print(i, animal, animales[i])


# Ejercicio 2, imprimir la cantidad de veces los elementos de la cadena '⚽🏀🏐🎱' 
# de acuerdo a su posición más 1
print ("Ejercicio 2")
esferas = '⚽🏀🏐🎱'
for i, esfera in enumerate(esferas):
    print(esfera*(i+1))
    
# While
# El ciclo while es un ciclo que se ejecuta mientras una condición sea verdadera
# Es como un ciclo for pero no se sabe cuantas veces se ejecutará
# Similar a un if pero se ejecuta varias veces

# La estructura de control while es la siguiente
# while condicion:
    # print("Código a ejecutar")
    
# while es la palabra reservada
# condicion es la expresión que se evaluará tiene que ser True o False
# : es el delimitador de inicio del ciclo
# print("Código a ejecutar") es el código a ejecutar posee un nivel de indentación
# condicion se evalúa en cada iteración

# Ejemplo 12, imprimir los números mientras sean menores o igual a 5 empezando desde 0
print ("Ejemplo 12")
i = 0
while i <= 5:
    print(i)
    i += 1
    
# Ejemplo 13, sumar los números mientras no se ingrese por teclado el número 0
print ("Ejemplo 13")
suma = 0
numero = int(input("Ingrese un número: "))
while numero != 0:
    suma += numero
    numero = int(input("Ingrese un número: "))
print(suma)

# Ejercicio 3, Ingresa un número por teclado y genera un contador hasta 0, 
# si el número es negativo no hace nada
num = int(input("Digite un numero por teclado: "))
while num >= 0:
    print (f"contador =  {num}")
    num -=1

# Break
# La sentencia break es una palabra reservada que se usa para salir de un ciclo
# Termina el ciclo actual y ejecuta la siguiente instrucción después del ciclo
# Es útil para salir de un ciclo cuando se cumple una condición antes de que termine el ciclo
# Ejemplo 14, De la siguiente lista de frutas imprimir los elementos hasta que se 
# encuentre un gusano 🐛 con for
frutas = ['🍎','🍌','🍇','🍉','🍊','🐛','🍋','🍍']
print ("Ejemplo 14")
for fruta in frutas:
    if fruta == '🐛':
        break
    print(fruta)
print ("Fin")

# Con while
frutas = ['🍎','🍌','🍇','🍉','🍊','🐛','🍋','🍍']
print ("Ejemplo 14")
i = ""
while i != '🐛':
    i = frutas.pop(0)
    print(i)
print ("Fin")

# Ciclos infinitos
# Un ciclo infinito es un ciclo que no tiene una condición de salida
# Se ejecuta indefinidamente hasta que se detiene manualmente con Ctrl+C
# o mediante un break

# Se puede usar para ejecutar tareas en segundo plano
# Un mal uso de un ciclo infinito puede hacer que el programa se bloquee

# Ejemplo 15, Crear un ciclo infinito que imprima un contador incremental
print ("Ejemplo 15")
contador = 0
while True:
    print(contador)
    contador += 1
print ("Fin")

# Ejemplo 16, Crear un ciclo infinito que pida una cadena de texto la 
# ponga en mayúsculas y la imprima hasta que se ingrese la palabra salir
print ("Ejemplo 16")
while True:
    texto = input("Ingrese un texto: ")
    if texto == 'salir':
        break
    print(texto.upper())
print ("Fin")


# Ejercicio 4, Crear un ciclo infinito que reciba un número por teclado y 
# verifique si es par o impar hasta que se ingrese el número 0

num = int(input("Digite numero: "))
while num != 0:
    result = num % 2 == 0
    if result:
        print(f"el {num} es par")
        num = int(input("Digite numero: "))
    else:
        print (f"El {num} es impar")
        num = int(input("Digite numero: "))
print ("fin")

print ("Ejercicio 4")
while True:
    numero = int(input("Ingrese un número: "))
    if numero == 0:
        break
    print ("Par" if numero % 2 == 0 else "Impar")


# Estructuras por comprensión
# Las Estructuras por comprensión son una forma de crear estructuras de manera concisa 
# utilizando una sola línea de código
# Utiliza la estructura de un ciclo for y se puede agregar condicionales
# Se puede crear listas, tuplas, diccionarios y conjuntos

# Estructura de una lista por comprensión
# [expresion for variable in secuencia]
# expresion es la expresión que se evaluará
# for es la palabra reservada
# variable es el nombre de la variable que se usará para iterar
# in es la palabra reservada de pertenencia
# secuencia es la secuencia de elementos
# [ y ] son los delimitadores de la lista


# Estructura de una lista por comprensión y condicional
# [expresion for variable in secuencia if condicion]
# expresion es la expresión que se evaluará
# for es la palabra reservada
# variable es el nombre de la variable que se usará para iterar
# in es la palabra reservada de pertenencia
# secuencia es la secuencia de elementos
# if es la palabra reservada de condición
# condicion es la expresión que se evaluará
# [ y ] son los delimitadores de la lista

# Ejemplo 17, Crear una lista de los números pares del 2 al 10
print ("Ejemplo 17")
pares = [i for i in range(2, 11, 2)]
print(pares)

# Ejemplo 18, Crear una lista de los números pares del 2 al 10 con condicional
print ("Ejemplo 18")
pares = [i for i in range(2, 11) if i % 2 == 0]
print(pares)

# Ejemplo 19, Crear un diccionario números 2 al 10 donde si es par vale "Par" y si es 
# impar valga "Impar"
print ("Ejemplo 19")
pares = {i: "Par" if i % 2 == 0 else "Impar" for i in range(2, 11)}
print(pares)

# Ejercicio 5, Crear una tupla de los números impares del 1 al 10 usando una tupla por comprensión
print ("Ejercicio 5")
impares = tuple(i for i in range(1, 11) if i % 2 != 0)
print(impares)

# Ciclos anidados
# Son ciclos dentro de otros ciclos
# Se pueden anidar ciclos for y while

# Ejemplo 20, Imprimir las tablas de multiplicar del 1 y 2
print ("Ejemplo 20")
for i in range(1, 3):
    print(f"Tabla del {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
        
# Ejemplo 21, Introducir un número por teclado y crear una tabla de multiplicar 
# de ese número del 1 al 10, si se ingresa 0 termina el programa
print ("Ejemplo 21")
while True:
    numero = int(input("Ingrese un número: "))
    if numero == 0:
        break
    print(f"Tabla del {numero}")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero*i}")
print ("Fin")

# Una matriz es una lista de listas que se puede recorrer con ciclos anidados
# Las matrices nos sirven para representar datos en dos dimensiones
# Son útiles para representar tablas, imágenes, mapas, etc.
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in matriz:
    for columna in fila:
        print(columna, end=" ")
    print()
    
# Ejemplo 22, Introducir un número por teclado y crear una matriz nxn con la letra X
print ("Ejemplo 22")
n = int(input("Ingrese un número: "))
matriz = [['X' for i in range(n)] for j in range(n)]
for fila in matriz:
    for columna in fila:
        print(columna, end=" ")
    print()
print (matriz)

# Ejercicio 6, Crear una matriz ingresando un número por teclado 
# para el tamaño de la matriz y en cada posición colocar una tupla con (i, j)
print ("Ejercicio 6")
n = int(input("Ingrese un número: "))
matriz = [[(j, i) for i in range(n)] for j in range(n)]
for fila in matriz:
    for columna in fila:
        print(columna, end=" ")
    print()
print (matriz)
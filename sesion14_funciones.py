# Funciones
# Una función es un bloque de código que realiza una tarea específica
# Se le asigna un nombre y se puede llamar en cualquier parte del programa
# Solo se ejecuta cuando se llama por su nombre
# Permite dividir un programa en bloques de código más pequeños
# Facilita la lectura y mantenimiento del código
# Permite reutilizar el código

# ¿Cómo se declara una función?
# Para definir un bloque de código como función se utiliza la palabra reservada def
# def nombre_funcion():
    # print ("Bloque de código")
# def es la palabra reservada
# nombre_funcion es el nombre de la función
# () son los paréntesis que pueden contener parámetros
# : es el delimitador de inicio del bloque de código
# print es el código a ejecutar
# Posee un nivel de indentación

# Una función puede recibir argumentos de entrada
# Una función puede no devolver ningún valor
# Una función puede devolver un valor o varios valores
# Para devolver un valor se utiliza la palabra reservada return seguida del valor a devolver
# def nombre_funcion():
    #return "Bloque de código"

# Se llama a una función utilizando su nombre seguido de paréntesis y los argumentos si los tiene

def nombre_funcion():
    print ("Bloque de código")

nombre_funcion()
print (type(nombre_funcion))

#Bloque de código
#<class 'function'>

# Los nombres de las funciones deben ser en minúsculas y separados por guiones bajos
# Los nombres de las funciones deben ser descriptivos

# Funciones sin argumentos y sin retorno
# No esta definido ningún parámetro
# No recibe argumentos de entrada
# No devuelve ningún valor

def funcion():
	    print ("Bloque de código")
	 
funcion()

# Ejemplo 1, Crear una función para imprimir una lista de 10 números pares y llamarla dos veces
print ("Ejemplo 1")
print ("1. Definir función")
def imprimir_pares():
    pares = [i for i in range(0, 21, 2)]
    print (pares)
	 
print ("2. Llamar función")
imprimir_pares()
imprimir_pares()

# Ejercicio 1, crear una función que imprima un mensaje de bienvenida del siguiente conjunto de forma aleatoria
# mensajes = {"Bienvenido al Python Study Group 🐍",
# "¡Hola y bienvenido al Python Study Group! ✨",
# "Hola, aprendamos Python juntos 🐍"}
def bienvenida():
    mensajes = {"Bienvenido al Python Study Group 🐍",
    "¡Hola y bienvenido al Python Study Group! ✨",
    "Hola, aprendamos Python juntos 🐍"}
    print (mensajes.pop())

bienvenida()

# Funciones sin argumentos y con un retorno
# No esta definido ningún parámetro
# No recibe argumentos de entrada
# Devuelve un valor
def funcion():
	    return "Bloque de código"
	 
resultado = funcion()
print (resultado)

# Ejemplo 2, Crear una función que devuelva un saludo en diferentes idiomas
print ("Ejemplo 2")
print ("1. Definir función")
def saludo():
    saludos = {"Hola", "Hello", "Bonjour", "Ciao"}
    return saludos.pop()
 
print ("2. Llamar función")
resultado = saludo()
print (resultado)

# Ejercicio 2, Devolver una fruta aleatoria del siguiente conjunto
# frutas = {'🍅','🍌','🍎','🍇','🍉'}

def devolver_fruta():
    frutas = {'🍅','🍌','🍎','🍇','🍉'}
    return frutas.pop()

fruta = devolver_fruta()
print (fruta)

# Funciones sin argumentos y con múltiple retorno
# No recibe argumentos de entrada
# Devuelve múltiples valores
# Devuelve una tupla en Python
# Esto tambien se llama empaquetado y desempaquetado
def funcion():
    return "Bloque", "de", "código"

x,y,z = funcion()
print (type(x), x,y,z)
resultado = funcion()
print (resultado)
print (type(resultado))


# Ejemplo 3, Crear una función que devuelva un saludo en dos idiomas
print ("Ejemplo 3")
print ("1. Definir función")
def saludo():
    saludos_es = {"Hola", "Holi", "Buenos días"}
    saludos_en = {"Hello", "Hi", "Good morning"}
    return saludos_es.pop(), saludos_en.pop()
 
print ("2. Llamar función")
resultado = saludo()
print (resultado)


# Ejercicio 3, Devolver una fruta y un color aleatorio de los siguientes conjuntos
# frutas = {'🍅','🍌','🍎','🍇','🍉'}
# colores = {'🔴','🟠','🟡','🟢','🔵'}
import random

def fruta():
    frutas = list({'🍅', '🍌', '🍎', '🍇', '🍉'})
    return frutas.pop(random.randint(0, len(frutas) - 1))

def color():
    colores = list({'🔴', '🟠', '🟡', '🟢', '🔵'})
    return colores.pop(random.randint(0, len(colores) - 1))
print(fruta(), color())

# ///////////////////////////////
def obtener_fruta_y_color():
    frutas = {'🍅','🍌','🍎','🍇','🍉'}
    colores = {'🔴','🟠','🟡','🟢','🔵'}
    return frutas.pop(), colores.pop()

resultado = obtener_fruta_y_color()
print( resultado, type(resultado))

# //////////////////////////////
def devolver_fruta_color():
    frutas = {'🍅','🍌','🍎','🍇','🍉'}
    colores = {'🔴','🟠','🟡','🟢','🔵'}
    return frutas.pop(), colores.pop()

fruta, color = devolver_fruta_color()
print (fruta, color)

# Funciones con un argumento y sin retorno
# Tiene definido un parámetro de entrada
# Recibe un argumento de entrada
# No devuelve ningún valor

# El parámetro es una variable de la función puede ser de cualquier tipo
# Números, cadenas, listas, diccionarios, tuplas, conjuntos, etc.

# Ejemplo 4, Crear una función que imprima el cuadrado de un número
print ("Ejemplo 4")
print ("1. Definir función")
def cuadrado(numero):
    print (numero**2)
 
print ("2. Llamar función")
cuadrado(5)
cuadrado(10)

# Ejercicio 4, Crear una función que imprima el mensaje de bienvenida de acuerdo al un 
# idioma enviado como argumento, si no existe imprimir un mensaje por defecto
# mensajes = {"es":"Bienvenido al Python Study Group 🐍",
# "en": "Hello and welcome to the Python Study Group! ✨",}

def bienvenida(idioma):
    mensajes = {
        "es":"Bienvenido al Python Study Group 🐍",
        "en": "Hello and welcome to the Python Study Group! ✨",
    }
    print (mensajes.get(idioma, "¡Hola!"))

bienvenida("es")
bienvenida("en")
bienvenida("fr")

# Funciones con múltiples argumentos y sin retorno
# Tiene definido múltiples parámetros de entrada
# Recibe múltiples argumentos de entrada separados por coma
# No devuelve ningún valor
# Los argumentos son variables de la función
# El orden de los argumentos debe coincidir con los parámetros
# Los parámetros definidos pueden ser de cualquier tipo

# Ejemplo 5, Crear una función que reciba una cadena y un entero y repita la cadena el número de veces
print ("Ejemplo 5")
print ("1. Definir función")
def repetir(cadena, veces):
    print (cadena*veces)
	 
print ("2. Llamar función")
repetir("✨🎉", 10)

# Ejercicio 5, Crear una función que reciba una lista de animales, un entero e 
# imprima una lista con los animales repetidos el número de veces
# # Entrada
# animales = ['🐶','🐱','🐭','🐹','🐰']
# Salida
# animales = ['🐶🐶🐶', '🐱🐱🐱', '🐭🐭🐭', '🐹🐹🐹', '🐰🐰🐰']

def repetir_animales(animales, veces):
    lista = [animal*veces for animal in animales]
    print (lista)

animales = ['🐶','🐱','🐭','🐹','🐰']
repetir_animales(animales, 3)

# /////////////////////

def repetir_animales(animales, veces):
    animales_nuevo = []
    for i in animales:
        animales_nuevo.append(i * veces)
    return animales_nuevo

animales = ['🐶','🐱','🐭','🐹','🐰']
print (repetir_animales(animales, 5))

# Funciones con múltiples argumentos y con un retorno
# Tiene definido múltiples parámetros de entrada
# Recibe múltiples argumentos de entrada separados por coma
# Devuelve un valor
# El orden de los argumentos debe coincidir con los parámetros

# Ejemplo 6, Crear una función que reciba dos números y devuelva una lista con la suma, 
# resta, multiplicación y división de los números

print ("Ejemplo 6")
print ("1. Definir función")
def operaciones(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    return [suma, resta, multiplicacion, division]
	 
print ("2. Llamar función")
resultado = operaciones(10, 5)
print (resultado)

# Ejercicio 6, Crear una función que reciba dos enteros y una cadena devolver el 
# resultado de la operación de los números según la cadena puede ser suma, resta, 
# multiplicación o división

def operacion(numero1, numero2, operacion):
    if operacion == "suma":
        return numero1 + numero2
    elif operacion == "resta":
        return numero1 - numero2
    elif operacion == "multiplicacion":
        return numero1 * numero2
    elif operacion == "division":
        return numero1 / numero2
    else:
        return "Operación no válida"

resultado = operacion(10, 5, "suma")
print (resultado)

# Funciones con múltiples argumentos y con múltiple retorno
# Tiene definido múltiples parámetros de entrada
# Recibe múltiples argumentos de entrada separados por coma
# Devuelve múltiples valores
# Devuelve una tupla en Python

# Ejemplo 7, Crear una función que reciba dos números y devuelva la suma, 
# resta, multiplicación y división de los dos números

print ("Ejemplo 7")
print ("1. Definir función")
def operaciones(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    return suma, resta, multiplicacion, division
	 
print ("2. Llamar función")
suma, resta, multiplicacion, division = operaciones(10, 5)
print (suma, resta, multiplicacion, division)

# Ejercicio 7, Crear una juego de piedra papel o tijera, donde reciba dos jugadas por teclado
# y devuelva las jugadas y el resultado, si ingresa salir terminar el juego
def jugar_piedra_papel_tijera(jugada1, jugada2):
    if jugada1 == jugada2:
        resultado = "Empate"
    elif jugada1 == "piedra" and jugada2 == "tijera":
        resultado = "Jugador 1 gana"
    elif jugada1 == "papel" and jugada2 == "piedra":
        resultado = "Jugador 1 gana"
    elif jugada1 == "tijera" and jugada2 == "papel":
        resultado = "Jugador 1 gana"
    else:
        resultado = "Jugador 2 gana"
    return jugada1, jugada2, resultado

while True:
    jugador1 = input("Jugador 1: ")
    jugador1 = jugador1.lower()
    if jugador1 == "salir":
        print ("Fin del juego por jugador 1")
        break
    if jugador1 == "piedra" or jugador1 == "papel" or jugador1 == "tijera":
        jugador2 = input("Jugador 2: ")
        jugador2 = jugador2.lower()
        if jugador2 == "salir":
            print ("Fin del juego por jugador 2")
            break
        if jugador2 == "piedra" or jugador2 == "papel" or jugador2 == "tijera":
            resultado = jugar_piedra_papel_tijera(jugador1, jugador2)
            print (resultado)
        else:
            print ("Jugador 2 ingreso op no valida")
    else:
            print ("Jugador 1 ingreso op no valida")
    
# Variables globales y locales
# Las variables globales son accesibles desde cualquier parte del programa
# Las variables locales son accesibles solo dentro de un bloque de código como una función
# Si hay una variable local y una global con el mismo nombre, la variable local tendrá prioridad donde está definida
variable_global = "Variable global"

def funcion():
    variable_local = "Variable local"
    print ("✨",variable_global)
    print ("✨",variable_local)

funcion()
print ("🎈",variable_global)
#print ("🎈",variable_local) # es una variable local 

# Prioridad
variable = "Variable global"
print ('0.',variable)

def funcion():
    variable = "Variable local"
    print ('1.',variable)

funcion()
print ('2.',variable)

# Ejemplo 8, De la siguiente lista de números obtener el mayor y menor número con una función
numeros = [10, 5, 20, 15, 25, 30] #Global

def mayor_menor(): #No recibe argumentos
    mayor = max(numeros) #Local
    menor = min(numeros) #Local
    return mayor, menor #Devuelve dos valores

resultado = mayor_menor()
print (resultado)

# Ejercicio 8, De la siguiente cadena global convertir en formato título y contar 
# las vocales aeiou con una función
# cadena = "python es un lenguaje de programación"
def formato_vocales():
    titulo = cadena.title()
    vocales = sum([1 for letra in titulo if letra in "aeiou"])
    return titulo, vocales

cadena = "python es un lenguaje de programación"
resultado = formato_vocales()

print (resultado)

# ////////////////////////////

cadena = "python es un lenguaje de programación"
def funcion_vocales():
    titulo = cadena.title()
    cont = 0
    for vocal in titulo:
        if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
            cont +=1
    return cont

resultado = funcion_vocales()
print (resultado)


# Args y Kwargs
# *args es una lista de parámetros sin clave
# **kwargs es un diccionario de parámetros con clave

# Los argumentos utilizando *args son enviados como una tupla
# Los *args se escriben después de los parámetros de la función
# Se utiliza cuando no se sabe la cantidad de argumentos que se enviarán
# Pueden ser iterados

# Estructura de *args
def funcion(*args):
    print (args)
    print (type(args))

funcion("Bloque", "de", "código")

# Ejemplo 9 Crear una función que reciba un número y una cantidad de cadenas, 
# concatene las cadenas y la devuelva repetida N veces
print ("Ejemplo 9")
print ("1. Definir función")
def concatenar(numero, *cadenas):
    concatenado = ""
    for cadena in cadenas:
        concatenado += cadena
    return concatenado*numero
 
print ("2. Llamar función")
resultado = concatenar(3, "🍎", "🍌", "🍍")
print (resultado)

# Ejercicio 9, Crear una función que reciba N objetos y genere una tupla y una 
# lista con los objetos usando *args
# 1, 1.1, True, "🍎"
def tupla_lista(*args):
    tupla = tuple(args)
    lista = list(args)
    return tupla, lista

lista, tupla = tupla_lista(1, 1.1, True, "🍎")

print (lista)
print (tupla)

# Kwargs
# Los argumentos utilizando **kwargs son enviados como un diccionario 
# Los **kwargs se escriben después de los parámetros de la función
# Se utiliza cuando no se sabe la cantidad de argumentos que se enviarán con clave
# Pueden ser iterados
# Se accede a los valores con la clave del diccionario

# Estructura de **kwargs
def funcion(**kwargs):
    print (kwargs)
    print (type(kwargs))

funcion(nombre="Jhon", apellido="Doe", genero="M")

# Ejemplo 10, Crear una función que reciba los datos de una persona y 
# devuelva un mensaje con los datos
print ("Ejemplo 10")
print ("1. Definir función")
def datos_persona(**datos):
    mensaje = ""
    for clave, valor in datos.items():
        mensaje += f"{str(clave).title()}: {str(valor).upper()}\n"
    return mensaje
print ("2. Llamar función")
resultado = datos_persona(nombre="Jhon", apellido="Doe", edad=20, boliviano=True)
print (resultado)

# Ejercicio 10, Crea un simulador de lavar platos con una función que reciba los 
# objetos a lavar y el tiempo de lavado de cada objeto devuelva un mensaje con los 
# objetos lavados y el tiempo total de lavado
# Plato: 5 minutos, Vaso: 3 minutos, Tenedor: 1 minuto, Cuchara: 0.5 minutos
def lavar(**objetos):
    tiempo_total = 0
    mensaje = ""
    for objeto, tiempo in objetos.items():
        tiempo_total += tiempo
        mensaje += f"{objeto}: {tiempo} minutos\n"
    mensaje += f"Tiempo total: {tiempo_total} minutos"
    return mensaje

resultado = lavar(plato=5, vaso=3, tenedor=1, cuchara=0.5)
print (resultado)

# Documentación de funciones
# Es importante documentar las funciones para que otros programadores puedan 
# entender su funcionamiento
# Se puede documentar una función con un comentario de varias líneas
# Se accede con la función .__doc__

def funcion():
    """
    Documentación aquí
    """
    print ("Bloque de código")

# def funcion(): es la definición de la función
# """ es el inicio de la documentación
# Documentación aquí es el texto de la documentación
# """ es el fin de la documentación
# print es el bloque de código indentado

# Acceso a la documentación con .__doc__
print ("Acceso a la documentación")
def funcion():
    """
    Documentación aquí
    """
    print ("Bloque de código")
print (funcion.__doc__)
print ("Fin de la ejecución")

# Llamado de funciones dentro de funciones
# Se pueden llamar funciones dentro de otras funciones
# Se utiliza para dividir una función en bloques de código más pequeños
# Se puede llamar una función dentro de un bucle o condicional

# Ejemplo 11, Crear tres funciones una principal que reciba un número y dos 
# funciones anidadas que devuelvan el cuadrado y el cubo del número
print ("Ejemplo 11")
print ("1. Definir función Principal")
def principal(numero):
    cuadrado = cuadrado_numero(numero)
    cubo = cubo_numero(numero)
    return cuadrado, cubo
 
print ("2. Definir función Cuadrado")
def cuadrado_numero(numero):
    return numero**2
 
print ("3. Definir función Cubo")
def cubo_numero(numero):
    return numero**3
 
print ("4. Llamar función Principal")
numero = 5
resultado = principal(numero)
print (numero, resultado)


# Ejercicio 11, Crear funciones de limpieza de una cadena para obtener las letras y 
# convertir todo en mayúsculas crea funciones de limpieza y función una principal
# cadena = "Python es un lenguaje de programación 🎈. Feliz Aprendizaje el 2024"
def limpiar_letras(cadena):
    """
    Elimina los números de una cadena y espacios
    """
    return "".join([letra for letra in cadena if letra.isalpha()])
def limpiar_mayusculas(cadena):
    """
    Convierte una cadena en mayúsculas
    """
    return cadena.upper()

def limpiar(cadena):
    cadena = limpiar_letras(cadena)
    cadena = limpiar_mayusculas(cadena)
    return cadena

cadena = "Python es un lenguaje de programación 🎈. Feliz Aprendizaje el 2024"
resultado = limpiar(cadena)
print (cadena)
print (resultado)


# Funciones Recursivas
# Una función recursiva es una función que se llama a sí misma
# Se utiliza para reprocesar un bloque de código
# Se debe tener un caso base para evitar un bucle infinito
# Se utiliza para resolver problemas matemáticos, grafos, árboles, etc.

# Estructura de una función recursiva
# def funcion_recursiva(valor):
#     if caso_base:
#         return valor
#     else:
#         return funcion_recursiva(valor)
    
# def funcion_recursiva(valor): es la definición de la función
# if caso_base: es la condición para terminar la recursividad
# return valor es el valor a devolver
# else: es el bloque de código recursivo
# return funcion_recursiva(valor) es la llamada recursiva

# Ejemplo 12, Crear una función recursiva para obtener el 10 número par
print ("Ejemplo 12")
print ("1. Definir función")
def numero_par(numero):
    if numero == 0:
        return 0
    else:
        return numero_par(numero-1) + 2
 
print ("2. Llamar función")
resultado = numero_par(10)
print (resultado)

# Ejercicio 12, Crear una función recursiva para obtener el factorial de un número
# 5!=5∗4∗3∗2∗1=1205
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero*factorial(numero-1)

resultado = factorial(5)
print (resultado)

# Funciones anónimas o lambda
# Una función anónima es una función sin nombre
# Se utiliza para funciones pequeñas y simples
# Se utiliza para funciones que se van a pasar como argumento
# Se realiza en una sola línea
# se puede asignar a una variable

# Se recomienda utilizar para funciones pequeñas y simples
# Según PEP-8 no se recomienda utilizar lambda sino crear una función definida
# Se puede utilizar en funciones como map, filter, reduce, sorted, etc. para procesar datos

# Estructura de una función anónima
# lambda argumento: expresión
# lambda es la palabra reservada
# argumento es el argumento de la función
# : es el delimitador de la expresión
# expresión es el bloque de código

# Ejemplo 13, Crear una función anónima para obtener el cuadrado de un número
print ("Ejemplo 13")
cuadrado = lambda numero: numero**2
resultado = cuadrado(5)
print (resultado)
resultado = cuadrado(10)
print (resultado)

# Ejercicio 13, Crear una función anónima para obtener de una cadena las letras solo 
# los alfanuméricos y convertir en mayúsculas
# cadena = "Python es un lenguaje de programación"
cadena = "Python es un lenguaje de programación"
limpiar = lambda cadena: "".join([letra for letra in cadena if letra.isalnum()]).upper()
resultado = limpiar(cadena)
print (cadena)
print (resultado)
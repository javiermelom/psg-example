# ESTRUCTURAS DE CONTROL DE FLUJO
# Sentencias condicionales

# Estructura de control
# En un programa las estructuras de control son el orden en el que se ejecutan las instrucciones
# Python soporta las siguientes estructuras de control
#       Secuencial o lineal -> Es la ejecución de las instrucciones en el orden en el que se escriben
#           primero = 1
#           segundo = 2
#           tercero = 3
#       Selección o condicionales
#       Repetición o ciclos

# El problema con la secuencialidad es que no siempre queremos que las instrucciones se ejecuten en el orden en el que se escriben
# Para eso existen las estructuras de control de selección y repetición

# Selección o condicionales
# Las estructuras de selección o condicionales permiten ejecutar un bloque de código si se cumple una condición
# Permite a los programas tomar decisiones y ejecutar diferentes acciones dependiendo de las condiciones
# En Python se utilizan las siguientes condicionales
#       if -> permite ejecutar un bloque de código si se cumple una condición. La condición tiene que ser un booleano
#       else
#       if anidado
#       elif

# Como se declara un if
# if tiene la siguiente estructura
# if condicion:
#   print ("Cumple")

# En Python la estructura de un condicional if es la siguiente

print ("Inicio")
condicion = True
if condicion:
    # Bloque de código
    print ("Cumple condición")
print ("Fin")

# Ejemplo: Dado un número, imprimir si es par
print ("Inicio")
numero = 4
if numero % 2 == 0: # Si el módulo de 2 es 0
    print ("El número es par")
print ("Fin")

# if-else
# La sentencia else permite ejecutar un bloque de código si no se cumple la condición del if
# Si la condición es True se ejecuta el bloque de código del if
# Si la condición es False se ejecuta el bloque de código del else

# Como se declara un if-else
# if-else tiene la siguiente estructura

if condicion:
    print ("Cumple")
else:
    print ("No cumple")

# En Python la estructura de un condicional if-else es la siguiente
print ("Inicio")
condicion = False
if condicion:
    # Bloque de código
    print ("Cumple condición")
else:
    # Bloque de código
    print ("No cumple condición")
print ("Fin")

# Ejemplo: Dado un número, imprimir si es par o impar
print ("Inicio")
numero = 3
if numero % 2 == 0: # Si el módulo de 2 es 0
    print ("El número es par")
else:
    print ("El número es impar")
print ("Fin")

# if-anidado
# La sentencia if anidado permite ejecutar un bloque de código si se cumple una condición
# Dentro del bloque de código del if-else se puede anidar otro if-else de manera ilimitada
# Como se declara un if-anidado
# if-anidado tiene la siguiente estructura

print ("Inicio Anidado")
condicion_1 = True
condicion_2 = False
if condicion_1:
    print ("Cumple condición 1")
    if condicion_2:
        print ("Cumple condición 2")
    else:
        print ("No cumple condición 2")
else:
    print ("No cumple condición 1")
print ("Fin")

# Ejemplo: Dado un número, imprimir si es par, impar o cero
print ("Inicio Par, Impar o Cero")
numero = 0  
if numero > 0 or numero < 0:
    if numero % 2 == 0: # Si el módulo de 2 es 0
        print ("El número es par")
    else:
        print ("El número es impar")
else:
    print ("El número es cero")
print ("Fin")

# Una desventaja de los condicionales anidados es que pueden ser difíciles de leer y entender
# Tener una indentación excesiva puede hacer que el código no sea optimo
# En Python existe una estructura de control que permite simplificar los condicionales anidados
# Se llama elif
# La sentencia elif es la abreviatura de else if
# Permite ejecutar un bloque de código si no se cumple la condición del if y sí cumple una nueva condición
# En Python la estructura de un condicional elif es la siguiente
print ("Inicio ELIF")
condicion_1 = False
condicion_2 = True
if condicion_1:
    print ("Cumple condición 1")
elif condicion_2:
    print ("Cumple condición 2")
else:
    print ("No cumple condición 1 ni 2")
print ("Fin")

# Ejemplo: Dado un número, imprimir si es positivo, negativo o cero
print ("Inicio Positivo, Negativo o Cero")
numero = -1
if numero > 0:
    print ("El número es positivo")
elif numero < 0:
    print ("El número es negativo")
else:
    print ("El número es cero")
    
# Existe una forma de compactar una condicional en una sola línea. Se llama operador ternario
# es una forma de compactar una condicional en una sola línea
# Como su nombre lo indica, tiene tres partes
#   Condición
#   Resultado verdadero si es True
#   Resultado falso si es False

# resultado = verdadero if condicion else falso
# En Python la estructura de un operador ternario es la siguiente
print ("Inicio Ternario")
condicion = True
resultado = "Cumple" if condicion else "No cumple"
print (resultado)
print ("Fin")

# Ejemplo: Dado un número, imprimir si es par o impar
print ("Inicio Ternario Par, Impar")
numero = 3
resultado = "El número es par" if numero % 2 == 0 else "El número es impar"
print (resultado)
print ("Fin")

# ¿Qué es Truthiness?
# Es un término que se utiliza para describir el valor de verdad de un objeto
# En Python, todos los objetos tienen un valor de verdad
# Hay valores que se consideran True y otros que se consideran False

# En enteros
#    0 es False
#   1 es True
#    -1 es True
# Todos los números enteros positivos y negativos son True excepto 0
# x∈Z∧x≠0

# Se puede utilizar un entero como condición. Introducir dos números enteros y dividirlos
print ("Truthiness Enteros")
dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
print (dividendo,divisor)
if divisor: #divisor != 0
    print (dividendo / divisor)
else:
    print ("No se puede dividir entre cero")
print ("Fin")

# En los flotantes
#    0.0 es False
#    1.0 es True
#    -1.0 es True
# Todos los números flotantes positivos y negativos son True excepto 0.0
#x∈R∧x≠0.0

# Se puede utilizar un flotante como condición
# Introducir dos números flotantes y dividirlos

print ("Truthiness Flotantes")
dividendo = float(input("Dividendo: "))
divisor = float(input("Divisor: "))
print (dividendo,divisor)
if divisor: #divisor != 0.0
    print (dividendo / divisor)
else:
    print ("No se puede dividir entre cero")
print ("Fin")

# En las cadenas
#    "" es False
#    " " es True
#    "hola" es True
#    "0" es True
# Todas las cadenas no vacías son True
# Las cadenas vacías son False

# Se puede utilizar una cadena como condición
# Introducir una cadena y verificar si es vacía
print ("Truthiness Cadenas")
cadena = input("Cadena: ")
print (cadena)
if cadena: # len(cadena) != 0 or cadena != "" 
    print ("La cadena no está vacía")
else:
    print ("La cadena está vacía")
print ("Fin")

# En las tuplas
#    () es False
#   (0,) es True
#    ("0",) es True
#    ("♎",) es True
# Todas las tuplas no vacías son True
# Las tuplas vacías son False
# Se puede utilizar una tupla como condición
# Introducir una tupla y verificar si es vacía
print ("Truthiness Tuplas")
tupla = tuple(input("Tupla: "))
print (tupla)
if tupla: # len(tupla) != 0 or tupla != ()
    print ("La tupla no está vacía")
else:
    print ("La tupla está vacía")
print ("Fin")

# En las listas
#    [] es False
#    [0] es True
#    [""] es True
#    ["♎"] es True
# Todas las listas no vacías son True
# Las listas vacías son False
# Se puede utilizar una lista como condición
# Introducir una lista y verificar si es vacía

print ("Truthiness Listas")
lista = list(input("Lista: "))
print (lista)
if lista: # len(lista) != 0 or lista != []
    print ("La lista no está vacía")
else:
    print ("La lista está vacía")
print ("Fin")

# En conjuntos
#    set() es False
#    {0} es True
#    {"0"} es True
#    {"♎"} es True
# Todos los conjuntos no vacíos son True
# Los conjuntos vacíos son False
# Se puede utilizar un conjunto como condición
# Introducir un conjunto y verificar si es vacío

print ("Truthiness Conjuntos")
conjunto = set(input("Conjunto: "))
print (conjunto)
if conjunto: # len(conjunto) != 0 or conjunto != set()
    print ("El conjunto no está vacío")
else:
    print ("El conjunto está vacío")
print ("Fin")

# En diccionarios
#    {} es False
#    {'': ''} es True
#    {"0":0} es True
#    {"♎":"Libra"} es True
# Todos los diccionarios no vacíos son True
# Los diccionarios vacíos son False
# Se puede utilizar un diccionario como condición
# Introducir la clave y un valor y verificar si es vacío
print ("Truthiness Diccionarios")
diccionario = {}
clave = input("Clave: ")
valor = input("Valor: ")
if clave:
  diccionario = {clave:valor}
print (diccionario)
if diccionario: # diccionario != {}
    print ("El diccionario no está vacío")
else:
    print ("El diccionario está vacío")
print ("Fin")

# None es un valor especial en Python
# None es False
# None es un valor especial que representa la ausencia de un valor
# Se puede utilizar None como condición
# Introducir un valor y verificar si es None
print ("Truthiness None")
valor = None
print (valor, type(valor))
if valor: # valor != None
    print ("El valor no es None")
else:
    print ("El valor es None")
print ("Fin")

# Con operadores ternarios es bastante útil para asignar valores a variables
entero = int(input("Entero: "))
resultado = "Diferente de 0" if entero else "Igual a 0"
print (resultado)
flotante = float(input("Flotante: "))
resultado = "Diferente de 0.0" if flotante else "Igual a 0.0"
print (resultado)
cadena = input("Cadena: ")
resultado = "No está vacía" if cadena else "Está vacía"
print (resultado)

# Tienes un dispositivo que mide la temperatura y si la temperatura es mayor a 30°C
# enciende un ventilador y si es menor a 20°C lo apaga
temp = int(input("Digite la temperatura:"))
if (temp > 30):
    print ("ventilador encendido")
elif (temp < 20):
    print ("Ventilador apagado")
else:
    print ("Valor de temperatura menor a 30 y mayor a 20")

# Tienes una cesta de frutas y quieres saber si tienes manzanas, si hay manzanas 
# las cuentas y si no hay compras dos manzanas
cesta = ("manzana", "pera", "manzana", "manzana", "durazno")
if cesta:
    print ("La cesta esta vacia")
else:
    print (cesta.count("manzana"))
    

# con solo un if
cesta = ['🍎','🍑','🍓','🍉']
print (cesta)
if '🍎' in cesta:
    print (f"Hay {cesta.count('🍎')} manzanas")
else:
    cesta.extend(['🍎','🍎'])
    print (cesta)
    
# Con operador ternario
cesta = ['🍑','🍓','🍉']
print (cesta)
resultado = f"Hay {cesta.count('🍎')} manzanas" if '🍎' in cesta else cesta.extend(['🍎','🍎'])
print (resultado)
print (cesta)

# En un diccionario tienes almacenado un animal y quieres saber si es un mamífero
animal = {'especie':'🐶', 'nombre': 'Firulais', 'mamifero': True}
consulta = 'mamifero'
if animal.get(consulta):
    print('es mamifero')
else:
    print('no es mamifero')


# Dado dos conjuntos, verificar si tienen elementos en común y mostrarlos y si no, unirlos
# {'⚽','🏀','🏐'} , {'🏈','🏉','🏓'}
conjunto_1 = {'⚽','🏀','🏐'}
conjunto_2 = {'🏈','🏉','🏓'}
print (conjunto_1, conjunto_2)
if conjunto_1.isdisjoint(conjunto_2): # len(conjunto_1.intersection(conjunto_2)) == 0
    conjunto_1.update(conjunto_2)
    print (conjunto_1)
else:
    print ("Tienen elementos en común")
    print (conjunto_1.intersection(conjunto_2))
    
# Validar si un correo electrónico es válido usando input

#    ✅: mail@domain.com, ma.il@domain.com
#    ❌: mail@domain, maildomain.com, @.
#    ❌: mail@@domain.com, mail@.com

# Solución anidada
correo = input("Correo: ")
if "@" in correo and "." in correo and correo.count("@") == 1:
    if correo.find("@") < correo.rfind(".") and correo.find("@") > 0 and correo.rfind(".") < len(correo) - 1:
        if correo.rfind(".") - correo.find("@") > 1:
            if correo.find(".") - correo.find("@") > 1:
                print ("El correo es válido")
            else:
                print ("El correo no es válido")
        else:
            print ("El correo no es válido")
    else:
        print ("El correo no es válido")
else:
    print ("El correo no es válido")

# Solución con elif
correo = input("Correo: ")
if "@" not in correo or "." not in correo or correo.count("@") != 1:
    print("El correo no es válido")
elif correo.find("@") >= correo.rfind(".") or correo.find("@") == 0 or correo.rfind(".") == len(correo) - 1:
    print("El correo no es válido")
elif correo.rfind(".") - correo.find("@") <= 1:
    print("El correo no es válido")
elif correo.find(".") - correo.find("@") == 1:
    print("El correo no es válido")
else:
    print("El correo es válido")
    
    
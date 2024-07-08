# Errores y Excepciones
# Un error es una situación que se produce cuando una instrucción no puede ejecutarse correctamente.
# En Python, un error puede ser un error de sintaxis o un error de excepción
# Un error de sintaxis se produce cuando Python no puede interpretar nuestro código
# Generalmente porque hemos escrito mal alguna parte del código

# ¿Qué es una excepción?
# Una excepción es un error que ocurre durante la ejecución de un programa
# Cuando se produce una excepción, el programa se detiene y muestra un mensaje de error
# La mayoría de las excepciones son ya gestionadas por Python
# Aveces es necesario gestionar las excepciones nosotros mismos
# En Python las excepciones se pueden manejar para evitar que el programa se detenga inesperadamente

# Estructura de una excepción Simple
# try:
    # Código que puede lanzar una excepción
# except Exception as e:
    # Código que se ejecuta si se produce una excepción
# Código que se ejecuta siempre fuera del bloque try-except

# try: Bloque de código que puede lanzar una excepción posee indentación
# except: Bloque de código que se ejecuta si se produce una excepción
# Exception as e: Captura la excepción y la almacena en la variable e

# Ejemplo 1, División por cero
print ("Inicio Ejemplo 1")
x = 1 / 0
print (x)
print ("Fin Ejemplo 1")

# Ejemplo 1, División por cero
print ("Inicio Ejemplo 1")
try:
    x = 1 / 0
    print (x)
except Exception as e:
    print("💀 Error:", e, type(e))
print ("Fin Ejemplo 1")

# Ejercicio 1, Crear un programa que solicite dos números y realice la 
# división de ambos números Si hay un error mostrar un mensaje de error 
# El programa se detiene si se ingresa "salir"

while True:
    try:
        num1 = input("Ingrese el primer número: ")
        if num1 == "salir":
            break
        num2 = input("Ingrese el segundo número: ")
        if num2 == "salir":
            break
        num1 = float(num1)
        num2 = float(num2)
        print("Resultado:", num1 / num2)
    except Exception as e:
        print("💀 Error:", e)

# Tipos de excepciones
# Algunos tipos de excepciones son:
# ZeroDivisionError: Se produce cuando se intenta dividir por cero
# NameError: Se produce cuando no se encuentra una variable
# TypeError: Se produce cuando se intenta realizar una operación no permitida
# ValueError: Se produce cuando se intenta realizar una operación con un valor incorrecto
# KeyError: Se produce cuando se intenta acceder a una clave que no existe en un diccionario
# IndexError: Se produce cuando se intenta acceder a un índice que no existe en una lista

# Excepciones múltiples
# try puede detectar un tipo de excepción específico y ejecutar un bloque de código diferente para cada tipo de excepción
# Se debe poner un bloque except el tipo de excepción que se desea capturar con jerarquía de arriba hacía abajo

try:
    # Código que puede lanzar una excepción
    print()
except ZeroDivisionError as e:
    # Código si se produce una excepción de división por cero
    print()
except Exception as e:
    # Código si se produce una excepción genérica
    print()
    
# Ejemplo 2, División por cero
print ("Inicio Ejemplo 2")
divisor = 0
try:
    x = 1 / divisor
    print (x)
except ZeroDivisionError as e:
    print("0️⃣ Error:", e, type(e))
except Exception as e:
    print("💀 Error:", e, type(e))
print ("Fin Ejemplo 2")

# Ejemplo 2, División por cero
print ("Inicio Ejemplo 2")
divisor = "0"
try:
    x = 1 / divisor
    print (x)
except ZeroDivisionError as e:
    print("0️⃣ Error:", e, type(e))
except Exception as e:
    print("💀 Error:", e, type(e))
print ("Fin Ejemplo 2")

# Jerarquía de excepciones
# Ejemplo 2, División por cero
print ("Inicio Ejemplo 2")
divisor = 0
try:
    x = 1 / divisor
    print (x)
except Exception as e: # Captura cualquier excepción
    print("💀 Error:", e, type(e))
except ZeroDivisionError as e:
    print("0️⃣ Error:", e, type(e))
print ("Fin Ejemplo 2")

# Ejemplo 3, De la lista de calificaciones obtener el promedio
calificaciones = [20,40,80,"A"]
suma = 0
try:
    for i in range(len(calificaciones)+1):
        suma += calificaciones[i] 
    promedio = suma / len(calificaciones)
    print("Promedio:", promedio)
except ZeroDivisionError as e:
    print("0️⃣ Error:", e, type(e))
except TypeError as e:
    print("🎭 Error:", e, type(e))
except Exception as e:
    print("💀 Error:", e, type(e))
    
# Ejemplo 3, De la lista de calificaciones obtener el promedio
calificaciones = [20,40,80]
suma = 0
try:
    for i in range(len(calificaciones)+1):
        suma += calificaciones[i]
    promedio = suma / len(calificaciones)
    print("Promedio:", promedio)
except ZeroDivisionError as e:
    print("0️⃣ Error:", e, type(e))
except TypeError as e:
    print("🎭 Error:", e, type(e))
except Exception as e: # Captura cualquier excepción
    print("💀 Error:", e, type(e))

# Ejemplo 3, De la lista de calificaciones obtener el promedio
calificaciones = [20,40,80]
suma = 0
try:
    for i in range(len(calificaciones)):
        suma += calificaciones[i] # suma = suma + calificaciones[i]
    promedio = suma / len(calificaciones)
    print("Promedio:", promedio)
except ZeroDivisionError as e:
    print("0️⃣ Error:", e, type(e))
except TypeError as e:
    print("🎭 Error:", e, type(e))
except Exception as e:
    print("💀 Error:", e, type(e))
    
# Bloque else
# Se puede agregar un bloque else que se ejecuta si no se produce ninguna excepción
# Se debe poner después de todos los bloques except
# Lo utilizamos validar la entrada de datos o para mostrar un mensaje de éxito

# Estructura de un bloque else
try:
    # Código que puede lanzar una excepción
    print()
except Exception as e:
    # Código si se produce una excepción
    print()
else:
    # Código si no se produce ninguna excepción
    print()


# Ejemplo 4, De la lista de calificaciones obtener el promedio
print ("Inicio Ejemplo 4")
calificaciones = [20,40,80]
suma = 0
try:
    for i in range(len(calificaciones)):
        suma += calificaciones[i]
    promedio = suma / len(calificaciones)
    print("Promedio:", promedio)
except Exception as e:
    print("💀 Error:", e, type(e))
else:
    print ("🎉 Sin errores")
print ("Fin Ejemplo 4")

# Ejercicio 2, Crear un programa que solicite dos números y mediante una función 
# devuelva la división de ambos Si hay un error mostrar un mensaje de error. 
# El programa se detiene si se ingresa "salir" Añadir un bloque else que 
# muestre el resultado de la función

def division(num1, num2):
    return num1 / num2

while True:
    try:
        num1 = input("Ingrese el primer número: ")
        if num1 == "salir":
            break
        num2 = input("Ingrese el segundo número: ")
        if num2 == "salir":
            break
        num1 = float(num1)
        num2 = float(num2)
        resultado = division(num1, num2)
    except Exception as e:
        print("💀 Error:", e)
    else:
        print("🎉 Resultado: ",resultado)

# Bloque finally
# Se puede agregar un bloque finally que se ejecuta siempre, independientemente de si se produce una excepción
# Se debe poner después de todos los bloques except y else
# Se utiliza para liberar recursos o cerrar archivos
# Para garantizar que se ejecute un código importante sin importar si se produce una excepción o no

# Estructura de un bloque finally
try:
    # Código que puede lanzar una excepción
    print()
except Exception as e:
    # Código si se produce una excepción
    print()
else:
    # Código si no se produce ninguna excepción
    print()
finally:
    # Código que se ejecuta siempre
    print()
    
# Ejemplo 5, Simula una conexión a internet que haga ping y cerrar la conexión
print ("Inicio Ejemplo 5")
try:
    print("🔗 Ping...")
except Exception as e:
    print("💀 Error:", e)
else:
    print("🎉 Ping Exitoso")
finally:
    print("🔌 Cerrando conexión")
    
# ¿Cómo generamos una excepción?
# Para probar que finally se ejecuta siempre

# Raise
# raise se utiliza para generar una excepción
# Se puede generar una excepción específica o una excepción genérica

# Estructura de raise
# raise Exception("Mensaje de error")
# raise es una palabra reservada de Python
# Exception es el tipo de excepción que se desea generar
# "Mensaje de error" es el mensaje que se mostrará


# Ejemplo 6, Simula una conexión a internet que haga ping y cerrar la conexión
print ("Inicio Ejemplo 6")
try:
    print("🔗 Ping...")
    raise Exception("Error de conexión") #Excepción genérica
except Exception as e: # Captura cualquier excepción
    print("💀 Error:", e)
else:
    print("🎉 Ping Exitoso")
finally:
    print("🔌 Cerrando conexión")


# Ejercicio 3, Escriba un programa que solicite un número por teclado y se almacene en una lista
# Si es 0 se genera una excepción
# Si la ejecución es correcta muestra "🎉Agregado"
# Termina la ejecución sólo con la palabra "salir" utilizar la excepción KeyboardInterrupt
# Finalmente imprima siempre la suma de los números y la lista

numeros = []
while True:
    try:
        num = input("Ingrese un número: ")
        if num == "salir":
            break
        num = float(num)
        if num == 0:
            raise Exception("No se puede agregar el número 0")
        numeros.append(num)
    except KeyboardInterrupt as e:
        print('🚫 Para salir escriba "salir"')
    except Exception as e:
        print("💀 Error:", e)
    else:
        print("🎉 Número agregado")
    finally:
        print("Suma:", sum(numeros))

# Pass
# pass es una palabra reservada de Python que no hace nada
# Se utiliza para evitar errores de sintaxis
# Se puede utilizar para evitar errores de indentación

# Ejemplo 7, Crea una función que no hace nada
print("Inicio Ejemplo 7")
def funcion():
    pass

funcion()
print("Fin Ejemplo 7")

# Excepciones personalizadas
# Se pueden crear excepciones personalizadas
# Nos permite crear excepciones específicas para nuestro programa
# Se utiliza para crear excepciones de acuerdo a las necesidades del programa

#Estructura de una excepción personalizada
# class MiError(Exception):
#    pass

#raise MiError("Mensaje de error")

# class: palabra reservada de Python para crear una clase
# MiError (Exception): nombre de la clase y la excepción de la que hereda
# pass: palabra reservada de Python para indicar que no hace nada

# Ejemplo 8, Tienes un frutero, saca las frutas mientras no sea un 
# gusano y genera una excepción
print("Inicio Ejemplo 8")
class GusanoError(Exception):
    pass
 
frutero = ['🍎', '🍌', '🍐', '🐛', '🍇']
for fruta in frutero:
    try:
        if fruta == '🐛':
            raise GusanoError("😱 Ewww!")
        print(fruta)
    except GusanoError as e:
        print("🐛 Error:", e)
    except Exception as e:
        print("💀 Error:", e)
print("Fin Ejemplo 8")

# Ejercicio 4, Crear un programa que solicite palabras por teclado y almacene en una lista
# Si se inserta caracteres no alfabéticos se genera una excepción personalizada y no se almacena
# Si se ingresa "salir" se termina la ejecución
# Finalmente imprimir la lista de palabras


class NoAlfabeticoError(Exception):
    pass

palabras = []
while True:
    try:
        palabra = input("Ingrese una palabra: ")
        if palabra == "salir":
            break
        if not palabra.isalpha():
            raise NoAlfabeticoError("Solo se permiten letras")
        palabras.append(palabra)
    except NoAlfabeticoError as e:
        print("🚫 Error:", e)
    except Exception as e:
        print("💀 Error:", e)
    else:
        print("🎉 Palabra agregada")
    finally:
        print("Lista:", palabras)
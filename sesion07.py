simple = 'Mi cadena permite comillas "dobles" en una sola línea'
doble  = "Mi cadena permite comillas 'simples' en una sola línea"
triple_simple = '''Mi cadena
permite contenido 
en varias líneas y comillas "dobles" '''
triple_doble = """Mi cadena
permite contenido 
en varias líneas y comillas 'simples' """
print (simple)
print (doble)
print (triple_simple)
print (triple_doble)

entero = str(1)
flotante = str(1E-3)
hexadecimal = str(0xA)
booleano = str (True)
print (entero)
print (flotante)
print (hexadecimal)
print (booleano)
print (type(entero))
print (type(flotante))
print (type(hexadecimal))
print (type(booleano))

print ("El mensaje enviado fue: \"Hello, I\'m a message\"")
print ('El mensaje enviado fue: \"Hello, I\'m a message\"')

mensaje = "Hola,\n\teste es un mensaje \vcon algunos caracteres \
especiales como \\ y tabulador."
print(mensaje)

entrada = input("Ingrese un valor: ")
print (entrada)
print (type(entrada))

entero = int(input("Ingrese un valor entero: "))
print (entero, type(entero))

flotante = float(input("Ingrese un valor flotante: "))
print (flotante, type(flotante))

booleano = bool(input("Ingrese un valor booleano: "))
print (booleano, type(booleano))

print ("Indexado positivo")
fruta = "banana"
print (fruta)
print (fruta[0])
print (fruta[5])

print ("Indexado negativo")
fruta = "banana"
print (fruta)
print (fruta[-1])
print (fruta[-3])

print ("Slicing")
ciudad =  "LaPaz-Bolivia"
print (ciudad)
print ("Slicing con índices positivos")
print (ciudad[0:6])
print (ciudad[0:6:2])
print ("Slicing con índices negativos")
print (ciudad[-10:-2])
print (ciudad[-10:-2:2])

print ("Slicing sin índice inicial y final")
print (ciudad[:6])
print (ciudad[6:])
print ("Slicing sin índice inicial ni final")
print (ciudad[:])
print (ciudad[::2])

print ("Slicing con paso negativo")
print (ciudad[10:4:-1])
print (ciudad[10::-2])

print ("Concatenación de cadenas")
cadena1 = "Hola"
cadena2 = "Mundo"
concatenada = cadena1 + " " + cadena2
print (concatenada)

print ("Repetición de cadenas")
cadena = "-#-"
repetida = cadena * 10
print (repetida)

print ("Longitud de una cadena")
cadena = "Hola Mundo :D"
longitud = len(cadena)
print (cadena)
print (longitud, type(longitud))

print ("Función Upper")
cadena = "cadena Inicial #1"
mayuscula  = cadena.upper()
print (cadena)
print (mayuscula)
print ("Función Lower")
cadena = "Cadena INICIAL #2"
minuscula  = cadena.lower()
print (cadena)
print (minuscula)

print ("Función Capitalize")
cadena = "cadena INICIAL #3"
capital = cadena.capitalize()
print (cadena)
print (capital)

print ("Función Title")
cadena = "CADENA inicial #4"
titulo = cadena.title()
print (cadena)
print (titulo)

print ("Función Swapcase")
cadena = "CADena InIcIaL #5"
swap = cadena.swapcase()
print (cadena)
print (swap)

print ("Función Count")
cadena = "Cantidad de veces la letra A"
contar = cadena.count("a")
print(cadena)
print(contar, type(contar))

print ("Función Find")
cadena = "Encontrar las letras las"
buscar = cadena.find("las")
print(cadena)
print(buscar, type(buscar))

print ("Función Rfind")
cadena = "Encontrar las letras las"
buscar = cadena.rfind("las")
print(cadena)
print(buscar, type(buscar))

print ("Función Find y Rfind")
cadena = "Encontrar tres O"
buscar = cadena.find("OOO")
print(cadena)
print(buscar, type(buscar))
buscar = cadena.rfind("OOO")
print(buscar, type(buscar))

print ("Función isdigit")
resultado = "100".isdigit()
print (resultado, type(resultado))
print ("Función isalpha")
resultado = "Hola".isalpha()
print (resultado, type(resultado))
print ("Función isalnum")
resultado = "usuario123".isalnum()
print (resultado, type(resultado))

print ("Función split")
cadena = "pan,carne,huevos"
separado = cadena.split(",")
print (cadena)
print (separado, type(separado))

print ("Función join")
cadena = "abcdefghij"
unido = "-".join(cadena)
print (cadena)
print (unido)

#strip(): Remueve los caracteres la izquierda y a la derecha de la cadena por defecto remueve espacios en blanco, 
# si se envía un valor eliminará esos 
print ("Función strip")
cadena = "      Hola    Mundo     "
limpio = cadena.strip()
print (cadena)
print (limpio)
cadena = "-abc--def-ghi-cba----"
limpio = cadena.strip("bac-")
print (cadena)
print (limpio)

print ("Función replace")
cadena = "Me gusta programar en JS, Amo JS"
reemplazado = cadena.replace("JS", "Python")
print (cadena)
print (reemplazado)

#format(): Realiza una operación de formateo e inserta contenido a la cadena delimitado por llaves {}
print ("Función format")
cadena = "El valor de PI es: {}"
formateado = cadena.format(3.1416)
print (cadena)
print (formateado)

print ("Función format con índices")
cadena = "{2} es la suma de {0} y {1}"
valor_1 = 5
valor_2 = 3
resultado = valor_1+valor_2
formateado = cadena.format(valor_1, valor_2, resultado)
print (cadena)
print (formateado)

print ("Función format con nombres")
cadena = "{ciudad} es la capital de {pais}"
pais = "Francia"
ciudad = "París"
formateado = cadena.format(pais=pais, ciudad=ciudad)
print (cadena)
print (formateado)

#Se puede formatear cadenas de forma más directa utilizando f-strings
print ("Función format con f-string")
moneda = "Boliviano"
pais = "Bolivia"
formateado = f"La moneda de {pais} es el {moneda}"
print (formateado)
def cuenta_regresiva (numero):
    if (numero <= 0):
        print(numero)
    else:
        print (numero)
        return cuenta_regresiva (numero -1)
num = int(input("Digite nuemro: "))
cuenta_regresiva(num)
print ()

def cuenta (numero):
    if (numero >= 0):
        print (numero)
        return cuenta (numero -1)
    else:
        print ()
cuenta (num)

def factorial (num):
    if (num > 1):
        num = num * factorial (num -1)
    return num

print ()

def fac (num):
    if (num <= 1):
        return num
    else:
        num = num * fac (num -1)
        return num

factorial (num)
fac (num)
# //////////////////////////////////////////////////////////
area = lambda radio: 3.14 * radio**2
rad = 5
print(area(rad))

pi= 3.1416
area_circulo = lambda radio_circulo: pi * radio_circulo**2
radio_circ = 5
print(f"El área del círculo con radio {radio_circ} es {area_circulo(radio_circ)}")


funcion_exponenete = lambda numero, exponente: pow(numero, exponente)
print (funcion_exponenete(5,2))
# ///////////////////////////////////////
def cadena_invertida (cadena):
    cadena = cadena[::-1]
    return cadena

cadena = input("Digite cadena: ")
print (cadena_invertida(cadena))
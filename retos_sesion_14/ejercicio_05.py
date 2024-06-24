# Crear una función que reciba una cadena y devuelva la cadena invertida
def cadena_invertida (cadena):
    return cadena[::-1]

cadena = input("Ingrese cadena a invertir: ")
resultado = cadena_invertida(cadena)
print (f"La cadena invertida es: {resultado}")
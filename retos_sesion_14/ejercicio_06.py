# Crear una función que reciba una lista de números y devuelva solo los números pares
def num_pares (numeros):
    return [num for num in numeros if num % 2 == 0]

list_caracter = input("Ingrese lista numeros sin espacios y separados por el simbolo de coma: ")
print (type(list_caracter), list_caracter)
list_separados = list_caracter.split(",")
print(type(list_separados),list_separados)
lista_numeros = list(map(int, list_separados))
resultado = num_pares (lista_numeros)
print (resultado)
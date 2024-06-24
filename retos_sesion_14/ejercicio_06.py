# Crear una función que reciba una lista de números y devuelva solo los números pares
def num_pares(list_numeros):
    return [num for num in list_numeros if num % 2 == 0]

# list_numeros = list(input("Ingrese lista numeros: "))
# print (list_numeros, type(list_numeros))
list_numeros = [2,4,3,5,6,7,8,9,18,20,11,13,16]
resultado = num_pares(list_numeros)
print(f"Los números pares en la lista ingresada son {resultado}")
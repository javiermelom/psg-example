# Ingresa una cadena por teclado y almacena el valor en una tupla
# Concatena la tupla ('¡', ) + tupla almacenada + la tupla ('!', )
# Imprime el resultado concatenado
# Repite la tupla final 3 veces e imprime el nuevo resultado
string = input("Digite una cadena de caracteres:")
tupla_string = tuple(string)
tupla_start = ("¡",)
tupla_end = ("!",)
print (type(tupla_start))
print (type(tupla_string))
concatena = tupla_start + tupla_string + tupla_end
print (concatena)
# print (concatena * 3)
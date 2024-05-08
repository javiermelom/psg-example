# Escribe un programa que reciba una cadena y retorna verdadero o falso si es palindrome la frase o palabra ejemplo "Anita lava la Tina" es verdad
string = input("Escriba una frase o palabra: ")
string = string.upper()
string_without_space = (string.replace(" ",""))
print ((string_without_space) == (string_without_space[::-1]))
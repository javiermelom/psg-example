# Crea un ciclo infinito que reciba una palabra por teclado y verifique si es palíndrome, 
# termina la ejecución si se ingresa la palabra salir
while True:
    word = input ("Introduzca palabra a verificar: ")
    word = word.lower()
    if word == "salir":
        break
    else:
        word_without_space = (word.replace(" ",""))
        print ((word_without_space) == (word_without_space[::-1]))
# Agregar 5 Ejemplos con otras funciones no vistas en la sesión. Utilizar la documentación Métodos de cadenas
print ("First Example - REMOVEPREFIX")
word = "OnlyText"
print (word)
new_word = word.removeprefix("Only")
print (new_word)
print()

print ("Second Example - REMOVESUFFIX")
word = "OnlyText"
print (word)
new_word = word.removesuffix("Text")
print (new_word)
print()

print ("Third Example - MAKETRANS")
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))
print()

print ("Fourth Example - ZFILL")
txt = "50"
x = txt.zfill(4)
print(x) 
print()

print ("Fifth Example - CENTER")
txt = "banana"
x = txt.center(50)
print(x) 
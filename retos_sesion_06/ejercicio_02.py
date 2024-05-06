# Construir el operador XNOR en Python

print ("Operador OR")
a = True
b = False
print (a or a)
print (a or b)
print (b or a)
print (b or b)
print()

print ("Operador XOR")
a = True
b = False
print ((a or b) and not (a and b))
a = True
b = True
print ((a or b) and not (a and b))

print()
print ("Operador XNOR")
a = True
b = False
print (not ((a or b) and not (a and b)))
a = True
b = True
print (not ((a or b) and not (a and b)))
# Imprime una tabla de verdad para la siguiente afirmación: "Una puerta tiene dos interruptores que controlan dos luces,
# la puerta sólo debe abrirse cuando las dos luces están apagadas o las dos están encendidas, caso contrario la puerta no se abre, 
# ¿qué operador lógico se puede utilizar?"
print ("TABLA DE VERDAD")
switch1 = True
switch2 = True
print (not ((switch1 or switch2) and not (switch1 and switch2)))
switch1 = True
switch2 = False
print (not ((switch1 or switch2) and not (switch1 and switch2)))
switch1 = False
switch2 = True
print (not ((switch1 or switch2) and not (switch1 and switch2)))
switch1 = False
switch2 = False
print (not ((switch1 or switch2) and not (switch1 and switch2)))

print ("El operador logico que se utiliza es el XNOR")
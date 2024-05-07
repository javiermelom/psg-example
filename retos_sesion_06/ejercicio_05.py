# Comparar los números 123 y 890, comprobar si tienen la misma paridad ambos pares o ambos impares
num1 = 123
num2 = 890
num_1 = (num1 % 2 != 0)
num_2 = (num2 % 2 != 0)
print (num1)
print (num2)
print ("Es",(num_1 == num_2),"que los numeros",num1,"y",num2,"tengan la misma paridad")
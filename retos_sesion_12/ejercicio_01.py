# Crear un script que pida un número entero y verifique si es par o impar usando operador ternario
num = int(input("Digite un numero entero: "))
result = "El numero ingresado es par" if num % 2 == 0 else "El numero ingresado es impar"
print (result)
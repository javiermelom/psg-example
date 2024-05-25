# Crea una calculadora por consola que realice las operaciones de suma, resta, multiplicación y división, 
# ingresa dos números y la operación a realizar, verifica si la operación es válida y muestra el resultado
# Número 1: 10
# Número 2: 5
# Operación: +
# ------------
# Resultado: 15
num1 = float(input("Ingresa primer numero: "))
operator = input("Ingresa que operacion quieres realizar: \n (+, -, *, /): ")
num2 = float(input("Ingresa segundo numero: "))
print (operator, type(operator))

if (operator == "+"):
    result = num1 + num2
    print (f"El resultado de sumar {num1} + {num2} es: {result}")
elif (operator == "-"):
    result = num1 - num2
    print (f"El resultado de restar {num1} - {num2} es: {result}")
elif (operator == "*"):
    result = num1 * num2
    print (f"El resultado de multiplicar {num1} * {num2} es: {result}")
elif (operator == "/"):
    if num2:
        result = num1 / num2
        print (f"El resultado de dividir {num1} / {num2} es: {result}")
    else:
        print ("Num2 es cero y no se puede dividir por cero")
else:
    print ("Ingreso un operador Invalido")
    
    
# if (operator != "+" or operator != "-" or operator != "*" or operator != "/"):
#     print ("Digito un operador invalido")
# else:
#     num2 = float(input("Ingresa segundo numero: "))
#     if (operator == "+"):
#         result = num1 + num2
#         print (f"El resultado de sumar {num1} + {num2} es: {result}")
#     elif (operator == "-"):
#         result = num1 - num2
#         print (f"El resultado de restar {num1} - {num2} es: {result}")
#     elif (operator == "*"):
#         result = num1 * num2
#         print (f"El resultado de multiplicar {num1} * {num2} es: {result}")
#     else:
#         if num2:
#             result = num1 / num2
#             print (f"El resultado de dividir {num1} / {num2} es: {result}")
#         else:
#             print ("Num2 es cero y no se puede dividir por cero")
# print ("FIN")
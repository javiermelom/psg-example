# Crear una calculadora que solicite dos números y realice las operaciones básicas de suma,
# resta, multiplicación y división con manejo de excepciones, para salir del programa se debe ingresar "salir"

def calculadora (num1, num2, *operaciones):
    resultado = ""
    for operacion in operaciones:
        if operacion == "suma":
            resultado += (f"el resultado de la {operacion} es: {num1 + num2}\n")
        elif operacion == "resta":
            resultado += (f"el resultado de la {operacion} es: {num1 - num2}\n")
        elif operacion == "multiplicacion":
            resultado += (f"el resultado de la {operacion} es: {num1 * num2}\n")
        elif operacion == "division":
            try:
                resultado += (f"el resultado de la {operacion} es: {num1 / num2}\n")
            except ZeroDivisionError:
                return "No se puede dividir por cero"
        else:
            return ("operador invalido")
    return resultado

num1 = float (input("Digite el primer numero: "))
num2 = float (input("Digite el segundo numero: "))
resultado = calculadora (num1, num2, "multiplicacion", "suma", "resta", "division")
print (resultado)

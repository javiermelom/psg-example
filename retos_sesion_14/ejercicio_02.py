# Calculadora flexible: Crea una calculadora que acepte diferentes operaciones matemáticas como argumentos de palabras 
# clave y realice los cálculos correspondientes, las operaciones son suma, resta, multiplicación y división
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
            resultado += (f"el resultado de la {operacion} es: {num1 / num2}\n")
        else:
            return ("operador invalido")
    return resultado

resultado = calculadora (5, 5, "multiplicacion", "suma", "resta", "division")
print (resultado)
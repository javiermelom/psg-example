# Crear una función recursiva para obtener el N número de la serie de Fibonacci

def num_fibonacci(num):
    if num <= 1:
        return num
    else:
        return num_fibonacci(num-1) + num_fibonacci(num-2)

num = int(input("Digite numero para calcular serie Fibonacci: "))
print(f"El número {num} de la serie Fibonacci es {num_fibonacci(num)}")
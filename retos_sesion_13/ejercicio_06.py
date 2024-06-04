# Crea un ciclo infinito que reciba un número por teclado y verifique si es un número primo, 
# termina la ejecución si se ingresa el número 0
num = int (input ("Digite un numero: "))
aux = 1
cont = 0
while True:
    if num == 0:
        break
    else:
        if num % aux == 0:
            cont += 1
            aux += 1
            if aux >= num:
                if cont == 2:
                    print (f"el numero {num} si es primo")
                    aux = 1
                    cont = 0
                    num = int (input ("Digite un numero: "))
                else:
                    print (f"El numero {num} no es primo")
                    aux = 1
                    cont = 0
                    num = int (input ("Digite un numero: "))
        else:
            aux += 1    
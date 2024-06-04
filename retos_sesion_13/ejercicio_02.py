# Imprimir los 20 primeros números primos
num = 3
aux = 1
cont = 0
lista = [2]

while len(lista) < 20:
    for i in range(num):
        if num % aux == 0:
            aux +=1
            cont +=1
            if aux >= num:
                if cont == 2:
                    print(f"El numero {num} es primo")
                    lista.append(num)
                    num += 1
                    aux = 1
                    cont = 0
                else:
                    # print(f"El numero {num} no es primo")
                    num += 1
                    aux = 1
                    cont = 0
        else:
            aux +=1
print (lista)
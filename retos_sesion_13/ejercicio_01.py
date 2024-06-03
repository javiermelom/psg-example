# Imprimir los 20 primeros números de la serie de Fibonacci

lista = [0,1]
for i in range (20):
    lista.append(lista[-1] + lista[-2])
    print (lista)
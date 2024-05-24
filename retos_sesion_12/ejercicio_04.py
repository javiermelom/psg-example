# Una tienda ofrece descuentos a sus clientes, si el cliente es mayor de edad y tiene una compra mayor a 1000,
# se le aplica un descuento del 10%, si es menor de edad y tiene una compra mayor a 500 se le aplica un 
# descuento del 5%, si no cumple ninguna condición se le aplica un descuento del 2%
age_customer = int(input("Digite su edad: "))
buys = int(input("Digite el valor de la compra: $"))
adult = 18
if age_customer:
    if buys:
        if (age_customer >= adult and buys >= 1000):
            total_buys = buys - (buys * 0.1)
            print (f"El total de la compra es: {total_buys}")
        elif (age_customer < adult and buys > 500):
            total_buys = buys - (buys * 0.05)
            print (f"El total de la compra es: {total_buys}")
        else:
            total_buys = buys - (buys * 0.02)
            print (f"El total de la compra es: ${total_buys}")
    else:
        ("Valor de la compra Invalido")
else:
    print ("Edad Invalida")
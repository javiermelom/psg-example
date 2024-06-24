# Crear una función anónima para obtener el área de un círculo con radio 5
pi = 3.1416
area_circulo = lambda radio_circulo: pi * radio_circulo**2

radio_circ = 5
print(f"El área del círculo con radio {radio_circ} es {area_circulo(radio_circ)}")
# Escribe un programa en Python que convierta las siguientes temperaturas de grados Celsius a grados Fahrenheit:
#    30 ºC
#    -273.99 ºC
#    100 ºC
temp1_cels = 30
temp2_cels = -273.99
temp3_cels = 100

temp1_fahr = temp1_cels * (9/5) + 32
temp2_fahr = temp2_cels * (9/5) + 32
temp3_fahr = temp3_cels * (9/5) + 32

print(temp1_cels,"°C are equivalent",temp1_fahr,"°F")
print(temp2_cels,"°C are equivalent",temp2_fahr,"°F")
print(temp3_cels,"°C are equivalent",temp3_fahr,"°F")
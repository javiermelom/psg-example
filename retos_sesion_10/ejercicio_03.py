# Dos mochileros se encuentran en el Salar de Uyuni y se ponen a comparar la cantidad de lugares que han visitado
# Cada uno quiere saber en que parte del mundo ha estado el otro que el no haya visitado
# mochilero_a = {"París", "Londres", "Nueva York", "Tokio","Peru", "Chile", "Colombia", "Bolivia"}
# mochilero_b = {"Londres", "Roma", "Nueva York", "Sidney","Argentina","Brasil","Panama","Bolivia"}
# Ahora quieren saber en que ciudades han estado ambos mochileros

mochilero_a = {"París", "Londres", "Nueva York", "Tokio","Peru", "Chile", "Colombia", "Bolivia"}
mochilero_b = {"Londres", "Roma", "Nueva York", "Sidney","Argentina","Brasil","Panama","Bolivia"}

diferencia = mochilero_b - mochilero_a
print ("Los lugares que NO ha visitado mochilero_a y SI ha visitado mochilero_b son:", diferencia)
diferencia = mochilero_a - mochilero_b
print ("Los lugares que NO ha visitado mochilero_b y SI ha visitado mochilero_a son:", diferencia)
interseccion_mochileros = mochilero_a & mochilero_b
print ("Las ciudades en que ambos mochileros han estado son:",interseccion_mochileros)
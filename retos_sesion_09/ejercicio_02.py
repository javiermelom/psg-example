# De la siguiente lista [1,2,3,4,5,6,7,8,9,10] obtener una sub lista inversa utilizando índices de 3 en 3
list = [1,2,3,4,5,6,7,8,9,10]
print (list)
sublist = list.copy()
sublist.reverse()
print (sublist)
sublist = sublist[::3]
print (sublist)
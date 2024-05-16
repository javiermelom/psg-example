# Tienes una tienda de abarrotes y tienes dos listas una con los productos que tienes y otra con los precios
product = ["Leche","Huevo","Pan","Banano","Manzana"]
price = [80.0,6.5,3.5,4.0,20.5]
print (product)
print (price)

# Agregar 5 productos nuevos al final de las listas
product.extend(["Naranja","Piña","Tomate","Cebolla","Sal"])
price.extend([18.5,50.20,8.2,4.5,20.12])
print (product)
print (price)

# Eliminar el producto con el nombre "Leche" de las listas
index = product.index("Leche")
print (index)
product.pop(index)
price.pop(index)
print (product)
print (price)

# ¿Cuanto cuesta el producto "Pan" y "Huevo"?
index = product.index("Pan")
print (index)
print ("El producto", product[index],"cuesta: $",price[index])
index = product.index("Huevo")
print (index)
print ("El producto", product[index],"cuesta: $",price[index])

# ¿Cual es el producto más caro y más barato?
max_price = max(price)
print (max_price)
index = price.index(max_price)
print (index)
print ("El producto mas caro de la lista es",product[index],"con un valor de: $", price[index])
min_price = min(price)
print (min_price)
index = price.index(min_price)
print (index)
print ("El producto mas barato de la lista es",product[index],"con un valor de: $", price[index])

# ¿Cuántos productos tienes en total?
count_product = len(product)
print (count_product)
print ("La cantidad de productos en mi lista es de:", count_product)

# ¿Cuanto cuesta el total de los productos?
sum = sum(price)
print ("El total de los productos cuesta: $", sum)

# Ordena los productos alfabéticamente y precios si es posible
list_product = list(zip(product,price))
print (list_product)
list_product.sort()
print (list_product)
order_product, order_price = zip(*list_product)
order_product = list(order_product)
order_price = list(order_price)
print (order_product)
print (order_price)

# Eliminar todos los productos de las listas
product.clear()
price.clear()
print (product)
print (price)
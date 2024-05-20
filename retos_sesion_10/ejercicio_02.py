# El dueño de un restaurante de comida Mexicana ha decidido comprar un restaurante de comida Italiana y abrir 
# un nuevo restaurante de comida fusion. La apertura esta a la vuelta de la esquina y aun no hay podido actualizar 
# el Menu, Ayuda a actualizar su menu de platos disponibles

# menu_mexicano: "Tacos", "Enchiladas", "Guacamole", "Tamales"
# menu_italiano: "Pizza", "Pasta", "Lasagna", "Tiramisú"
menu_mexicano = {"Tacos", "Enchiladas", "Guacamole", "Tamales"}
menu_italiano = {"Pizza", "Pasta", "Lasagna", "Tiramisú"}
# menu_fusion = menu_mexicano.update({"Pizza", "Pasta", "Lasagna", "Tiramisú"})
menu_fusion = menu_mexicano.copy()
menu_fusion.update({"Pizza", "Pasta", "Lasagna", "Tiramisú"})
print ("El menu fusion es el siguiente:", menu_fusion)
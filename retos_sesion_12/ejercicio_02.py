# Tienes una página web y un usuario quiere acceder a ella, verifica si el usuario inició sesión 
# para acceder a la página, caso contrario muestra un mensaje de error
user = input("Digite usuario para ingresar: ")
password = input("Digite password de usuario: ")
if user:
    if password:
        print ("Ya puedes acceder a tu pag Web")
    else:
        print ("Password Invalido")
else:
    print ("User Invalido")
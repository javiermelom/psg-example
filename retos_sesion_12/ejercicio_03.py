# El usuario Jhon Doe esta en una red social sus amigos son:
# {Alice, Bob, Charlie, David, Eve}
# La usuaria Jess Doe tiene los siguientes amigos
# {Alice, Bob,  Frank, Grace}
# ¿Tienen Jhon y Jess amigos en común?, ¿Cuáles son?
friends_Jhon = {'Alice', 'Bob', 'Charlie', 'David', 'Eve'}
friends_Jess = {'Alice', 'Bob', 'Frank', 'Grace'}
interseccion = friends_Jhon & friends_Jess
print (interseccion)
if interseccion:
    print (f"{interseccion} son los amigos en común")
else:
    print ("No tienen amigos en común")
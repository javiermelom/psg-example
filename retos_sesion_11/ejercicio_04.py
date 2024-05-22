# Gestión de hábitats en peligro: Crea un diccionario que asocie especies animales en peligro de extinción
# con información sobre sus hábitats amenazados, lo que permite priorizar la protección de áreas críticas
# para la supervivencia de estas especies
# habitats = {"polo norte" : {"especies": {"oso polar", "morsa", "ballena"}}, "amazonas" : {"especies": {"tigre", "mono", "guacamayo"}}}
# Añade al diccionario de habitats 2 habitats más usando update()
# Existe en el diccionario de habitats el habitat 'amazonas'?
# Añade al diccionario de amazonas la especie 'anaconda'


# Create dict
habitats = {"polo norte" : {"especies": {"oso polar", "morsa", "ballena"}}, "amazonas" : {"especies": {"tigre", "mono", "guacamayo"}}}
print (habitats)
# Update dict
habitats.update({"bosques frios": {"especies": {"oso negro", "oso anteojos"}}, "oceano pacifico": {"especies": {"tortuga caguama"}}})
print (habitats)
# consult
exist = 'amazonas' in habitats
print ("Amazonas esta en el diccionario de habitats: ",exist)
# Update value
habitats.update(amazonas = {"especies": {"tigre", "mono", "guacamayo", "anaconda"}})
print (habitats)
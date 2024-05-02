#Convertir a cuantos días, horas, minutos y segundos corresponde la siguiente cantidad de segundos: 288325
time_in_seconds = 288325

# 1min-> 60seg.
# 1hr -> 60min -> 3600seg.
# 1day -> 24hr -> 1440min -> 86400seg.

days = time_in_seconds // 86400 # calculate days, 1day -> 24hr -> 1440min -> 86400seg.
rest = time_in_seconds % 86400 # get rest with module % for calculate hours
hours = rest // 3600 # calculate hours, 1hr -> 60min -> 3600seg.
rest1 = rest % 3600 # get rest1 with module % for calculate minutes
minutes = rest1 // 60 # calcualte minutes, 1min-> 60seg.
second = rest1 % 60

print (time_in_seconds,"seconds are equivalent",days,"days",hours,"hours",minutes,"minutes",second,"seconsds")
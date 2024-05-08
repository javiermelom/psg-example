# Invierte la siguiente palabra "programación"
word = "programacion"
long = len(word)
print (long)
# new_word = word[(long-1):0:-1] + word[0]
new_word = word[::-1]
print (new_word)
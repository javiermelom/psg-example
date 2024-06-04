# Imprimir un tablero de ajedrez de 8x8 con los caracteres # y *
n = 8
for i in range(n):
    fila = ""
    for j in range(n):
        if (i + j) % 2 == 0:
            fila += "* "
        else:
            fila += "# "
    print(fila)
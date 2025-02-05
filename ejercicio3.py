def calcular_potencia(b, e):
    if e == 0:
        return 1
    elif e == 1:
        return b
    return calcular_potencia(b, e-1) * b
base = int(input('Introduzca la base: '))
exponente = int(input('Introduzca el exponente: '))
resultado = calcular_potencia(base, exponente)
print(resultado)
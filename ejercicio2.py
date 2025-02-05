def calcular_enesimo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        return calcular_enesimo(n-1) + calcular_enesimo(n-2)
numero = int(input('Introduzca un número para calcular el enésimo: '))
resultado = calcular_enesimo(numero)
print(resultado)
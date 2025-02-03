def calcular_factorial(n):
    factorial = 1
    for i in range(n):
        factorial *= n-i
    return factorial
numero = int(input('Introduzca un número para calcular su factorial: '))
resultado = calcular_factorial(numero)
print(resultado)
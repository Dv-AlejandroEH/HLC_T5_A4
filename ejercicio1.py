# def calcular_factorial(n):
#     factorial = 1
#     for i in range(n):
#         factorial *= n-i
#     return factorial
# numero = int(input('Introduzca un número para calcular su factorial: '))
# resultado = calcular_factorial(numero)
# print(resultado)

def calcular_factorial(n):
    if n == 0 or n == 1:
        return n
    return n * calcular_factorial(n-1)
numero = int(input('Introduzca un número para calcular su factorial: '))
resultado = calcular_factorial(numero)
print(resultado)
def calcular_suma(n):
    if n == 0:
        return n
    return n%10 + calcular_suma(int(n/10))
print(calcular_suma(1234))
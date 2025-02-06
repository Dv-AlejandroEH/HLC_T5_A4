def contar_digitos(n):
    if n == 0:
        return 0
    return 1 + contar_digitos(int(n/10))
print(contar_digitos(123456789))
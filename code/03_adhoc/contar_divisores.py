def contar_divisores(n):
    divisores = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i * i == n:
                divisores += 1  # divisor doble (raiz cuadrada)
            else:
                divisores += 2  # par de divisores
    return divisores


if __name__ == "__main__":
    assert contar_divisores(1) == 1
    assert contar_divisores(12) == 6   # 1,2,3,4,6,12
    assert contar_divisores(36) == 9   # 1,2,3,4,6,9,12,18,36
    assert contar_divisores(13) == 2   # primo
    print("OK")

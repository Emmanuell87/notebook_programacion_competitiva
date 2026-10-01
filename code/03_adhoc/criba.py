def criba(n):
    # devuelve is_prime, lista booleana de tamaño n+1
    is_prime = [True] * (n + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime


if __name__ == "__main__":
    is_prime = criba(30)
    primos = [i for i in range(31) if is_prime[i]]
    assert primos == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], primos
    assert criba(1) == [False, False]
    print("OK")

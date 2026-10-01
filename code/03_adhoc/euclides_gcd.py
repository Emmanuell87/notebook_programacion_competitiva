def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


if __name__ == "__main__":
    assert gcd(12, 18) == 6
    assert gcd(17, 5) == 1
    assert gcd(0, 5) == 5
    assert lcm(4, 6) == 12
    assert lcm(7, 3) == 21
    print("OK")

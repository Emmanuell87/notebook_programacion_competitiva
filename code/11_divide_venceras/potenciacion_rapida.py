# Potenciacion rapida: O(log n).


def power(x, n):
    if n == 0:
        return 1
    half = power(x, n // 2)
    return half * half if n % 2 == 0 else half * half * x


if __name__ == "__main__":
    assert power(2, 10) == 1024
    assert power(3, 0) == 1
    assert power(5, 1) == 5
    assert power(2, 20) == 2 ** 20
    print("OK")

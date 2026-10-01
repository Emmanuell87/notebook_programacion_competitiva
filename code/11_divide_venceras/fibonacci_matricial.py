# Fibonacci con exponenciacion matricial: O(log n).

MOD = 999999937


def mult(A, B):
    return [
        [
            (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
            (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD
        ],
        [
            (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
            (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD
        ]
    ]


def matrix_pow(M, k):
    if k == 1:
        return M
    half = matrix_pow(M, k // 2)
    result = mult(half, half)
    return result if k % 2 == 0 else mult(result, M)


def fibonacci(n):
    if n == 0:
        return 0
    base = [[1, 1], [1, 0]]
    return matrix_pow(base, n)[0][1]


if __name__ == "__main__":
    esperados = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for i, e in enumerate(esperados):
        assert fibonacci(i) == e, (i, fibonacci(i), e)
    print("OK")

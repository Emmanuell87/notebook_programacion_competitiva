def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


if __name__ == "__main__":
    assert dot((1, 0), (0, 1)) == 0       # perpendiculares
    assert dot((2, 3), (2, 3)) == 13      # |v|^2
    assert cross((1, 0), (0, 1)) == 1     # giro antihorario
    assert cross((0, 1), (1, 0)) == -1    # giro horario
    assert cross((1, 1), (2, 2)) == 0     # paralelos/colineales
    print("OK")

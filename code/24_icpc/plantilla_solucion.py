import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def resolver():
    n = int(input())
    arr = list(map(int, input().split()))
    return sum(arr)               # reemplazar por la solucion del problema


def main():
    t = int(input())              # quitar si el problema tiene un solo caso
    salida = []
    for _ in range(t):
        salida.append(str(resolver()))
    print("\n".join(salida))


def preguntar(x):
    # problemas INTERACTIVOS: con input = sys.stdin.readline (arriba) no hay
    # envio automatico; sin flush=True el juez nunca recibe la consulta
    print("?", x, flush=True)
    return int(input())


if __name__ == "__main__":
    import io
    from contextlib import redirect_stdout

    # --- ejemplo ---
    sys.stdin = io.StringIO("2\n3\n1 2 3\n2\n10 20\n")
    input = sys.stdin.readline
    with redirect_stdout(io.StringIO()) as salida_capturada:
        main()
    assert salida_capturada.getvalue() == "6\n30\n"
    # --- fin ejemplo ---

    sys.stdin = io.StringIO("7\n")
    input = sys.stdin.readline
    with redirect_stdout(io.StringIO()) as salida_capturada:
        assert preguntar(5) == 7
    assert salida_capturada.getvalue() == "? 5\n"
    print("OK")

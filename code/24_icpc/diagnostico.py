import platform
import sys
import time


def diagnostico():
    # implementacion y version: CPython o PyPy cambian mucho la velocidad
    print(platform.python_implementation(), sys.version.split()[0])

    t = time.time()
    s = 0
    for i in range(10 ** 7):
        s += i
    print("10^7 iteraciones:", round(time.time() - t, 2), "s")

    sys.setrecursionlimit(10 ** 6)

    def prof(n):
        return 0 if n == 0 else 1 + prof(n - 1)

    print("recursion de 10^5 niveles:", prof(10 ** 5))   # si el programa se cierra aqui, usar un hilo con pila grande

    try:
        print("entero de 5000 digitos a texto:", len(str(10 ** 5000)))
    except ValueError:
        print("limite de digitos activo: usar sys.set_int_max_str_digits(0)")


if __name__ == "__main__":
    import io
    from contextlib import redirect_stdout

    with redirect_stdout(io.StringIO()) as capturado:
        diagnostico()
    lineas = capturado.getvalue().splitlines()
    assert lineas[0].split()[0] in ("CPython", "PyPy")
    assert lineas[1].startswith("10^7 iteraciones:")
    assert float(lineas[1].split(":")[1].replace("s", "")) > 0
    assert lineas[2] == "recursion de 10^5 niveles: 100000"
    assert lineas[3].startswith(("entero de 5000 digitos", "limite de digitos"))
    print("OK")

# Backtracking + Programacion Dinamica. Ejemplo clasico: Fibonacci con
# memorizacion. Cuando una recursion (backtracking) recalcula los
# mismos subproblemas muchas veces -- @lru_cache guarda
# automaticamente el resultado de cada llamada para no repetirla.
# Sirve como plantilla general: cualquier funcion recursiva con
# parametros hasheables puede memorizarse igual.

from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(10) == 55
    assert fib(30) == 832040  # sin memo esto tardaria mucho (2^30 llamadas)
    print("OK")

import sys
import threading

# Truco estandar para recursion muy profunda: correr todo en un hilo
# con una pila de memoria grande. Si el juez limita la memoria, bajar
# el tamano (2 ** 26 = 64 MB).


def correr_con_pila_grande(funcion):
    sys.setrecursionlimit(10 ** 6)
    threading.stack_size(2 ** 27)            # 128 MB
    hilo = threading.Thread(target=funcion)
    hilo.start()
    hilo.join()


if __name__ == "__main__":
    # --- ejemplo ---
    resultado = []

    def main():
        def suma(n):                          # recursion de 10^5 niveles
            return 0 if n == 0 else n + suma(n - 1)
        resultado.append(suma(10 ** 5))

    correr_con_pila_grande(main)
    assert resultado == [10 ** 5 * (10 ** 5 + 1) // 2]
    # --- fin ejemplo ---
    print("OK")

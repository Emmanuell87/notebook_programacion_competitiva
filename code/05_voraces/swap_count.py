# Dada una secuencia con igual numero de parentesis de apertura y
# cierre, hallar el minimo numero de intercambios adyacentes para
# hacerla balanceada. La cadena debe convertirse a lista (list(s))
# antes de llamar la funcion. O(n), usa el arreglo pos para saber
# donde estan los siguientes '('.


def swap_count(s: list):
    pos = [i for i, c in enumerate(s) if c == '(']
    count = p = ans = 0

    for i in range(len(s)):
        if s[i] == '(':
            count += 1
            p += 1
        else:
            count -= 1
            if count < 0:
                ans += pos[p] - i
                s[i], s[pos[p]] = s[pos[p]], s[i]
                count = 1
                p += 1
    return ans


if __name__ == "__main__":
    assert swap_count(list("))((")) == 3
    assert swap_count(list("()()")) == 0
    assert swap_count(list(")(")) == 1
    print("OK")

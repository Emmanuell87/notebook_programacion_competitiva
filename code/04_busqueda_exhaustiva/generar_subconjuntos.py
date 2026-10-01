# Util para problemas de sumas, combinaciones, particion, etc.


def generar_subconjuntos(nums):
    res = []

    def backtrack(i, path):
        if i == len(nums):
            res.append(path[:])
            return
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()
        backtrack(i + 1, path)

    backtrack(0, [])
    return res


if __name__ == "__main__":
    subs = generar_subconjuntos([1, 2, 3])
    assert len(subs) == 8  # 2^3
    assert [] in subs
    assert [1, 2, 3] in subs
    assert [2] in subs
    print("OK")

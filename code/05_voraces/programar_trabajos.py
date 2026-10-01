# Dado un conjunto de trabajos, cada uno con una ganancia y una fecha
# limite, seleccionar el subconjunto que maximiza la ganancia,
# ejecutando a lo sumo un trabajo por unidad de tiempo antes de su
# deadline. jobs = lista de (ganancia, deadline), deadline >= 1
# (deadline d significa que debe ejecutarse en algun slot 1..d).
# Devuelve la ganancia total maxima (no la asignacion en si).


def programar_trabajos(jobs):
    jobs.sort(reverse=True)
    max_d = max(d for _, d in jobs)
    ocupado = [False] * max_d
    total = 0
    for g, d in jobs:
        for i in range(min(d, max_d) - 1, -1, -1):
            if not ocupado[i]:
                ocupado[i] = True
                total += g
                break
    return total


if __name__ == "__main__":
    # (ganancia, deadline)
    jobs = [(100, 2), (19, 1), (27, 2), (25, 1), (15, 3)]
    assert programar_trabajos(jobs) == 142
    print("OK")

def kadane(arr):
    max_actual = max_global = arr[0]
    for x in arr[1:]:
        max_actual = max(x, max_actual + x)
        max_global = max(max_global, max_actual)
    return max_global


if __name__ == "__main__":
    assert kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert kadane([1]) == 1
    assert kadane([-5, -2, -8]) == -2
    assert kadane([5, 4, -1, 7, 8]) == 23
    print("OK")

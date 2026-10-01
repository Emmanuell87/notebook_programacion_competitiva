# Dados numeros en una lista, seleccionar un subconjunto de elementos
# NO ADYACENTES que maximice la suma. nums = lista de numeros (pueden
# ser negativos). Es el clasico "House Robber": no puedes tomar dos
# elementos consecutivos.


def max_indep_set(nums):
    if not nums:
        return 0
    n = len(nums)
    if n == 1:
        return nums[0]

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

    return dp[-1]


if __name__ == "__main__":
    assert max_indep_set([]) == 0
    assert max_indep_set([5]) == 5
    assert max_indep_set([2, 7, 9, 3, 1]) == 12  # 2+9+1
    assert max_indep_set([-1, -2, -3]) == -1     # mejor tomar el menos malo
    print("OK")

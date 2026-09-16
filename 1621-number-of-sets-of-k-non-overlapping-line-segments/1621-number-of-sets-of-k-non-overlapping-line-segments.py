class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        return comb(n + k - 1, 2 * k) % MOD

def comb(n, r):
    MOD = 10**9 + 7
    res = 1
    for i in range(1, r + 1):
        res = res * (n - r + i) % MOD
        res = res * pow(i, MOD - 2, MOD) % MOD
    return res
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False

        p = 2
        while p * p < n:
            if isPrime[p]:
                for i in range(p * p, n, p):
                    isPrime[i] = False
            p += 1

        return sum(isPrime)
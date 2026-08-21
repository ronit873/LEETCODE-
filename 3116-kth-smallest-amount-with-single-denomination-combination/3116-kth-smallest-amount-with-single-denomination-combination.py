class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        from math import gcd
        from itertools import combinations

        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            ans = 0

            for mask in range(1, 1 << n):
                v = 1
                bits = 0

                for i in range(n):
                    if mask >> i & 1:
                        v = lcm(v, coins[i])
                        if v > x:
                            break
                        bits += 1

                else:
                    if bits % 2:
                        ans += x // v
                    else:
                        ans -= x // v

            return ans

        left, right = 1, min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
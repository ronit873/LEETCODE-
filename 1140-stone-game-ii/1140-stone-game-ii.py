from functools import lru_cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def dfs(i: int, m: int) -> int:
            if i >= n:
                return 0
            if 2 * m >= n - i:
                return suffix[i]

            ans = 0
            for x in range(1, 2 * m + 1):
                ans = max(ans, suffix[i] - dfs(i + x, max(m, x)))
            return ans

        return dfs(0, 1)
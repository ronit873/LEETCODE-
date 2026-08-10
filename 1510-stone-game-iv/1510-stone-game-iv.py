from functools import lru_cache

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def dfs(rem):
            k = 1
            while k * k <= rem:
                if not dfs(rem - k * k):
                    return True
                k += 1
            return False

        return dfs(n)
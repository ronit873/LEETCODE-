class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        x = 1000
        while x <= n:
            ans += n - x + 1   # every number from x..n gets (at least) one more comma
            x *= 1000
        return ans
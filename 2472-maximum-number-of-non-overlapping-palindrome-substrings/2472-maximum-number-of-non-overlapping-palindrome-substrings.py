class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        for i in range(n):
            dp[i + 1] = dp[i]

        for center in range(n):
            l, r = center, center
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    dp[r + 1] = max(dp[r + 1], dp[l] + 1)
                l -= 1
                r += 1

            l, r = center, center + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    dp[r + 1] = max(dp[r + 1], dp[l] + 1)
                l -= 1
                r += 1

            if center + 1 < n:
                dp[center + 2] = max(dp[center + 2], dp[center + 1])

        return dp[n]
class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            num_mod = num % k
            new_dp = [0] * k

            new_dp[num_mod] = 1

            for r in range(k):
                if dp[r]:
                    new_r = (r * num_mod) % k
                    new_dp[new_r] += dp[r]

            for r in range(k):
                ans[r] += new_dp[r]

            dp = new_dp

        return ans
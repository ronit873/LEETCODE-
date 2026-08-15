class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        x = 0
        for n in nums:
            x ^= n

        if x != 0:
            return len(nums)

        if any(n != 0 for n in nums):
            return len(nums) - 1

        return 0
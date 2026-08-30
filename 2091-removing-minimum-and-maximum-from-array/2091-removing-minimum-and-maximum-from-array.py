class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)
        min_i = nums.index(min(nums))
        max_i = nums.index(max(nums))

        a = min(min_i, max_i)
        b = max(min_i, max_i)

        return min(
            b + 1,
            n - a,
            (a + 1) + (n - b)
        )
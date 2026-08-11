class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            s += nums[i]
            i += 1

        st = set(nums)
        while s in st:
            s += 1
        return s
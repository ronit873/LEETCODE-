class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        n = len(nums)

        if target < 0:
            return -1

        if target == 0:
            return n

        left = 0
        curr = 0
        max_len = -1

        for right in range(n):
            curr += nums[right]

            while left <= right and curr > target:
                curr -= nums[left]
                left += 1

            if curr == target:
                max_len = max(max_len, right - left + 1)

        return -1 if max_len == -1 else n - max_len
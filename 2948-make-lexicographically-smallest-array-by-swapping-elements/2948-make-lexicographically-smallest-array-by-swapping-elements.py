class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        arr = sorted((v, i) for i, v in enumerate(nums))
        res = nums[:]
        n = len(nums)

        start = 0
        while start < n:
            end = start
            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            indices = sorted(i for _, i in arr[start:end + 1])
            values = [arr[i][0] for i in range(start, end + 1)]

            for i, v in zip(indices, values):
                res[i] = v

            start = end + 1

        return res
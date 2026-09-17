class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = n + 1
        best = INF
        ans = INF

        left = 0
        curr = 0

        min_len = [INF] * n

        for right in range(n):
            curr += arr[right]

            while curr > target and left <= right:
                curr -= arr[left]
                left += 1

            if curr == target:
                length = right - left + 1

                if left > 0 and min_len[left - 1] != INF:
                    ans = min(ans, length + min_len[left - 1])

                min_len[right] = min(
                    length,
                    min_len[right - 1] if right > 0 else INF
                )
            else:
                min_len[right] = min_len[right - 1] if right > 0 else INF

        return ans if ans != INF else -1
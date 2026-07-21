class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        ones = 0
        i = 0

        prev_zero = float("-inf")
        best = 0

        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1

            length = j - i

            if s[i] == '1':
                ones += length
            else:
                best = max(best, prev_zero + length)
                prev_zero = length

            i = j

        return ones + best
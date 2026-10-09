class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        right = 0

        for ch in s:
            if ch == '(':
                if right % 2 == 1:
                    res += 1
                    right -= 1
                right += 2
            else:
                right -= 1
                if right < 0:
                    res += 1
                    right = 1

        return res + right
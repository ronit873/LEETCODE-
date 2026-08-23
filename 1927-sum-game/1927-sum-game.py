class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2

        left = right = 0
        lq = rq = 0

        for i in range(mid):
            if num[i] == '?':
                lq += 1
            else:
                left += int(num[i])

        for i in range(mid, n):
            if num[i] == '?':
                rq += 1
            else:
                right += int(num[i])

        # Difference in number of '?' must be even
        if (lq + rq) % 2 == 1:
            return True

        # Alice can force inequality if the current difference
        # cannot be balanced by the remaining '?'s
        diff = left - right

        return diff != 9 * (rq - lq) // 2
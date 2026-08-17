from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i, v in enumerate(stoneValue):
            prefix[i + 1] = prefix[i] + v

        dp = [[0] * n for _ in range(n)]
        # maxLeft[i][j]  = max over k in [i,j] of dp[i][k] + sum(i..k)
        # maxRight[i][j] = max over k in [i,j] of dp[k][j] + sum(k..j)
        maxLeft = [[0] * n for _ in range(n)]
        maxRight = [[0] * n for _ in range(n)]

        for i in range(n):
            maxLeft[i][i] = stoneValue[i]
            maxRight[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                total = prefix[j + 1] - prefix[i]

                # Binary search for the largest split point k where
                # sum(i..k) <= sum(k+1..j)  (left ≤ right)
                lo, hi, k = i, j - 1, i - 1
                while lo <= hi:
                    mid = (lo + hi) // 2
                    ls = prefix[mid + 1] - prefix[i]
                    if 2 * ls <= total:
                        k = mid
                        lo = mid + 1
                    else:
                        hi = mid - 1

                res = 0
                tie = False
                if k >= i:
                    res = maxLeft[i][k]
                    ls = prefix[k + 1] - prefix[i]
                    tie = (2 * ls == total)

                # For splits m > k, right side is kept (sums start at m+1 >= k+2,
                # except when tied at k, right side can also start at k+1)
                right_start = (k + 1) if tie else (k + 2)
                if right_start <= j:
                    res = max(res, maxRight[right_start][j])

                dp[i][j] = res
                maxLeft[i][j] = max(maxLeft[i][j - 1], dp[i][j] + total)
                maxRight[i][j] = max(maxRight[i + 1][j], dp[i][j] + total)

        return dp[0][n - 1]
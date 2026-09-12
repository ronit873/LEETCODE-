from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)
        order = sorted(range(n), key=lambda i: intervals[i][1])
        starts = [intervals[order[i]][0] for i in range(n)]
        ends = [intervals[order[i]][1] for i in range(n)]
        weights = [intervals[order[i]][2] for i in range(n)]

        prev = [0] * n
        for i in range(n):
            prev[i] = bisect_left(ends, starts[i], 0, i)

        dp = [[0] * 5 for _ in range(n + 1)]
        best = [[() for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            idx = i - 1
            for k in range(5):
                if k == 0:
                    dp[i][k] = 0
                    best[i][k] = ()
                    continue

                skip_val = dp[i - 1][k]
                skip_seq = best[i - 1][k]

                take_val = dp[prev[idx]][k - 1] + weights[idx]
                take_seq = tuple(sorted(best[prev[idx]][k - 1] + (order[idx],)))

                if take_val > skip_val:
                    dp[i][k] = take_val
                    best[i][k] = take_seq
                elif take_val < skip_val:
                    dp[i][k] = skip_val
                    best[i][k] = skip_seq
                else:
                    dp[i][k] = skip_val
                    best[i][k] = min(skip_seq, take_seq)

        return list(best[n][4])
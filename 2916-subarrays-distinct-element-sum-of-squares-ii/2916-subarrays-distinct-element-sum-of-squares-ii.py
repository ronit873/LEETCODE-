from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, start, end, val):
            length = end - start + 1
            tree_sq[node] = (
                tree_sq[node] + 2 * val * tree_sum[node]
                + length * val * val
            ) % MOD
            tree_sum[node] = (tree_sum[node] + length * val) % MOD
            lazy[node] = (lazy[node] + val) % MOD

        def push(node, start, end):
            if lazy[node] == 0 or start == end:
                return

            mid = (start + end) // 2
            apply(node * 2, start, mid, lazy[node])
            apply(node * 2 + 1, mid + 1, end, lazy[node])
            lazy[node] = 0

        def update(node, start, end, left, right, val):
            if right < start or end < left:
                return

            if left <= start and end <= right:
                apply(node, start, end, val)
                return

            push(node, start, end)
            mid = (start + end) // 2

            update(node * 2, start, mid, left, right, val)
            update(node * 2 + 1, mid + 1, end, left, right, val)

            tree_sum[node] = (
                tree_sum[node * 2] + tree_sum[node * 2 + 1]
            ) % MOD
            tree_sq[node] = (
                tree_sq[node * 2] + tree_sq[node * 2 + 1]
            ) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)
            update(1, 0, n - 1, prev + 1, i, 1)
            last[x] = i
            ans = (ans + tree_sq[1]) % MOD

        return ans
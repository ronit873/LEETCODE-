class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)
        size = 1
        while size < n:
            size <<= 1

        # tree[node] = [product % k, count of prefix products]
        tree = [[1 % k, [0] * k] for _ in range(2 * size)]

        def merge(a, b):
            prod = (a[0] * b[0]) % k
            cnt = a[1][:]

            for r in range(k):
                cnt[(a[0] * r) % k] += b[1][r]

            return [prod, cnt]

        # Build
        for i in range(n):
            v = nums[i] % k
            tree[size + i] = [v, [1 if j == v else 0 for j in range(k)]]

        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        def update(pos, value):
            pos += size
            value %= k
            tree[pos] = [
                value,
                [1 if j == value else 0 for j in range(k)]
            ]

            pos //= 2
            while pos:
                tree[pos] = merge(tree[2 * pos], tree[2 * pos + 1])
                pos //= 2

        def query(l, r):
            # [l, r)
            left_res = None
            right_res = None

            l += size
            r += size

            while l < r:
                if l & 1:
                    left_res = tree[l] if left_res is None else merge(left_res, tree[l])
                    l += 1

                if r & 1:
                    r -= 1
                    right_res = tree[r] if right_res is None else merge(tree[r], right_res)

                l //= 2
                r //= 2

            if left_res is None:
                return right_res
            if right_res is None:
                return left_res

            return merge(left_res, right_res)

        ans = []

        for index, value, start, x in queries:
            update(index, value)
            res = query(start, n)
            ans.append(res[1][x])

        return ans
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        # Total path length must be even
        if (m + n - 1) % 2 != 0:
            return False

        # First and last characters are necessary
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        # dp[r][c] = set of possible balances at (r, c)
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue

                current = 1 if grid[r][c] == '(' else -1

                # From top
                if r > 0:
                    for balance in dp[r - 1][c]:
                        new_balance = balance + current
                        if new_balance >= 0:
                            dp[r][c].add(new_balance)

                # From left
                if c > 0:
                    for balance in dp[r][c - 1]:
                        new_balance = balance + current
                        if new_balance >= 0:
                            dp[r][c].add(new_balance)

        return 0 in dp[m - 1][n - 1]
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        res = set()

        def dfs(i, left, right, path, balance):
            if i == len(s):
                if balance == 0:
                    res.add("".join(path))
                return

            if s[i] not in "()":
                path.append(s[i])
                dfs(i + 1, left, right, path, balance)
                path.pop()
            else:
                if s[i] == "(":
                    if left > 0:
                        dfs(i + 1, left - 1, right, path, balance)
                    path.append("(")
                    dfs(i + 1, left, right, path, balance + 1)
                    path.pop()
                else:
                    if right > 0:
                        dfs(i + 1, left, right - 1, path, balance)
                    if balance > 0:
                        path.append(")")
                        dfs(i + 1, left, right, path, balance - 1)
                        path.pop()

        left = right = 0
        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                if left:
                    left -= 1
                else:
                    right += 1

        dfs(0, left, right, [], 0)
        return list(res)
class Solution:
    def generateParenthesis(self, n):
        res = []

        def backtrack(openP, closeP, s):
            if len(s) == 2 * n:
                res.append(s)
                return

            if openP < n:
                backtrack(openP + 1, closeP, s + "(")

            if closeP < openP:
                backtrack(openP, closeP + 1, s + ")")

        backtrack(0, 0, "")
        return res
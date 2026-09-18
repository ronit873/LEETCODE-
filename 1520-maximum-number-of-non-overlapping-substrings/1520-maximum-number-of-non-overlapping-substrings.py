class Solution:
    def maxNumOfSubstrings(self, s: str):
        first = [len(s)] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            x = ord(ch) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        for i in range(26):
            if last[i] == -1:
                continue

            l, r = first[i], last[i]
            j = l
            valid = True

            while j <= r:
                x = ord(s[j]) - ord('a')

                if first[x] < l:
                    valid = False
                    break

                r = max(r, last[x])
                j += 1

            if valid:
                intervals.append((r, l))

        intervals.sort()

        ans = []
        end = -1

        for r, l in intervals:
            if l > end:
                ans.append(s[l:r + 1])
                end = r

        return ans
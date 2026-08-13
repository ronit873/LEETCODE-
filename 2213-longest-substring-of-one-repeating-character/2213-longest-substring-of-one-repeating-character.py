from sortedcontainers import SortedList

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)
        s = list(s)

        segs = SortedList()
        lens = SortedList()

        i = 0
        while i < n:
            j = i
            while j + 1 < n and s[j + 1] == s[i]:
                j += 1
            segs.add((i, j))
            lens.add(j - i + 1)
            i = j + 1

        ans = []

        for idx, ch in zip(queryIndices, queryCharacters):
            if s[idx] == ch:
                ans.append(lens[-1])
                continue

            pos = segs.bisect_right((idx, n)) - 1
            l, r = segs.pop(pos)
            lens.remove(r - l + 1)

            if l <= idx - 1:
                segs.add((l, idx - 1))
                lens.add(idx - l)
            if idx + 1 <= r:
                segs.add((idx + 1, r))
                lens.add(r - idx)

            s[idx] = ch

            nl = nr = idx

            pos = segs.bisect_left((idx, idx))

            if pos > 0:
                pl, pr = segs[pos - 1]
                if pr + 1 == idx and s[pl] == ch:
                    segs.pop(pos - 1)
                    lens.remove(pr - pl + 1)
                    nl = pl
                    pos -= 1

            if pos < len(segs):
                rl, rr = segs[pos]
                if rl - 1 == idx and s[rl] == ch:
                    segs.pop(pos)
                    lens.remove(rr - rl + 1)
                    nr = rr

            segs.add((nl, nr))
            lens.add(nr - nl + 1)
            ans.append(lens[-1])

        return ans
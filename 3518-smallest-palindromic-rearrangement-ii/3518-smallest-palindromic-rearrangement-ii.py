import collections

class Solution:
    def __init__(self):
        self.MAX = 10**6 + 1

    def smallestPalindrome(self, s: str, k: int) -> str:
        count = collections.Counter(s)

        odd = sum(v & 1 for v in count.values())
        if odd > 1:
            return ""

        half = [0] * 26
        mid = ""

        for ch, v in count.items():
            half[ord(ch) - ord("a")] = v // 2
            if v & 1:
                mid = ch

        if self._count(half) < k:
            return ""

        left = []
        m = sum(half)

        for _ in range(m):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                ways = self._count(half)

                if ways >= k:
                    left.append(chr(i + ord("a")))
                    break

                k -= ways
                half[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]

    def _count(self, cnt):
        total = sum(cnt)
        ans = 1

        for x in cnt:
            if x:
                ans *= self._nCr(total, x)
                if ans >= self.MAX:
                    return self.MAX
                total -= x

        return ans

    def _nCr(self, n, r):
        if r > n:
            return 0

        r = min(r, n - r)
        ans = 1

        for i in range(1, r + 1):
            ans = ans * (n - i + 1) // i
            if ans >= self.MAX:
                return self.MAX

        return ans
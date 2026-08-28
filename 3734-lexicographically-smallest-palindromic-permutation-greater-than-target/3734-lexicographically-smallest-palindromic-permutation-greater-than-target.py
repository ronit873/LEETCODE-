from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        odd_chars = [c for c, v in cnt.items() if v % 2 == 1]
        if len(odd_chars) > 1:
            return ""
        mid_char = odd_chars[0] if odd_chars else None

        half = n // 2
        H = Counter()
        for c, v in cnt.items():
            hv = v // 2
            if hv > 0:
                H[c] = hv

        for k in range(half, -1, -1):
            if k == half:
                prefix_cnt = Counter(target[:half])
                if prefix_cnt != H:
                    continue
                first_half = target[:half]
                candidate = (first_half + mid_char + first_half[::-1]
                             if mid_char is not None
                             else first_half + first_half[::-1])
                if candidate > target:
                    return candidate
                continue
            else:
                prefix = target[:k]
                prefix_cnt = Counter(prefix)
                if any(prefix_cnt[c] > H.get(c, 0) for c in prefix_cnt):
                    continue

                remaining = dict(H)
                for c, v in prefix_cnt.items():
                    remaining[c] = remaining.get(c, 0) - v

                choices = sorted(c for c, v in remaining.items()
                                  if v > 0 and c > target[k])
                if not choices:
                    continue

                chosen = choices[0]
                remaining[chosen] -= 1

                rest_chars = []
                for c in sorted(remaining.keys()):
                    rest_chars.extend([c] * remaining[c])

                first_half = prefix + chosen + "".join(rest_chars)
                candidate = (first_half + mid_char + first_half[::-1]
                             if mid_char is not None
                             else first_half + first_half[::-1])
                return candidate

        return ""
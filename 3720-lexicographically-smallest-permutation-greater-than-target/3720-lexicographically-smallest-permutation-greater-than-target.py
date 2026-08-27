class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        ans = []

        for i in range(len(target)):
            t = ord(target[i]) - ord('a')

            # Try to put target[i]
            if cnt[t] > 0:
                cnt[t] -= 1
                ans.append(target[i])
                continue

            # Can't match target[i]
            # Find the smallest character > target[i]
            for c in range(t + 1, 26):
                if cnt[c] > 0:
                    ans.append(chr(c + ord('a')))
                    cnt[c] -= 1

                    # Put all remaining characters in sorted order
                    for x in range(26):
                        ans.extend([chr(x + ord('a'))] * cnt[x])

                    return ''.join(ans)

            # No greater character here.
            # Backtrack to an earlier position.
            while ans:
                last = ans.pop()
                cnt[ord(last) - ord('a')] += 1

                prev = len(ans)

                for c in range(
                    ord(target[prev]) - ord('a') + 1, 26
                ):
                    if cnt[c] > 0:
                        ans.append(chr(c + ord('a')))
                        cnt[c] -= 1

                        for x in range(26):
                            ans.extend([chr(x + ord('a'))] * cnt[x])

                        return ''.join(ans)

            return ""

        # s itself is equal to target
        # Need a strictly greater permutation
        for i in range(len(target) - 1, -1, -1):
            cnt[ord(target[i]) - ord('a')] += 1

            t = ord(target[i]) - ord('a')

            for c in range(t + 1, 26):
                if cnt[c] > 0:
                    result = target[:i] + chr(c + ord('a'))
                    cnt[c] -= 1

                    for x in range(26):
                        result += chr(x + ord('a')) * cnt[x]

                    return result

        return ""
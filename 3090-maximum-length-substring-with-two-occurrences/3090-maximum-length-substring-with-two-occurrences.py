class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cnt = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            cnt[s[right]] = cnt.get(s[right], 0) + 1

            while cnt[s[right]] > 2:
                cnt[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
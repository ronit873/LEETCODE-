from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        if m > n:
            return []
        
        suf = [0] * (m + 1)
        suf[m] = n
        pos = n
        for j in range(m - 1, -1, -1):
            pos -= 1
            while pos >= 0 and word1[pos] != word2[j]:
                pos -= 1
            suf[j] = pos
        
        result = []
        j = 0
        changed = False
        for i in range(n):
            if j == m:
                break
            if word1[i] == word2[j]:
                result.append(i)
                j += 1
            elif not changed and suf[j + 1] >= i + 1:
                result.append(i)
                j += 1
                changed = True
        
        return result if j == m else []